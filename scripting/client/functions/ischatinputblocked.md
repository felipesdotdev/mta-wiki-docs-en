---
doc_id: "mta-wiki:13368"
title: "IsChatInputBlocked"
source_title: "IsChatInputBlocked"
source_url: "https://wiki.multitheftauto.com/wiki/IsChatInputBlocked"
revision_id: 81319
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:53.738711+00:00"
---

# IsChatInputBlocked

This function checks if the player's chat input is blocked.

## Syntax

```
bool isChatInputBlocked ( )
```

### Returns

Returns *true* if the chat input is blocked, *false* otherwise.

## Example

This example shows how to block and unblock the chat input:

```
function toggleInputBlocked ()
    local visible = isChatVisible () -- check if the chat is visible
    showChat (visible, not isChatInputBlocked ()) -- toggle inputBlocked
end

addCommandHandler("blockchat", toggleInputBlocked)
```

## See Also

- [clearDebugBox](mta://scripting/client/functions/cleardebugbox.md)

- isChatInputBlocked

- [isChatVisible](mta://scripting/client/functions/ischatvisible.md)
  

- **Shared**

- [clearChatBox](mta://scripting/shared/functions/clearchatbox.md)

- [outputChatBox](mta://scripting/shared/functions/outputchatbox.md)

- [outputConsole](mta://scripting/shared/functions/outputconsole.md)

- [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md)

- [showChat](mta://scripting/shared/functions/showchat.md)
