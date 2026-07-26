---
doc_id: "mta-wiki:3327"
title: "Resource : Spawnmanager/onSpawnpointUse"
source_title: "Resource:Spawnmanager/onSpawnpointUse"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/onSpawnpointUse"
revision_id: 14050
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:17:14.444786+00:00"
---

# Resource : Spawnmanager/onSpawnpointUse

This event is triggered when a player spawns at a spawnpoint.

## Syntax

```
void onSpawnpointUse ( player player )
```

## Variables

- The [source](mta://reference/misc/event-system.md) of this event refers to the spawnpoint that was used when a player spawned

- **player**:  A player element representing the player who spawned at the source spawnpoint.

## Example

This example plays a sound when a player spawns

```
function spawnUse ( player ) --when a player spawns
	playSoundFrontEnd ( player, 16 ) --play a sound for him
end
addEventHandler ( "onSpawnpointUse", getElementRoot(), spawnUse ) --add an event for onSpawnpointUse
```
