---
doc_id: "mta-wiki:4950"
title: "Modules/SebasIRC/onIRCRaw"
source_title: "Modules/SebasIRC/onIRCRaw"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/onIRCRaw"
revision_id: 21708
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.149017+00:00"
---

# Modules/SebasIRC/onIRCRaw

This event triggers when raw data is sent from the IRC server to the module. Thanks to this, scripts can know when something has happened on IRC. (i.e. chatting)

## Parameters

```
string content
```

- **content**: The raw command that has been sent to the module

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](mta://reference/misc/root-element.md).

## Example

```
local root = getRootElement()

function handleRawIRCData(msg)
  if msg then
    outputServerLog(msg) -- Shows all incoming IRC data as a string
  end
end
addEventHandler("onIRCRaw", root, handleRawIRCData)
```

## See also

- onIRCRaw

**There are no more events, more events are made in lua with onIRCRaw so that you can create your own syntax.**
