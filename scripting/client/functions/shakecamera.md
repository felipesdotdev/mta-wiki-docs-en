---
doc_id: "mta-wiki:14382"
title: "ShakeCamera"
source_title: "ShakeCamera"
source_url: "https://wiki.multitheftauto.com/wiki/ShakeCamera"
revision_id: 79966
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:50.407620+00:00"
---

# ShakeCamera

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22631](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22631))

This function allows you to trigger camera shake effect (just like explosion does).

| [[{{{image}}}\|link=\|]] | Note: The camera shaking duration depends on the force. High values ​​can result in very long durations |
| --- | --- |
|  |  |

## Syntax

```
bool shakeCamera ( float force, [ float x, float y, float z ] )
```

### Required arguments

- **force**: Intensity and time of the shake. The higher the value, the longer the camera shakes

### Optional Arguments

- **x:** Center X coordinate of the shake.

- **y:** Center Y coordinate of the shake.

- **z:** Center Z coordinate of the shake.

If not given, it will defaults to local player position.

### Returns

Always returns *true*.

## Example

This example allows you to constantly trigger camera shake effect in center of the map, the closer you are to center the stronger effect will be.

```
local shakeStrength = 1.4 -- define strength of the camera shake
local shakePosX, shakePosY, shakePosZ = 0, 0, 3 -- define position where camera shake would happen

function triggerCameraShake()
	shakeCamera(shakeStrength, shakePosX, shakePosY, shakePosZ) -- trigger camera shake
end
setTimer(triggerCameraShake, 100, 0) -- call this function indefinitely, every 100 ms
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

- [setCameraViewMode](mta://scripting/client/functions/setcameraviewmode.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22631](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22631):

- shakeCamera

- [resetShakeCamera](mta://scripting/client/functions/resetshakecamera.md)

- **Shared**

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
