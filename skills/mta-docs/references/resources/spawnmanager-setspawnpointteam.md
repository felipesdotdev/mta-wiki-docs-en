---
doc_id: "mta-wiki:3325"
title: "Resource : Spawnmanager/setSpawnpointTeam"
source_title: "Resource:Spawnmanager/setSpawnpointTeam"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ASpawnmanager/setSpawnpointTeam"
revision_id: 14044
language: "en"
categories: ["Server_functions"]
---

# Resource : Spawnmanager/setSpawnpointTeam

This function sets the team that players will be added to when they spawn at the specified spawnpoint. Please note that although players will be removed from any team they were previously in when spawning at a team spawnpoint, spawning at a spawnpoint with no team associated to it won't remove a player from their team.

## Syntax

```
bool setSpawnpointTeam ( spawnpoint spawn, [ team theTeam ] )
```

### Required Arguments

- **spawn:** The spawnpoint element you want to change team of.

### Optional Arguments

- **theTeam:** A [team](https://wiki.multitheftauto.com/index.php?search=team) element representing the team players will join on spawn. If this isn't specified, the spawnpoint is unlinked to any team it was associated to.

### Returns

Returns *true* if the team was successfully set, *false* if invalid arguments were passed.

## Example

This page lacks an example

```
--add an example here
```
