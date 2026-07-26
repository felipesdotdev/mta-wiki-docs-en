---
doc_id: "mta-wiki:2587"
title: "GetKeyState"
source_title: "GetKeyState"
source_url: "https://wiki.multitheftauto.com/wiki/GetKeyState"
revision_id: 67091
language: "en"
categories: ["Client_functions"]
---

# GetKeyState

This function determines if a certain key is pressed or not.

**Note:** 'ralt' may trigger both 'ralt' and 'lctrl', this is due to AltGr

## Syntax

```
bool getKeyState ( string keyName )
```

### Required Arguments

- **keyName:** The name of the key you're checking state of. See [Key names](mta://reference/misc/key-names.md).

### Returns

Returns *true* if the specified key is pressed, *false* if it isn't or if an invalid key name is passed.

## Example

This clientside example prints a message when "p" is pressed, and a different one for the "control+p" combination.

```
-- define a function that outputs a message if control is pressed, and a different one if it isn't
function printMessageFunction()
	-- if the left or right control keys are pressed, the user has pressed the "lctrl + p" combo.
	if getKeyState("lctrl") or getKeyState("rctrl") then
		outputChatBox ("You have pressed 'Left Control + P'.")
	-- if none of those were pressed, the player just pressed the "p" key.
	else
		outputChatBox ("You have pressed 'p'.")
	end
end
-- bind the "p" key to our function
bindKey("p", "down", printMessageFunction)
```

## See Also

- [getAnalogControlState](mta://scripting/client/functions/getanalogcontrolstate.md)

- [getBoundKeys](mta://scripting/client/functions/getboundkeys.md)

- [getCommandsBoundToKey](mta://scripting/client/functions/getcommandsboundtokey.md)

- [getKeyBoundToCommand](mta://scripting/client/functions/getkeyboundtocommand.md)

- getKeyState

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
