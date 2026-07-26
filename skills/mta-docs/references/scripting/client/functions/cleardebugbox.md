---
doc_id: "mta-wiki:13317"
title: "ClearDebugBox"
source_title: "ClearDebugBox"
source_url: "https://wiki.multitheftauto.com/wiki/ClearDebugBox"
revision_id: 81308
language: "en"
categories: ["Client_functions"]
---

# ClearDebugBox

This function clears the debug box.

## Syntax

```
bool clearDebugBox ( )
```

### Returns

Always returns *true*.

## Example

Click to collapse [-]
Client

This example clears the debug window when any new debug message is displayed:

```
addEventHandler ("onClientDebugMessage", root,
    function ()
         clearDebugBox ()
    end
)
```

## See Also

- clearDebugBox

- [isChatInputBlocked](mta://scripting/client/functions/ischatinputblocked.md)

- [isChatVisible](mta://scripting/client/functions/ischatvisible.md)
  

- **Shared**

- [clearChatBox](mta://scripting/shared/functions/clearchatbox.md)

- [outputChatBox](mta://scripting/shared/functions/outputchatbox.md)

- [outputConsole](mta://scripting/shared/functions/outputconsole.md)

- [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md)

- [showChat](mta://scripting/shared/functions/showchat.md)
