---
doc_id: "mta-wiki:7403"
title: "MTA:Eir/functions/createCivilian"
source_title: "MTA:Eir/functions/createCivilian"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/createCivilian"
revision_id: 37945
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.365006+00:00"
---

# MTA:Eir/functions/createCivilian

This function creates a civilian. A civilian is a ped that acts like it would in single player.

## Syntax

```
civilian createCivilian ( int model, float x, float y, float z, [ float rot=0 ] )
```

### Arguments

- **model:** A whole integer specifying the [GTASA skin ID](mta://reference/misc/character-skins.md).

- **x, y, z:** position vector on the GTA:SA world

### Optional Arguments

- **rot:** Rotation on the Z axis of the civilian.

### Returns

Returns a civilian if successfully created, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet creates a civilian and warps the local player to it.

```
local myCivilian = createCivilian( 7, 0, 0, 10 );
setElementPosition( localPlayer, 0, 0, 12 );
```
