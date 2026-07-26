---
doc_id: "mta-wiki:7391"
title: "MTA:Eir/functions/getEntitiesInRenderQueue"
source_title: "MTA:Eir/functions/getEntitiesInRenderQueue"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/getEntitiesInRenderQueue"
revision_id: 37869
language: "en"
categories: []
---

# MTA:Eir/functions/getEntitiesInRenderQueue

This function returns a table of all MTA entities that are currently added to the rendering queue. Entities on the rendering queue are rendered in a specific order per frame. GTA:SA creates a new rendering queue every frame, so it is up to date all the time. This function should be called during **onClientGameEntityPreRender** as it is the time the lists are sure to be intact: the rendering lists are cleared at the end of the frame.

## Syntax

```
table getEntitiesInRenderQueue ()
```

### Returns

Returns a **table** with all entities that are rendering this frame.

## Example

Click to collapse [-]
Client

This snippet marks all entities on the rendering queue for deletion. Since the entities are referenced during the render process to prevent crashes due to invalid pointers, the entities are deleted at the end of the frame when the rendering lists are cleared.

```
addEventHandler( "onClientGameEntityPreRender", root,
    function()
        local renderingEntities = getEntitiesInRenderQueue();

        for m,n in ipairs( renderingEntities ) do
            destroyElement( n );
        end
    end
);
```
