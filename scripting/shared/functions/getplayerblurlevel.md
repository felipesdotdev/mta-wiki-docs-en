---
doc_id: "mta-wiki:2771"
title: "GetPlayerBlurLevel"
source_title: "GetPlayerBlurLevel"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerBlurLevel"
revision_id: 43552
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:19.193366+00:00"
---

# GetPlayerBlurLevel

This function allows you to check the current blur level of a specified [player](mta://reference/misc/player.md).

## Syntax

Click to collapse [-]
Server

```
int getPlayerBlurLevel ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getBlurLevel(...)*

**Counterpart**: *[setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)*

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) whose blur level you want to check.

### Returns

Returns the player's blur level if successful, *false* if an invalid player was given.

Click to collapse [-]
Client

```
int getBlurLevel ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](mta://reference/misc/player.md).getBlurLevel(...)*

**Variable**: *.blurLevel*

**Counterpart**: *[setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)*

### Returns

Returns the local blur level.

## Example

Click to collapse [-]
Server

This example adds a command *blurlevel* with which you can check your current blur level.

```
function checkBlurLevel( playerSource )
    local blur = getPlayerBlurLevel( playerSource )
    if blur then
        outputChatBox( "Blur level: " .. blur, playerSource )
    end
end
addCommandHandler("blurlevel", checkBlurLevel)
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- getPlayerBlurLevel

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
