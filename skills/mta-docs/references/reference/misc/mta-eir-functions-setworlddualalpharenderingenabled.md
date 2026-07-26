---
doc_id: "mta-wiki:7394"
title: "MTA:Eir/functions/setWorldDualAlphaRenderingEnabled"
source_title: "MTA:Eir/functions/setWorldDualAlphaRenderingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/setWorldDualAlphaRenderingEnabled"
revision_id: 37873
language: "en"
categories: []
---

# MTA:Eir/functions/setWorldDualAlphaRenderingEnabled

This function modifies the rendering order, the rendering complexity and the render-states assigned to world entity rendering. If world dual alpha rendering is enabled, first all opaque pixels of entities are rendered and then the alpha pixels, depending on whether they are closer to the screen or not. Otherwise the original rendering method is used which does not use two-pass depth layer rendering.

By enabling world dual alpha rendering, rendering artifacts related to alpha such as seeing through solid surfaces are avoided. By default, it is disabled.

## Syntax

```
bool setWorldDualAlphaRenderingEnabled ( bool enabled )
```

### Returns

Returns **true** if enabled is passed as valid boolean, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet should fix many annoying alpha issues on the main GTA:SA world.

```
setWorldDualAlphaRenderingEnabled( true );
```
