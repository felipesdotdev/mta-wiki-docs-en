---
doc_id: "mta-wiki:2360"
title: "SetPlayerNametagText"
source_title: "SetPlayerNametagText"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerNametagText"
revision_id: 40781
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetPlayerNametagText

This will change the text of a player's nickname in the world to something besides the nickname he chose. This will not change the player's actual nickname, it only changes the visible aspect inside the world (you will see his original nickname in the scoreboard and will refer to his original name in scripts).

## Syntax

```
bool setPlayerNametagText ( player thePlayer, string text )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setNametagText(...)*

**Variable**: *.nametagText*

**Counterpart**: *[getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)*

### Required Arguments

- **thePlayer:** The player whose nickname text you wish to change

- **text:** The new nickname text that will be displayed

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Server

This console command lets you change the name tag of lamers.

```
function iHateLamers ( thePlayer, commandName, playername )
    -- This is a command handler that activates on text "lamer" followed by the playername
    -- in the console. The playername argument was added as an extra function argument to store the
    -- name of the player whose text will be changed.
    if not playername then
        -- Prevents the command from running if the player did not specify a value for playername
        outputChatBox ( "You MUST define a player to change his name tag!", thePlayer )
    else
        local culprit = getPlayerFromName ( playername )
        -- This variable stores the result of trying to find the player associated with the playername
        -- that the user of the command specified
        if culprit then
            -- This checks to make sure a player nick was found. If it was not then the playername argument
            -- specified by the command user was not equivalent to the name of any players in the server
            setPlayerNametagText ( culprit, "IM_LAME" )
            -- finally, the nickname text is changed since the command arguments were checked and are valid
        else
            outputChatBox ( "Player does not exist!", thePlayer )
        end
    end
end
addCommandHandler ( "lamer", iHateLamers )
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

- setPlayerNametagText

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
