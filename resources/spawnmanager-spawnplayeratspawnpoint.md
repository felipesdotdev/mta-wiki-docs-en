---
doc_id: "mta-wiki:3326"
title: "Resource : Spawnmanager/spawnPlayerAtSpawnpoint"
source_title: "Resource:Spawnmanager/spawnPlayerAtSpawnpoint"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/spawnPlayerAtSpawnpoint"
revision_id: 17765
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:17:00.128432+00:00"
---

# Resource : Spawnmanager/spawnPlayerAtSpawnpoint

This function spawns the player at a spawnpoint.

## Syntax

```
bool spawnPlayerAtSpawnpoint ( player thePlayer, [spawnpoint theSpawnpoint = random, bool useWaves ] )
```

### Required Arguments

- **thePlayer:** the player to spawn

### Optional Arguments

- **theSpawnpoint:** the spawnpoint element at which to spawn the player.  If this is not specified, or *false* is passed, a random spawnpoint will be used.

- **useWaves:** Specifies whether spawn waves will be used from [setSpawnWave](mta://resources/spawnmanager-setspawnwave.md).  If no wave has been set, this will be ignored.

### Returns

Returns *true* if the player was spawned successfully, *false* otherwise.

## Example

This example spawns all the players in the map at the first spawnpoint there is.

```
-- Get a table of all the players
players = getElementsByType ( "player" )
-- Get a table of all the spawnpoints
spawnpoints = getElementsByType ( "spawnpoint" )
-- Go through every player
for playerKey, playerValue in players do
	-- Spawn them at the first spawnpoint
	call(getResourceFromName("spawnmanager"), "spawnPlayerAtSpawnpoint", playerValue, spawnpoints[1] )
end
```
