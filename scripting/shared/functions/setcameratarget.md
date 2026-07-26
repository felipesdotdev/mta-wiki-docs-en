---
doc_id: "mta-wiki:2265"
title: "SetCameraTarget"
source_title: "SetCameraTarget"
source_url: "https://wiki.multitheftauto.com/wiki/SetCameraTarget"
revision_id: 78885
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.3.1"]
generated_at: "2026-07-26T16:16:38.599184+00:00"
---

# SetCameraTarget

This function allows you to set a player's camera to follow other elements instead. Currently supported element type is:

- [Players](mta://reference/misc/player.md)

- [Peds](mta://reference/misc/ped.md)

- [Vehicles](mta://reference/misc/vehicle.md)

## Syntax

Click to collapse [-]
Server

```
bool setCameraTarget ( player thePlayer [, element target = nil ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):setCameraTarget(...)*

**Variable**: *.cameraTarget*

**Counterpart**: *[getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)*

### Required Arguments

- **thePlayer:** The player whose camera you wish to modify.

### Optional Arguments

- **target:** The element who you want the camera to follow. If none is specified, the camera will target the player.

Click to collapse [-]
Client 1

```
bool setCameraTarget ( element target )
```

### Required Arguments

- **target:** The element who you want the local camera to follow.

Click to collapse [-]
Client 2

This syntax mantains the player targeted by the camera, but makes the camera look at the specified coordinates. It has no effect when the camera doesn't have a target.

```
bool setCameraTarget ( float targetX, float targetY, float targetZ )
```

### Required Arguments

- **targetX, targetY, targetZ:** The target position that you want the local camera to look at.

### Returns

Returns *true* if the function was successful, *false* otherwise.

## Example

This is an example of how one could implement a spectator function. Using the left and right arrow keys you can view other players. Note that this code isn't complete as it doesn't take into account joining or quitting players.

Click to collapse [-]
Client script

```
g_Players = getElementsByType("player")        -- get a list of all players in the server
for i,aPlayer in ipairs(g_Players) do          -- find out what index the local player has in the list
    if aPlayer == localPlayer then
        g_CurrentSpectated = i
        break
    end
end

function spectatePrevious()                    -- decrement the spectate index and spectate the corresponding player
     if g_CurrentSpectated == 1 then
         g_CurrentSpectated = #g_Players
     else
         g_CurrentSpectated = g_CurrentSpectated - 1
     end
    setCameraTarget(g_Players[g_CurrentSpectated])
end

function spectateNext()                        -- increment the spectate index and spectate the corresponding player
     if g_CurrentSpectated == #g_Players then
         g_CurrentSpectated = 1
     else
         g_CurrentSpectated = g_CurrentSpectated + 1
     end
    setCameraTarget(g_Players[g_CurrentSpectated])
end

-- Bind above functions to arrow keys
bindKey("arrow_l", "down", spectatePrevious)
bindKey("arrow_r", "down", spectateNext)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.8-9.20683 | Added support for vehicle and ped types |
| --- | --- |

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- [getCameraTarget](mta://scripting/shared/functions/getcameratarget.md)

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- setCameraTarget
