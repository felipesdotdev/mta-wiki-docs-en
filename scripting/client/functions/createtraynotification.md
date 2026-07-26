---
doc_id: "mta-wiki:9157"
title: "CreateTrayNotification"
source_title: "CreateTrayNotification"
source_url: "https://wiki.multitheftauto.com/wiki/CreateTrayNotification"
revision_id: 82137
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:12:13.731388+00:00"
---

# CreateTrayNotification

This function creates a notification balloon on the desktop.

| [[{{{image}}}\|link=\|]] | Note: MTA won't show any tray notifications if the MTA window is focused, because there is no reason to show tray notifications if you are in-game. If you want to test this function you should use a Timer and switch to your desktop. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: You can only show a tray notification every 30 seconds. |
| --- | --- |
|  |  |

## Syntax

```
bool createTrayNotification ( string notificationText [, string iconType = "default", bool useSound = true ] )
```

 

Tray Notification GIF

### Required Arguments

- **notificationText:** The text to send in the notification.

### Optional Arguments

- **iconType:** The notification icon type. Possible values are: **"default" (the MTA icon), "info", "warning", "error"**

- **useSound:** A boolean value indicating whether or not to play a sound when receiving the notification.

### Returns

Returns *true* if the notification is correctly created, *false* otherwise.

## Examples

```
-- Note: You have to wait 30 seconds before showing another tray notification, there is no queuing

createTrayNotification("Hello World") -- Show a 'Hello World' notification

createTrayNotification("Hello World", "warning") -- Show a notification with a warning symbol

createTrayNotification("Hello World", "default", false) -- Show a default notification without sound
```

Example of notification on minimize MTA application:

```
function setTrayOnMinimize()
     createTrayNotification("We are waiting for you again...", "warning")
end
addEventHandler("onClientMinimize", root, setTrayOnMinimize)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.6-9.16925 | Added support for Windows 10 |
| --- | --- |

## See Also

- createTrayNotification

- [downloadFile](mta://scripting/client/functions/downloadfile.md)

- [getKeyboardLayout](mta://scripting/client/functions/getkeyboardlayout.md)

- [getLocalization](mta://scripting/client/functions/getlocalization.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIp](mta://scripting/client/functions/getserverip.md)

- [isShowCollisionsEnabled](mta://scripting/client/functions/isshowcollisionsenabled.md)

- [isShowSoundEnabled](mta://scripting/client/functions/isshowsoundenabled.md)

- [isTransferBoxAlwaysVisible](mta://scripting/client/functions/istransferboxalwaysvisible.md)

- [isTrayNotificationEnabled](mta://scripting/client/functions/istraynotificationenabled.md)

- [setClipboard](mta://scripting/client/functions/setclipboard.md)

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
