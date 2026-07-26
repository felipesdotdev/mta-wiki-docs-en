---
doc_id: "mta-wiki:4957"
title: "SetCameraClip"
source_title: "SetCameraClip"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraClip"
revision_id: 73703
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# SetCameraClip

This function sets if the camera will "collide" with any objects or vehicles in its way. This means that if object clip is enabled an object is in the way of where the camera actually wants to be, the camera will try to be in front of it. This function can disable that.

## Syntax

```
bool setCameraClip ( [ bool objects = true, bool vehicles = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Camera](https://wiki.multitheftauto.com/index.php?search=Camera).setClip(...)*

**Counterpart**: *[getCameraClip](mta://scripting/client/functions/getcameraclip.md)*

### Optional Arguments

- **objects:** Sets if you want the camera to clip on objects.

- **vehicles:** Sets if you want the camera to clip on vehicles.

### Returns

Always returns *true*.

## Example

This function enables it to look through cars

```
function enableCameraThoughCars ()
  setCameraClip (true,false)
  outputChatBox ("Your camera can see the vehicle interior now!",255,0,0,false)
end
addEventHandler ("onClientResourceStart",resourceRoot,enableCameraThoughCars)
```

## See Also

- [getCamera](mta://scripting/client/functions/getcamera.md)

- [getCameraClip](mta://scripting/client/functions/getcameraclip.md)

- [getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)

- [getCameraGoggleEffect](mta://scripting/client/functions/getcameragoggleeffect.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21795](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21795):

- [getCameraDrunkLevel](mta://scripting/client/functions/getcameradrunklevel.md)

- [getCameraViewMode](mta://scripting/client/functions/getcameraviewmode.md)

- setCameraClip

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
