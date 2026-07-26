---
doc_id: "mta-wiki:3917"
title: "GetCameraMatrix"
source_title: "GetCameraMatrix"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraMatrix"
revision_id: 82235
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetCameraMatrix

This function gets the position of the camera and the position of the point it is facing.

| [[{{{image}}}\|link=\|]] | Important Note: Server-side this functions returns false or the latest value set via setCameraMatrix (called from server or client.) So if you never used setCameraMatrix on serverside for that player, then it will return false. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
float float float float float float float float getCameraMatrix ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):getCameraMatrix(...)*

**Variable**: *.cameraMatrix*

**Counterpart**: *[setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)*

### Required Arguments

- **thePlayer:** The player whose camera matrix is to be returned.

Click to collapse [-]
Client

```
float float float float float float float float getCameraMatrix ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Camera](https://wiki.multitheftauto.com/index.php?search=Camera).getMatrix(...)*

**Variable**: *.matrix*

**Counterpart**: *[setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)*

### Returns

This function returns 8 [floats](mta://reference/misc/float.md) if the argument is valid (when applicable); the first three indicate the position of the camera, the next three indicate the position of the point it's facing, and the last two are the roll and field of view. Returns *false* if the argument is invalid.

### Example

Click to collapse [-]
Client

```
local x, y, z, lx, ly, lz = getCameraMatrix ()
x, lx = x + 1, lx + 1

setCameraMatrix (x, y, z, lx, ly, lz)
```

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- getCameraMatrix

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
