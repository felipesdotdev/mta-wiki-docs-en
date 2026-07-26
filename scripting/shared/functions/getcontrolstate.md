---
doc_id: "mta-wiki:1716"
title: "GetControlState"
source_title: "GetControlState"
source_url: "https://wiki.multitheftauto.com/wiki/GetControlState"
revision_id: 79210
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:08.945272+00:00"
---

# GetControlState

This function will check if a player is pressing a particular control. Controls are those that affect GTA. If you wish to get the state of another key, use [bindKey](mta://scripting/shared/functions/bindkey.md) and a command function.

Note: Not all control states are sent to the server at all times, as such their state may be given incorrectly. As a rule, keys that move or affect the player or their vehicle are most likely to be accurate. For increased accuracy (and also increased bandwidth usage) use bindKey instead to bind a GTA control name to a function.

## Syntax

```
bool getControlState ( player thePlayer, string controlName )
```

### Required Arguments

- **thePlayer:** The player you wish to get the control state of. Do not use this parameter when scripting for client.

- **controlName:** The control that you want to get the state of. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

**Note:** several controls are not synched with the server, therefore the function will always return *false* for these controls serverside. These controls are:

- next_weapon

- previous_weapon

- jump

- zoom_in

- zoom_out

- look_behind

- change_camera

- conversation_yes

- conversation_no

- group_control_forwards

- group_control_back

- sub_mission

- radio_next

- radio_previous

- vehicle_look_left

- vehicle_look_right

- vehicle_look_behind

- vehicle_mouse_look

- special_control_*

### Returns

Returns the state of the control, *false* if the control doesn't exist or if the player is dead.

## Example

This example starts a repeating check when a player spawns, if a player presses the fire key, they'll be killed.

```
function onPlayerSpawn ( theSpawnpoint )
    killPlayerIfTheyPressThisKey ( source, "fire" ) -- start a repeating check
end
addEventHandler ( "onPlayerSpawn", root, onPlayerSpawn )

function killPlayerIfTheyPressThisKey ( thePlayer, key )
    if ( getControlState ( thePlayer, key ) ) then        -- if they're pressing the fire key
        outputChatBox ( "Violence will not be tolerated!", thePlayer )
        killPed ( thePlayer )                          -- kill them
    else                                                  -- otherwise..
        setTimer ( killPlayerIfTheyPressThisKey, 500, 1, thePlayer, key ) -- call this function again in 500ms
    end
end
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
