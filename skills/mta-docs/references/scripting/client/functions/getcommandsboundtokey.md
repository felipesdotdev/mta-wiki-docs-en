---
doc_id: "mta-wiki:5803"
title: "GetCommandsBoundToKey"
source_title: "GetCommandsBoundToKey"
source_url: "https://wiki.multitheftauto.com/wiki/GetCommandsBoundToKey"
revision_id: 56295
language: "en"
categories: ["Client_functions"]
---

# GetCommandsBoundToKey

Gets the commands bound to a key.

## Syntax

```
table getCommandsBoundToKey ( string theKey, string keyState )
```

### Required Arguments

- **theKey:** See [key names](mta://reference/misc/key-names.md) for a list of possible keys

- **keyState:** A string that has one of the following values:

- **"up":** If the bound key should trigger the function when the key is released

- **"down":** If the bound key should trigger the function when the key is pressed

- **"both":** If the bound key should trigger the function when the key is pressed or released

### Returns

Returns a table of the commands bound on that key.

## Example

Click to collapse [-]
Client

This example adds the command /keycommands <theKey> <keyState>

```
addCommandHandler ( "keycommands",
	function ( commandName, theKey, keyState )
		if ( theKey and keyState ) then -- We check if theKey and keyState is valid.
			local commands = getCommandsBoundToKey ( theKey, keyState )
			if ( commands and type ( commands ) == "table" ) then
				for command, state in pairs ( commands ) do
					outputChatBox ( command )
				end
			end
		else
			outputChatBox (	commandName ..": Correct syntax: [ theKey ] [ keyState ]" )
		end
	end
)
```

## See Also

- [getAnalogControlState](mta://scripting/client/functions/getanalogcontrolstate.md)

- [getBoundKeys](mta://scripting/client/functions/getboundkeys.md)

- getCommandsBoundToKey

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
