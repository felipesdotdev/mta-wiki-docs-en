---
doc_id: "mta-wiki:5491"
title: "InterpolateBetween"
source_title: "InterpolateBetween"
source_url: "https://wiki.multitheftauto.com/wiki/InterpolateBetween"
revision_id: 70955
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# InterpolateBetween

Interpolates a 3D Vector between a source value and a target value using either linear interpolation or any other [easing function](mta://reference/misc/easing.md).
It can also be used to interpolate 2D vectors or scalars by only setting some of the x, y, z values and putting 0 to the others.

## Syntax

```
float float float interpolateBetween ( float x1, float y1, float z1, float x2, float y2, float z2, float fProgress, string strEasingType, [ float fEasingPeriod, float fEasingAmplitude, float fEasingOvershoot ] )
```

### Required Arguments

- **x1, y1, z1:** 3D coordinates of source vector/value

- **x2, y2, z2:** 3D coordinates of target vector/value

- **fProgress:** float between 0 and 1 indicating the interpolation progress (0 at the beginning of the interpolation, 1 at the end). If it is higher than 1, it will start from the beginning.

- **strEasingType:** the [easing function](mta://reference/misc/easing.md) to use for the interpolation

### Optional Arguments

- **fEasingPeriod:** the period of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

- **fEasingAmplitude:** the amplitude of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

- **fEasingOvershoot:** the overshoot of the [easing function](mta://reference/misc/easing.md) (only some easing functions use this parameter)

### Returns

Returns *x, y, z* the interpolated 3D vector/value if successful, *false* otherwise (error in parameters).
As mentioned before, interpolateBetween can be used on 2D vectors or scalars in which case only some (x, y or just x) of the returned values are to be used (cf. alpha interpolation in marker example or size interpolation in window example).

## Example

The examples below are only clientside examples even though the function can be used on both sides. Indeed it makes more sense to use it with onClientRender/onClientPreRender but the freedom is given to use it in any other context.
**Example 1**:

Click to collapse [-]
Client

This clientside example uses interpolateBetween to create position and color interpolation(with effect) on a marker.
The command to test it is "/marker".
The position is interpolated with "OutBounce" as strEasingType to make the marker bounce off the ground and "Linear" interpolation for the color.

```
local g_Marker = nil
addCommandHandler("marker",
function ()
	if g_Marker then return end
	
	local x, y, z = getElementPosition(getLocalPlayer())
	z = z - 1
	
	g_Marker = {}
	g_Marker.startPos = {x, y, z + 5}
	g_Marker.startTime = getTickCount()
	g_Marker.startColor = {255, 0, 0, 0}
	g_Marker.endPos = {x, y, z}
	g_Marker.endTime = g_Marker.startTime + 2000
	g_Marker.endColor = {0, 0, 255, 255}	
	
	local x, y, z = unpack(g_Marker.startPos)
	local r, g, b, a = unpack(g_Marker.startColor)
	g_Marker.marker = createMarker(x, y, z, "cylinder", 1, 255, r, g, b, a)
		
	addEventHandler("onClientRender", getRootElement(), popMarkerUp)
end)

function popMarkerUp()
	local now = getTickCount()
	local elapsedTime = now - g_Marker.startTime
	local duration = g_Marker.endTime - g_Marker.startTime
	local progress = elapsedTime / duration

	local x1, y1, z1 = unpack(g_Marker.startPos)
	local x2, y2, z2 = unpack(g_Marker.endPos)
	local x, y, z = interpolateBetween ( 
		x1, y1, z1,
		x2, y2, z2, 
		progress, "OutBounce")
		
	setElementPosition(g_Marker.marker, x, y, z)
			
	local r1, g1, b1, a1 = unpack(g_Marker.startColor)
	local r2, g2, b2, a2 = unpack(g_Marker.endColor)
	local r, g, b = interpolateBetween ( 
		r1, g1, b1,
		r2, g2, b2, 
		progress, "Linear")
	local a = interpolateBetween ( 
		a1, 0, 0,
		a2, 0, 0,
		progress, "Linear")
		
	setMarkerColor(g_Marker.marker , r, g, b, a)
	
	if now >= g_Marker.endTime then
		removeEventHandler("onClientRender", getRootElement(), popMarkerUp)
		setTimer(
			function ()
				destroyElement(g_Marker.marker)
				g_Marker = nil
			end, 3000, 1)
	end
end
```

**Example 2**:

Click to collapse [-]
Client

This clientside example uses interpolateBetween to create size and position interpolation (with effect) on a gui-window.
The command to test it is "/window".
When the window pops up it uses "OutElastic" as the strEasingType to create the bouncing/elastic effect.
When it fades away, it uses "InQuad" to have an accelerating fading.

```
local g_Window = nil
addCommandHandler("window",
function ()
	if g_Window then return end
	
	g_Window = {}
	
	local screenWidth, screenHeight = guiGetScreenSize()
	g_Window.windowWidth, g_Window.windowHeight = 400, 315
	local left = screenWidth/2 - g_Window.windowWidth/2
	local top = screenHeight/2 - g_Window.windowHeight/2
	
	g_Window.window = guiCreateWindow(left, top, g_Window.windowWidth, g_Window.windowHeight, "Interpolation on GUI", false)
	
	g_Window.closeBtn = guiCreateButton(320, 285, 75, 23, "Close", false, g_Window.window)
		
	guiWindowSetSizable(g_Window.window, false)
	guiWindowSetMovable(g_Window.window, false)
	guiSetEnabled(g_Window.window, false)
	guiSetVisible(g_Window.window, false)
	
	g_Window.startTime = getTickCount()
	g_Window.startSize = {0, 0}
	g_Window.endSize = {g_Window.windowWidth, g_Window.windowHeight}
	g_Window.endTime = g_Window.startTime + 1000
	addEventHandler("onClientRender", getRootElement(), popWindowUp)
end)

function on_closeBtn_clicked(button, state, absoluteX, absoluteY)
	if (button ~= "left") or (state ~= "up") then
		return
	end
	
	if not g_Window then return end
	
	showCursor(false)
	guiSetEnabled(g_Window.window, false)
	guiWindowSetMovable(g_Window.window, false)
	
	local screenWidth, screenHeight = guiGetScreenSize()
	local posX, posY = guiGetPosition(g_Window.window, false)
	
	g_Window.startTime = getTickCount()
	g_Window.startSize = {g_Window.windowWidth, g_Window.windowHeight}
	g_Window.startCenter = 
	{
		posX + g_Window.windowWidth/2,
		posY + g_Window.windowHeight/2,
	}
	
	g_Window.endSize = {0, 0}
	g_Window.endTime = g_Window.startTime + 1000
	g_Window.endCenter = 
	{
		screenWidth, 
		screenHeight
	}
	
	addEventHandler("onClientRender", getRootElement(), popWindowDown)
end

function popWindowUp()
	local now = getTickCount()
	local elapsedTime = now - g_Window.startTime
	local duration = g_Window.endTime - g_Window.startTime
	local progress = elapsedTime / duration
		
	local width, height, _ = interpolateBetween ( 
		g_Window.startSize[1], g_Window.startSize[2], 0, 
		g_Window.endSize[1], g_Window.endSize[2], 0, 
		progress, "OutElastic")
		
	guiSetSize(g_Window.window, width, height, false)
	
	local screenWidth, screenHeight = guiGetScreenSize()
	guiSetPosition(g_Window.window, screenWidth/2 - width/2, screenHeight/2 - height/2, false)
	
	if not guiGetVisible(g_Window.window) then
		guiSetVisible(g_Window.window, true)
		guiBringToFront(g_Window.window)
	end
	
	if now >= g_Window.endTime then
		guiSetEnabled(g_Window.window, true)
		
		guiBringToFront(g_Window.window)
		removeEventHandler("onClientRender", getRootElement(), popWindowUp)
		addEventHandler("onClientGUIClick", g_Window.closeBtn, on_closeBtn_clicked, false)
		showCursor(true)
		guiWindowSetMovable(g_Window.window, true)
	end
end

function popWindowDown()
	local now = getTickCount()
	local elapsedTime = now - g_Window.startTime
	local duration = g_Window.endTime - g_Window.startTime
	local progress = elapsedTime / duration
	
	local width, height, _ = interpolateBetween ( 
		g_Window.startSize[1], g_Window.startSize[2], 0, 
		g_Window.endSize[1], g_Window.endSize[2], 0, 
		progress, "InQuad")
		
	guiSetSize(g_Window.window, width, height, false)
	
	local centerX, centerY, _ = interpolateBetween ( 
		g_Window.startCenter[1], g_Window.startCenter[2], 0, 
		g_Window.endCenter[1], g_Window.endCenter[2], 0, 
		progress, "InQuad")
	
	guiSetPosition(g_Window.window, centerX - width/2, centerY - height/2, false)
	
	if now >= g_Window.endTime then
		removeEventHandler("onClientRender", getRootElement(), popWindowDown)
		destroyElement(g_Window.window)
		g_Window = nil
	end
end
```

**Example 3**:

Click to collapse [-]
Client

This clientside example uses interpolateBetween to create and position interpolation (with effect) on a camera.
The command to test it is "/ccam".
When the camera pops up it uses "OutQuad" as the strEasingType to create the slow down effect.

```
local enabled = false
 
addCommandHandler("ccam", function()
    enabled = not enabled
    if enabled then
        start = getTickCount()
        dx, dy, dz, lx, ly, lz = getCameraMatrix()
        addEventHandler("onClientPreRender", root, interpolateCam)
    else
        start = nil
        setCameraTarget(localPlayer)
        removeEventHandler("onClientPreRender", root, interpolateCam)
    end
end)
 
function interpolateCam()
    local now = getTickCount()
    local endTime = start + 2000
    local elapsedTime = now - start
    local duration = endTime - start
    local progress = elapsedTime / duration
    local px, py, pz = getElementPosition(localPlayer)
    local x, y, z = interpolateBetween ( dx, dy, dz, dx+4, dy+4, dz, progress, "OutQuad")
    setCameraMatrix(x, y, z, px, py, pz+0.6, 0, 0)
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

- [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md)

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

- interpolateBetween

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
