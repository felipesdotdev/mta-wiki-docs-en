---
doc_id: "mta-wiki:14594"
title: "ToggleAllVehicleControls"
source_title: "ToggleAllVehicleControls"
source_url: "https://wiki.multitheftauto.com/wiki/ToggleAllVehicleControls"
revision_id: 82327
language: "en"
categories: []
---

# ToggleAllVehicleControls

Toggles all vehicle controls for a player based on the provided boolean method (true to enable, false to disable).

## Syntax

```
toggleAllVehicleControls(player, method)
```

### Required Arguments

- **player:** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose vehicle controls will be toggled.

- **method:** A [boolean](mta://reference/misc/boolean.md) indicating whether to enable (true) or disable (false) the controls.

### Returns

Returns false if the method is not a boolean value, otherwise it returns true.

## Code

Click to collapse [-]
Server and Client Side Script

```
local vehicleControls = {
    "vehicle_fire", "vehicle_secondary_fire", "vehicle_left", "vehicle_right",
    "steer_forward", "steer_back", "accelerate", "brake_reverse", "radio_next", "radio_previous", "radio_user_track_skip", "horn", "sub_mission",
    "handbrake", "vehicle_look_left", "vehicle_look_right", "vehicle_look_behind", "vehicle_mouse_look", "special_control_left", "special_control_right",
    "special_control_down", "special_control_up"
}

function toggleAllVehicleControls(player, method)
    if type(method) ~= "boolean" then return false end
    for index, control in ipairs(vehicleControls) do
        toggleControl(player, control, method)
    end
end
```

## Example 1

This example toggles player's vehicle controls off when it entered an Andromeda.

Click to collapse [-]
Server

```
addEventHandler("onPlayerVehicleEnter", root, function(vehicle)
    if getElementModel(vehicle) == 592 then
        toggleAllVehicleControls(source, false)
    end
end)
```

**Author:** [Abolfazl](https://wiki.multitheftauto.com/wiki/User:Abolfazl)
