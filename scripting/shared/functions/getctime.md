---
doc_id: "mta-wiki:3448"
title: "GetRealTime"
source_title: "GetCTime"
source_url: "https://wiki.multitheftauto.com/wiki/GetCTime"
revision_id: 75377
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.4.1"]
generated_at: "2026-07-26T16:15:07.916941+00:00"
---

# GetRealTime

This function gets the server or client (if used client sided it returns time as set on client's computer) real time and returns it in a table. If you want to get the in-game time (shown on GTA's clock) use [getTime](mta://scripting/shared/functions/gettime.md).

## Syntax

```
table getRealTime( [ int seconds = current, bool localTime = true ] )
```

### Optional Arguments

- **seconds:** A count in seconds from the year 1970.  Useful for storing points in time, or for retrieving time information for [getBanTime](mta://scripting/server/functions/getbantime.md). The valid range of this argument is 0 to 32,000,000,000

- **localTime:** Set to *true* to adjust for the locally set timezone.

### Returns

Returns a *table* of substrings with different time format or *false* if the **seconds** argument is out of range.

| Member | Meaning | Range |
| --- | --- | --- |
| second | seconds after the minute | 0-61* |
| minute | minutes after the hour | 0-59 |
| hour | hours since midnight | 0-23 |
| monthday | day of the month | 1-31 |
| month | months since January | 0-11 |
| year | years since 1900 |  |
| weekday | days since Sunday | 0-6 |
| yearday | days since January 1 | 0-365 |
| isdst | Daylight Saving Time flag |  |
| timestamp | seconds since 1970 (Ignoring set timezone) |  |

** second* is generally 0-59. Extra range to accommodate for leap seconds in certain systems.

## Remarks

The **seconds** parameter can be left out entirely while still using the **localTime** parameter. To achieve that simply pass the boolean localTime parameter as first argument where you would otherwise pass the **seconds** parameter. This way you can retrieve a current timepoint that is not denoted in local time.

## Example

This example adds 'showtime' like the default MTA 'time' command:

```
function showtime ()
    local time = getRealTime()
    local hours = time.hour
    local minutes = time.minute
    local seconds = time.second

    -- use string.format to keep it 2 digits. eg 1 will be converted to 01
    outputChatBox ( string.format("Local Time: %02d:%02d:%02d",  hours, minutes, seconds) )
end
addCommandHandler("showtime", showtime)
```

Example with year, month, monthday using string.format:

```
function showtime ()
	local time = getRealTime()
	local hours = time.hour
	local minutes = time.minute
	local seconds = time.second

        local monthday = time.monthday
	local month = time.month
	local year = time.year

        local formattedTime = string.format("%04d-%02d-%02d %02d:%02d:%02d", year + 1900, month + 1, monthday, hours, minutes, seconds)
	outputChatBox ( "Local Time: ".. formattedTime )
end
addCommandHandler("showtime", showtime)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.4.0-9.06976 | Added localTime argument |
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

- getRealTime

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
