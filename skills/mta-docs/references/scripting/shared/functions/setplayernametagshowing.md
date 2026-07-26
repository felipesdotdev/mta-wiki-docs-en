---
doc_id: "mta-wiki:2387"
title: "SetPlayerNametagShowing"
source_title: "SetPlayerNametagShowing"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerNametagShowing"
revision_id: 46983
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetPlayerNametagShowing

This function allows you to set whether a player's nametag visibility both clientside and serverside

Use this to define whether the player's name tag is visible or invisible.

## Syntax

```
bool setPlayerNametagShowing ( player thePlayer, bool showing )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setNametagShowing(...)*

**Variable**: *.nametagShowing*

**Counterpart**: *[isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)*

### Required Arguments

- **thePlayer:** Define the player whos tag visiblity status you want to change

- **showing:** Use true or false to show/hide the tag

### Returns

Returns *true* if successful, *false* otherwise

## Example

This script will turn off player tags for everyone

```
function onResourceStart ( )
    local players = getElementsByType ( "player" ) -- Store all the players in the server into a table
    for key, player in ipairs ( players ) do       -- for all the players in the table
        setPlayerNametagShowing ( player, false )  -- turn off their nametag
    end
end
addEventHandler ( "onResourceStart", resourceRoot, onResourceStart )

function onPlayerJoin ( )
      -- Whoever joins the server should also have their nametags deactivated
	setPlayerNametagShowing ( source, false )
end
addEventHandler ( "onPlayerJoin", root, onPlayerJoin )
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

- setPlayerNametagShowing

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
