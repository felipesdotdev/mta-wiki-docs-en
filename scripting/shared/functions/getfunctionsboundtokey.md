---
doc_id: "mta-wiki:4361"
title: "GetFunctionsBoundToKey"
source_title: "GetFunctionsBoundToKey"
source_url: "https://wiki.multitheftauto.com/wiki/GetFunctionsBoundToKey"
revision_id: 56294
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:13.870258+00:00"
---

# GetFunctionsBoundToKey

Gets the functions bound to a key. To bind a function to a key use the [bindKey](mta://scripting/shared/functions/bindkey.md) function

## Syntax

Click to collapse [-]
Server

```
table getFunctionsBoundToKey ( player thePlayer, string key, string keyState )
```

### Required Arguments

- **thePlayer:** The player to get the functions from a key.

- **theKey:** The key you wish to check the functions from.

- **keyState:** A string that has one of the following values:

- **"up":** If the bound key should trigger the function when the key is released

- **"down":** If the bound key should trigger the function when the key is pressed

- **"both":** If the bound key should trigger the function when the key is pressed or released

Click to collapse [-]
Client

```
table getFunctionsBoundToKey ( string key, string keyState )
```

### Required Arguments

- **theKey:** The key you wish to check the functions from.

- **keyState:** A string that has one of the following values:

- **"up":** If the bound key should trigger the function when the key is released

- **"down":** If the bound key should trigger the function when the key is pressed

- **"both":** If the bound key should trigger the function when the key is pressed or released

### Returns

Returns a table of the key function(s).

## Example

Click to collapse [-]
Client

This loops through all the keys and outputs the keyname and the function bound to that key.

```
local keyTable = { "mouse1", "mouse2", "mouse3", "mouse4", "mouse5", "mouse_wheel_up", "mouse_wheel_down", "arrow_l", "arrow_u",
 "arrow_r", "arrow_d", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "num_0", "num_1", "num_2", "num_3", "num_4", "num_5",
 "num_6", "num_7", "num_8", "num_9", "num_mul", "num_add", "num_sep", "num_sub", "num_div", "num_dec", "F1", "F2", "F3", "F4", "F5",
 "F6", "F7", "F8", "F9", "F10", "F11", "F12", "backspace", "tab", "lalt", "ralt", "enter", "space", "pgup", "pgdn", "end", "home",
 "insert", "delete", "lshift", "rshift", "lctrl", "rctrl", "[", "]", "pause", "capslock", "scroll", ";", ",", "-", ".", "/", "#", "\\", "=" }

addCommandHandler("gakf",function()
	for _,i in ipairs(keyTable)do --loop through keyTable
		for _,v in ipairs(getFunctionsBoundToKey(i))do --loop through the key bounded functions
			outputChatBox(i..":"..tostring(v)) --output the keyname and the function bound to it
		end
	end
end)
```

Click to expand [+]
Server

This loops through all the keys and outputs the keyname and the function bound to that key.

```
function output()
	outputChatBox("Hi")
end
bindKey(root,"f2","down",output)
local keyTable = { "mouse1", "mouse2", "mouse3", "mouse4", "mouse5", "mouse_wheel_up", "mouse_wheel_down", "arrow_l", "arrow_u",
 "arrow_r", "arrow_d", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
 "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "num_0", "num_1", "num_2", "num_3", "num_4", "num_5",
 "num_6", "num_7", "num_8", "num_9", "num_mul", "num_add", "num_sep", "num_sub", "num_div", "num_dec", "F1", "F2", "F3", "F4", "F5",
 "F6", "F7", "F8", "F9", "F10", "F11", "F12", "backspace", "tab", "lalt", "ralt", "enter", "space", "pgup", "pgdn", "end", "home",
 "insert", "delete", "lshift", "rshift", "lctrl", "rctrl", "[", "]", "pause", "capslock", "scroll", ";", ",", "-", ".", "/", "#", "\\", "=" }

addCommandHandler("gakf",function(source) --source is the player
	for _,i in ipairs(keyTable)do --loop through keyTable
		for _,v in ipairs(getFunctionsBoundToKey(source,i))do --loop through the key bounded functions
			outputChatBox(i..":"..v,source) --output the keyname and the function bound to it
		end
	end
end)
```

## See Also

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- [bindKey](mta://scripting/shared/functions/bindkey.md)

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- getFunctionsBoundToKey

- [getKeyBoundToFunction](mta://scripting/shared/functions/getkeyboundtofunction.md)

- [isControlEnabled](mta://scripting/shared/functions/iscontrolenabled.md)

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
