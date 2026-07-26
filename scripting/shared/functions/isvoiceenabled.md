---
doc_id: "mta-wiki:5807"
title: "IsVoiceEnabled"
source_title: "IsVoiceEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsVoiceEnabled"
revision_id: 46760
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.4"]
generated_at: "2026-07-26T16:16:03.419365+00:00"
---

# IsVoiceEnabled

Added to client side.
This function allows you to make the server reveal whether or not voice is currently enabled.

## Syntax

```
bool isVoiceEnabled ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Player](mta://reference/misc/player.md).isVoiceEnabled(...)*

### Returns

Returns *true* if the voice is enabled on the server, *false* otherwise.

## Example

Click to collapse [-]
Server

This example shows how to forbid use voice for muted (in chat) players

```
-- only if voice enabled
if isVoiceEnabled() then
    -- adding handler for voice start event
    addEventHandler( 'onPlayerVoiceStart', root,
        function()
            -- if player is muted in chat
            -- do not broadcast his voice to other players
            if isPlayerMuted(source) then cancelEvent() end
        end
    )
end
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

- isVoiceEnabled

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
