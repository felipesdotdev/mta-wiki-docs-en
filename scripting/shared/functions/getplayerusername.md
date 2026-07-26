---
doc_id: "mta-wiki:3770"
title: "GetPlayerUserName"
source_title: "GetPlayerUserName"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerUserName"
revision_id: 47423
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:20.663402+00:00"
---

# GetPlayerUserName

|  | This function is deprecated. This means that its use is discouraged. |
| --- | --- |
| MTA Community accounts were dropped in favor of serials for identifying players. |  |

This function returns the community.mtasa.com (or mtabeta.com) account of the specified user.

## Syntax

Click to collapse [-]
Server

```
string getPlayerUserName ( player thePlayer )
```

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) whose MTA account username you want to retrieve.

### Returns

A *string* value containing the MTA account username or *false* if no account exists for the player.

Click to collapse [-]
Client

```
string getPlayerUserName ()
```

### Returns

A *string* value containing local player's MTA account username or *false* if no account exists for the local player.

## Example

Click to collapse [-]
Server

```
function outputMTAAccount ( sourcePlayer )
        -- if the command was triggered by an ingame player
        if ( sourcePlayer ) then
                local mtaaccount = getPlayerUserName( sourcePlayer )
                if ( mtaaccount ) then
                        outputChatBox("Your community.mtasa.com account is " .. mtaaccount, sourcePlayer )
                else
                        outputChatBox("Can't find an account for you.", sourcePlayer )
                end
        end
end

-- register outputMTAAccount as a handler for the mta-account command
addCommandHandler ( "mtaaccount", outputMTAAccount )
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
