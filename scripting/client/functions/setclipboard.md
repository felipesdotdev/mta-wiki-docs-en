---
doc_id: "mta-wiki:5815"
title: "SetClipboard"
source_title: "SetClipBoard"
source_url: "https://wiki.multitheftauto.com/wiki/SetClipBoard"
revision_id: 71435
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:38.792497+00:00"
---

# SetClipboard

This function sets the players clipboard text (what appears when you paste with CTRL + V)

## Syntax

```
bool setClipboard ( string theText )
```

### Required Arguments

- **theText:** The new text to be in the players clipboard when the player pastes with CTRL + V.

### Returns

Returns *true* if the text in the clip board was set correctly.

## Example

This example adds a command called clipboard which lets you set your clipboard text.

```
addCommandHandler( "clipboard", -- add a command handler for the command
   function( command, ... )
      local text = table.concat({...}, " ") -- if the text has spaces this will turn it into a string
      local success = setClipboard( text ) -- set the clipboard and find out if it worked
      if success then
         outputChatBox( "Clipboard text set to: " .. text, 0, 255, 0 ) -- if it did, tell the player
      else
         outputChatBox( "Failed to set the clipboards text", 255, 0, 0 ) -- if it didn't, tell the player
      end
   end
)
```

This example is to allow you to copy the words that are written in edit box

```
window = guiCreateWindow(47, 105, 262, 56, "example By ProGamer", false) 
edit = guiCreateEdit(47, 105, 262, 56, "", false, window)  
button1 = guiCreateButton(58, 220, 234, 46, "copy", false, window)

function clickedButton1()
    local text = guiGetText(edit)
    setClipboard(text)
end
addEventHandler("onClientGUIClick", button1, clickedButton1, false)
```

## See Also

- [createTrayNotification](mta://scripting/client/functions/createtraynotification.md)

- [downloadFile](mta://scripting/client/functions/downloadfile.md)

- [getKeyboardLayout](mta://scripting/client/functions/getkeyboardlayout.md)

- [getLocalization](mta://scripting/client/functions/getlocalization.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIp](mta://scripting/client/functions/getserverip.md)

- [isShowCollisionsEnabled](mta://scripting/client/functions/isshowcollisionsenabled.md)

- [isShowSoundEnabled](mta://scripting/client/functions/isshowsoundenabled.md)

- [isTransferBoxAlwaysVisible](mta://scripting/client/functions/istransferboxalwaysvisible.md)

- [isTrayNotificationEnabled](mta://scripting/client/functions/istraynotificationenabled.md)

- setClipboard

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
