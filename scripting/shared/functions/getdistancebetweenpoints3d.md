---
doc_id: "mta-wiki:1389"
title: "GetDistanceBetweenPoints3D"
source_title: "GetDistanceBetweenPoints3D"
source_url: "https://wiki.multitheftauto.com/wiki/GetDistanceBetweenPoints3D"
revision_id: 80011
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:10.097481+00:00"
---

# GetDistanceBetweenPoints3D

| [[{{{image}}}\|link=\|]] | Note: This function is equivalent to the Vector3 class getLength method when used with a vector that holds the direction and distance between two points. In other words, it produces exactly the same result as substracting the points' coordinates and getting the length of the result vector. |
| --- | --- |
|  |  |

This function returns the distance between two 3 dimensional points using the pythagorean theorem.

## Syntax

```
float getDistanceBetweenPoints3D ( float x1, float y1, float z1, float x2, float y2, float z2 )
```

### Required Arguments

- **x1**: The X position of the first point

- **y1**: The Y position of the first point

- **z1**: The Z position of the first point

- **x2**: The X position of the second point

- **y2**: The Y position of the second point

- **z2**: The Z position of the second point

### Returns

Returns a float containing the distance between the two points as a [float](mta://reference/misc/float.md). Returns *false* if an argument passed was invalid.

## Example

This example gets the distance between two vehicles and outputs it to the chat box.

Click to collapse [-]
Server

```
-- create the vehicles which we're going to measure distance between of
vehicle1 = createVehicle(445, -2629.79248, 1370.82996, 7.10079)
vehicle2 = createVehicle(560, -2629.71899, 1350.18188, 7.10897)

-- get position of both created vehicles
vehicle1x, vehicle1y, vehicle1z = getElementPosition(vehicle1)
vehicle2x, vehicle2y, vehicle2z = getElementPosition(vehicle2)

-- measure the distance
outputChatBox("The distance between vehicle1 and vehicle2 is " ..tostring(getDistanceBetweenPoints3D(vehicle1x, vehicle1y, vehicle1z, vehicle2x, vehicle2y, vehicle2z)))
```

This example checks whether or not the player is close enough (5 meters from a location of SF Bridge)

Click to collapse [-]
Server

```
function checkIfClose(p, cmd)
    -- player x, y, z
    local x1, y1, z1 = getElementPosition(p)
    -- location x, y, z (to check if player is close enough to)
    local x2, y2, z2 = -2629.79248, 1370.82996, 7.10079

    if getDistanceBetweenPoints3D(x1, y1, z1, x2, y2, z2) <= 5 then
        return outputChatBox("You are close enough (within 5 meters)!")
    else
        return outputChatBox("You are NOT close enough!")
    end
end
addCommandHandler("closeornot", checkIfClose)

--[REWRITE BY ANDREI]
local half = 1 / 2
function getDistanceFromPoints(x1, y1, z1, x2, y2, z2)
    return ((x2 - x1) * (x2 - x1) ^ 2 + (y2 - y1) * (y2 - y1) ^ 2 + (z2 - z1) * (z2 - z1)) ^ half
end
```

*getDistanceBetweenPoints3D* can also be used to measure the length of 3 dimensional vectors. This example calculates the speed of a vehicle by measuring the size of the it's velocity vector:

```
speed = getDistanceBetweenPoints3D ( 0, 0, 0, getElementVelocity ( vehicle ) )
```

*Lua note: Using multiple return values as arguments for another function can only be done at the end of the argument list.*

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

- getDistanceBetweenPoints3D

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
