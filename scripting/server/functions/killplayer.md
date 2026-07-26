---
doc_id: "mta-wiki:1348"
title: "KillPlayer"
source_title: "KillPlayer"
source_url: "https://wiki.multitheftauto.com/wiki/KillPlayer"
revision_id: 67663
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:03.900538+00:00"
---

# KillPlayer

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use killPed instead. |  |

This function kills the specified player.

## Syntax

```
bool killPlayer ( player thePlayer, [ player theKiller = nil, int weapon=255, int bodyPart=255 ] )
```

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) to kill

### Optional Arguments

- **theKiller:** The player responsible for the kill

- **weapon:** The ID of the weapon that should appear to have killed the player (doesn't affect how they die)

- **bodyPart:** The ID of the body part that should appear to have been hit by the weapon (doesn't affect how they die)

### Returns

Returns *true* if the player was killed, *false* if the player specified could not be killed or is invalid.

## Example

**Example 1:** This simple example adds a **kill** command to commit suicide.

```
function commitSuicide(sourcePlayer)
	-- kill the player and make him responsible for it
	killPlayer(sourcePlayer, sourcePlayer)
end
-- attach our handler to the "kill" command
addCommandHandler("kill", commitSuicide)
```

**Example 2:** This example enables 1 hit kills if a player is shot in the head.

```
function headshotKill ( attacker, attackerweapon, bodypart, loss )
	if bodypart == 9 then --if the bodypart is the head
		--kill the player, emulating the correct killer, weapon and bodypart.
		killPlayer ( source, attacker, attackerweapon, bodypart )
	end
end
addEventHandler ( "onPlayerDamage", root, headshotKill )
```

## See Also

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
