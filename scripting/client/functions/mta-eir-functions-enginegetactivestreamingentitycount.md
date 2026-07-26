---
doc_id: "mta-wiki:7369"
title: "MTA:Eir/functions/engineGetActiveStreamingEntityCount"
source_title: "MTA:Eir/functions/engineGetActiveStreamingEntityCount"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetActiveStreamingEntityCount"
revision_id: 77708
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.392295+00:00"
---

# MTA:Eir/functions/engineGetActiveStreamingEntityCount

This function returns how many entities are inside of the [streaming garbage collection system](mta://reference/misc/gta-sa-streaming-garbage-collection.md). It is useful for performance debugging purposes. More uses come out of it if combined with other engine streaming functions.

## Syntax

```
int engineGetActiveStreamingEntityCount ()
```

### Returns

Returns the amount of entities that are registered inside of the streaming garbage collector.

## Example

Click to collapse [-]
Client

This snippet draws the amount of active streaming entities on your screen.

```
addEventHandler( "onClientRender", root,
    function()
        local count = engineGetActiveStreamingEntityCount();

        dxDrawText( "#streaming-entities: " .. count, 100, 400 );
    end
);
```
