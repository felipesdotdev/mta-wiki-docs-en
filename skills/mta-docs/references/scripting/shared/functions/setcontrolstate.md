---
doc_id: "mta-wiki:1715"
title: "SetControlState"
source_title: "SetControlState"
source_url: "https://wiki.multitheftauto.com/wiki/SetControlState"
revision_id: 79209
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetControlState

Sets a state of a specified player's control, as if they pressed or released it.

## Syntax

```
bool setControlState ( player thePlayer, string control, bool state )
```

### Required Arguments

- **thePlayer:** The player you wish to set the control state of.

- **control:** The control that you want to set the state of. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

- **state:** A boolean value representing whether or not the key will be set to pressed or not.

### Returns

Returns *true* if the control state was successfully set, *false* otherwise.

## Example

This example will disable the use of the accelerate, brake/reverse and handbrake keys, then force the accelerate on for any player who enters a vehicle.

```
function onPlayerEnterVehicle ( theVehicle, seat, jacked )
    toggleControl ( source, "accelerate", false ) -- disable the accelerate key
    toggleControl ( source, "brake_reverse", false ) -- disable the brake_reverse key
    toggleControl ( source, "handbrake", false ) -- disable the handbrake key
    setControlState ( source, "accelerate", true ) -- force the accelerate key on
end
addEventHandler ( "onPlayerVehicleEnter", root, onPlayerEnterVehicle )
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.5-3.11427 | Deprecated client-side. Use setPedControlState and getPedControlState client-side. |
| --- | --- |

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

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
