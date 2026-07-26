---
doc_id: "mta-wiki:2633"
title: "GetPlayerName"
source_title: "GetPlayerName"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerName"
revision_id: 78777
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:20.030336+00:00"
---

# GetPlayerName

This function returns a string containing the name of the specified player.

## Syntax

```
string getPlayerName ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):getName(...)*

**Variable**: *.name*

**Counterpart**: *[setPlayerName](mta://scripting/server/functions/setplayername.md)*

### Required Arguments

- **thePlayer:** the [player](mta://reference/misc/player.md) you want to get the name of

### Returns

Returns a string containing the requested player's name, or *false* if the player passed to the function is invalid.

### Limits

- Player name can consist of ASCII characters between 33 and 126 are allowed (basic latin):

```
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
```

- Minimal player name length is 1 character.

- Maximum player name length is 22 characters.

- Player names are case-insensitive. It is not possible to have two clients with same name but different character case.

## Example

Click to collapse [-]
Server

```
addCommandHandler("myname", function(ply)
    outputChatBox("Your name: "..getPlayerName(ply), ply)
end)
```

Click to collapse [-]
Client

This example outputs the local player name to the chatbox.

```
addCommandHandler("myname", function()
    -- output local player's name to the chatbox
    outputChatBox(getPlayerName(localPlayer))
end)
```

## See Also

- [getLocalPlayer](mta://scripting/client/functions/getlocalplayer.md)

- [getPlayerMapBoundingBox](mta://scripting/client/functions/getplayermapboundingbox.md)

- [getPlayerMapOpacity](mta://scripting/client/functions/getplayermapopacity.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [getPlayerHudComponentProperty](mta://scripting/client/functions/getplayerhudcomponentproperty.md)

- [isPlayerMapVisible](mta://scripting/client/functions/isplayermapvisible.md)

- [isPlayerHudComponentVisible](mta://scripting/client/functions/isplayerhudcomponentvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22751](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22751):

- [isPlayerCrosshairVisible](mta://scripting/client/functions/isplayercrosshairvisible.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [resetPlayerHudComponentProperty](mta://scripting/client/functions/resetplayerhudcomponentproperty.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22868](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22868):

- [setPlayerHudComponentProperty](mta://scripting/client/functions/setplayerhudcomponentproperty.md)

- **Shared**

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- getPlayerName

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
