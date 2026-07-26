---
doc_id: "mta-wiki:3322"
title: "Resource : Spawnmanager/getSpawnpointTeam"
source_title: "Resource:Spawnmanager/getSpawnpointTeam"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/getSpawnpointTeam"
revision_id: 14038
language: "en"
categories: ["Server_functions"]
---

# Resource : Spawnmanager/getSpawnpointTeam

This function returns the [team](https://wiki.multitheftauto.com/index.php?search=team) element from a particular spawnpoint.

## Syntax

```
team getSpawnpointTeam ( spawnpoint spawn )
```

### Required Arguments

- **spawn:** A valid spawnpoint element.

### Returns

If the spawnpoint given is valid and has a team, it returns a [team](https://wiki.multitheftauto.com/index.php?search=team) element representing the team players will join when spawning there, *false* otherwise.

## Example

This example outputs which team, if any, the spawnpoint is associated with when a player spawns.

```
function checkPlayerSpawn ( theSpawnpoint )
	local outString = "Player spawned"
	local spawnTeam
	
	if ( theSpawnpoint ) then
		outString = outString .. " on a spawnpoint"
		
		spawnTeam = call(getResourceFromName("spawnmanager"), "getSpawnpointTeam", theSpawnpoint )
		if ( spawnTeam ) then
			outString = outString .. " for team: " .. getTeamName ( spawnTeam )
		end
	end
	
	outString = outString .. "."
	outputChatBox ( outString )
end
addEventHandler ( "onPlayerSpawn", getRootElement(), checkPlayerSpawn )
```
