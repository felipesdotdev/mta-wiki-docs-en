---
doc_id: "mta-wiki:1771"
title: "GetColorFromString"
source_title: "GetColorFromString"
source_url: "https://wiki.multitheftauto.com/wiki/GetColorFromString"
revision_id: 63930
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetColorFromString

This function will extract Red, Green, Blue and Alpha values from a hex string you provide it. These strings follow the same format as used in HTML, with addition of the Alpha values.

## Syntax

```
int, int, int, int getColorFromString ( string theColor )
```

### Required Arguments

- **theColor:** A string containing a valid color code.

Valid strings are:

- **#RRGGBB**: Colors specified, Alpha assumed to be 255.

- **#RRGGBBAA**: All values specified.

- **#RGB**: Shortened form, will be expanded internally to RRGGBB, as such it provides a smaller number of colors.

- **#RGBA**: As above, shortened - each character is duplicated.

For example:

- **#FF00FF** is Red: 255, Green: 0, Blue: 255, Alpha: 255

- **#F0F** is Red: 255, Green: 0, Blue: 255, Alpha: 255 (the same as the example above)

- **#34455699** is Red: 52, Green: 69, Blue: 86, Alpha: 153

All colors used must begin with a # sign.

### Returns

Returns four integers in RGBA format, with a maximum value of 255 for each.  Each stands for *red*, *green*, *blue*, and *alpha*.  Alpha decides transparancy where 255 is opaque and 0 is transparent.  *false* is returned if the string passed is invalid (for example, is missing the preceeding # sign).

## Example

Click to collapse [-]
Server

This example will set the blip attached to a player to a color they specify by typing *set_my_color [color]* in the console.

```
function setPlayerBlipColor ( playerSource, commandName, colorString )
    local red, green, blue, alpha = getColorFromString ( colorString )  -- convert the color string to numbers
    local playerBlip = getBlipAttachedTo ( playerSource )               -- find the blip attached to the player
    if ( playerBlip and red ) then                                      -- check a blip is attached to the player and that a valid color was specified
        setBlipColor ( playerBlip, red, green, blue, alpha )            -- set the player's blip color
    end
end
addCommandHandler ( "set_my_color", setPlayerBlipColor )

-- specify the getBlipAttachedTo function
function getBlipAttachedTo( thePlayer )
	local blips = getElementsByType( "blip" )
	for k, theBlip in ipairs( blips ) do
		if getElementAttachedTo( theBlip ) == thePlayer then
			return theBlip
		end
	end
	return false
end
```

## See Also

- [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- [decodeString](mta://scripting/shared/functions/decodestring.md)

- [encodeString](mta://scripting/shared/functions/encodestring.md)

- [fromJSON](mta://scripting/shared/functions/fromjson.md)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- getColorFromString

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
