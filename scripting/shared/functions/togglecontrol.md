---
doc_id: "mta-wiki:1713"
title: "ToggleControl"
source_title: "ToggleControl"
source_url: "https://wiki.multitheftauto.com/wiki/ToggleControl"
revision_id: 67701
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:58.716694+00:00"
---

# ToggleControl

Enables or disables the use of a GTA control for a specific player.

| [[{{{image}}}\|link=\|]] | Note: If you want to disable weapons fire, remember to also disable the control action in addition to the control fire . |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool toggleControl ( player thePlayer, string control, bool enabled )
```

### Required Arguments

- **thePlayer:** The player you wish to toggle the control ability of.

- **control:** The control that you want to toggle the ability of. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

- **enabled:** A boolean value representing whether or not the key will be usable or not.

Click to collapse [-]
Client

```
bool toggleControl ( string control, bool enabled )
```

### Required Arguments

- **control:** The control that you want to toggle the ability of. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

- **enabled:** A boolean value representing whether or not the key will be usable or not.

## Returns

This function *true* if the control was set successfully, *false* otherwise.

## Example

Click to collapse [-]
Example 1

This function will disable the use of the vehicle secondary-fire key for anyone in a Hydra, consequently removing the ability to fire rockets.

```
function disableFireForHydra ( theVehicle, seat, jacked )
    if ( getElementModel ( theVehicle ) == 520 ) then -- if they entered a hydra
        toggleControl ( source, "vehicle_secondary_fire", false ) -- disable their fire key
    else -- if they entered another vehicle
        toggleControl ( source, "vehicle_secondary_fire", true ) -- enable their fire key
    end
end
addEventHandler ( "onPlayerVehicleEnter", root, disableFireForHydra )
```

Click to collapse [-]
Example 2

This function will disable the use of the vehicle secondary-fire key for anyone in a Hydra, consequently removing the ability to fire rockets.

```
function disableFireForHydra ( theVehicle, seat )
    if ( getElementModel ( theVehicle ) == 520 ) then -- if they entered a hydra
        toggleControl ( "vehicle_secondary_fire", false ) -- disable their fire key
    else -- if they entered another vehicle
        toggleControl ( "vehicle_secondary_fire", true ) -- enable their fire key
    end
end
addEventHandler ( "onClientPlayerVehicleEnter", localPlayer, disableFireForHydra )
```

## See Also

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- [bindKey](mta://scripting/shared/functions/bindkey.md)

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- [getFunctionsBoundToKey](mta://scripting/shared/functions/getfunctionsboundtokey.md)

- [getKeyBoundToFunction](mta://scripting/shared/functions/getkeyboundtofunction.md)

- [isControlEnabled](mta://scripting/shared/functions/iscontrolenabled.md)

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- toggleControl

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
