---
doc_id: "mta-wiki:1762"
title: "IsPlayerOnGround"
source_title: "IsPlayerOnGround"
source_url: "https://wiki.multitheftauto.com/wiki/IsPlayerOnGround"
revision_id: 40335
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# IsPlayerOnGround

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use isPedOnGround instead. |  |

This function is used to determine whether or not a player is on the ground. This is for on-foot usage only.

## Syntax

Click to collapse [-]
Server and client

```
bool isPlayerOnGround ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) you are checking.

### Returns

Returns *true* if the player is on foot and on the ground, *false* otherwise, even if he is in a vehicle capable of flying.

## Example

Click to collapse [-]
Serverside example

This example checks if the player who enters the 'amiflying' command is on the ground and outputs a message.

```
[lua]
function isHeFlying ( sourcePlayer )
    if ( isPlayerOnGround ( sourcePlayer ) ) then
        outputChatBox ( "No, you're not flying, you're just stoned!", sourcePlayer )
    else
        outputChatBox ( "Is it a bird, is it a plane... No it's " .. getClientName ( sourcePlayer ) .. "!", sourcePlayer )
    end
end
addCommandHandler ( "amiflying", isHeFlying )
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
