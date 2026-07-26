---
doc_id: "mta-wiki:7377"
title: "MTA:Eir/functions/engineGetStreamingFocusEntity"
source_title: "MTA:Eir/functions/engineGetStreamingFocusEntity"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetStreamingFocusEntity"
revision_id: 77715
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineGetStreamingFocusEntity

This function returns the entity that the world is streaming around. By default, this is the local player.

## Syntax

```
element engineGetStreamingFocusEntity ()
```

### Returns

Returns the MTA entity that the world is streaming around.

## Example

Click to collapse [-]
Client

This snippet centers the camera around the streaming focus entity.

```
setCameraTarget( entineGetStreamingFocusEntity() );
```
