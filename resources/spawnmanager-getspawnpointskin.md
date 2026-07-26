---
doc_id: "mta-wiki:3321"
title: "Resource : Spawnmanager/getSpawnpointSkin"
source_title: "Resource:Spawnmanager/getSpawnpointSkin"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/getSpawnpointSkin"
revision_id: 14036
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:17:00.053935+00:00"
---

# Resource : Spawnmanager/getSpawnpointSkin

This function returns the ID of the current skin from a particular spawnpoint.

## Syntax

```
int getSpawnpointSkin ( spawnpoint spawn )
```

### Required Arguments

- **spawn:** A valid spawnpoint element.

### Returns

Returns an [int](mta://reference/misc/int.md) containing the [skin ID](mta://reference/misc/character-skins.md) if the spawnpoint exists, *false* otherwise.

## Example

This example outputs the skin, if any, associated with a spawnpoint when a player spawns.

```
function checkPlayerSpawn ( theSpawnpoint )
	local outString = "Player spawned"
	local spawnSkin
		
	if ( theSpawnpoint ) then
		outString = outString .. " on a spawnpoint"
		
		spawnSkin = call(getResourceFromName("spawnmanager"), "getSpawnpointSkin", theSpawnpoint )
		if ( spawnSkin ) then
			outString = outString .. " with skin: " .. tostring(spawnSkin)
		end
	end
	
	outString = outString .. "."
	outputChatBox ( outString )
end
addEventHandler ( "onPlayerSpawn", getRootElement(), checkPlayerSpawn )
```
