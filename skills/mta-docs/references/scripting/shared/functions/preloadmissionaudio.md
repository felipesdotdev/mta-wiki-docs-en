---
doc_id: "mta-wiki:2482"
title: "PreloadMissionAudio"
source_title: "PreloadMissionAudio"
source_url: "https://wiki.multitheftauto.com/wiki/PreloadMissionAudio"
revision_id: 27909
language: "en"
categories: ["Disabled_Functions_and_Events", "Server_functions", "Client_functions"]
---

# PreloadMissionAudio

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: Its functionality left for a post-r1 release - Bugtracker Issue: #1838 |  |

This function preloads a game sound into a specific sound slot. The sound can then be played with [PlayMissionAudio](https://wiki.multitheftauto.com/index.php?title=PlayMissionAudio&action=edit&redlink=1).

## Syntax

Click to collapse [-]
Server

```
bool preloadMissionAudio ( player thePlayer, int sound, int slot )
```

### Required Arguments

- **thePlayer:** the [player](https://wiki.multitheftauto.com/index.php?search=player) you want to play the sound for.

- **sound:** the [int](mta://reference/misc/int.md) sound id to play (interpreted as unsigned short). Valid values are those from the **data/AudioEvents.txt** file.

- **slot:** [int](mta://reference/misc/int.md) sound slot in which you preloaded the sound.

Click to collapse [-]
Client

```
bool preloadMissionAudio ( int sound, int slot )
```

### Required Arguments

- **sound:** the [int](mta://reference/misc/int.md) sound id to play (interpreted as unsigned short). Valid values are those from the **data/AudioEvents.txt** file.

- **slot:** [int](mta://reference/misc/int.md) sound slot in which you preloaded the sound.

### Returns

Returns *true* if the sound was successfully preloaded, *false* otherwise.

## Example

Click to collapse [-]
server

This example plays a sound when a player spawns

```
function onPlayerSpawn ( theSpawnpoint, theTeam )
    preloadMissionAudio ( source, 5000, 1 )
    local x, y, z = getElementPosition ( source )
    playMissionAudio ( source, 1, x, y, z )
end
addEventHandler ( "onPlayerSpawn", getElementRoot(), onPlayerSpawn )
```

Click to collapse [-]
client

This example plays a sound when the server triggers the onSoundEvent client event.

```
function onSoundEvent ( )
    preloadMissionAudio ( source, 5000, 1 )
    local x, y, z = getElementPosition ( source )
    playMissionAudio ( 1, x, y, z )
end
addEvent ( "onSoundEvent" )
addEventHandler ( "onSoundEvent", getElementRoot(), onSoundEvent )
```

## See Also

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
