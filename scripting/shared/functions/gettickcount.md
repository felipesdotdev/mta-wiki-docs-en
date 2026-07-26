---
doc_id: "mta-wiki:1324"
title: "GetTickCount"
source_title: "GetTickCount"
source_url: "https://wiki.multitheftauto.com/wiki/GetTickCount"
revision_id: 72047
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:26.208794+00:00"
---

# GetTickCount

This function returns amount of time that your system has been running in milliseconds. By comparing two values of getTickCount, you can determine how much time has passed (in milliseconds) between two events. This could be used to determine how efficient your code is, or to time how long a player takes to complete a task.

| [[{{{image}}}\|link=\|]] | Important Note: The value returned by this function client-side may not be reliable if a client is maliciously modifying their operating system speed. |
| --- | --- |
|  |  |

## Syntax

```
int getTickCount ()
```

### Returns

Returns an integer containing the number of milliseconds since the system the server is running on started. This has the potential to wrap-around.

## Example

The below code is a good example on how to implement basic anti-spam protection for a command, for which using getTickCount is better than the regular timer functions.

```
local spam = {}

function setSkin(player, cmd, skin)
    if spam[player] and getTickCount() - spam[player] < 4000 then
        return outputChatBox("You cannot change skin that often!", player, 255, 0, 0)
    end

    skin = skin and tonumber(skin)

    if getElementModel(player) == skin or isPedDead(player) then
        return
    end

    if skin and skin <= 99999 then -- what do we know about dynamic ped ID range?
        setElementModel(player, skin)
        spam[player] = getTickCount()
    else
        outputChatBox("Invalid skin ID!", player, 255, 0, 0)
    end
end
addCommandHandler("skin", setSkin)

function cleanUp()
    if spam[source] then
        spam[source] = nil
    end
end
addEventHandler("onPlayerQuit", root, cleanUp)
```

This example will start a timer displayed at the top of the screen displayed every frame. You can log any specific moment in time by outputting the currentCount variable.

```
local firstColor = tocolor(0, 0, 0, 150)
local secondColor = tocolor(255, 255, 255, 255)
local screenX, screenY = guiGetScreenSize()
local currentCount = 0
local systemUpTime = getTickCount() -- Store the system tick count, this will be 0 for us

function onClientRenderClock()
	currentCount = getTickCount()
	
	dxDrawRectangle(screenX *.40, screenY * .09, 250, 50, firstColor)
	dxDrawText(currentCount - systemUpTime, screenX * .48, screenY * .1, screenX, screenY, secondColor, 2)
end
addEventHandler("onClientRender", root, onClientRenderClock)
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

- getTickCount

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

- [tocolor](mta://scripting/shared/functions/tocolor.md)

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
