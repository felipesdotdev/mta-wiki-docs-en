---
doc_id: "mta-wiki:7375"
title: "MTA:Eir/functions/engineGetActiveStreamingEntities"
source_title: "MTA:Eir/functions/engineGetActiveStreamingEntities"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetActiveStreamingEntities"
revision_id: 77713
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.386208+00:00"
---

# MTA:Eir/functions/engineGetActiveStreamingEntities

This function returns a table of MTA entities that have a [streaming garbage collection](mta://reference/misc/gta-sa-streaming-garbage-collection.md) node allocated. Those entities can be deallocated once GTA:SA has reached its maximum **streaming memory** (the setting in your Video options tab). Certain types of entities can only render if they have a streaming node allocated.

## Syntax

```
table engineGetActiveStreamingEntities ()
```

### Returns

Returns a **table** of all MTA entities that reside inside of the *streaming garbage collector*.

## Example

Click to collapse [-]
Client

This snippet makes every entity inside of the streaming garbage collector transparent.

```
addCommandHandler( "alpha_test",
    function()
        local entities = engineGetActiveStreamingEntities();

        for m,n in ipairs( entities ) do
            setElementAlpha( n, 101 );
        end
    end
);
```
