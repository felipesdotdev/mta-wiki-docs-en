---
doc_id: "mta-wiki:1780"
title: "CanPlayerUseFunction"
source_title: "CanPlayerUseFunction"
source_url: "https://wiki.multitheftauto.com/wiki/CanPlayerUseFunction"
revision_id: 44577
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# CanPlayerUseFunction

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use hasObjectPermissionTo instead. |  |

This function can be used to check if the player can use a function, based on their current access level. Access levels for functions are stored in the server's config file. Use this if you want to prevent a player using a function unless they are logged in with enough rights.

## Syntax

```
bool canPlayerUseFunction ( player thePlayer, string functionName )
```

### Required Arguments

- **thePlayer:** The player who you consider is running the function.

- **functionName** The name of the function which you want to check.

### Returns

Returns *true* if the player specified can use the function specified, *false* otherwise.

## Example

This example adds a console function called *kill_player* that can only be used by players with enough access rights. These access rights can be specified in the server's config file.

```
function adminKillPlayer ( source, commandName, killPlayerName )
    if ( canPlayerUseFunction ( source, "kill_player" ) ) then     -- if the player can use the "kill_player" function
        local playerToKill = getPlayerFromNick ( killPlayerName )  -- look up the player to kill
        if ( playerToKill ~= false ) then                          -- check if we found him
            killPlayer ( playerToKill )                            -- if so, kill him
            outputConsole ( killPlayerName .. " has been killed!", source )   -- and notify the admin
        else
            outputConsole ( "Couldn't find a player called '" .. killPlayerName .. "'", source ) -- otherwise tell him the player was not found
        end
    else
        outputConsole ( "You do not have access to this function!", source ) -- if he isn't allowed to use the function, tell him so
    end
end
addCommandHandler ( "kill_player", adminKillPlayer )
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
