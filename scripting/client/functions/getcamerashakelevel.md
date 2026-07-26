---
doc_id: "mta-wiki:8360"
title: "GetCameraShakeLevel"
source_title: "GetCameraShakeLevel"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraShakeLevel"
revision_id: 76929
language: "en"
categories: ["Client_functions", "Deprecated", "Changes_in_1.5", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:08.094099+00:00"
---

# GetCameraShakeLevel

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getCameraDrunkLevel instead. Deprecated as of 1.6.0 r21795. |  |

This function gets the camera shake level set by [setCameraShakeLevel](mta://scripting/client/functions/setcamerashakelevel.md).

## Syntax

```
int getCameraShakeLevel ( )
```

### Returns

Returns an integer representing the camera shake level, from 0 (no shaking effect) to 255 (maximum shaking effect). By default, the camera has no shaking effect.

## Example

This example checks for changes in the camera shake level of any player every frame and outputs different messages according to it.

```
local lastDrunkLevel = getCameraShakeLevel()
local function warnPlayerAboutDrunkenness()
    local currentDrunkLevel = getCameraShakeLevel()
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

- [getCameraDrunkLevel](mta://scripting/client/functions/getcameradrunklevel.md)

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
