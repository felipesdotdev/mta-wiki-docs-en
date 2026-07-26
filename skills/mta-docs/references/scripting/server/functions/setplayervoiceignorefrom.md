---
doc_id: "mta-wiki:5806"
title: "SetPlayerVoiceIgnoreFrom"
source_title: "SetPlayerVoiceIgnoreFrom"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerVoiceIgnoreFrom"
revision_id: 80406
language: "en"
categories: ["Server_functions"]
---

# SetPlayerVoiceIgnoreFrom

This function allows you to mute voices for a player.

| [[{{{image}}}\|link=\|]] | Important Note: This function should only be used as a low-level function for advanced users. For typical Voice scripting, please see the Voice Resource |
| --- | --- |
|  |  |

## Syntax

```
bool setPlayerVoiceIgnoreFrom ( element thePlayer, mixed ignoreFrom )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setVoiceIgnoreFrom(...)*

**Variable**: *.voiceIgnoreFrom*

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) you wish to change

- **ignoreFrom:** Element or table of elements which the player should not hear voices from. Use *nil* if no one should be ignored.

### Returns

Returns *true* if the value was set successfully, *false* otherwise.

## Example

By this example mute a player voice to yourself so you won't hear him
( **note:** use setPlayerVoiceMuted function if you are using the voice resource more information at [https://wiki.multitheftauto.com/wiki/Resource:Voice](https://wiki.multitheftauto.com/wiki/Resource:Voice) )

Click to collapse [-]
Server

```
function voiceMuteFunction( Muter , cmd , MutedName , mutual)
	if not MutedName then
		return outputChatBox("Syntax: /".. cmd .." <player name> <mutual>", Muter)
	end
	local Muted = getPlayerFromName(MutedName)
	if not Muted then
		return outputChatBox('enter the correct player name' , Muter)
	end
	if Muted == Muter then
		return outputChatBox("You cannot mute yourself!", Muter)
	end
	if mutual then --enter any string as the second arg for making this mute mutual or enter nothing to make it one-way
		setPlayerVoiceIgnoreFrom(Muter,Muted)
		setPlayerVoiceIgnoreFrom(Muted,Muter)
	else
		setPlayerVoiceIgnoreFrom(Muter,Muted)
	end    
end
addCommandHandler('voiceMute' ,voiceMuteFunction )
-- e.g. /voiceMute jacky y  (mutual)
-- e.g. /voiceMute jacky  (one-way)
```

## See Also

- [getAlivePlayers](mta://scripting/server/functions/getaliveplayers.md)

- [getDeadPlayers](mta://scripting/server/functions/getdeadplayers.md)

- [getPlayerAnnounceValue](mta://scripting/server/functions/getplayerannouncevalue.md)

- [getPlayerCount](mta://scripting/server/functions/getplayercount.md)

- [getPlayerIdleTime](mta://scripting/server/functions/getplayeridletime.md)

- [getPlayerIP](mta://scripting/server/functions/getplayerip.md)

- [getPlayerVersion](mta://scripting/server/functions/getplayerversion.md)

- [getRandomPlayer](mta://scripting/server/functions/getrandomplayer.md)

- [isPlayerMuted](mta://scripting/server/functions/isplayermuted.md)

- [redirectPlayer](mta://scripting/server/functions/redirectplayer.md)

- [resendPlayerACInfo](mta://scripting/server/functions/resendplayeracinfo.md)

- [resendPlayerModInfo](mta://scripting/server/functions/resendplayermodinfo.md)

- [setPlayerAnnounceValue](mta://scripting/server/functions/setplayerannouncevalue.md)

- [setPlayerMuted](mta://scripting/server/functions/setplayermuted.md)

- [setPlayerScriptDebugLevel](mta://scripting/server/functions/setplayerscriptdebuglevel.md)

- [setPlayerTeam](mta://scripting/server/functions/setplayerteam.md)

- [setPlayerName](mta://scripting/server/functions/setplayername.md)

- [setPlayerVoiceBroadcastTo](mta://scripting/server/functions/setplayervoicebroadcastto.md)

- setPlayerVoiceIgnoreFrom

- [setPlayerWantedLevel](mta://scripting/server/functions/setplayerwantedlevel.md)

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md)

- [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md)
  

- **Shared**

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
