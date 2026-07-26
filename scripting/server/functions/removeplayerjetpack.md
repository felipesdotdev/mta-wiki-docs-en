---
doc_id: "mta-wiki:1759"
title: "RemovePlayerJetPack"
source_title: "RemovePlayerJetPack"
source_url: "https://wiki.multitheftauto.com/wiki/RemovePlayerJetPack"
revision_id: 40346
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:32.576201+00:00"
---

# RemovePlayerJetPack

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use removePedJetPack instead. |  |

This function is used to remove a player's jetpack.

## Syntax

```
bool removePlayerJetPack ( player thePlayer )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) you want to remove the jetpack from.

### Returns

Returns *true* if the player had a jetpack, *false* otherwise.

## Example

This example adds a "jetpack" command in console, which allows toggling of a jetpack.

```
function jetPackCommand ( source, key )
    if ( doesPlayerHaveJetPack ( source ) ) then  -- if the player has a jetpack
        removePlayerJetPack ( source )            -- remove it
    else
        givePlayerJetPack ( source )              -- otherwise give him one
    end
end
addCommandHandler ( "jetpack", jetPackCommand )
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
