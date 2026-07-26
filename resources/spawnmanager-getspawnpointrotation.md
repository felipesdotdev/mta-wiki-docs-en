---
doc_id: "mta-wiki:3320"
title: "Resource : Spawnmanager/getSpawnpointRotation"
source_title: "Resource:Spawnmanager/getSpawnpointRotation"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/getSpawnpointRotation"
revision_id: 14034
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:17:00.046553+00:00"
---

# Resource : Spawnmanager/getSpawnpointRotation

This function returns the current rotation of the specified spawnpoint.

## Syntax

```
float getSpawnpointRotation ( spawnpoint theSpawn )
```

### Required Arguments

- **theSpawn:** The spawnpoint element to get rotation of.

### Returns

Returns the rotation as a [float](mta://reference/misc/float.md) if the spawnpoint is valid, *false* otherwise.

## Example

This example outputs the rotation associated with a spawnpoint when a player spawns.

```
function checkPlayerSpawn ( theSpawnpoint )
	local outString = "Player spawned"
	local spawnRotation
		
	if ( theSpawnpoint ) then
		outString = outString .. " on a spawnpoint"
		
		spawnRotation = call(getResourceFromName("spawnmanager"), "getSpawnpointRotation", theSpawnpoint )
		if ( spawnRotation ) then
			outString = outString .. " with rotation: " .. tostring(spawnRotation)
		end
	end
	
	outString = outString .. "."
	outputChatBox ( outString )
end
addEventHandler ( "onPlayerSpawn", getRootElement(), checkPlayerSpawn )
```
