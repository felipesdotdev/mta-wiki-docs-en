---
doc_id: "mta-wiki:7965"
title: "IsOOPEnabled"
source_title: "IsOOPEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsOOPEnabled"
revision_id: 42562
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.4.1"]
---

# IsOOPEnabled

This function checks whether *[OOP](mta://tutorials/oop.md)* (Object Oriented Programming) is enabled in the current [resource](mta://reference/misc/resource.md) or not.

## Syntax

```
bool isOOPEnabled ( )
```

### Returns

Returns *true* or *false* if *[OOP](mta://tutorials/oop.md)* is enabled or not. Returns *nil* if an error arised.

## Example

Click to collapse [-]
Example

This shared (clientside and serverside) example outputs if *[OOP](mta://tutorials/oop.md)* is enabled when the [resource](mta://reference/misc/resource.md) which contains it starts, and teleports a random player 10 units left if so.

```
local function checkOOPStatus()
   if isOOPEnabled() then
        outputChatBox("* OOP is enabled! Welcome to matrices' paradise.", getRandomPlayer and root or 0, getRandomPlayer and 0 or 255, getRandomPlayer and 255 or 0, getRandomPlayer and 0 or nil)
        local player
        if getRandomPlayer then -- Are we executed serverside?
            player = Player.getRandom() -- Make it easy, use OOP to get a random player
        else
            local players = getElementsByType("player")
            if #players > 0 then -- Is the server empty?
                player = players[math.random(1, #players)]  -- Get a random player using player elements table
            end
        end
        if not player then
            return -- We don't have a player. Cancel further execution of this function.
        end
        player.position = player.position + player.matrix.left * 10 -- Move him 10 units left, taking into account rotation
        outputChatBox(player.name .. " was moved 10 meters left as a demostration of OOP capabilities!", getRandomPlayer and root or 180, 180, getRandomPlayer and 180 or 255, getRandomPlayer and 255 or nil)
   else
        outputChatBox("* OOP is disabled! You should like the good ol' tables.", getRandomPlayer and root or 255, getRandomPlayer and 255 or 140, getRandomPlayer and 140 or 0, getRandomPlayer and 0 or nil)
   end
end
checkOOPStatus() -- Execute this at resource start
```

## See also

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

- isOOPEnabled

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
