---
doc_id: "mta-wiki:2273"
title: "GetCameraMode"
source_title: "GetCameraMode"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraMode"
revision_id: 44587
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GetCameraMode

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getCameraTarget instead. |  |

This function returns a [string](mta://reference/misc/string.md) containing the current mode of the player's camera.

## Syntax

```
string getCameraMode ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The player whose camera mode you wish to obtain.

### Returns

Returns a [string](mta://reference/misc/string.md) with one of two values if successful:

- **player:** The camera is attached to a player.

- **fixed:** The camera is in a fixed position.

The function will return *false* if unsuccessful.

## Example

This function checks the camera state of a player, by specifying his name:

```
function checkCamera( source, command, targetName )
      local targetPlayer = getPlayerFromNick ( targetName )   -- Get the player using his name
      outputConsole( targetName.."'s camera mode is: "..getCameraMode( targetPlayer ), source )  -- Output the state of player's camera
end
addCommandHandler( "camera", checkCamera )
```

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
