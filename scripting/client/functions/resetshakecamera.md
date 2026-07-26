---
doc_id: "mta-wiki:14385"
title: "ResetShakeCamera"
source_title: "ResetShakeCamera"
source_url: "https://wiki.multitheftauto.com/wiki/ResetShakeCamera"
revision_id: 81864
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:33.559752+00:00"
---

# ResetShakeCamera

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22631](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22631))

This function cancels the shaking effect caused by **shakeCamera**

## Syntax

```
bool resetShakeCamera ( )
```

### Returns

Always returns *true*.

## Example

This example allows you to trigger huge camera shake effect near you and then cancels the effect after 5 seconds.

```
addCommandHandler('doShake', function()
    shakeCamera(100)
    setTimer(resetShakeCamera, 5000, 1)
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

- [setCameraViewMode](mta://scripting/client/functions/setcameraviewmode.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22631](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22631):

- [shakeCamera](mta://scripting/client/functions/shakecamera.md)

- resetShakeCamera

- **Shared**

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
