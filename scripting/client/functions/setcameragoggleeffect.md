---
doc_id: "mta-wiki:5451"
title: "SetCameraGoggleEffect"
source_title: "SetCameraGoggleEffect"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraGoggleEffect"
revision_id: 78518
language: "en"
categories: ["Client_functions", "Changes_in_1.5.5", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:38.472641+00:00"
---

# SetCameraGoggleEffect

This function allows you to set the camera's current goggle effect. This means you can activate nightvision or infrared effects by script

## Syntax

```
bool setCameraGoggleEffect ( string goggleEffect [, bool noiseEnabled = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.setGoggleEffect(...)*

**Variable**: *.goggleEffect*

**Counterpart**: *[getCameraGoggleEffect](mta://scripting/client/functions/getcameragoggleeffect.md)*

### Required Arguments

- **goggleEffect:** the goggle effect you wish to set

- **normal**: No camera goggle effect

- **nightvision**: Nightvision camera

- **thermalvision**: Infrared camera

- **noiseEnabled:** whether or not there should be a fuzzy noise effect

### Returns

- *true* if the effect was set correctly.

- *false* otherwise.

## Example

```
function nightvision()
   local effect = (getCameraGoggleEffect() == "normal") and "nightvision" or "normal"
   setCameraGoggleEffect(effect)
end
addCommandHandler("nightvision", nightvision)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.5-9.13999 | Added noiseEnabled argument |
| --- | --- |

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

- setCameraGoggleEffect

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
