---
doc_id: "mta-wiki:7667"
title: "IsChatVisible"
source_title: "IsChatVisible"
source_url: "https://wiki.multitheftauto.com/wiki/IsChatVisible"
revision_id: 72417
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:53.744809+00:00"
---

# IsChatVisible

This function checks if player's chat is visible.

## Syntax

```
bool isChatVisible ( )
```

### Returns

Returns *true* if the chat is visible, *false* otherwise.

## Example

This example does the same thing as *showchat* command does.

```
addCommandHandler("sc",
	function ()
		showChat(not isChatVisible())
	end)
```

## See Also

- [clearDebugBox](mta://scripting/client/functions/cleardebugbox.md)

- [isChatInputBlocked](mta://scripting/client/functions/ischatinputblocked.md)

- isChatVisible
  

- **Shared**

- [clearChatBox](mta://scripting/shared/functions/clearchatbox.md)

- [outputChatBox](mta://scripting/shared/functions/outputchatbox.md)

- [outputConsole](mta://scripting/shared/functions/outputconsole.md)

- [outputDebugString](mta://scripting/shared/functions/outputdebugstring.md)

- [showChat](mta://scripting/shared/functions/showchat.md)
