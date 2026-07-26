---
doc_id: "mta-wiki:7030"
title: "PregFind"
source_title: "PregFind"
source_url: "https://wiki.multitheftauto.com/wiki/PregFind"
revision_id: 81173
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:29.728020+00:00"
---

# PregFind

This function stops at the first occurrence of the pattern in the input string and returns the result of the search.

| [[\|link=\|]] | Warning: When declaring a pattern string in quotes, the backslash character should be doubled up. e.g. "\\(" will match a single bracket. |
| --- | --- |
|  |  |

| [[\|link=\|]] | Warning: Multiline flag does not work correctly |
| --- | --- |
|  |  |

## Syntax

```
bool pregFind ( string subject, string pattern [, int/string flags ] )
```

### Required Arguments

- **subject:** The input [string](mta://reference/misc/string.md)

- **pattern:** The pattern [string](mta://reference/misc/string.md) to search for in the input [string](mta://reference/misc/string.md).

### Optional Arguments

- **flags:** Conjuncted value that contains flags ( 1 - ignorecase, 2 - multiline, 4 - dotall, 8 - extended, 16 - unicode ) or ( i - Ignore case, m - Multiline, d - Dotall, e - Extended, u - Unicode )

### Returns

Returns *true* if the pattern was found in the input string, *false* otherwise.

## Example

Click to collapse [-]
Shared ( client and server )

Some examples:

```
addCommandHandler( 'examples',
	function( )
                -- find the first occurrence of 'hello world' in a string
		outputDebugString( pregFind( 'hello world, hello world, hello world', 'hello world' ) and 'found' or 'not found' ) -- found 
                -- find the first occurrence of an integer in a string
                outputDebugString( pregFind( '123', '^-{0,1}\\d+$' ) and 'found' or 'not found' ) -- found
                -- check if the input string consists of at least 3 letters from a to z (both uppercase and lowercase) and does not contain any whitespace characters
                outputDebugString( pregFind( 'Kenix', '^[a-zA-Z]{3,}$' ) and 'found' or 'not found' ) -- found
                -- check if the input string matches the format of a role-play name
                outputDebugString( pregFind( 'Garry_Newman', '([A-Z]{1,1})[a-z]{2,9}_([A-Z]{1,1})[a-z]{2,9}' ) and 'found' or 'not found' ) -- found
                -- example of a search for non-ASCII characters (i.e. cyrillic) - привет
                outputDebugString( pregFind( 'Всем привет парни, ещё раз привет :D', 'привет' ) and 'found' or 'not found' ) -- found
                -- example of a search for a specific sequence of numbers
                outputDebugString( pregFind( '5, 10', '^([1-9]{1}[0-9]{0,})+(((,\s|,)[1-9]{1}[0-9]{0,}){0,1}){1,1}' ) and 'found' or 'not found' ) -- found

                
	end
)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.0-9.07315 | Added flag "u" in regular expressions |
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

- pregFind

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
