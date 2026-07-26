---
doc_id: "mta-wiki:4318"
title: "GetBanAdmin"
source_title: "GetBanAdmin"
source_url: "https://wiki.multitheftauto.com/wiki/GetBanAdmin"
revision_id: 67027
language: "en"
categories: ["Server_functions"]
---

# GetBanAdmin

This function will return the responsible admin (nickname of the admin) of the specified [ban](mta://reference/misc/ban.md).

## Syntax

```
string getBanAdmin ( ban theBan )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):getAdmin(...)*

**Variable**: *.admin*

**Counterpart**: *[setBanAdmin](mta://scripting/server/functions/setbanadmin.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) you want to return the admin of.

### Returns

Returns a *string* of the admin if everything was successful, *false* if invalid arguments are specified if there was no admin specified for the [ban](mta://reference/misc/ban.md).

## Example

```
function outputBan(ban)
	local banned = getBanNick(ban) -- Get the name of the player who was banned
	local banner = getBanAdmin(ban) -- Get the name of the admin who banned the player
	local reason = getBanReason(ban) -- Get the reason the player was banned
	outputChatBox("-----BAN-----",root,255,0,0)
	if (banned) then
		outputChatBox("Player banned: "..banned,root,255,0,0) -- Output the player name who was banned
	end
	if (banner) then
		outputChatBox("Banner: "..banner,root,255,0,0) -- Output the admin name who performed the ban
	end
	if (reason) then
		outputChatBox("Reason: "..reason,root,255,0,0) -- outputt the reason the player was banned
	end
end
addEventHandler("onBan",root,outputBan) -- When a player is banned trigger the outputBan function
```

## See Also

- [addBan](mta://scripting/server/functions/addban.md)

- [banPlayer](mta://scripting/server/functions/banplayer.md)

- getBanAdmin

- [getBanIP](mta://scripting/server/functions/getbanip.md)

- [getBanNick](mta://scripting/server/functions/getbannick.md)

- [getBanReason](mta://scripting/server/functions/getbanreason.md)

- [getBanSerial](mta://scripting/server/functions/getbanserial.md)

- [getBanTime](mta://scripting/server/functions/getbantime.md)

- [getBans](mta://scripting/server/functions/getbans.md)

- [getUnbanTime](mta://scripting/server/functions/getunbantime.md)

- [isBan](mta://scripting/server/functions/isban.md)

- [kickPlayer](mta://scripting/server/functions/kickplayer.md)

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
