---
doc_id: "mta-wiki:5802"
title: "GetKeyBoundToCommand"
source_title: "GetKeyBoundToCommand"
source_url: "https://wiki.multitheftauto.com/wiki/GetKeyBoundToCommand"
revision_id: 45361
language: "en"
categories: ["Client_functions"]
---

# GetKeyBoundToCommand

This function allow you get first key bound to command.

## Syntax

```
string getKeyBoundToCommand( string command )
```

### Required Arguments

- **command:** command what you need check.

### Returns

Returns a string of first key binded to current command.

## Example

This example adds a /getcommandbind command, allowing players to see what keys are bound to the given command.

```
--This function is executed when the player uses the /getcommandbind [command] command.
--It outputs the key the command is bound to (if it is bound).
local function playerCommand(_, command)
	if not command then --if no command name was given, output a syntax error message.
		outputChatBox("* Syntax: /getcommandbind [command name] .", 255, 0, 0)
		return
	end
	
	local keyName = getKeyBoundToCommand(command)
	if keyName then
		outputChatBox("* The command /"..command.." is bound to the "..keyName.." key.", 0, 0, 255)
	else
		outputChatBox("* The command /"..command.." is not bound to any keys.", 0, 0, 255)
	end
end
addCommandHandler("getcommandbind", playerCommand)
```

## See Also

- [getAnalogControlState](mta://scripting/client/functions/getanalogcontrolstate.md)

- [getBoundKeys](mta://scripting/client/functions/getboundkeys.md)

- [getCommandsBoundToKey](mta://scripting/client/functions/getcommandsboundtokey.md)

- getKeyBoundToCommand

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
