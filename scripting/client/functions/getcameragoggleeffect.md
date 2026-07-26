---
doc_id: "mta-wiki:5450"
title: "GetCameraGoggleEffect"
source_title: "GetCameraGoggleEffect"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraGoggleEffect"
revision_id: 67466
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:15:08.008819+00:00"
---

# GetCameraGoggleEffect

This function returns what goggle effect is currently affecting the camera.

## Syntax

```
string getCameraGoggleEffect (  )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.getGoggleEffect(...)*

**Variable**: *.goggleEffect*

**Counterpart**: *[setCameraGoggleEffect](mta://scripting/client/functions/setcameragoggleeffect.md)*

### Returns

- [String](mta://reference/misc/string.md) indicating the current camera goggle effect. Their meanings can be seen below.

- **normal**: No camera goggle effect

- **nightvision**: Nightvision camera

- **thermalvision**: Infrared camera

## Example

This example adds a command to enable or disable the nightvision effect.

```
function nightvision()
    if (getCameraGoggleEffect() == "normal") then
        setCameraGoggleEffect("nightvision")
    elseif (getCameraGoggleEffect() == "nightvision") then
        setCameraGoggleEffect("normal")
    end
end

addCommandHandler("nightvision", nightvision)
```

## See Also

- [getCamera](mta://scripting/client/functions/getcamera.md)

- [getCameraClip](mta://scripting/client/functions/getcameraclip.md)

- [getCameraFieldOfView](mta://scripting/client/functions/getcamerafieldofview.md)

- getCameraGoggleEffect

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
