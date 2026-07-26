---
doc_id: "mta-wiki:6632"
title: "Slothman/Slothbot"
source_title: "Slothbot"
source_url: "https://wiki.multitheftauto.com/wiki/Slothbot"
revision_id: 71588
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:16:51.333993+00:00"
---

# Slothman/Slothbot

This is a resource designed to allow scripts or gamemodes to insert a ped into the game that roughly simulates combat with a real player. Gamemodes can implement the bots as opponents to actual players or as teammates.  

Download can be found at [MTA Community - Slothbot](https://community.multitheftauto.com/index.php?p=resources&s=details&id=672)

# Features

**Teamplay:**
The bot is capable of identifying friend from foe

**Map Navigation:**
When the bot is placed in a map that has suitable pathways marked out (see below on how to do that) the bot will navigate the map, seeking out enemies. Without pathways, a bot can still think for itself, but wont move around as proficiently.

**Aggressiveness:**
Bots will attack any ped, player or bot that's not on it's team.

**Cooperation:**
Bots can automatically team up with teammates (either player or bot) by meeting up with them and sticking together

**Advanced movement:**
If there's obstacles blocking a bots path, the bot will attempt to get around or over it instead of just walking into a wall for eternity

**Multiple modes of playing:**

- "hunting" - travel pathways until finding an enemy or teammate

- "waiting" - stand still until an enemy of teammate comes into view

- "guarding" - the bot will attack any enemy that comes within sight, but not move from its spawn position

- "following" - the bot will follow a player or bot while attacking enemies

- "chasing" - the bot will attack an enemy bot or player

**Gamemode/Script integration:**
This script provides several functions and events to allow other resources to see and control what the bot's are doing, and even take control of certain behavior.

**EDF for map path creation:**
Integrated into the map editor, map designers can easily place paths for bots to follow along in their maps. this greatly increased the bots ability to simulate true playing.

# Server Events

## onBotFindEnemy

This triggers when a bot locates an enemy, This event can be cancelled to prevent the bot from chasing players

**Parameters**

```
element enemy
```

- **enemy**: The Player or Ped the bot has spotted

**Source**

The [source](mta://reference/misc/event-system.md) of this event is the Bot that has found an enemy

## onBotWasted

This triggers when a bot is killed.

**Parameters**

```
element attacker, float weapon, float bodypart
```

- **attacker**: The Element that killed the bot

- **weapon**: The weapon id used to kill the bot

- **bodypart**: The bodypart id that was hit to kill the bot

**Source**

The [source](mta://reference/misc/event-system.md) of this event is the Bot that died

## onBotSpawned

This triggers when a bot is spawned.

**Source**
The [source](mta://reference/misc/event-system.md) of this event is the Bot that spawned

## onBotFollow

This triggers when a bot starts following a teammate

**Parameters**

```
element leader
```

- **leader**: The Player or Ped the bot has started following

**Source**

The [source](mta://reference/misc/event-system.md) of this event is the Bot that starts following a teammate

# Server Functions

All of these functions will have to be used through the [call](mta://scripting/shared/functions/call.md) function, otherwise they won't work

## spawnBot

This function spawns a bot ingame, will return the bot element, or false if there was a problem.

**Syntax**

```
element spawnBot ( float x, float y, float z, int rotation = 0, [ int skinID = 0, int interior = 0, int dimension = 0, team theTeam = nil, int weapon = 0, string theMode = "hunting", element theModesubject = nil ] )
```

**Required Arguments**

- **x:** The x co-ordinate to spawn the bot at

- **y:** The y co-ordinate to spawn the bot at

- **z:** The z co-ordinate to spawn the bot at

- **rotation:** Rotation of the bot on spawn

**Optional Arguments**

- **skinID:** Bots skin on spawn

- **interior:** Interior the bot will spawn into

- **dimension:** The ID of the [dimension](mta://reference/misc/dimension.md) that the bot should be in

- **theTeam:** The team the bot will join. Set *false* to the bot not join a team.

- **weapon:** The weapon the ped will carry

- **theMode:** The action the bot will be performing when spawned (see "modes of playing" above)

- **theModeSubject:** If theMode is "chasing" or "following" this arg is needed to tell the bot what opponent to chase or teammate to follow

## setBotHunt

makes the bot travel pathways until finding an enemy or teammate

**Syntax**

```
bool setBotHunt ( element theBot )
```

**Required Arguments**

- **theBot:** The bot you want to hunt

## setBotWait

makes the bot stand still until an enemy of teammate comes into view

**Syntax**

```
bool setBotWait ( element theBot )
```

**Required Arguments**

- **theBot:** The bot you want to wait

## setBotChase

makes the bot attack an anemy bot or player

**Syntax**

```
bool setBotChase ( element theBot, element theTarget )
```

**Required Arguments**

- **theBot:** The bot that you want to do the chasing

- **theTarget:** The bot or player you want to be chased

## setBotFollow

makes the bot follow a teammate bot or player

**Syntax**

```
bool setBotFollow( element theBot, element theTarget )
```

**Required Arguments**

- **theBot:** The bot that you want to do the following

- **theTarget:** The bot or player you want to be followed

## setBotGuard

makes the bot move to the specific coords and stay there while attacking any enemies

**Syntax**

```
bool setBotGuard( element theBot, float x, float y, float z, [ bool priority = false ] )
```

**Required Arguments**

- **theBot:** The bot you want to do the guarding

- **x:** The X coords you want the bot to guard

- **y:** The Y coords you want the bot to guard

- **z:** The Z coords you want the bot to guard

**Optional Arguments**

- **priority:** Set to true only if you want the bot to only shoot once it has reached the location to guard

## getBotTeam

returns the Team the bot is on, false if no team

**Syntax**

```
string getBotTeam ( element theBot)
```

**Required Arguments**

- **theBot:** The bot you want to check the team of

## setBotTeam

changes the bot's team and loyalties

**Syntax**

```
bool setBotTeam ( element theBot, team theTeam )
```

**Required Arguments**

- **theBot:** The bot you want to change the team of

- **theTeam:** The team the bot should join

## getBotAttackEnabled

returns true if the bot is allowed to attack, false otherwise

**Syntax**

```
bool getBotAttackEnabled( element theBot)
```

**Required Arguments**

- **theBot:** The bot you want to check if it can attack

## setBotAttackEnabled

allow or disallow the bot to attack (press fire)

**Syntax**

```
bool setBotAttackEnabled( element theBot, bool enabled)
```

**Required Arguments**

- **theBot:** The bot you want to set if it can attack

- **enabled:** set to false to remove the bots ability to attack, true to allow it

## getBotMode

returns the mode the bot is in ("chasing", "waiting", "guarding", "hunting", "following") or if the bot is chasing or following, it will return the mode and the target

**Syntax**

```
string getBotMode( element theBot)
```

**Required Arguments**

- **theBot:** The bot you want to check the status of

## isPedBot

returns true if the ped is a bot, false otherwise

**Syntax**

```
bool isPedbot( element thePed)
```

**Required Arguments**

- **thePed:** The ped you want to check if its a bot

## setBotWeapon

sets the bots weapon id (ammo is always infinite)

**Syntax**

```
bool setBotWeapon( element theBot, float weapon)
```

**Required Arguments**

- **theBot:** The bot you want to set the weapon of

- **weapon:** the weapon id you want to give the bot

# Credits

- **Slothman:** Bot creator, main scripter

- **Gamesnert:** EDF creator, scripting, testing

- **Dragon:** Gamemode creator, testing, scripting help

- **EvGeniz:** early testing, mapping

**Thanks to Everyone else who made suggestions, tested the script, helped when i was stuck, etc**
