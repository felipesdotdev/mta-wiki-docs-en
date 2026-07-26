---
doc_id: "mta-wiki:5718"
title: "SetCameraViewMode"
source_title: "SetCameraView"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraView"
revision_id: 72680
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:38.618733+00:00"
---

# SetCameraViewMode

This function allows you to set the camera view modes. This indicates at what distance the camera will follow the player or vehicle.

## Syntax

```
bool setCameraViewMode ( int vehicleCameraMode [, int pedCameraMode ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.setCameraViewMode(...)*

**Variable**: *.viewMode*

**Counterpart**: *[getCameraViewMode](mta://scripting/client/functions/getcameraviewmode.md)*

### Required Arguments

- **vehicleCameraMode**: The view mode you wish to use when inside vehicles.

### Optional Arguments

- **pedCameraMode**: The view mode you wish to use when you are not inside vehicles.

Vehicle Modes:

- **0**: Bumper

- **1**: Close external

- **2**: Middle external

- **3**: Far external

- **4**: Low external

- **5**: Cinematic

Ped Modes:

- **1**: Close

- **2**: Middle

- **3**: Far

### Returns

Returns *true* if the view(s) were set correctly, *false* otherwise.

## Example

This example sets the camera to bumper view when the local player enters any vehicle.

```
addEventHandler("onClientPlayerVehicleEnter", localPlayer, function()
  setCameraViewMode(0)
end)
```

## See Also

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

- setCameraViewMode

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
