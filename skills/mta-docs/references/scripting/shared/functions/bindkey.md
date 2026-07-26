---
doc_id: "mta-wiki:1692"
title: "BindKey"
source_title: "BindKey"
source_url: "https://wiki.multitheftauto.com/wiki/BindKey"
revision_id: 78900
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# BindKey

Binds a player's key to a handler function or command, which will be called when the key is pressed.

| [[{{{image}}}\|link=\|]] | Note: Using escape key or F8 key will always return false. Use onClientKey event instead. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Handler function won't be triggered while focused in CEGUI editbox. You can use guiSetInputMode or onClientKey in order to fix that. |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server - Syntax 1

```
bool bindKey ( player thePlayer, string key, string keyState, function handlerFunction,  [ var arguments, ... ] )
```

### Required Arguments

- **thePlayer:** The player you wish to bind the key of.

- **key:** The key or control you wish to bind to the command. See [key names](mta://reference/misc/key-names.md) for a list of possible keys and [control names](mta://reference/misc/control-names.md) for a list of possible controls.

- **keyState:** A string that has one of the following values:

- **"up":** If the bound key should trigger the function when the key is released

- **"down":** If the bound key should trigger the function when the key is pressed

- **"both":** If the bound key should trigger the function when the key is pressed or released

- **handlerFunction:** The function that will be triggered when the player's key is pressed. This function should have the form:

```
function functionName ( player keyPresser, string key, string keyState, [ var arguments, ... ] )
```

The values passed to this function are:

- **keyPresser:** The player who pressed the key

- **key:** The key that was pressed

- **keyState:** The state of the key that was pressed, *down* if it was pressed, *up* if it was released.

- **arguments** The optional arguments you specified when calling bindKey (see below).

Click to collapse [-]
Server - Syntax 2

This alternative syntax allows you to bind a key with a command.  This will also allow users to customize the control in their Settings menu.  Use in conjunction with [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md) to add handler functions to the keybind.

```
bool bindKey ( player thePlayer, string key, string keyState, string commandName, [ string arguments ] )
```

### Required Arguments

- **thePlayer:** The player you wish to bind the key of.

- **key:** The key or control you wish to bind to the command. See [key names](mta://reference/misc/key-names.md) for a list of possible keys.

- **keyState:** A string that has one of the following values:

- **"up":** If the bound key should trigger the function when the key is released

- **"down":** If the bound key should trigger the function when the key is pressed

- **"both":** If the bound key should trigger the function when the key is pressed or released

- **commandName:** The name of the command that the key should be binded to.

### Optional Arguments

- **arguments** Space delimited arguments that are entered as if one was typing the command.

Click to collapse [-]
Client - Syntax 1

```
bool bindKey ( string key, string keyState, function handlerFunction,  [ var arguments, ... ] )
```

### Required Arguments

- **key:** The key or control you wish to bind to the command. See [key names](mta://reference/misc/key-names.md) for a list of possible keys and [control names](mta://reference/misc/control-names.md) for a list of possible controls.

- **keyState:** A string that has one of the following values:

- **"up":** If the bound key should trigger the function when the key is released

- **"down":** If the bound key should trigger the function when the key is pressed

- **"both":** If the bound key should trigger the function when the key is pressed or released

- **handlerFunction:** The function that will be triggered when the player's key is pressed. This function should have the form:

```
function functionName ( string key, string keyState, [ var arguments, ... ] )
```

The values passed to this function are:

- **key:** The key that was pressed

- **keyState:** The state of the key that was pressed, *down* if it was pressed, *up* if it was released.

- **arguments** The optional arguments you specified when calling bindKey (see below).

Click to collapse [-]
Client - Syntax 2

This alternative syntax allows you to bind a key with a command.  This will also allow users to customize the control in their Settings menu.  Use in conjunction with [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md) to add handler functions to the keybind.

```
bool bindKey ( string key, string keyState, string commandName, [ string arguments ] )
```

### Required Arguments

- **key:** The key or control you wish to bind to the command. See [key names](mta://reference/misc/key-names.md) for a list of possible keys.

- **keyState:** A string that has one of the following values:

- **"up":** If the bound key should trigger the function when the key is released

- **"down":** If the bound key should trigger the function when the key is pressed

- **"both":** If the bound key should trigger the function when the key is pressed or released

- **commandName:** The name of the command that the key should be binded to.

- **arguments** Space delimited arguments that are entered as if one was typing the command.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **arguments:** Any arguments you may want to pass to the function when the key is pressed by the user. Any number of arguments of  can be specified, each being passed to the designated function. You may not pass functions.

### Returns

Returns *true* if the key was bound, *false* otherwise.

## Example

Example 1

Click to collapse [-]
Server

This example will bind a player's 'F1' key and 'fire' control to 1 input function.

```
function funcInput ( player, key, keyState )
  outputChatBox ( getPlayerName ( player) .. " " .. (keyState == "down" and "pressed" or "released") .. " the " .. key .. " key!" )
end

function bindTheKeys ( player, commandName )
  bindKey ( player, "F1", "down", funcInput )   -- bind the player's F1 down key
  bindKey ( player, "F1", "up", funcInput )     -- bind the player's F1 up key
  bindKey ( player, "fire", "both", funcInput ) -- bind the player's fire down and up control
end
addCommandHandler ( "bindme", bindTheKeys )
```

Example 2

Click to collapse [-]
Client

This example will bind a player's 'F1' key and 'fire' control to 1 input function, clientside.

```
function funcInput ( key, keyState )
	outputChatBox( "You " .. (keyState == "down" and "pressed" or "let go of") .. " the " .. key .. " key!" )
end

function bindTheKeys ( commandName )
	bindKey( "F1", "down", funcInput )   -- bind the player's F1 down key
	bindKey( "F1", "up", funcInput )     -- bind the player's F1 up key
	bindKey( "fire", "both", funcInput ) -- bind the player's fire down and up control
end
addCommandHandler ( "bindme", bindTheKeys )
```

Click to collapse [-]
Server

This example says how cool is the MTA:SA is if players wants to move.

```
function fanFunction()
  bindKey (source,"forwards","down",
    function(player,key,state)
      outputChatBox (getPlayerName (player) .. "#FFFF00 thinks MTA:SA is so cool.",root,255,255,0,true)
    end
  )
end
addEventHandler ("onPlayerLogin",root,fanFunction)
```

## See Also

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- bindKey

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- [getFunctionsBoundToKey](mta://scripting/shared/functions/getfunctionsboundtokey.md)

- [getKeyBoundToFunction](mta://scripting/shared/functions/getkeyboundtofunction.md)

- [isControlEnabled](mta://scripting/shared/functions/iscontrolenabled.md)

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
