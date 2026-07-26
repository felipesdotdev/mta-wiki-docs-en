---
doc_id: "mta-wiki:4441"
title: "SetPlayerName"
source_title: "SetPlayerName"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerName"
revision_id: 63617
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:43.880677+00:00"
---

# SetPlayerName

This function changes the specified [player](mta://reference/misc/player.md)'s name. Note that any change made to a players name with this function is not saved in their settings so the name change only lasts till they disconnect.

## Syntax

```
bool setPlayerName ( player thePlayer, string newName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):setName(...)*

**Variable**: *.name*

**Counterpart**: *[getPlayerName](mta://scripting/shared/functions/getplayername.md)*

### Required Arguments

- **thePlayer:** the [player](mta://reference/misc/player.md) that will have its name set.

- **newName:** the new name to set for the player.

### Returns

Returns *true* if the player name was changed succesfully, *false* if invalid arguments are specified.

### Limits

- Only ASCII characters between 33 and 126 are allowed (basic latin, no spaces):

```
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
```

- Minimal player name length is 1 character.

- Maximum player name length is 22 characters.

- Player names are case-insensitive. It is not possible to have two clients with same name but different character case.

## Example

Click to collapse [-]
Server

This example adds a tag before a player's nickname via a /changetag command

```
-- Define the function for this command (/changetag, as defined below)
-- source = the player that triggered this command
-- command = the command passed into the function (changetag)
-- thePlayer = the player that you wish to add a tag to
-- tag = the tag to add to the players nickname
function tagPlayer ( source, command, thePlayer, tag )
	-- Attempt to grab the element id for the player from the parsed name.
	local sPlayerElement = getPlayerFromName ( thePlayer )
	-- Check to see if the player were changing the tag for exists.
	if ( sPlayerElement ) then
		-- make sure that the element type of thePlayer is acctually pointing to a player element
		if getElementType ( sPlayerElement ) == "player" then
			-- we store the player's current name,
			local oldName = getPlayerName ( sPlayerElement )
			-- append the tag passed to this function before it
			local taggedName = tag .. oldName
			-- then set it as his new name
			setPlayerName ( sPlayerElement, taggedName )
			-- Tell the player who triggerd the command that the tag has been applied
			outputChatBox ( "Player " .. thePlayer .. "'s tag changed to " .. taggedName, source )
		end
	else
		-- Tell the player who triggerd the command that the player could not be found
		outputChatBox ( "Unable to change player tag: Player " .. thePlayer .. " not found", source )
	end
end
-- Add a command handler for either the console or / chat commands
-- Example: /changetag <playername> <tag>
addCommandHandler ( "changetag", tagPlayer )
```

This example allows you to check if string is valid mta nickname

```
function isNicknameValid(nick)
  for _, codepoint in utf8.next, nick do
    if(codepoint < 33 or codepoint > 126)then
      return false
    end
  end
  return true
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

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
