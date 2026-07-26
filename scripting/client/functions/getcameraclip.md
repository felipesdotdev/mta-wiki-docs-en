---
doc_id: "mta-wiki:8122"
title: "GetCameraClip"
source_title: "GetCameraClip"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraClip"
revision_id: 67461
language: "en"
categories: ["Client_functions", "Changes_in_1.4.1", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:07.952274+00:00"
---

# GetCameraClip

This function checks if the camera will "collide" with any objects or vehicles in its way. Read more about this [here](mta://scripting/client/functions/setcameraclip.md).

## Syntax

```
bool, bool getCameraClip()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Camera](mta://scripting/client/functions/camera.md).getClip(...)*

**Counterpart**: *[setCameraClip](mta://scripting/client/functions/setcameraclip.md)*

### Returns

- **objects:** if you want the camera to clip on objects.

- **vehicles:** if you want the camera to clip on vehicles.

## Example

This function checks the clip status.

```
function checkClipStatus()
  local obj, veh = Camera.getClip()
  outputChatBox ("Your camera can" .. (veh and "" or "not") .. "see the vehicle interior at the moment!",255,0,0,false)
  outputChatBox ("Your camera can" .. (obj and "" or "not") .. "collide with objects at the moment!",255,0,0,false)
end
addEventHandler("clipstatus",checkClipStatus)
```

## See Also

- [getCamera](mta://scripting/client/functions/getcamera.md)

- getCameraClip

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
