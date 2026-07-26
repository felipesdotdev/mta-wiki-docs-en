---
doc_id: "mta-wiki:2266"
title: "SetCameraLookAt"
source_title: "SetCameraLookAt"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraLookAt"
revision_id: 44584
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:38.507378+00:00"
---

# SetCameraLookAt

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setCameraMatrix instead. |  |

This function allows you to set a player's camera to look at a specific point when the camera is fixed (see [setCameraMode](mta://scripting/server/functions/setcameramode.md)).

## Syntax

```
bool setCameraLookAt ( player thePlayer, float x, float y, float z )
```

### Required Arguments

- **thePlayer:** The player whose camera you wish to modify. (not needed for clientside scripting)

- **x:** The x coordinate of the point to be looked at.

- **y:** The y coordinate of the point to be looked at.

- **z:** The z coordinate of the point to be looked at.

### Returns

Returns *true* if the function was successful, *false* otherwise.

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
