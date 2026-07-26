---
doc_id: "mta-wiki:5429"
title: "GetCameraViewMode"
source_title: "GetCameraViewMode"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraViewMode"
revision_id: 72713
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# GetCameraViewMode

This function allows you to get the active camera view modes. This indicates at what distance the camera will follow the player or vehicle.

## Syntax

```
int, int getCameraViewMode ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.getCameraViewMode(...)*

**Variable**: *.viewMode*

**Counterpart**: *[setCameraViewMode](mta://scripting/client/functions/setcameraviewmode.md)*

### Returns

BEFORE VERSION 1.5.8 [r20851](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=20851):

Returns an [int](mta://reference/misc/int.md) indicating the current vehicle camera view mode. Their meanings can be seen below.

Returns two [ints](mta://reference/misc/int.md) indicating the current vehicle and ped camera view mode respectively. Their meanings can be seen below.

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

## Example

This example tells the player their current camera view when they change it

```
function onPlayerSpawn(theSpawnpoint)
    currentCam("fire") -- start a repeating check
end
addEventHandler("onClientPlayerSpawn", root, onPlayerSpawn)

function currentCam(key)
   if (getControlState(key)) then
      local vehicleMode, pedMode = getCameraViewMode()
      outputChatBox("Your current cam view is: " .. vehicleMode .. ".")
   end
end
```

## See Also

- [getCamera](mta://scripting/client/functions/getcamera.md)

- [getCameraClip](mta://scripting/client/functions/getcameraclip.md)

- [getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)

- [getCameraGoggleEffect](mta://scripting/client/functions/getcameragoggleeffect.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

- [getCameraDrunkLevel](mta://scripting/client/functions/getcameradrunklevel.md)

- getCameraViewMode

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
