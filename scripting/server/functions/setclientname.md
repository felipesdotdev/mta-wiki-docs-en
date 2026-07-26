---
doc_id: "mta-wiki:2351"
title: "SetClientName"
source_title: "SetClientName"
source_url: "https://wiki.multitheftauto.com/wiki/SetClientName"
revision_id: 40350
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:38.767124+00:00"
---

# SetClientName

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPlayerName instead. |  |

This function changes the specified [client](mta://reference/misc/client.md)'s name.

## Syntax

```
bool setClientName ( client theClient, string newName )
```

### Required Arguments

- **theClient:** the [client](mta://reference/misc/client.md) that will have its name set.

- **newName:** the new name to set for the client.

### Returns

Returns *true* if the client's name was changed succesfully, *false* if invalid arguments are specified.

## Example

Click to collapse [-]
Server

This example adds a tag before a player's nickname via a /changetag command

```
--Define the function for this command (/changetag, as defined below)
--Source = the player that triggered this command
--Command = The command passed into the function (changetag)
--thePlayer = The player argument that you wish to add a tag too
--tag = The tag to add to the players nickname
function tagPlayer( source, command, thePlayer, tag )
	--Attempt to grab the elemennt id for the player from the parsed name.
	local sPlayerElement = getPlayerFromNick(thePlayer)
	--Check to see if the player were changing the tag for exists.
	if (sPlayerElement) then
		--make sure that the element type of thePlayer is acctually pointing to a player element
		if getElementType( sPlayerElement ) == "player" then
			--we store the player's current name,
			local oldName = getClientName( sPlayerElement )
			--append the tag passed to this function before it
			local taggedName = tag .. oldName
			--then set it as his new name
			setClientName( sPlayerElement, taggedName )
			--Tell the player who triggerd the command that the tag has been applied
			outputChatBox ( "Player " .. thePlayer .. "'s tag changed to " .. taggedName, source )
		end
	else
		--Tell the player who triggerd the command that the player could not be found
		outputChatBox ( "Unable to change player tag: Player " .. thePlayer .. " not found", source )
	end
end
--Add a command handler for either the console or / chat commands
--Example: /changetag <playername> <tag>
addCommandHandler ( "changetag", tagPlayer )
```

## See Also

BEFORE VERSION 1.0 :

- [getClientAccount](mta://scripting/server/functions/getclientaccount.md)

- [getClientIP](mta://scripting/server/functions/getclientip.md)

- [getClientName](mta://scripting/server/functions/getclientname.md)

- setClientName
