---
doc_id: "mta-wiki:9139"
title: "Iprint"
source_title: "Iprint"
source_url: "https://wiki.multitheftauto.com/wiki/Iprint"
revision_id: 53985
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# Iprint

This function intelligently outputs debug messages into the Debug Console.  It is similar to [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md), but outputs useful information for **any** variable type, and does not require use of Lua's tostring.  This includes information about element types, and table structures.  It is especially useful for quick debug tasks.

## Syntax

```
bool iprint ( mixed var1[, mixed var2, mixed var3...] )
```

### Required Arguments

- **var1:** A variable of any type to print intelligent information for.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **var2+:** Another variable to be output.  An unlimited number of arguments can be supplied

### Returns

Always returns *nil*.

## Issues

If one of the arguments is nil, any arguments after it will not appear.

## Example

Click to collapse [-]
Server

This example prints some sample debug messages, assuming the server is running a typical freeroam/play environment:

```
function resourceStartNotify ( resourcename )
	-- Example of outputting tables, and elements directly
	iprint(getElementsByType("player"))
	iprint(getElementsByType("vehicle"))
	-- Example of outputting multiple items at once
	iprint("this resource:",getThisResource(),"state:",getResourceState(getThisResource()),"resource root:",getResourceRootElement(getThisResource()))
end
addEventHandler( "onResourceStart", getRootElement(), resourceStartNotify )
```

The output from the server might look like this:

```
[2016-10-01 21:25:43] INFO: { elem:player[MrPlayer] }

[2016-10-01 21:25:43] INFO: { elem:vehicle[Monster 3]2ED3EF60, elem:vehicle[Monster 3]2ED3F620, elem:vehicle[Banshee]2ED3F548, elem:vehicle[Banshee]2ED3F590, elem:vehicle[Bullet]2ED3F5D8, elem:vehicle[BMX]2ED3FA58, elem:vehicle[BMX]2ED3FE00, elem:vehicle[Sparrow]2ED3F788, elem:vehicle[Sanchez]2ED3F6B0, elem:vehicle[Sanchez]2ED3F8A8, elem:vehicle[Sanchez]2ED3FE48, elem:vehicle[Jetmax]2ED3FC98, elem:vehicle[Dinghy]2ED3FA10, elem:vehicle[Marquis]2ED3FB78, elem:vehicle[Bandito]2ED3FAA0, elem:vehicle[Beagle]2ED3F980, elem:vehicle[Buffalo]2ED3FDB8, elem:vehicle[Sabre]2ED3F6F8, elem:vehicle[Caddy]2ED3F7D0, elem:vehicle[Sparrow]2ED3F938, elem:vehicle[Sanchez]2ED3FED8, elem:vehicle[Sanchez]2ED3FCE0, elem:vehicle[Sanchez]2ED3F860, elem:vehicle[Monster 3]2ED3F8F0, elem:vehicle[Monster 3]2ED3FC08, elem:vehicle[Buffalo]2ED3F9C8, elem:vehicle[Bandito]2ED3FAE8, elem:vehicle[Caddy]2ED3FB30, elem:vehicle[Sabre]2ED3F668, elem:vehicle[Bullet]2ED3FBC0, elem:vehicle[Banshee]2ED3FF20, elem:vehicle[Banshee]2ED3F818, elem:vehicle[Monster 3]2ED3FC50, elem:vehicle[Monster 3]2ED3FD28, elem:vehicle[Buffalo]2ED3FD70, elem:vehicle[Bandito]2ED3FE90, elem:vehicle[Caddy]2ED3F740, elem:vehicle[Sabre]2ED405E0, elem:vehicle[Bullet]2ED406B8, elem:vehicle[Banshee]2ED40748, elem:vehicle[Banshee]2ED401F0, elem:vehicle[Sanchez]2ED40508, elem:vehicle[Sanchez]2ED401A8, elem:vehicle[Sanchez]2ED40040, elem:vehicle[Sparrow]2ED40118, elem:vehicle[Sanchez]2ED40238, elem:vehicle[Sanchez]2ED3FFB0, elem:vehicle[Sanchez]2ED40598, elem:vehicle[Monster 3]2ED40550, elem:vehicle[Monster 3]2ED40700, elem:vehicle[Buffalo]2ED40280, elem:vehicle[Bandito]2ED403A0, elem:vehicle[Caddy]2ED400D0, elem:vehicle[Sabre]2ED402C8, elem:vehicle[Bullet]2ED40160, elem:vehicle[Banshee]2ED40790, elem:vehicle[Banshee]2ED40628, elem:vehicle[Sparrow]2ED3FFF8 }

[2016-10-01 21:25:43] INFO: "this resource:"    resource[runcode]    "state:"    "running"    "resource root:"    elem:resource2B696440
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

- [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md)

- iprint

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
