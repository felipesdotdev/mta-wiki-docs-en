---
doc_id: "mta-wiki:2286"
title: "ForcePlayerMap"
source_title: "ForcePlayerMap"
source_url: "https://wiki.multitheftauto.com/wiki/ForcePlayerMap"
revision_id: 81391
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:02.062383+00:00"
---

# ForcePlayerMap

This function is used to forcefully show a player's map (F11).

## Syntax

Click to collapse [-]
Server

```
bool forcePlayerMap ( player thePlayer, bool forceOn )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):forceMap(...)*

**Variable**: *.mapForced*

**Counterpart**: *[isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)*

### Required Arguments

- **thePlayer**: A [player](mta://reference/misc/player.md) object referencing the specified player

- **forceOn**: A boolean value representing whether or not the player's map will be forced on

Click to collapse [-]
Client

```
bool forcePlayerMap ( bool forceOn )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](mta://reference/misc/player.md).forceMap(...)*

**Counterpart**: *[isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)*

### Required Arguments

- **forceOn**: A boolean value representing whether or not the player's map will be forced on

### Returns

Returns *true* if the player's map was forced on, *false* otherwise.

## Example

This example forces the map to show for the player named "dave" on for 10 seconds, if it hasn't been already.

```
-- Get the player named "dave"
dave = getPlayerFromName ( "dave" )
-- Make sure we found him
if ( dave ) then
    if not isPlayerMapForced ( dave ) then                  -- if his map isn't already forced on
        forcePlayerMap ( dave, true )                       -- force it on
        setTimer ( forcePlayerMap, 10000, 1, dave, false )  -- stop forcing in 10 seconds
    end
end
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- forcePlayerMap

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
