---
doc_id: "mta-wiki:3330"
title: "Resource : Spawnmanager/setSpawnWave"
source_title: "Resource:Spawnmanager/setSpawnWave"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/setSpawnWave"
revision_id: 17766
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:17:14.462409+00:00"
---

# Resource : Spawnmanager/setSpawnWave

This function sets the spawn wave time.  This can be used in conjunction with [spawnPlayerAtSpawnpoint](mta://resources/spawnmanager-spawnplayeratspawnpoint.md) to spawn players when a wave is reached.

## Syntax

```
bool setSpawnWave ( bool enabled, [ float time = 15000 ] )
```

### Required Arguments

- **enabled:** A bool representing whether to enable waves or not

### Optional Arguments

- **time:** The time, in milliseconds, of how regularly a spawn wave occurs.

### Returns

Returns *true* if the spawnwave was enabled or disabled, or *false* if a bad argument was specified.

## Example

This page lacks an example

```
--add an example here.
```
