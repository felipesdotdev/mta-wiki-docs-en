---
doc_id: "mta-wiki:4317"
title: "GetBanNick"
source_title: "GetBanNick"
source_url: "https://wiki.multitheftauto.com/wiki/GetBanNick"
revision_id: 48712
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:07.360528+00:00"
---

# GetBanNick

This function will return the nickname (nickname that the player had when he was banned) of the specified [ban](mta://reference/misc/ban.md).

## Syntax

```
string getBanNick ( ban theBan )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):getNick(...)*

**Variable**: *.nick*

**Counterpart**: *[setBanNick](mta://scripting/server/functions/setbannick.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) element which nickname you want to return.

### Returns

Returns a *string* of the nickname if everything was successfull, *false* if invalid arguments are specified if there was no nickname specified for the [ban](mta://reference/misc/ban.md) element.

## Example

```
function outputBan(ban)
	local banned = getBanNick(ban) -- Get the name of the player who was banned
	local banner = getBanAdmin(ban) -- Get the name of the admin who banned the player
	local reason = getBanReason(ban) -- Get the reason the player was banned
	outputChatBox("-----BAN-----",getRootElement(),255,0,0)
	if (banned) then
		outputChatBox("Player banned: "..banned,getRootElement(),255,0,0) -- Output the player name who was banned
	end
	if (banner) then
		outputChatBox("Banner: "..banner,getRootElement(),255,0,0) -- Output the admin name who performed the ban
	end
	if (reason) then
		outputChatBox("Reason: "..reason,getRootElement(),255,0,0) -- outputt the reason the player was banned
	end
end
addEventHandler("onBan",getRootElement(),outputBan) -- When a player is banned trigger the outputBan function
```

## See Also

- [addBan](mta://scripting/server/functions/addban.md)

- [banPlayer](mta://scripting/server/functions/banplayer.md)

- [getBanAdmin](mta://scripting/server/functions/getbanadmin.md)

- [getBanIP](mta://scripting/server/functions/getbanip.md)

- getBanNick

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
