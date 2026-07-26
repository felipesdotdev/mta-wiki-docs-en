---
doc_id: "mta-wiki:3853"
title: "Tocolor"
source_title: "Tocolor"
source_url: "https://wiki.multitheftauto.com/wiki/Tocolor"
revision_id: 57536
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:16:58.447753+00:00"
---

# Tocolor

This function retrieves the hex number of a specified color, useful for the dx functions.
Added server-side.

## Syntax

```
int tocolor ( int red, int green, int blue [, int alpha = 255 ] )
```

### Required Arguments

- **red:** The amount of [red](http://en.wikipedia.org/wiki/RGBA_color_space) in the color (0-255).

- **green:** The amount of [green](http://en.wikipedia.org/wiki/RGBA_color_space) in the color (0-255).

- **blue:** The amount of [blue](http://en.wikipedia.org/wiki/RGBA_color_space) in the color (0-255).

### Optional Arguments

- **alpha:** The amount of [alpha](http://en.wikipedia.org/wiki/RGBA_color_space) in the color (0-255).

### Returns

Returns a single value representing the color.

## Example

Click to collapse [-]
Client

This example displays the text "Tuna" in small at the top left side of your screen. The color of this text can be changed using the command /tunaColor.

```
local tunaColor = tocolor(255, 0, 0, 255) -- Default color

-- This function draws the text
local function drawTuna()
	dxDrawText("Tuna", 5, 5, 100, 100, tunaColor)
end
addEventHandler("onClientRender", root, drawTuna)

--This function handles the /tunaColor command, allowing players to set the color of tuna
local function tunaColorCommand(command, red, green, blue, alpha)
	red, green, blue, alpha = tonumber(red), tonumber(green), tonumber(blue), tonumber(alpha) -- Convert all the args to numbers. NOTE: tonumber will return false if the arg is not provided/is not valid.
	
	-- Remind the user of the proper syntax if they failed to provide all the args
	if not red or not green or not blue then
		outputChatBox("* USAGE: /tunaColor [red] [green] [blue] [alpha]", 255, 0, 0)
		return
	end
	
	-- Make the alpha arg optional
	if not alpha then
		alpha = 255
	end
	
	-- Update the color
	tunaColor = tocolor(red, green, blue, alpha)
end
addCommandHandler("tunaColor", tunaColorCommand)
-- Example /setcoloroftuna 255 0 0 255 - for red.
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.5-r13977 | Added server-side |
| --- | --- |

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

- [pregFind](mta://scripting/shared/functions/pregfind.md)

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

- tocolor

- [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md)

- [utfChar](mta://scripting/shared/functions/utfchar.md)

- [utfCode](mta://scripting/shared/functions/utfcode.md)

- [utfLen](mta://scripting/shared/functions/utflen.md)

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
