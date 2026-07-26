---
doc_id: "mta-wiki:7382"
title: "MTA:Eir/functions/engineStreamingIsElementManaged"
source_title: "MTA:Eir/functions/engineStreamingIsElementManaged"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingIsElementManaged"
revision_id: 77723
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.509000+00:00"
---

# MTA:Eir/functions/engineStreamingIsElementManaged

This function returns whether the given element is managed by the [Streaming garbage collector](mta://reference/misc/gta-sa-streaming-garbage-collection.md). If an entity is managed, its RenderWare data can be deallocated once the engine is lacking available **streaming memory** (an option found in your game settings under the Video tab).

## Syntax

```
bool engineStreamingIsElementManaged ( element entity )
```

### Arguments

- **entity:** an entity that is streamed in and has a visible game representation

### Returns

Returns **true** if the given entity is being managed by the engine Streaming GC system. Returns **false** if the entity type is not being managed at all, entity does not have a visible game representation or entity is not passed as valid parameter.

## Example

Click to collapse [-]
Client

This snippet returns every object that is managed by the Streaming GC system.

```
function getStreamingManagedObjects()
    local objects = getElementsByType( "object" );
    local managedObjects = {};
    local num = 1;

    for m,n in ipairs( objects ) do
        if ( engineStreamingIsElementManaged( n ) ) then
            managedObjects[num] = n;

            num = num + 1;
        end
    end

    return managedObjects, num;
end
```
