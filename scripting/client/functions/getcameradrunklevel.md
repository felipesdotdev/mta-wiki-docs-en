---
doc_id: "mta-wiki:14070"
title: "GetCameraDrunkLevel"
source_title: "GetCameraDrunkLevel"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraDrunkLevel"
revision_id: 76927
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:07.971161+00:00"
---

# GetCameraDrunkLevel

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

This function gets the camera drunk level set by [setCameraDrunkLevel](mta://scripting/client/functions/setcameradrunklevel.md). This function was renamed from [getCameraShakeLevel](mta://scripting/client/functions/getcamerashakelevel.md). 

## Syntax

```
int getCameraDrunkLevel ( )
```

### Returns

Returns an integer representing the camera drunk level, from 0 (no drunk effect) to 255 (maximum drunk effect). By default, the camera has no drunk effect. Drunk effect is a wavy motion of the camera depicting the player being drunk. This function used to be called [getCameraShakeLevel](mta://scripting/client/functions/getcamerashakelevel.md) which has since been deprecated.

## Example

This example checks for changes in the camera drunk level of any player every frame and outputs different messages according to it.

```
local lastDrunkLevel = getCameraDrunkLevel()
local function warnPlayerAboutDrunkenness()
    local currentDrunkLevel = getCameraDrunkLevel()
    if currentDrunkLevel ~= lastDrunkLevel and (currentDrunkLevel == 0 or currentDrunkLevel == 255) then
        outputChatBox(currentDrunkLevel == 255 and "You're completly drunk! You should stop drinking!" or "Now you are completely sober! You sohuld keep it like that.", currentDrunkLevel == 255 and 255 or 0, currentDrunkLevel == 0 and 255 or 0, 0)
    end
    lastDrunkLevel = currentDrunkLevel
end
addEventHandler("onClientRender", root, warnPlayerAboutDrunkenness)
```

## See also

- [getCamera](mta://scripting/client/functions/getcamera.md)

- [getCameraClip](mta://scripting/client/functions/getcameraclip.md)

- [getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)

- [getCameraGoggleEffect](mta://scripting/client/functions/getcameragoggleeffect.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

- getCameraDrunkLevel

- [getCameraViewMode](mta://scripting/client/functions/getcameraviewmode.md)

- [setCameraClip](mta://scripting/client/functions/setcameraclip.md)

- [setCameraFieldOfView](mta://scripting/client/functions/setcamerafieldofview.md)

- [setCameraGoggleEffect](mta://scripting/client/functions/setcameragoggleeffect.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

- [setCameraDrunkLevel](mta://scripting/client/functions/setcameradrunklevel.md)

- [setCameraViewMode](mta://scripting/client/functions/setcameraviewmode.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22631](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22631):

- [shakeCamera](mta://scripting/client/functions/shakecamera.md)

- [resetShakeCamera](mta://scripting/client/functions/resetshakecamera.md)

- **Shared**

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
