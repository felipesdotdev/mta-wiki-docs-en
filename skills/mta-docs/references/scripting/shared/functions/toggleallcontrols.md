---
doc_id: "mta-wiki:1714"
title: "ToggleAllControls"
source_title: "ToggleAllControls"
source_url: "https://wiki.multitheftauto.com/wiki/ToggleAllControls"
revision_id: 67702
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions"]
---

# ToggleAllControls

Enables or disables the use of all GTA controls for a specified player.

## Syntax

Click to collapse [-]
Server

```
bool toggleAllControls ( player thePlayer, bool enabled, [ bool gtaControls = true, bool mtaControls = true ] )
```

### Required Arguments

- **thePlayer:** The player you wish to toggle the control ability of.

- **enabled:** A boolean value representing whether or not the controls will be usable.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **gtaControls:** A boolean deciding whether the *enabled* parameter will affect GTA's internal controls.

- **mtaControls:** A boolean deciding whether the *enabled* parameter will affect MTA's own controls., e.g. chatbox.

Click to collapse [-]
Client

```
bool toggleAllControls ( bool enabled, [ bool gtaControls = true, bool mtaControls = true ] )
```

### Required Arguments

- **enabled:** A boolean value representing whether or not the controls will be usable.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **gtaControls:** A boolean deciding whether the *enabled* parameter will affect GTA's internal controls.

- **mtaControls:** A boolean deciding whether the *enabled* parameter will affect MTA's own controls., e.g. chatbox.

### Returns

This function returns *true* if controls were toggled successfully, false otherwise.

## Example

Click to collapse [-]
Server

This function will disable the use of all controls in order to freeze a player, which will be used every time someone enters a vehicle.

```
function freezeThisDude ( thePlayer, freezeTime )
    toggleAllControls ( thePlayer, false )                         -- disable this player's controls
    setTimer ( toggleAllControls, freezeTime, 1, thePlayer, true ) -- enable this player's controls after the specified time
end

function freezeOnEnterVehicle ( theVehicle, seat, jacked )
    freezeThisDude ( source, 5000 ) -- 'freeze' him for 5000ms = 5 seconds
end
addEventHandler ( "onPlayerVehicleEnter", root, freezeOnEnterVehicle )
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

- toggleAllControls

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
