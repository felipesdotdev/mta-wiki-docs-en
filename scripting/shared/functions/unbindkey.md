---
doc_id: "mta-wiki:1693"
title: "UnbindKey"
source_title: "UnbindKey"
source_url: "https://wiki.multitheftauto.com/wiki/UnbindKey"
revision_id: 71505
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:01.511393+00:00"
---

# UnbindKey

Removes an existing key bind from the specified player.

| [[{{{image}}}\|link=\|]] | Note: unbindKey will only work on binds that were added by the same resource |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: unbindKey on the server may return true on failure |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: If you call unbindKey twice, it will break other scripts: Issue 497 |
| --- | --- |
|  |  |

## Syntax

Click to collapse [-]
Server

```
bool unbindKey ( player thePlayer, string key, string keyState, string command )
```

```
bool unbindKey ( player thePlayer, string key [, string keyState, function handler ] )
```

### Required Arguments

- **thePlayer:** The player you wish to unbind the key of.

- **key:** The key you wish to unbind. See [Key names](mta://reference/misc/key-names.md) for a list of valid key names.

- **keyState:** Can be either:

- **"up":** If the bound key triggered a function when the key was released

- **"down":** If the bound key triggered a function when the key was pressed

- **"both":** If the bound key triggered a function when the key was pressed and released

- **command :** (Syntax 1) The command you wish to unbind.

### Optional Arguments

- **keyState:** is optional in Syntax 2.

- **handler:** (Syntax 2) The function you wish to unbind.

Note: If you do not specify *handler*, any instances of *key* being bound will be unbound, whatever function they are bound to.

### Returns

Returns '*true* if the key was unbound, *false* if it was not previously bound or invalid arguments were passed to the function.

Click to collapse [-]
Client

```
bool unbindKey ( string key, string keyState, string command )
```

```
bool unbindKey ( string key [, string keyState, function handler ] )
```

### Required Arguments

- **key:** The key you wish to unbind. See [Key names](mta://reference/misc/key-names.md) for a list of valid key names.

- **keyState:** Can be either:

- **"up":** If the bound key triggered a function when the key was released

- **"down":** If the bound key triggered a function when the key was pressed

- **"both":** If the bound key triggered a function when the key was pressed and released

- **command :** (Syntax 1) The command you wish to unbind.

### Optional Arguments

- **keyState:** is optional in Syntax 2.

- **handler:** (Syntax 2) The function you wish to unbind.

Note: If you do not specify *handler*, any instances of *key* being bound will be unbound, whatever function they are bound to.

### Returns

Returns '*true* if the key was unbound, *false* if it was not previously bound or invalid arguments were passed to the function.

## Example

Click to collapse [-]
Server

This function binds the player's *F1* key to a function *goMoo* which outputs a chat message when pressed. The key is then unbound so that it can effectively only be used once per life.

```
-- define the function that will be called when F1 is pressed
function goMoo( player )
    outputChatBox ( getPlayerName ( player ) .. " says Mooooooo!" )
    unbindKey ( player, "F1", "down", goMoo )   -- this function will no longer be triggered by the player, after removing the bind.
end

function playerSpawn ( )
    bindKey ( source, "F1", "down", goMoo ) -- bind the player's F1 key to the 'goMoo' function defined above
end
addEventHandler ( "onPlayerSpawn", root, playerSpawn ) -- make the playerSpawn function be called when a player spawns
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

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- unbindKey
