---
doc_id: "mta-wiki:6115"
title: "DownloadFile"
source_title: "DownloadFile"
source_url: "https://wiki.multitheftauto.com/wiki/DownloadFile"
revision_id: 50389
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:43.010615+00:00"
---

# DownloadFile

This function ensures the requested resource file is correct and then triggers [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md).  If the file has been previously downloaded and the CRC matches, the file will not be downloaded again but [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md) will still run. The **file** should also be included in the resource meta.xml with the **download** attribute set to "false", see [meta.xml](mta://reference/misc/meta-xml.md) for more details.

| [[{{{image}}}\|link=\|]] | Tip: If you are only using downloadFile to download mod files after other resources, then do not use downloadFile , and instead set '<download_priority_group>-1</download_priority_group>' in the resource meta.xml |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This function may cause performance issues with client and/or server. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: Avoid using fileExists before calling downloadFile . Always call downloadFile and handle the result in onClientFileDownloadComplete |
| --- | --- |
|  |  |

## Syntax

```
bool downloadFile ( string fileName )
```

### Required Arguments

- **fileName**: A string referencing the name of the file to download

### Returns

Returns *true* if file download has been queued, *false* otherwise.

## Example

**Example 1:** This client side event downloads a file when the current resource has started.

```
-- the function is called on resource start
function onThisResourceStart ( )
    downloadFile ( "test.xml" )
end
addEventHandler ( "onClientResourceStart", resourceRoot, onThisResourceStart )
```

## See Also

- [createTrayNotification](mta://scripting/client/functions/createtraynotification.md)

- downloadFile

- [getKeyboardLayout](mta://scripting/client/functions/getkeyboardlayout.md)

- [getLocalization](mta://scripting/client/functions/getlocalization.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIp](mta://scripting/client/functions/getserverip.md)

- [isShowCollisionsEnabled](mta://scripting/client/functions/isshowcollisionsenabled.md)

- [isShowSoundEnabled](mta://scripting/client/functions/isshowsoundenabled.md)

- [isTransferBoxAlwaysVisible](mta://scripting/client/functions/istransferboxalwaysvisible.md)

- [isTrayNotificationEnabled](mta://scripting/client/functions/istraynotificationenabled.md)

- [setClipboard](mta://scripting/client/functions/setclipboard--f18b656d.md)

- [setWindowFlashing](mta://scripting/client/functions/setwindowflashing.md)

- [showCol](mta://scripting/client/functions/showcol.md)

- [showSound](mta://scripting/client/functions/showsound.md)
  

- **Shared**

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
