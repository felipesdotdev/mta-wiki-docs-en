---
doc_id: "mta-wiki:7332"
title: "AddDebugHook"
source_title: "AddDebugHook"
source_url: "https://wiki.multitheftauto.com/wiki/AddDebugHook"
revision_id: 82476
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3", "Changes_in_1.5.5"]
---

# AddDebugHook

This function allows tracing of MTA functions and events. It should only be used when debugging scripts as it may degrade script performance.

Debug hooks are not recursive, so functions and events triggered inside the hook callback will not be traced.

## Syntax

```
bool addDebugHook ( string hookType, function callbackFunction [, table nameList ] )
```

### Required Arguments

- **hookType:** The type of hook to add. This can be:

- preEvent

- postEvent

- preFunction

- postFunction

- preEventFunction

- postEventFunction

- **callbackFunction:** The function to call

- Returning the string "skip" from the callback function will cause the original function/event to be skipped

### Optional Arguments

- **nameList:** Table of strings for restricting which functions and events the hook will be triggered on

- addDebugHook and removeDebugHook will only be hooked if they are specified in the name list

### Returns

Returns *true* if the hook was successfully added, or *false* otherwise.

## Callback parameters

```
string preFunction( resource sourceResource, string functionName, bool isAllowedByACL, string luaFilename, int luaLineNumber, ...functionArguments )
       postFunction( resource sourceResource, string functionName, bool isAllowedByACL, string luaFilename, int luaLineNumber, ...functionArguments )
string preEvent( resource sourceResource, string eventName, element eventSource, element eventClient, string luaFilename, int luaLineNumber, ...eventArguments )
       postEvent( resource sourceResource, string eventName, element eventSource, element eventClient, string luaFilename, int luaLineNumber, ...eventArguments )
```

```
string preEventFunction ( resource eventResource, string eventName, element eventSource, element eventClient, string eventFilename, int eventLineNumber, resource functionResource, string functionFilename, int functionLineNumber, ...eventArgs )
       postEventFunction ( resource eventResource, string eventName, element eventSource, element eventClient, string eventFilename, int eventLineNumber, resource functionResource, string functionFilename, int functionLineNumber, ...eventArgs )
```

## Example

This example will dump info about all triggered events:

```
function onPreEvent( sourceResource, eventName, eventSource, eventClient, luaFilename, luaLineNumber, ... )
    local args = { ... }
    local srctype = eventSource and getElementType(eventSource)
    local resname = sourceResource and getResourceName(sourceResource)
    local plrname = eventClient and getPlayerName(eventClient)
    outputDebugString( "preEvent"
        .. " " .. tostring(resname)
        .. " " .. tostring(eventName)
        .. " source:" .. tostring(srctype)
        .. " player:" .. tostring(plrname)
        .. " file:" .. tostring(luaFilename)
        .. "(" .. tostring(luaLineNumber) .. ")"
        .. " numArgs:" .. tostring(#args)
        .. " arg1:" .. tostring(args[1])
        )
end
addDebugHook( "preEvent", onPreEvent )
```

This example will dump info about all called MTA functions:

```
function onPreFunction( sourceResource, functionName, isAllowedByACL, luaFilename, luaLineNumber, ... )
    local args = { ... }
    local resname = sourceResource and getResourceName(sourceResource)
    outputDebugString( "preFunction"
        .. " " .. tostring(resname)
        .. " " .. tostring(functionName)
        .. " allowed:" .. tostring(isAllowedByACL)
        .. " file:" .. tostring(luaFilename)
        .. "(" .. tostring(luaLineNumber) .. ")"
        .. " numArgs:" .. tostring(#args)
        .. " arg1:" .. tostring(args[1])
        )
end
addDebugHook( "preFunction", onPreFunction)
```

This example adds a hook which will only be triggered for the named functions

```
addDebugHook( "preFunction", onPreFunction, {"setElementPosition","loadstring"} )
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.5-9.06054 | Added clientside |
| --- | --- |

| 1.3.5-9.06142 | Added option to restrict to specified functions and events |
| --- | --- |

| 1.5.2-9.07957 | Added option to skip original function/event Added ability to hook addDebugHook and removeDebugHook |
| --- | --- |

| 1.5.5-9.11856 | Added pre/postEventFunction hooks |
| --- | --- |

| 1.6.0-9.22741 | Removed ability to skip 'addDebugHook' |
| --- | --- |

## See Also

- addDebugHook

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
