---
doc_id: "mta-wiki:2271"
title: "GetCameraRotation"
source_title: "GetCameraRotation"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraRotation"
revision_id: 55466
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:08.077681+00:00"
---

# GetCameraRotation

|  | Warning: This function no longer exists . However, below is a function that achieves a similar result. |
| --- | --- |
|  |  |

```
local CAM = getCamera()--The camera is always the same element, so use this local variable to save cpu power.
function getCameraRotation ()
    return getElementRotation(CAM) --rx, ry, rz
end
```

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
