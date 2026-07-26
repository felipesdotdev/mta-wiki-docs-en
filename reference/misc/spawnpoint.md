---
doc_id: "mta-wiki:1844"
title: "Resource : Spawnmanager"
source_title: "Spawnpoint"
source_url: "https://wiki.multitheftauto.com/wiki/Spawnpoint"
revision_id: 30873
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:16:52.217953+00:00"
---

# Resource : Spawnmanager

Spawnmanager is a resource that provides some default spawning functions.  It provides ideal conditions for gamemodes which require fairly basic spawning systems, and uses the <spawnpoint/> element for all its functions.

Spawnmanager also offers basic support for a *waves* spawning system - which involves spawning multiple players at regular periods of time.  Spawnmanager does not internally support delayed spawning, though [setTimer](mta://scripting/shared/functions/settimer.md) can be used in conjunction with [spawnPlayerAtSpawnpoint](mta://resources/spawnmanager-spawnplayeratspawnpoint.md) to achieve this.

## Functions

The following functions are exported as part of spawnmanager:

- [createSpawnpoint](mta://resources/spawnmanager-createspawnpoint.md)

- [getSpawnpointRotation](mta://resources/spawnmanager-getspawnpointrotation.md)

- [getSpawnpointSkin](mta://resources/spawnmanager-getspawnpointskin.md)

- [getSpawnpointTeam](mta://resources/spawnmanager-getspawnpointteam.md)

- [setSpawnpointRotation](mta://resources/spawnmanager-setspawnpointrotation.md)

- [setSpawnpointSkin](mta://resources/spawnmanager-setspawnpointskin.md)

- [setSpawnpointTeam](mta://resources/spawnmanager-setspawnpointteam.md)

- [spawnPlayerAtSpawnpoint](mta://resources/spawnmanager-spawnplayeratspawnpoint.md)

- [setSpawnWave](mta://resources/spawnmanager-setspawnwave.md)

## Events

The following events are provided:

- [onSpawnpointUse](mta://resources/spawnmanager-onspawnpointuse.md)
