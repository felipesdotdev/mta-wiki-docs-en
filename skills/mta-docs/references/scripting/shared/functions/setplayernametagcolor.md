---
doc_id: "mta-wiki:2361"
title: "SetPlayerNametagColor"
source_title: "SetPlayerNametagColor"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerNametagColor"
revision_id: 48020
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetPlayerNametagColor

This allows you to change the RGB color mixture in the name tags of players.

| [[{{{image}}}\|link=\|]] | Note: If the player is using a hexcode in front of their name, it will override this function. You must first strip the name of the hexcode using removeHex |
| --- | --- |
|  |  |

## Syntax

```
bool setPlayerNametagColor ( player thePlayer, int r, int g, int b )
```

**OR**

```
bool setPlayerNametagColor ( player thePlayer, false )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setNametagColor(...)*

### Required Arguments

- **thePlayer:** The player whose name tag text you wish to change the color of

- **r:** The amount of red you want in the mixture of RGB (0-255 is valid)

- **g:** The amount of green you want in the mixture of RGB (0-255 is valid)

- **b:** The amount of blue you want in the mixture of RGB (0-255 is valid)

- **false:** If false is specified instead of the colors, the nametag color will reset to defaulting to your team color.

### Returns

Returns *true* if the function was successful, *false* otherwise.

## Example

This will allow a player to change the RGB color mixture of their nickname. Valid RGB is between 0-255.

```
-- The handler function for the console command
function nametagColorChange ( thePlayer, commandName, r, g, b )
    -- Apply the new color mix of RGB to the command handler activator
    setPlayerNametagColor ( thePlayer, r, g, b )
end
-- This is a command handler that activates on text "nametagcolor" in the console. It also asks 
-- the player to provide values for the extra parameters r, g, b after the command name. These will 
-- be the new color mix of RGB to apply to the player's name tag.
addCommandHandler ( "nametagcolor", nametagColorChange )
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

- setPlayerNametagColor

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
