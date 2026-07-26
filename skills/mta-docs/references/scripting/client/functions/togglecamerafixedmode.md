---
doc_id: "mta-wiki:2655"
title: "ToggleCameraFixedMode"
source_title: "ToggleCameraFixedMode"
source_url: "https://wiki.multitheftauto.com/wiki/ToggleCameraFixedMode"
revision_id: 18167
language: "en"
categories: ["Client_functions", "Deprecated"]
---

# ToggleCameraFixedMode

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions, but there should be a more generic way to perform what it does. |
| --- | --- |
|  |  |

This function toggles the camera mode between a fixed view and the default player chase view. The camera's position and rotation in fixed mode can be set with the [setCameraPosition](mta://scripting/shared/functions/setcameraposition.md) and [setCameraLookAt](mta://scripting/shared/functions/setcameralookat.md) functions respectively.

## Syntax

```
bool toggleCameraFixedMode ( bool fixed )
```

### Required Arguments

- **fixed:** A boolean indicating the camera mode; *true* for fixed view, *false* for chase view.

### Returns

Returns a [bool](https://wiki.multitheftauto.com/index.php?search=bool) with a value of *true* if the function was successful, *false* otherwise.

## Example

**Example 1:** This example sets the player's camera above Blueberry Acres at a downward angle:

```
toggleCameraFixedMode(true)
setCameraPosition(-16.268127441406, -46.674671173096, 29.565118789673)
setCameraLookAt(-68.21085357666, 34.687622070313, 11.11138343811)
```

**Example 2:** This example points the player's camera at the killer whenever the player dies:

```
local thePlayer = getLocalPlayer() -- get the player running this client-side script
-- add an event handler to call the onDeath function whenever the player dies
function onDeath(theAttacker, weapon, bodypart)
    if (theAttacker and theAttacker ~= thePlayer) then -- make sure there is a killer
        -- store the position of the victim and killer
        local playerX, playerY, playerZ = getElementPosition(thePlayer)
        local attackerX, attackerY, attackerZ = getElementPosition(theAttacker)
        -- set the player's camera to fixed view
        toggleCameraFixedMode(true)
        -- set the camera's position at the player and in the killer's direction
        setCameraPosition(playerX, playerY, playerZ)
        setCameraLookAt(attackerX, attackerY, attackerZ)
        -- set the camera back to normal after 3 seconds
        setTimer(toggleCameraFixedMode, 3000, 1, false)
    end
end
addEventHandler("onClientPlayerWasted", thePlayer, onDeath)
```

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
