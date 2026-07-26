---
doc_id: "mta-wiki:4312"
title: "RemoveBan"
source_title: "RemoveBan"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveBan"
revision_id: 78643
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:16:31.849996+00:00"
---

# RemoveBan

This function will remove a specific [ban](mta://reference/misc/ban.md).

| [[{{{image}}}\|link=\|]] | Note: Don't forget to give admin rights to the resource, in which you are using removeBan function or it won't work. |
| --- | --- |
|  |  |

## Syntax

```
bool removeBan ( ban theBan [, player responsibleElement = nil ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):remove(...)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) to be removed.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **responsibleElement:** The element that is responsible for removing the [ban](mta://reference/misc/ban.md) element. This can be a player or the root ([getRootElement](mta://scripting/shared/functions/getrootelement.md)()).

### Returns

Returns *true* if the [ban](mta://reference/misc/ban.md) was removed succesfully, *false* if invalid arguments are specified.

## Example

This example removes all the bans when the resource is started and outputs to everyone the players.

```
addEventHandler("onResourceStart",resourceRoot,function()
	bans = getBans()
	for i,d in ipairs(bans)do
		nick = getBanNick(d)
		if(removeBan(d))then
			outputChatBox(nick.."has been removed from ban",root)
		end
	end
end)
```

This example removes the ban for IP 1.2.3.4

```
for _,ban in ipairs(getBans())do
    if getBanIP(ban) == "1.2.3.4" then
        removeBan(ban)
    end
end
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

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- removeBan
