---
doc_id: "mta-wiki:5344"
title: "Slothman/Zombies"
source_title: "Slothman/Zombies"
source_url: "https://wiki.multitheftauto.com/wiki/Slothman/Zombies"
revision_id: 75787
language: "en"
categories: []
generated_at: "2026-07-26T16:16:51.458410+00:00"
---

# Slothman/Zombies

This is a resource designed spawn the undead wherever a player roams outside. It works without any configuration or scripting skills needed, but there are a few option for gamemode designers to use.

# Features

**Skins:**
There have been many contributed skins that change peds to look like the rotting/gory undead

**Semi-intelligence:**
Zombies are fairly mindless by nature, but they do have basic motor skills like being able to jump over objects, climb ledges, walk around corners, and break through barriers

**Behaviour:**
Zombies endlessly attack any player or ped that isn't one of them, then feast briefly on the remains before wandering off in search of more flesh

**Streaming:**
By default, anywhere a player goes outside will have a fairly dense population of zombies. this is done by deleting zombies that far away and spawning new ones within a close radius of the players.

**Gamemode/Script integration:**
This script provides several functions and events to allow other resources to see and control the zombies

**Helmet Zombies:**
zombie + helmet = big trouble! no headshots against these flesheaters.

**Choose your apocalypse:**
server option allows you to choose between allowing zombies to spawn anywhere, only at certain spawnpoints, or only when a script tells it to

**EDF:**
lets map designers pick where zombies spawn when that method of creating zombies is chose

# Server Options

There are 2 server options to customize the script's effect.

## MaxZombies

Allows the server to set the maximum allowable zombie population. Map resources can reduce this limit, but never exceed it.

## StreamMethod

Tells the script how to create zombies. set this option to 1 to allow random spawning anywhere in San Andreas. Set to 2 to only allow zombies to spawn where zombie spawnpoints have been placed. Set to 0 to spawn no zombies automatically, but allow scripts to spawn zombies using the exported function.

# Server Events

## onZombieSpawn

This triggers when a Zombie is streamed in automatically. It is a cancellable event, so scripts and gamemode can prevent zombies from spawning in certain areas.

**Parameters**

```
float x, float y, float z
```

- **x**: The X coord of the spawn location

- **y**: The Y coord of the spawn location

- **z**: The Z coord of the spawn location

**Source**

The [source](mta://reference/misc/event-system.md) of this event is the Zombie that is spawning

## onZombieWasted

This triggers when a zombie is killed.
**Parameters**

```
element attacker, float weapon, float bodypart
```

- **attacker**: The Element that killed the zombie

- **weapon**: The weapon id used to kill the zombie

- **bodypart**: The bodypart id that was hit to kill the zombie

**Source**

The [source](mta://reference/misc/event-system.md) of this event is the zombie that died

# Server Functions

All of these funtions will have to be used through the [call](mta://scripting/shared/functions/call.md) function, otherwise they won't work

## createZombie

This function spawns a zombie ingame, will return the zombie element, or false if there was a problem.

**Syntax**

```
element createZombie( float x, float y, float z, [int rotation = 0, int skinID = 0, int interior = 0, int dimension = 0 ] )
```

**Required Arguments**

- **x:** The x co-ordinate to spawn the zombie

- **y:** The y co-ordinate to spawn the zombie

- **z:** The z co-ordinate to spawn the zombie

**Optional Arguments**

- **rotation:** Rotation of the zombie on spawn

- **skinID:** skin on spawn

- **interior:** Interior the zombie will spawn into

- **dimension:** The ID of the [dimension](mta://reference/misc/dimension.md) that the zombie should be in

## isPedZombie

returns true if the ped is a zombie, false otherwise

**Syntax**

```
bool isPedZombie( element thePed)
```

**Required Arguments**

- **thePed:** The ped you want to check if its a zombie

# Credits

- **Slothman:** Creator/scripter/skin artist

- **Various artists:** see the client script to view zombie skin creators.

- **Thanks to Everyone else who made suggestions, tested the script, helped when i was stuck, etc**

# Other

Статья на русском : [https://wiki.multitheftauto.com/wiki/Slothman/%D0%97%D0%BE%D0%BC%D0%B1%D0%B8](https://wiki.multitheftauto.com/wiki/Slothman/%D0%97%D0%BE%D0%BC%D0%B1%D0%B8)
