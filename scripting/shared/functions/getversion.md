---
doc_id: "mta-wiki:4418"
title: "GetVersion"
source_title: "GetVersion"
source_url: "https://wiki.multitheftauto.com/wiki/GetVersion"
revision_id: 82296
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:29.929400+00:00"
---

# GetVersion

This function gives you various version information about MTA and the operating system.

MTA already has a built in command '/ver' which will show you your client version. Alongside that, there is also '/sver' which will show you the version of the server you are currently connected to. This function unlike [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md) shows a lot more information regarding MTA version.

| [[{{{image}}}\|link=\|]] | Note: Clientside will return the version from the player, and the server-sided will return version from the server. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Current MTA version: mta -> 1.6 netcode -> 474 number -> 352 sortable -> 1.6.0-9.22279.0 tag -> 1.6-release-22279 type -> Release |
| --- | --- |
|  |  |

## Syntax

```
table getVersion ( )
```

### Returns

Returns a table with version information. Specifically these keys are present in the table:

- **number:** the MTA server or client version (depending where the function was called) in pure numerical form, e.g. *"256"*

- **mta:** the MTA server or client version (depending where the function was called) in textual form, e.g. *"1.0"*

- **name:** the full MTA product name, either *"MTA:SA Server"* or *"MTA:SA Client"*.

- **netcode:** the netcode version number.

- **os:** returns the operating system on which the server or client is running

- **type:** the type of build.  can be:

- **"Nightly rX"** - A nightly development build.  **X** represents the nightly build revision.

- **"Custom"** - A build compiled manually

- **"Release"** - A build that is publicly released (provisional).

- **tag:** the build tag (from 1.0.3 onwards). Contains infomation about the underlying version used. i.e. The final version of 1.0.3 has the build tag of "1.0.3 rc-9". (This can be confirmed by using the console command 'ver'.)

- **sortable:** a 15 character sortable version string (from 1.0.4 onwards). Format of the string is described in [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md).

## Example

Click to collapse [-]
Server

This piece of code shows how you can use a simple command and a for loop to dump the output into chatbox, whilst capitalizing 1st character for extra bonus.

```
function showVersion(player)
    -- We use a for loop to dump the output into player chatbox
    outputChatBox("Version information (Server):", player, 0, 255, 0)
    for ind, dat in pairs(getVersion()) do
        -- Uppercasing first letter too
        outputChatBox(string.upper(string.sub(ind, 1, 1))..string.sub(ind, 2)..": "..dat, player, 0, 255, 0)
    end
end
addCommandHandler("version", showVersion) -- Define our command handler
```

Click to collapse [-]
Client

This piece of code shows how you can use a simple command and a for loop to dump the output into chatbox, whilst capitalizing 1st character for extra bonus. Keep in mind that this is the client sided version of this command which will output version information of your client, whilst the example above outputs information of the server you are connected to.

```
function showVersion()
    -- We use a for loop to dump the output into player chatbox
    outputChatBox("Version information (Client):", 0, 255, 0)
    for ind, dat in pairs(getVersion()) do
        -- Uppercasing first letter too
        outputChatBox(string.upper(string.sub(ind, 1, 1))..string.sub(ind, 2)..": "..dat, 0, 255, 0)
    end
end
addCommandHandler("version", showVersion) -- Define our command handler
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

- getVersion

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
