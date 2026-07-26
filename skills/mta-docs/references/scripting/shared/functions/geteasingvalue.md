---
doc_id: "mta-wiki:5492"
title: "GetEasingValue"
source_title: "GetEasingValue"
source_url: "https://wiki.multitheftauto.com/wiki/GetEasingValue"
revision_id: 63932
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetEasingValue

Used for custom Lua based interpolation, returns the easing value (animation time to use in your custom interpolation) given a progress and an [easing function](mta://reference/misc/easing.md).
In most cases, either [moveObject](mta://scripting/shared/functions/moveobject.md) or [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md) can do the job. getEasingValue is only provided in case you want to do your own custom interpolation based on easing.

## Syntax

```
float getEasingValue ( float fProgress, string strEasingType [, float fEasingPeriod, float fEasingAmplitude, float fEasingOvershoot ] )
```

### Required Arguments

- **fProgress:** float between 0 and 1 indicating the interpolation progress (0 at the beginning of the interpolation, 1 at the end).

- **strEasingType:** the [easing function](mta://reference/misc/easing.md) to use for the interpolation

### Optional Arguments

- **fEasingPeriod:** the period of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

- **fEasingAmplitude:** the amplitude of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

- **fEasingOvershoot:** the overshoot of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

### Returns

Returns *fAnimationTime* the animation time given by the easing function (can be < 0 or > 1 since some [easing functions](mta://reference/misc/easing.md) have overshoot or bounce/spring effects, *false* otherwise (error in parameters).

## Example

The examples below are only clientside ones, even though the functions can be used on both sides. Indeed it makes more sense to use them with onClientRender/onClientPreRender but the freedom is given to use it in any other context.

Click to collapse [-]
Client

This clientside example uses getEasingValue to make a custom camera fade.
The command to test it is "/fade".
The fading out is done with "InQuad" to have a slow fading which then accelerates and "OutQuad" is used for fading in to have a smooth end of the fading.
In this example [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md) could have been used directly to interpolate the alpha between 0 and 255 and then 255 and 0 but is example is just to illustrate the use of getEasingValue by itself.

```
local g_Fade = nil
addCommandHandler("fade", 
function ()
	if g_Fade then return end
	g_Fade = {}
	g_Fade.startTime = getTickCount()
	g_Fade.endTime = g_Fade.startTime + 2000
	g_Fade.easingFunction = "InQuad" --Slow at first and accelerating
	addEventHandler("onClientRender", getRootElement(), fadeCameraOut)
end)

function fadeCameraOut()
	local now = getTickCount()
	local elapsedTime = now - g_Fade.startTime
	local duration = g_Fade.endTime - g_Fade.startTime
	local progress = elapsedTime / duration
	
	local fAnimationTime = getEasingValue(progress, g_Fade.easingFunction)
	
	local alpha = fAnimationTime*255
	local width, height = guiGetScreenSize()
	dxDrawRectangle(0, 0, width, height, tocolor(0, 0, 0, alpha), true)
	
	if now > g_Fade.endTime then
		removeEventHandler("onClientRender", getRootElement(), fadeCameraOut)
		g_Fade.startTime = getTickCount()
		g_Fade.endTime = g_Fade.startTime + 2000
		g_Fade.easingFunction = "OutQuad" --Fast at first then decelerating
		addEventHandler("onClientRender", getRootElement(), fadeCameraIn)
	end
end

function fadeCameraIn()
	local now = getTickCount()
	local elapsedTime = now - g_Fade.startTime
	local duration = g_Fade.endTime - g_Fade.startTime
	local progress = elapsedTime / duration
	
	local fAnimationTime = getEasingValue(progress, g_Fade.easingFunction)
	
	local alpha = (1-fAnimationTime)*255
	local width, height = guiGetScreenSize()
	dxDrawRectangle(0, 0, width, height, tocolor(0, 0, 0, alpha), true)
		
	if now > g_Fade.endTime then
		removeEventHandler("onClientRender", getRootElement(), fadeCameraIn)
		g_Fade = nil
	end
end
```

## See Also

- [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- [decodeString](mta://scripting/shared/functions/decodestring.md)

- [encodeString](mta://scripting/shared/functions/encodestring.md)

- [fromJSON](mta://scripting/shared/functions/fromjson.md)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- [getColorFromString](mta://scripting/shared/functions/getcolorfromstring.md)

- [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md)

- [getDistanceBetweenPoints2D](mta://scripting/shared/functions/getdistancebetweenpoints2d.md)

- [getDistanceBetweenPoints3D](mta://scripting/shared/functions/getdistancebetweenpoints3d.md)

- getEasingValue

- [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md)

- [getNetworkUsageData](mta://scripting/shared/functions/getnetworkusagedata.md)

- [getPerformanceStats](mta://scripting/shared/functions/getperformancestats.md)

- [getRealTime](mta://scripting/shared/functions/getrealtime.md)

- [getTickCount](mta://scripting/shared/functions/gettickcount.md)

- [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md)

- [getTimers](mta://scripting/shared/functions/gettimers.md)

- [getFPSLimit](mta://scripting/shared/functions/getfpslimit.md)

- [getUserdataType](mta://scripting/shared/functions/getuserdatatype.md)

- [getVersion](mta://scripting/shared/functions/getversion.md)

- [gettok](mta://scripting/shared/functions/gettok.md)

- [isTransferBoxVisible](mta://scripting/shared/functions/istransferboxvisible.md)

- [setTransferBoxVisible](mta://scripting/shared/functions/settransferboxvisible.md)

- [hash](mta://scripting/shared/functions/hash.md)

- [inspect](mta://scripting/shared/functions/inspect.md)

- [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md)

- [iprint](mta://scripting/shared/functions/iprint.md)

- [isOOPEnabled](mta://scripting/shared/functions/isoopenabled.md)

- [isTimer](mta://scripting/shared/functions/istimer.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22701](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22701):

- [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md)

- [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md)

- [killTimer](mta://scripting/shared/functions/killtimer.md)

- [md5](mta://scripting/shared/functions/md5.md)

- [passwordHash](mta://scripting/shared/functions/passwordhash.md)

- [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

- [pregFind](https://wiki.multitheftauto.com/index.php?search=pregFind)

- [pregMatch](mta://scripting/shared/functions/pregmatch.md)

- [pregReplace](mta://scripting/shared/functions/pregreplace.md)

- [removeDebugHook](mta://scripting/shared/functions/removedebughook.md)

- [resetTimer](mta://scripting/shared/functions/resettimer.md)

- [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md)

- [setFPSLimit](mta://scripting/shared/functions/setfpslimit.md)

- [setTimer](mta://scripting/shared/functions/settimer.md)

- [ref](mta://scripting/shared/functions/ref.md)

- [deref](mta://scripting/shared/functions/deref.md)

- [sha256](mta://scripting/shared/functions/sha256.md)

- [split](mta://scripting/shared/functions/split.md)

- [teaDecode](mta://scripting/shared/functions/teadecode.md)

- [teaEncode](mta://scripting/shared/functions/teaencode.md)

- [toJSON](mta://scripting/shared/functions/tojson.md)

- [tocolor](mta://scripting/shared/functions/tocolor.md)

- [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md)

- [utfChar](mta://scripting/shared/functions/utfchar.md)

- [utfCode](mta://scripting/shared/functions/utfcode.md)

- [utfLen](https://wiki.multitheftauto.com/index.php?search=utfLen)

- [utfSeek](mta://scripting/shared/functions/utfseek.md)

- [utfSub](mta://scripting/shared/functions/utfsub.md)

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
