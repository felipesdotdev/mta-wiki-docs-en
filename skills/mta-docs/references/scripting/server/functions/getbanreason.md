---
doc_id: "mta-wiki:4320"
title: "GetBanReason"
source_title: "GetBanReason"
source_url: "https://wiki.multitheftauto.com/wiki/GetBanReason"
revision_id: 48714
language: "en"
categories: ["Server_functions"]
---

# GetBanReason

This function will return the ban reason of the specified [ban](mta://reference/misc/ban.md).

## Syntax

```
string getBanReason ( ban theBan )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):getReason(...)*

**Variable**: *.reason*

**Counterpart**: *[setBanReason](mta://scripting/server/functions/setbanreason.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) in which you want to return the reason of.

### Returns

Returns a *string* of the reason if everything was successful, *false* if invalid arguments are specified if there was no reason specified for the [ban](mta://reference/misc/ban.md).

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

- [getBanNick](mta://scripting/server/functions/getbannick.md)

- getBanReason

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
