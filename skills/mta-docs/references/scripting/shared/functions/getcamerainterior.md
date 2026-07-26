---
doc_id: "mta-wiki:3843"
title: "GetCameraInterior"
source_title: "GetCameraInterior"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraInterior"
revision_id: 68879
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetCameraInterior

Returns the interior of the local camera (independent of the interior of the local player).

## Procedural

### Syntax

Click to collapse [-]
Server

```
int getCameraInterior ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):getCameraInterior(...)*

**Variable**: *.cameraInterior*

**Counterpart**: *[setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)*

### Required Arguments

- **thePlayer**: The player whose camera interior you want to get.

Click to collapse [-]
Client

```
int getCameraInterior ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Camera.getInterior(...)*

**Variable**: *.interior*

**Counterpart**: *[setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)*

### Returns

Returns an *integer* indicating the camera's interior, *false* if the argument is invalid.

### Example

Click to collapse [-]
Server

```
function outputCameraInterior ( player, command )
	local interior = getCameraInterior ( player )
	outputChatBox ( "The camera is in the interior " .. interior, player, 255, 255, 0 )
end
addCommandHandler ( "camera", outputCameraInterior )
```

## Object-oriented

### Syntax

Click to collapse [-]
Server

```
int player:getCameraInterior ( )
-- or
int player.cameraInterior -- to get the camera interior value
player.cameraInterior = int someValue -- to set the camera interior value
```

Click to collapse [-]
Client

```
int Camera.getInterior ( )
```

Returns an *integer* indicating the camera's interior, *false* if the argument is invalid.

### Example

Click to collapse [-]
Client

```
function outputCameraInterior ( command )
	local interior = Camera.getInterior ( )
	outputChatBox ( "The camera is in the interior " .. interior, localPlayer, 255, 255, 0 )
end
addCommandHandler ( "camera", outputCameraInterior )
```

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- getCameraInterior

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
