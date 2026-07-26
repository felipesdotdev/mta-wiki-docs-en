---
doc_id: "mta-wiki:3323"
title: "Resource : Spawnmanager/setSpawnpointRotation"
source_title: "Resource:Spawnmanager/setSpawnpointRotation"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/setSpawnpointRotation"
revision_id: 14040
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:17:00.097940+00:00"
---

# Resource : Spawnmanager/setSpawnpointRotation

This function sets the starting Z rotation for the specified spawnpoint.

## Syntax

```
bool setSpawnpointRotation ( spawnpoint theSpawnpoint, float rotation )
```

### Required Arguments

- **theSpawnpoint:** The spawnpoint element you want to set rotation to.

- **rotation:** A [float](mta://reference/misc/float.md) rotation value around the Z axis in degrees.

### Returns

Returns *true* if rotation was successfully set, *false* if invalid arguments were passed.

## Example

This example randomizes a spawnpoint's rotation every time a player spawns on it.

```
-- we define our randomizing function
function randomizeSpawnpointRotation()
	-- we obtain a new value between 0 and 360 (math.random() generates numbers between 0 and 1)
	local newRotation = math.random() * 360
	-- we set it as the new rotation for the source spawnpoint
	call(getResourceFromName("spawnmanager"), "setSpawnpointRotation", source, newRotation )
end
-- we attach it as a handler for "onSpawnpointUse"
addEventHandler("onSpawnpointUse", getRootElement(), randomizeSpawnpointRotation)
```
