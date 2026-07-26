---
doc_id: "mta-wiki:11465"
title: "OnClientPaste"
source_title: "OnClientPaste"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPaste"
revision_id: 71481
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:19.273294+00:00"
---

# OnClientPaste

This event triggers when user paste whatever (**CTRL + V**). **This event isn't triggered if menu or console is visible or if any browser is focused, or if cursor is invisible.**

## Parameters

```
string clipboardText
```

- **clipboardText**: a [string](mta://reference/misc/string.md) representing the pasted value from clipboard.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client's [root element](mta://reference/misc/root-element.md).

## Example

Example show what player paste from clipboard.

```
addEventHandler("onClientPaste", root, function(text)
    outputChatBox("Clipboard value: "..text, 255,255,255)
end)
```

## See Also

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
