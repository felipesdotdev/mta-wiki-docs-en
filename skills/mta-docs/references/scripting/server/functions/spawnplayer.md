---
doc_id: "mta-wiki:1567"
title: "SpawnPlayer"
source_title: "SpawnPlayer"
source_url: "https://wiki.multitheftauto.com/wiki/SpawnPlayer"
revision_id: 80408
language: "en"
categories: ["Server_functions"]
---

# SpawnPlayer

This function spawns the player at an arbitrary point on the map.

| [[{{{image}}}\|link=\|]] | Note: setCameraTarget must be used to focus on the player. Also, all players have their camera initially faded out after connect. To ensure that the camera is faded in, please do a fadeCamera after. |
| --- | --- |
|  |  |

## Syntax

```
bool spawnPlayer ( player thePlayer, float x, float y, float z, [ int rotation = 0, int skinID = 0, int interior = 0, int dimension = 0, team theTeam = getPlayerTeam(thePlayer) ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):spawn(...)*

### Required Arguments

- **thePlayer:** The player you want to spawn.

- **x:** The x co-ordinate to spawn the player at.

- **y:** The y co-ordinate to spawn the player at.

- **z:** The z co-ordinate to spawn the player at.

### Optional Arguments

- **rotation:** rotation of the player on spawn.

- **skinID:** player's skin on spawn. [Character Skins](mta://reference/misc/character-skins.md)

- **interior:** interior the player will spawn into. [Interior IDs](mta://reference/misc/interior-ids.md)

- **dimension:** The ID of the [dimension](mta://reference/misc/dimension.md) that the player should be in.

- **theTeam:** the team the player will join.

### Returns

Returns *true* if the player was spawned successfully, *false* otherwise.

## Example

This example spawns all the players in the middle of the game map.

```
-- Get a table of all the players
local players = getElementsByType ( "player" )
-- Go through every player
for _, player in ipairs(players) do
	-- Spawn them at the desired coordinates
	spawnPlayer ( player, 0.0, 0.0, 5.0, 90.0, 0 )
	fadeCamera ( player, true)
	setCameraTarget ( player, player )
end
```

This example spawns a player **when he logs in.**

```
spawnTeam = createTeam ("Teamname", 255, 0, 0) -- Create team to spawn.
function spawnOnLogin (prevA, curA )
	outputChatBox ("Welcome to ...", source, 255, 0, 0, false)
	spawnPlayer (source, 0, 0, 5, 0, math.random (0,288), 0, 0, spawnTeam) -- spawns player with random skin
	fadeCamera (source, true)
	setCameraTarget (source, source)
end
addEventHandler("onPlayerLogin", root, spawnOnLogin)
```

## See Also

- [getAlivePlayers](mta://scripting/server/functions/getaliveplayers.md)

- [getDeadPlayers](mta://scripting/server/functions/getdeadplayers.md)

- [getPlayerAnnounceValue](mta://scripting/server/functions/getplayerannouncevalue.md)

- [getPlayerCount](mta://scripting/server/functions/getplayercount.md)

- [getPlayerIdleTime](mta://scripting/server/functions/getplayeridletime.md)

- [getPlayerIP](mta://scripting/server/functions/getplayerip.md)

- [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md)

- [getRandomPlayer](mta://scripting/server/functions/getrandomplayer.md)

- [isPlayerMuted](mta://scripting/server/functions/isplayermuted.md)

- [redirectPlayer](mta://scripting/server/functions/redirectplayer.md)

- [resendPlayerACInfo](mta://scripting/server/functions/resendplayeracinfo.md)

- [resendPlayerModInfo](mta://scripting/server/functions/resendplayermodinfo.md)

- [setPlayerAnnounceValue](mta://scripting/server/functions/setplayerannouncevalue.md)

- [setPlayerMuted](mta://scripting/server/functions/setplayermuted.md)

- [setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md)

- [setPlayerTeam](mta://scripting/server/functions/setplayerteam.md)

- [setPlayerName](mta://scripting/server/functions/setplayername.md)

- [setPlayerVoiceBroadcastTo](mta://scripting/server/functions/setplayervoicebroadcastto.md)

- [setPlayerVoiceIgnoreFrom](mta://scripting/server/functions/setplayervoiceignorefrom.md)

- [setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)

- spawnPlayer

- [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md)
  

- **Shared**

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
