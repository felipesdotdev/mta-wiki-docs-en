---
doc_id: "mta-wiki:2269"
title: "SetCameraMode"
source_title: "SetCameraMode"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraMode"
revision_id: 40349
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# SetCameraMode

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setCameraTarget instead. |  |

| [[{{{image}}}\|link=\|]] | Note: remember to set players camera mode back to "player" on resource unload, or you will encounter the invisible player 'bug' if players camera is still set to fixed. |
| --- | --- |
|  |  |

This function allows you to set a player's camera to either follow him or be fixed at a certain position.

## Syntax

```
bool setCameraMode ( player thePlayer, string mode )
```

### Required Arguments

- **thePlayer:** The player whose camera you wish to modify.

- **mode:** The mode to be set. It has the following possible values:

- **"player":** Sets the camera to follow a player.

- **"fixed":** Fixes the camera in a set position/rotation.

### Returns

Returns a [bool](https://wiki.multitheftauto.com/index.php?search=bool) with a value of *true* if the function was successful, *false* otherwise.

## Example

```
function spawnScreen ( source )
        setCameraMode ( source, "fixed" )                                     -- Make the camera fixed (instead of following the player)
        setTimer ( setCameraPosition, 1000, 1, source, 160.15, -1951.68, 50 ) -- Set the coordinates of the camera
        setTimer ( setCameraLookAt, 1000, 1, source, 165, -1951.68, 50 )      -- Make the camera look at specified coordinates
        bindKey ( source, "F1", "down", "Spawn as Vagos", spawnVagos )        -- Bind spawn key (function spawnVagos is not given here)
        bindKey ( source, "F2", "down", "Spawn as Aztecs", spawnAztecs )      -- Bind spawn key (function spawnAztecs is not given here)
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
