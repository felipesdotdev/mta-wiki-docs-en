---
doc_id: "mta-wiki:3522"
title: "Resource : Race"
source_title: "Resource:Race"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ARace"
revision_id: 82011
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:14.028053+00:00"
---

# Resource : Race

The "race" gamemode organizes sprint or freeroam races for one or more players. It supports both maps from MTA:Race and maps in the MTA:SA DM map syntax that were created in the map editor.

## Ingame

Playing race is quite straightforward. If there are checkpoints, drive from checkpoint to checkpoint and be the first to reach the finish line within the time. If there are no checkpoints, just drive around and have fun.

In races you may encounter three types of pickups which will have an effect on your vehicle:

- **Repair pickups:** this pickup looks like a wrench. If you drive over it, your vehicle will be restored to full health.

- **Nitrous oxide pickups:** a red NOS bottle. After you drive over one you can press the fire button (by default the left mouse button) to get a temporary speed boost.

- **Vehicle change pickups:** these display the name of a vehicle above them. As soon as you drive over a pickup your vehicle will be changed.

Lastly, if you get stuck during a race, you can enter the /kill command in the chatbox or press your vehicle enter/exit key to kill yourself and respawn at the previous checkpoint.

## Converting MTA:Race maps

Use the [batch converter](https://web.archive.org/web/20120128231117/https://files.mtasa.com/apps/1.0/raceconv.zip) to convert all your MTA:Race maps into MTA:SA maps in one go.

## Map syntax

You can create race maps using the MTA:SA [map editor](mta://resources/editor.md). The map syntax is given here for reference.

### .map file

```
<map>
    <!-- One or more -->
    <spawnpoint id="Textual or numeric spawnpoint ID" vehicle="Vehicle ID" interior="Interior ID" posX="posX" posY="posY" posZ="posZ" rotX="rotX" rotY="rotY" rotZ="rotZ" [ paintjob="Paintjob ID" upgrades="Comma-separated list of upgrades" ]></spawnpoint>

    <!-- Zero or more --> 
    <checkpoint id="Textual or numeric checkpoint ID" type="checkpoint|ring|corona|cylinder|arrow" color="#RrGgBbAa" size="Checkpoint size" interior="Interior ID" nextid="ID of checkpoint after this one" posX="posX" posY="posY" posZ="posZ" rotX="rotX" rotY="rotY" rotZ="rotZ" [ vehicle="Vehicle ID to change into" paintjob="Paintjob ID" upgrades="Comma-separated list of upgrades" ]></checkpoint>

    <!-- Zero or more -->
    <racepickup id="Textual or numeric pickup ID" type="nitro|repair|vehiclechange" respawn="Respawn time in milliseconds" interior="Interior ID" posX="posX" posY="posY" posZ="posZ" rotX="rotZ" rotY="rotY" rotZ="rotZ" [ vehicle="Vehicle ID to change into, if a vehiclechange pickup" paintjob="Paintjob ID" upgrades="Comma-separated list of upgrades" ]></racepickup>
</map>
```

Keep in mind that currently the cylinder checkpoint type uses the sphere [colshape](mta://reference/misc/element-collision-shape.md), not tube like you would expect.

### meta.xml

```
<meta>
    <info type="map" gamemodes="race" name="Map name" author="Author name" description="Map description" version="Map version number"/>
    <race src="Map file.map"/>
    <settings>
        <setting name="#optionName" value="optionValue"/>
        ...
    </settings>
</meta>
```

The <setting>s correspond to options in MTA:Race syntax. For example, 4:0 in MTA:Race syntax would correspond to <setting name="#time" value="4:0"/> in DM syntax.

## Addons

A Race 'addon' is no different from any other script resource, except that is has addon="race" in the <info> section of it's meta.xml file. This is simply to allow Race to identify it and put it in the /config menu for you. Addons communicate with Race via events. The current list of Race events and what they do are here:

## Events for version 0.8.3

**Note:** You may have to add the events in your script using addEvent() if you want to use them.

### Server

| Name | Source | Parameters |
| --- | --- | --- |

| onPlayerReachCheckpoint | player | int checkpoint, int time_ |
| --- | --- | --- |

| onPlayerPickUpRacePickup | player | int/string pickupID, string pickupType, int vehicleModel |
| --- | --- | --- |

| onMapStarting |  | table mapInfo, table mapOptions, table gameOptions |
| --- | --- | --- |

| onPlayerFinish | player | int rank, int time |
| --- | --- | --- |

| onPostFinish |  |  |
| --- | --- | --- |

| onPollStarting |  | table poll |
| --- | --- | --- |

| onRaceStateChanging |  | string newStateName, string oldStateName |
| --- | --- | --- |

| onPlayerRaceWasted | player | vehicle playersVehicle |
| --- | --- | --- |

### Client

| onClientMapStarting |  | table mapinfo |
| --- | --- | --- |

| onClientPlayerFinish | player |  |
| --- | --- | --- |

| onClientPlayerOutOfTime | player |  |
| --- | --- | --- |

| onClientMapStopping |  |  |
| --- | --- | --- |

| onClientScreenFadedOut |  |  |
| --- | --- | --- |

| onClientScreenFadedIn |  |  |
| --- | --- | --- |

## Events for version 0.8.3 in detail

**Note:** You may have to add the events in your script using addEvent() if you want to use them.

### onRaceStateChanging

Triggered when the race resource starts doing something else.

### Parameters

```
string newState, string oldState
```

- **newState:** the new state

- **oldState:** the old state

Possible states:

- undefined

- NoMap

- LoadingMap

- PreGridCountdown

- GridCountdown

- Running

- MidMapVote

- SomeoneWon

- TimesUp

- EveryoneFinished

- PostFinish

- NextMapSelect

- NextMapVote

- ResourceStopping

### Source

The root element.

### onPlayerReachCheckpoint

Triggered when a player reaches any checkpoint but the last one.

#### Parameters

```
int checkpoint, int time
```

- **checkpoint:** the number of the checkpoint the player went through. The first checkpoint has number 1.

- **time:** time since the race started, in milliseconds.

#### Source

The source is the player that reached the checkpoint.

### onPlayerFinish

Triggered when a player reaches the last checkpoint (i.e. has finished the race)

#### Parameters

```
int rank, int time
```

- **rank:** the player's rank. 1 means he won the race, 2 that he came in second place, etc.

- **time:** time since the race started, in milliseconds.

#### Source

The source is the player that finished the race.

### onPlayerPickUpRacePickup

#### Parameters

```
int/string pickupID, string pickupType, int vehicleModel
```

- **pickupID:** the number of the pickup in case of MTA:Race syntax (starting at 1), or the "id" attribute of the pickup in case of DM syntax.

- **pickupType:** the pickup type. Can be "nitro", "repair" or "vehiclechange".

- **vehicleModel:** if the pickup is of type vehiclechange, this is the vehicle model that it sets.

#### Source

The source is the player that picked up the pickup.

## Element data

These element data are set on each player:

- **race rank:** the current position of the player in the race. 1 = first, 2 = second etc. Updated on a 1 second interval.

- **race.checkpoint:** the number of the checkpoint the player is *heading for*. When the player spawns this number is 1, after he passed the first checkpoint it's 2, etc.

- **race.finished:** *true* if the player has finished, *false* if he's still racing.

This server only element data is set for the resource root element:

- **info:** which contains a table with these sub-tables: **mapInfo**, **mapOptions** and **gameOptions**.

## Super Advanced Element data

You can also set player element data to change the player collision status and render transparency:

```
e.g. setElementData( thePlayer, "overrideCollide.uniqueblah", 0, false )		-- Collide 'off' for this player
     setElementData( thePlayer, "overrideCollide.uniqueblah", nil, false )		-- Collide 'default' for this player
     setElementData( thePlayer, "overrideAlpha.uniqueblah", 120, false )		-- Alpha '120 maximum' for this player
     setElementData( thePlayer, "overrideAlpha.uniqueblah", nil, false )		-- Alpha 'default' for this player
```

Set 'uniqueblah' to whatever you like (up to 15 characters long)

## Exported Server functions

| int | getTimePassed |  |
| --- | --- | --- |

| int | getPlayerRank | player thePlayer |
| --- | --- | --- |

| boolean | isPlayerFinished | player thePlayer |
| --- | --- | --- |

| vehicle | getPlayerVehicle | player thePlayer |
| --- | --- | --- |
