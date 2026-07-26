---
doc_id: "mta-wiki:2272"
title: "GetCameraPosition"
source_title: "GetCameraPosition"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraPosition"
revision_id: 44586
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:08.069435+00:00"
---

# GetCameraPosition

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getCameraMatrix instead. |  |

This function returns the position that the player's camera would have if the camera mode was fixed (see [setCameraMode](mta://scripting/server/functions/setcameramode.md)).

## Procedural

```
float float float getCameraPosition ()
```

This function returns the X, Y and Z coordinates as three [floats](mta://reference/misc/float.md) if the function was successful, *false* otherwise.

### Example

This page lacks an example.

## Object-oriented

```
Vector3 Camera.getPosition ()
```

This function returns a vector with the coordinates if the function was successful, an empty vector otherwise.

### Example

This page lacks an example.

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
