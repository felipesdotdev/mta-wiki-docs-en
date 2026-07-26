---
doc_id: "mta-wiki:7370"
title: "MTA:Eir/functions/engineGetActiveStreamingFreeSlotCount"
source_title: "MTA:Eir/functions/engineGetActiveStreamingFreeSlotCount"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetActiveStreamingFreeSlotCount"
revision_id: 77709
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineGetActiveStreamingFreeSlotCount

This function returns how many streaming node are available to allocate inside of the [streaming garbage collection system](mta://reference/misc/gta-sa-streaming-garbage-collection.md). When entities allocate RenderWare data, they want to have a streaming node too. Failure to allocate it results in deletion of its RenderWare data.

## Syntax

```
int engineGetActiveStreamingFreeSlotCount ()
```

### Returns

Returns the amount of free nodes inside the streaming garbage collector.

## Example

Click to collapse [-]
Client

This snippet draws the amount of free streaming node slots on the screen.

```
addEventHandler( "onClientRender", root,
    function()
        local count = engineGetActiveStreamingFreeSlotCount();

        dxDrawText( "#free-streaming-slots: " .. count, 100, 420 );
    end
);
```
