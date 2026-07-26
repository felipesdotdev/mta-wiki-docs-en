---
doc_id: "mta-wiki:1732"
title: "GetClientName"
source_title: "GetClientName"
source_url: "https://wiki.multitheftauto.com/wiki/GetClientName"
revision_id: 44561
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:08.399443+00:00"
---

# GetClientName

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPlayerName instead. |  |

This function gets a [client](mta://reference/misc/client.md)'s name (a client can either be a [player](mta://reference/misc/player.md) or an admin).

## Syntax

```
string getClientName ( client theClient )
```

### Required Arguments

- **theClient:** the [client](mta://reference/misc/client.md) element (player or admin) you want to get the name of.

### Returns

Returns a *string* containing the requested client's name, or *false* if the client passed to the function is invalid.

## Example

This example adds a tag before a player's nick.

```
function tagPlayer( thePlayer, tag )
	--we check thePlayer is a player, otherwise this function could be used with admins
	if getElementType(thePlayer) == "player" then
		--we store the player's current name,
		local oldName = getClientName( thePlayer )
		--append the tag passed to this function before it,
		local taggedName = tag .. oldName
		--then set it as his new name
		setClientName( thePlayer, taggedName )
	end
end
```

## See Also

BEFORE VERSION 1.0 :

- [getClientAccount](mta://scripting/server/functions/getclientaccount.md)

- [getClientIP](mta://scripting/server/functions/getclientip.md)

- getClientName

- [setClientName](mta://scripting/server/functions/setclientname.md)
