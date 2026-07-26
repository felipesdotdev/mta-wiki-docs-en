---
doc_id: "mta-wiki:3456"
title: "CanPlayerBeKnockedOffBike"
source_title: "CanPlayerBeKnockedOffBike"
source_url: "https://wiki.multitheftauto.com/wiki/CanPlayerBeKnockedOffBike"
revision_id: 44605
language: "en"
categories: ["Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:10:41.409816+00:00"
---

# CanPlayerBeKnockedOffBike

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use canPedBeKnockedOffBike instead. |  |

This function checks if a player can fall off bikes.

## Syntax

```
bool canPlayerBeKnockedOffBike ( player thePlayer )
```

### Required Arguments

- **thePlayer:** the player whose knockoffstatus being asked

### Returns

Returns *true* if the player can be knocked off bikes, *false* if he can't or an invalid element was passed.

## Example

This example puts the knockoff status in the chatbox.

```
function canBeKnockedOff ( command )
    -- The player should enter /knockstatus
    if canPlayerBeKnockedOffBike ( getLocalPlayer() ) then
        outputChatBox ( "You can be knocked off your bike." )
    else
        outputChatBox ( "You can't be knocked off your bike." )
    end
end
addCommandHandler ( "knockstatus", canBeKnockedOff )
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
