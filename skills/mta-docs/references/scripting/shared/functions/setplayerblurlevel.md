---
doc_id: "mta-wiki:2772"
title: "SetPlayerBlurLevel"
source_title: "SetPlayerBlurLevel"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerBlurLevel"
revision_id: 52901
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetPlayerBlurLevel

Sets the motion blur level on the clients screen. Accepts a value between 0 and 255.

## Syntax

Click to collapse [-]
Server

```
bool setPlayerBlurLevel ( player thePlayer, int level )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setBlurLevel(...)*

**Variable**: *.blurLevel*

**Counterpart**: *[getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)*

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) whose blur level will be changed.

- **level:** The level to set the blur to (default: 36)

Click to collapse [-]
Client

```
bool setBlurLevel ( int level )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](https://wiki.multitheftauto.com/index.php?search=Player).setBlurLevel(...)*

**Counterpart**: *[getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)*

### Required Arguments

- **level:** The level to set the blur to (default: 36)

## Example

Click to collapse [-]
Server

This example allows the player to set their blur level via a command

```
function changeBlurLevel ( playerSource, command, blur )
    blur = tonumber(blur)
    if not blur or blur > 255 or blur < 0 then
        outputChatBox ( "Enter a value between 0 - 255.", playerSource )
    else
        setPlayerBlurLevel ( playerSource, blur )
        outputChatBox ( "Blur level set to: " .. blur, playerSource )
    end
end

addCommandHandler("blur", changeBlurLevel)
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- setPlayerBlurLevel

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
