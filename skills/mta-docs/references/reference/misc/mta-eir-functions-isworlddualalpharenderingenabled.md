---
doc_id: "mta-wiki:7395"
title: "MTA:Eir/functions/isWorldDualAlphaRenderingEnabled"
source_title: "MTA:Eir/functions/isWorldDualAlphaRenderingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/isWorldDualAlphaRenderingEnabled"
revision_id: 37876
language: "en"
categories: []
---

# MTA:Eir/functions/isWorldDualAlphaRenderingEnabled

This function returns whether world dual alpha rendering is enabled. If enabled, first all opaque pixels of entities are rendered and then the alpha pixels, depending on whether they are closer to the screen or not. Otherwise the original rendering method is used which does not use two-pass depth layer rendering.

By enabling world dual alpha rendering, rendering artifacts related to alpha such as seeing through solid surfaces are avoided. By default, it is disabled.

## Syntax

```
bool isWorldDualAlphaRenderingEnabled ()
```

### Returns

Returns **true** if world dual alpha rendering is enabled, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet notifies the user upon join whether this server wants to have alpha issues or not.

```
addEvent( "onClientReady", true );
addEventHandler( "onClientReady", root,
    function()
        if not ( isWorldDualAlphaRenderingEnabled() ) then
            outputChatBox( "This server may have alpha issues." );
        end
    end
);

-- Somewhere along the lines:
triggerEvent( "onClientReady", root );
```
