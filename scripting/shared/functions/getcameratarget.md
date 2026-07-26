---
doc_id: "mta-wiki:2270"
title: "GetCameraTarget"
source_title: "GetCameraTarget"
source_url: "https://wiki.multitheftauto.com/wiki/GetCameraTarget"
revision_id: 67474
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:08.112346+00:00"
---

# GetCameraTarget

This function returns an [element](mta://reference/misc/element.md) that corresponds to the current target of the specified player's camera (i.e. what it is following).

## Syntax

Click to collapse [-]
Server

```
element getCameraTarget ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getCameraTarget(...)*

**Variable**: *.cameraTarget*

**Counterpart**: *[setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)*

### Required Arguments

- **thePlayer:** The player whose camera you wish to receive the target of.

Click to collapse [-]
Client

```
element getCameraTarget ()
```

### Returns

- Returns an [element](mta://reference/misc/element.md) of the target if the function was successful, or *false* if bad arguments were specified

- Returns *false* if the camera is in Fixed mode and has no target.

## Example

This example checks whether a player's camera's target is another player, and returns true or false accordingly.

Click to collapse [-]
Server script

```
function isTargetPlayer( thePlayer )
    local target = getCameraTarget ( thePlayer )
    if ( getElementType ( target ) == "player" ) then   -- If target is a player
        return true                                     -- Return true
    else
        return false                                    -- Otherwise, return false.
    end
end
```

## See Also

- [fadeCamera](mta://scripting/shared/functions/fadecamera.md)

- [getCameraInterior](mta://scripting/shared/functions/getcamerainterior.md)

- [getCameraMatrix](mta://scripting/shared/functions/getcameramatrix.md)

- getCameraTarget

- [setCameraInterior](mta://scripting/shared/functions/setcamerainterior.md)

- [setCameraMatrix](mta://scripting/shared/functions/setcameramatrix.md)

- [setCameraTarget](mta://scripting/shared/functions/setcameratarget.md)
