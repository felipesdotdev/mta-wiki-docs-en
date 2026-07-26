---
doc_id: "mta-wiki:3539"
title: "GetBoundKeys"
source_title: "GetBoundKeys"
source_url: "https://wiki.multitheftauto.com/wiki/GetBoundKeys"
revision_id: 44705
language: "en"
categories: ["Client_functions"]
---

# GetBoundKeys

Returns a list of key names that are bound to the specified game [control](mta://reference/misc/control-names.md) or console command.

## Syntax

```
table getBoundKeys ( string command/control )
```

### Required Arguments

- **command/control:** the name of a game control or a console command. See the [control names](mta://reference/misc/control-names.md) page for valid controls.

### Returns

If one or more keys are bound to the specified control or console command, a table is returned indexed by the names of the keys and containing key states as values. If no keys are bound or an invalid name was passed, returns *false*.

## Example

This code adds a command handler with which you can check out the keybinds for any game control. As an example, typing "/keys forwards" would list all the keys which you can press to make the player walk forward.

```
function keysCommand ( command, controlName )
    if not controlName then                     -- make sure they specified a control name
        outputChatBox ( "No control name specified", 255, 0, 0 )
        return
    end
    local keys = getBoundKeys ( controlName )   -- get the keys bound to this control
    if not keys then                            -- make sure the control name is valid and any keys are bound to it
        outputChatBox ( "No keys bound to " .. controlName, 255, 0, 0 )
        return
    end
    outputChatBox ( "Keys bound to " .. controlName .. ":", 0, 255, 0 )
    for keyName, state in pairs(keys) do
        outputChatBox ( keyName, 0, 255, 0 )
    end
end

addCommandHandler ( "keys", keysCommand )
```

## See Also

- [getAnalogControlState](mta://scripting/client/functions/getanalogcontrolstate.md)

- getBoundKeys

- [getCommandsBoundToKey](mta://scripting/client/functions/getcommandsboundtokey.md)

- [getKeyBoundToCommand](mta://scripting/client/functions/getkeyboundtocommand.md)

- [getKeyState](mta://scripting/client/functions/getkeystate.md)

- [isCapsLockEnabled](mta://scripting/client/functions/iscapslockenabled.md)

- [setAnalogControlState](mta://scripting/client/functions/setanalogcontrolstate.md)
  

- **Shared**

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
