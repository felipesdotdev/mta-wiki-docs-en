---
doc_id: "mta-wiki:7841"
title: "SetBanReason"
source_title: "SetBanReason"
source_url: "https://wiki.multitheftauto.com/wiki/SetBanReason"
revision_id: 48761
language: "en"
categories: ["Server_functions"]
---

# SetBanReason

This function sets the reason for the specified [ban](mta://reference/misc/ban.md).

## Syntax

```
bool setBanReason( ban theBan, string theReason )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):setReason(...)*

**Variable**: *.reason*

**Counterpart**: *[getBanReason](mta://scripting/server/functions/getbanreason.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) that you wish to set the reason of.

- **theReason:** the new reason (max 60 characters).

### Returns

Returns *true* if the new reason was set successfully, *false* otherwise.

## Example

This example adds the command *setreason* which can be used to change the reason of a ban by nickname of the banned player. *For example: setreason someguy reason.*

```
function setReason (player,cmd,name,...)
	local reason = table.concat({...}," ")
	if name and reason then
		local bans = getBans()
		for i,v in ipairs(bans)do
			if getBanNick(v) == name then
				setBanReason(v,reason)
				outputChatBox("Successfully edited the new Ban Reason.",player,0,125,0)
			end
		end
	end
end
addCommandHandler("setreason", setReason)
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

- [getUnbanTime](mta://scripting/server/functions/getunbantime.md)

- [isBan](mta://scripting/server/functions/isban.md)

- [kickPlayer](mta://scripting/server/functions/kickplayer.md)

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- setBanReason

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
