---
doc_id: "mta-wiki:8348"
title: "GetCameraFieldOfView"
source_title: "GetCameraFieldOfView"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraFieldOfView"
revision_id: 82189
language: "en"
categories: ["Client_functions", "Changes_in_1.5.1", "Changes_in_1.6.0"]
---

# GetCameraFieldOfView

This function returns the field of view of the *dynamic camera* as set by [setCameraFieldOfView](mta://scripting/client/functions/setcamerafieldofview.md).

## Syntax

```
float getCameraFieldOfView ( string cameraMode )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.getFieldOfView(...)*

**Variable**: *.fov*

**Counterpart**: *[setCameraFieldOfView](mta://scripting/client/functions/setcamerafieldofview.md)*

### Required Arguments

- **cameraMode:** the camera mode to get the field of view of:

- "player": whilst walking/running

- "vehicle": whilst in vehicle

- "vehicle_max": the max the field of view can go to when the vehicle is moving at a high speed (must be higher than "vehicle")

### Returns

Returns one float - the field of view angle

## Example

In this example, the field of view is output to the chat whenever the /getfov command is written

```
function getCamFOV()
    outputChatBox("The camera field of view for 'player walking/running' is: " .. getCameraFieldOfView("player"))
end
addCommandHandler("getfov", getCamFOV)
```

## See Also

- [getCamera](mta://scripting/client/functions/getcamera.md)

- [getCameraClip](mta://scripting/client/functions/getcameraclip.md)

- getCameraFieldOfView

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
