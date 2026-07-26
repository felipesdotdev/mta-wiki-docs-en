---
doc_id: "mta-wiki:8347"
title: "SetCameraFieldOfView"
source_title: "SetCameraFieldOfView"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraFieldOfView"
revision_id: 82577
language: "en"
categories: ["Client_functions", "Changes_in_1.5.1", "Utility_templates", "Changes_in_1.6.0"]
---

# SetCameraFieldOfView

This function sets the field of view of the *dynamic camera* - this is the field of view of the *non-fixed camera* - yes, the camera that the user can control whilst on foot or in a vehicle. The higher the field of view angle, the more you will be able to see to your sides.

| [[{{{image}}}\|link=\|]] | Note: This function omits (but doesn't override) the user game option in Settings -> Video -> FOV |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: It doesn't affect the FOV for the following camera modes: 1) Player aiming 2) Vehicle front bumper camera 3) Fixed camera |
| --- | --- |
|  |  |

## Syntax

```
bool setCameraFieldOfView ( string cameraMode, float fieldOfView [, bool instant = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.setFieldOfView(...)*

**Counterpart**: *[getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)*

### Required Arguments

**Note:** after 100, some unexpected things may happen to the camera, particularly in vehicles, use carefully!

- **cameraMode:** the camera mode to set the field of view of:

- "player": whilst walking/running

- "vehicle": whilst in vehicle

- "vehicle_max": the max the field of view can go to when the vehicle is moving at a high speed (must be higher than "vehicle" | the normal difference between "vehicle" and "vehicle_max" is 10)

- **fieldOfView:** The field of view angle, 0 to 179.

### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

ADDED/UPDATED IN VERSION 1.6.0 [r23300](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23300):

- **instant**: If set to *true*, the value is applied immediately, without delay (does not work with "vehicle_max").

### Returns

Returns *true* if the arguments are valid, *false* otherwise.

## Example

In this example, the field of view for 'player walking/running' camera is set to 20, once resource fully starts.

```
local function changeCameraFovOnClientResourceStart()
    setCameraFieldOfView("player", 20)
end
addEventHandler("onClientResourceStart", resourceRoot, changeCameraFovOnClientResourceStart)
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

- setCameraFieldOfView

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
