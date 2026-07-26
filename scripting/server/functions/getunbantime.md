---
doc_id: "mta-wiki:4363"
title: "GetUnbanTime"
source_title: "GetUnbanTime"
source_url: "https://wiki.multitheftauto.com/wiki/GetUnbanTime"
revision_id: 48762
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:26.604086+00:00"
---

# GetUnbanTime

This function will return the unbanning time of the specified [ban](mta://reference/misc/ban.md) in **seconds**.

## Syntax

```
int getUnbanTime ( ban theBan )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):getUnbanTime(...)*

**Variable**: *.unbanTime*

**Counterpart**: *[setUnbanTime](mta://scripting/server/functions/setunbantime.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) in which you wish to retrieve the unban time of.

### Returns

- Returns an integer of the unbanning time in the format of seconds from the year 1970.  Use in conjunction with [getRealTime](mta://scripting/shared/functions/getrealtime.md) in order to retrieve detailed information.

- Returns **false** if invalid arguments are specified or if there was no unbanning time specified for the [ban](mta://reference/misc/ban.md).

## Example

```
function listBans ()
	local bansList = getBans() -- Return a table of all the bans.
 
	for banID, ban in ipairs ( banList ) do -- For every ban do the following...
		local nick = getBanNick ( ban ) -- Get the IP of the ban
                local timetounban = getUnbanTime ( ban ) -- get the time to wait of the banned player
		if nick then
			outputChatBox ( "Ban #" .. banID .. ": " .. nick.." || Time to unban: "..timetounban , source, 255, 0, 0 ) -- Output the baninfo
		end
	end
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

- [getBans](mta://scripting/server/functions/getbans.md)

- getUnbanTime

- [isBan](mta://scripting/server/functions/isban.md)

- [kickPlayer](mta://scripting/server/functions/kickplayer.md)

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
