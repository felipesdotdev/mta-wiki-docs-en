---
doc_id: "mta-wiki:4313"
title: "GetBans"
source_title: "GetBans"
source_url: "https://wiki.multitheftauto.com/wiki/GetBans"
revision_id: 48764
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:07.427013+00:00"
---

# GetBans

This function will return a table containing all the [bans](mta://reference/misc/ban.md) present in the server's banlist.xml.

## Syntax

```
table getBans ( )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Ban](mta://reference/misc/ban.md).getList(...)*

### Returns

Returns a [table](mta://reference/misc/table.md) containing all the [bans](mta://reference/misc/ban.md).

## Example

Click to collapse [-]
Example 1: Server

This example lists every ban when somebody types "/bans". WARNING: This will spam chat (for the player that executed the command) if the server has a lot of bans.

```
function listBans ( playerSource )
local banList = getBans() -- Return a table of all the bans.
	--
	for banID, ban in ipairs ( banList ) do -- For every ban do the following...	
		--
		local nick = getBanNick ( ban ) -- Get the IP of the ban
		--
		if nick then
			outputChatBox ( "Ban #" .. banID .. ": " .. nick, playerSource , 255, 0, 0, true ) -- Output the ban.
		end
		--
	end
	--
end
addCommandHandler ( "bans", listBans ) -- Add "/bans" as the trigger for the function.
```

## See Also

- [addBan](mta://scripting/server/functions/addban.md)

- [banPlayer](mta://scripting/server/functions/banplayer.md)

- [getBanAdmin](mta://scripting/server/functions/getbanadmin.md)

- [getBanIP](mta://scripting/server/functions/getbanip.md)

- [getBanNick](mta://scripting/server/functions/getbannick.md)

- [getBanReason](mta://scripting/server/functions/getbanreason.md)

- [getBanSerial](mta://scripting/server/functions/getbanserial.md)

- [getBanTime](mta://scripting/server/functions/getbantime.md)

- getBans

- [getUnbanTime](mta://scripting/server/functions/getunbantime.md)

- [isBan](mta://scripting/server/functions/isban.md)

- [kickPlayer](mta://scripting/server/functions/kickplayer.md)

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
