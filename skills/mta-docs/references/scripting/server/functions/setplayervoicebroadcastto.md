---
doc_id: "mta-wiki:5805"
title: "SetPlayerVoiceBroadcastTo"
source_title: "SetPlayerVoiceBroadcastTo"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerVoiceBroadcastTo"
revision_id: 80405
language: "en"
categories: ["Server_functions"]
---

# SetPlayerVoiceBroadcastTo

This function allows you to change who can hear the voice of a player.

| [[{{{image}}}\|link=\|]] | Important Note: This function should only be used as a low-level function for advanced users. For typical Voice scripting, please see the Voice Resource |
| --- | --- |
|  |  |

## Syntax

```
bool setPlayerVoiceBroadcastTo ( element thePlayer, mixed broadcastTo )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):setVoiceBroadcastTo(...)*

**Variable**: *.voiceBroadcastTo*

### Required Arguments

- **thePlayer:** The [player](https://wiki.multitheftauto.com/index.php?search=player) you wish to change

- **broadcastTo :** Element or table of elements who should hear the voice from this player

### Returns

Returns *true* if the value was set successfully, *false* otherwise.

## Example

Click to collapse [-]
Server

```
function getPlayer( ... )
	if ( ... ) then
		
		local elements = {};
		for _, string in ipairs( { ... } ) do
			for _, element in ipairs( getElementsByType( 'player' ) ) do
				if ( string.find( string:lower(), getPlayerName(element):lower(), 1, true ) ) then
					table.insert( elements, element );
				end
			end
		end
		
		return elements;
	end
	
	return false
end

addCommandHandler( 'broadcast', 
	function( player, command, target, target_ )
		if ( target and target_ ) then
			target, target_ = getPlayer( target, target_ );
			if ( target and target_ ) then
				setPlayerVoiceBroadcastTo( target, target_ );
			else
				outputChatBox( not target and "Target 1 not found!" or not target_ and "Target 2 not found!", root, 255, 0, 0, false );
			end
		end
	end
)
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

- setPlayerVoiceBroadcastTo

- [setPlayerVoiceIgnoreFrom](mta://scripting/server/functions/setplayervoiceignorefrom.md)

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
