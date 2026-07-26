---
doc_id: "mta-wiki:2617"
title: "IsControlEnabled"
source_title: "IsControlEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsControlEnabled"
revision_id: 35261
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# IsControlEnabled

Checks whether a GTA control is enabled or disabled for a certain player.

## Syntax

Click to collapse [-]
Server

```
bool isControlEnabled ( player thePlayer, string control )
```

### Required Arguments

- **thePlayer:** The player you wish the control status of.

- **control:** The control you wish to check. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

Click to collapse [-]
Client

```
bool isControlEnabled ( string control )
```

### Required Arguments

- **control:** The control you wish to check. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

### Returns

Returns *true* if control is enabled, *false* otherwise.

## Example

Click to collapse [-]
Example 1

This example uses a command handler to allow a player to toggle whether he can use vehicle weapons by disabling or enabling the primary and secondary vehicle fire keys. The command handler is trigged with 'toggleweapons'

```
function changeWeaponControls ( player, commandName )
	--Check to see if the player can use primary/secondary vehicle fire controls
        primaryWeaponControl = isControlEnabled ( player, "vehicle_fire" )
        secondaryWeaponControl = isControlEnabled ( player, "vehicle_secondary_fire" )
	--Toggle the use of the primary vehicle fire control ability.
        if ( primaryWeaponControl == true ) then
             toggleControl ( player, "vehicle_fire", false )
    	     outputChatBox ( "Disabled your ability to use primary vehicle weapons." )
        else
             toggleControl ( player, "vehicle_fire", true )
    	     outputChatBox ( "Enabled your ability to use primary vehicle weapons." )
        end
        --Toggle the use of the secondar vehicle fire control ability.
        if ( secondaryWeaponControl == true ) then
             toggleControl ( player, "vehicle_secondary_fire", false )
    	     outputChatBox ( "Disabled your ability to use secondary vehicle weapons." )
        else
             toggleControl ( player, "vehicle_secondary_fire", true )
    	     outputChatBox ( "Enabled your ability to use secondary vehicle weapons." )
        end
end  
addCommandHandler ( "toggleweapons", changeWeaponControls )
```

## See Also

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- [bindKey](mta://scripting/shared/functions/bindkey.md)

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- [getFunctionsBoundToKey](mta://scripting/shared/functions/getfunctionsboundtokey.md)

- [getKeyBoundToFunction](mta://scripting/shared/functions/getkeyboundtofunction.md)

- isControlEnabled

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
