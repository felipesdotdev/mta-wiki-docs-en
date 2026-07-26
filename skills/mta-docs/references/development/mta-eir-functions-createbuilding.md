---
doc_id: "mta-wiki:7398"
title: "MTA:Eir/functions/createBuilding"
source_title: "MTA:Eir/functions/createBuilding"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/createBuilding"
revision_id: 38263
language: "en"
categories: []
---

# MTA:Eir/functions/createBuilding

This function creates a building. A building is a special type of [object](https://wiki.multitheftauto.com/index.php?search=object) that does not have physical properties itself. It is lightweight rendering and collidable instance on the GTA:SA world. As opposed to Objects, buildings do not stream. They can have an infinite drawing distance.

This function is part of the discussion: **[shall buildings be made MTA entities?](https://wiki.multitheftauto.com/wiki/Talk:MTA:Eir/functions/createBuilding)**

## Syntax

```
building createBuilding ( int model, float x, float y, float z )
```

### Arguments

- **model:** the atomic model info index to use with this model

- **x, y, z:** position vector on the GTA:SA world

### Returns

Returns a building instance if successfully created, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet creates a random building instance and warps the local player to it.

```
local myBuilding = createBuilding( 3376, 0, 0, 10 );
setElementPosition( localPlayer, 0, 0, 12 );
```
