---
doc_id: "mta-wiki:2773"
title: "GetKeyBoundToFunction"
source_title: "GetKeyBoundToFunction"
source_url: "https://wiki.multitheftauto.com/wiki/GetKeyBoundToFunction"
revision_id: 37228
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetKeyBoundToFunction

getKeyBoundToFunction allows retrieval of the first key bound to a function.

## Syntax

Click to collapse [-]
Server

```
string getKeyBoundToFunction( player thePlayer, function theFunction )
```

### Required Arguments

- **thePlayer:** The player you are checking the function bound to a key

- **theFunction:** The function in which you would like to check the bound key

### Returns

Returns a string of the first key the function was bound to.

Click to collapse [-]
Client

```
string getKeyBoundToFunction( function theFunction )
```

### Required Arguments

- **theFunction:** The function in which you would like to check the bound key

### Returns

Returns a string of the first key the function was bound to.

## Example

Click to collapse [-]
Client

/key command gives bounded key to our chat function

```
function chat ()
  outputChatBox("Test")
end
bindKey("F2","down",chat)

function key()
  local boundKey = getKeyBoundToFunction(chat)
  outputChatBox(boundKey)
end
addCommandHandler("key",key)
```

This example written by **Samurai**

## See Also

- [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md)

- [bindKey](mta://scripting/shared/functions/bindkey.md)

- [executeCommandHandler](mta://scripting/shared/functions/executecommandhandler.md)

- [getCommandHandlers](mta://scripting/shared/functions/getcommandhandlers.md)

- [getFunctionsBoundToKey](mta://scripting/shared/functions/getfunctionsboundtokey.md)

- getKeyBoundToFunction

- [isControlEnabled](mta://scripting/shared/functions/iscontrolenabled.md)

- [removeCommandHandler](mta://scripting/shared/functions/removecommandhandler.md)

- [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md)

- [toggleControl](mta://scripting/shared/functions/togglecontrol.md)

- [unbindKey](mta://scripting/shared/functions/unbindkey.md)
