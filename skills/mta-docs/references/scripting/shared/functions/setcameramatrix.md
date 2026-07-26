---
doc_id: "mta-wiki:3916"
title: "SetCameraMatrix"
source_title: "SetCameraMatrix"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraMatrix"
revision_id: 67478
language: "en"
categories: ["Changes_in_1.4.1", "Server_functions", "Client_functions"]
---

# SetCameraMatrix

This function sets the camera's position and direction. The first three arguments are the point at which the camera lies, the last three are the point the camera faces (or the point it "looks at").

| [[{{{image}}}\|link=\|]] | Note: Calling this function takes the camera's focus away from the player and sets the camera in a fixed position and rotation. The camera's focus can be brought back to the player using the setCameraTarget function. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool setCameraMatrix ( player thePlayer, float positionX, float positionY, float positionZ [, float lookAtX, float lookAtY, float lookAtZ, float roll = 0, float fov = 70 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setCameraMatrix(...)*

**Variable**: *.cameraMatrix*

**Counterpart**: *[getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)*

### Required Arguments

- **thePlayer:** The player whose camera is to be changed.

- **positionX:** The x coordinate of the camera's position.

- **positionY:** The y coordinate of the camera's position.

- **positionZ:** The z coordinate of the camera's position.

- **Instead of six coordinates, or two vectors, a Matrix can be supplied.**

### Optional Arguments

- **lookAtX:** The x coordinate of the point the camera faces.

- **lookAtY:** The y coordinate of the point the camera faces.

- **lookAtZ:** The z coordinate of the point the camera faces.

- **roll:** The camera roll angle, -180 to 180. A value of 0 means the camera sits straight, positive values will turn it counter-clockwise and negative values will turn it clockwise. -180 or 180 means the camera is upside down.

- **fov:** the field of view angle, 0.01 to 180. The higher this value is, the more you will be able to see what is to your sides.

Click to collapse [-]
Client

```
bool setCameraMatrix ( float positionX, float positionY, float positionZ [, float lookAtX, float lookAtY, float lookAtZ, float roll = 0, float fov = 70 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This is under the static class **Camera***

**Method**: *Camera.setMatrix(...)*

**Variable**: *.matrix*

**Counterpart**: *[getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)*

### Required Arguments

- **positionX:** The x coordinate of the camera's position.

- **positionY:** The y coordinate of the camera's position.

- **positionZ:** The z coordinate of the camera's position.

- **Instead of six coordinates, or two vectors, a Matrix can be supplied.**

### Optional Arguments

- **lookAtX:** The x coordinate of the point the camera faces.

- **lookAtY:** The y coordinate of the point the camera faces.

- **lookAtZ:** The z coordinate of the point the camera faces.

- **roll:** The camera roll angle, -180 to 180. A value of 0 means the camera sits straight, positive values will turn it counter-clockwise and negative values will turn it clockwise. -180 or 180 means the camera is upside down.

- **fov:** the field of view angle, 0.01 to 180. The higher this value is, the more you will be able to see what is to your sides.

### Returns

Returns *true* if the arguments are valid, *false* otherwise.

## Example

This code fixates the camera onto the Vinewood sign in Los Santos for any player that joins the server:

Click to collapse [-]
Server script

```
function setCameraOnPlayerJoin()
     -- slowly fade the camera in to make the screen visible
     fadeCamera(source, true, 5)
     -- set the player's camera to a fixed position, looking at a fixed point
     setCameraMatrix(source, 1468.8785400391, -919.25317382813, 100.153465271, 1468.388671875, -918.42474365234, 99.881813049316)
end
addEventHandler("onPlayerJoin", root, setCameraOnPlayerJoin)
```

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- setCameraMatrix

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
