---
doc_id: "mta-wiki:3324"
title: "Resource : Spawnmanager/setSpawnpointSkin"
source_title: "Resource:Spawnmanager/setSpawnpointSkin"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/setSpawnpointSkin"
revision_id: 14042
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:17:14.476051+00:00"
---

# Resource : Spawnmanager/setSpawnpointSkin

This function sets the skin that players will spawn with when they spawn at the specified spawnpoint.

## Syntax

```
bool setSpawnpointSkin ( spawnpoint theSpawnpoint, int skin )
```

### Required Arguments

- **theSpawnpoint:** The spawnpoint you want to change skin of.

- **skin:** An [int](mta://reference/misc/int.md) corresponding to the ID of the desired skin. See [Character Skins](mta://reference/misc/character-skins.md).

### Returns

Returns *true* if the skin was successfully set, *false* if invalid arguments were passed.

## Example

This code alters all existing spawnpoints so everyone spawns as construction workers.

```
-- get a table of all spawnpoints
local allSpawnpoints = getElementsByType("spawnpoint")
-- for each spawnpoint,
for index, spawn in ipairs (allSpawnpoints) do
    -- change the spawn skin to 27
    call(getResourceFromName("spawnmanager"), "setSpawnpointSkin", spawn, 27 )
end
```
