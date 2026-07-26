---
doc_id: "mta-wiki:2301"
title: "IsKeyBound"
source_title: "IsKeyBound"
source_url: "https://wiki.multitheftauto.com/wiki/IsKeyBound"
revision_id: 80369
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:56.099948+00:00"
---

# IsKeyBound

This function can be used to find out if a key has already been bound. If you do not specify a keyState or handler, any instances of key being bound will cause isKeyBound to return true.

## Syntax

```
bool isKeyBound ( player thePlayer, string key, [ string keyState, function handler ] )
```

### Required Arguments

- **thePlayer:** The player you're checking.

- **key:** The key you're checking. See [Key names](mta://reference/misc/key-names.md) for a list of valid key names.

### Optional Arguments

- **keyState:** Is the state of the key when it calls the function, Can be either:

- **"up":** when the key is released

- **"down":** when the key is pressed

- **handler:** The function you're checking against

### Returns

Returns *true* if the key is bound, *false* otherwise.

## Example

```
-- This function tells everyone in the server if someone has numpad 9 bound!
function onPlayerJoin ()
  if (isKeyBound (source,"num_9")) then -- if num pad 9 is bound
    outputChatBox (getPlayerName (source) .. " has bound numpad 9!",getRootElement(),255,0,0,false) -- let see everybody that he has binded it
  end
end
addEventHandler ("onPlayerJoin",getRootElement(),onPlayerJoin) -- add event.
```

## See Also

- isKeyBound
  

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
