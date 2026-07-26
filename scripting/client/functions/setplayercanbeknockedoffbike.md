---
doc_id: "mta-wiki:3457"
title: "SetPlayerCanBeKnockedOffBike"
source_title: "SetPlayerCanBeKnockedOffBike"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerCanBeKnockedOffBike"
revision_id: 49086
language: "en"
categories: ["Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:43.650932+00:00"
---

# SetPlayerCanBeKnockedOffBike

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedCanBeKnockedOffBike instead. |  |

This function controls if you can fall of your bike by accident - namely by banging into a wall.

## Syntax

```
bool setPlayerCanBeKnockedOffBike ( player thePlayer, bool canBeKnockedOffBike )
```

### Required Arguments

- **thePlayer:** the player whose knockoffstatus being changed

- **state:** the true or false state

## Example

This example allows the local player to toggle whether or not he can fall of bikes.

```
function changeCanBeKnockedOff ( command )
    -- The player should enter /knock
    if canPedBeKnockedOffBike ( getLocalPlayer() ) then
        setPlayerCanBeKnockedOffBike ( getLocalPlayer(), false )
        outputChatBox ( "Now you can't be knocked off your bike." )
    else
        setPlayerCanBeKnockedOffBike ( getLocalPlayer(), true )
        outputChatBox ( "Now you can be knocked off your bike." )
    end
end
addCommandHandler ( "knock", changeCanBeKnockedOff )
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
