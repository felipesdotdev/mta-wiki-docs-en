---
doc_id: "mta-wiki:7406"
title: "GetCamera"
source_title: "GetCamera"
source_url: "https://wiki.multitheftauto.com/wiki/GetCamera"
revision_id: 67459
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# GetCamera

This function returns an [element](mta://reference/misc/element.md) that corresponds to the game camera

| [[{{{image}}}\|link=\|]] | Note: Using attachElements with the camera and the main player can interfere with movement |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Using setElementPosition/Rotation/Matrix on the camera element will automatically clear any target set with setCameraTarget |
| --- | --- |
|  |  |

## Syntax

```
element getCamera ()
```

### Returns

Returns an [element](mta://reference/misc/element.md) that corresponds to the game camera

## Example

This example attaches (fixes) the camera to a vehicle.

```
local cam = getCamera()
setElementPosition( cam, 0,0,0 )  -- Clear camera target
local myVehicle = getPedOccupiedVehicle(localPlayer)
attachElements( cam, myVehicle, 0,-4,2, -20,0,0 )
```

## See Also

- getCamera

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
