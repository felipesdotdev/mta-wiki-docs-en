---
doc_id: "mta-wiki:2349"
title: "KickPlayer"
source_title: "KickPlayer"
source_url: "https://wiki.multitheftauto.com/wiki/KickPlayer"
revision_id: 69587
language: "en"
categories: ["Server_functions"]
---

# KickPlayer

| [[{{{image}}}\|link=\|]] | Note: Don't forget to give admin rights to the resource, in which you are using kickPlayer function or it won't work. |
| --- | --- |
|  |  |

This function will kick the specified player from the server.

## Syntax

```
bool kickPlayer ( player kickedPlayer, [ player/string responsiblePlayer, string reason = "" ] )
```

*or*

```
bool kickPlayer ( player kickedPlayer, [ string reason = "" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](https://wiki.multitheftauto.com/index.php?search=player):kick(...)*

### Required Arguments

- **kickedPlayer:** The player that will be kicked from the server

### Optional Arguments

- **responsiblePlayer:** The player that is responsible for the event. **Note**: If left out as in the second syntax, responsible player for the kick will be "Console" (Maximum 30 characters if using a string).

- **reason:** The reason for the kick. (Maximum 64 characters before 1.5.8, Maximum 128 characters after 1.5.8)

### Returns

Returns *true* if the player was kicked succesfully, *false* if invalid arguments are specified.

## Example

This example lets a player kick anyone who has a lower level.

```
function kickPlayerHandler ( sourcePlayer, commandname, kickedname, ... )
	-- Get player element from the name
	local kicked = getPlayerFromName ( kickedname )
	-- If the client who sent the command has a higher level
        local reason = table.concat({...}, " ")
	if ( hasObjectPermissionTo ( sourcePlayer, "function.kickPlayer" ) ) then
		-- Kick the player
		kickPlayer ( kicked, sourcePlayer, reason )
	end
end
-- Add the "kick" command handler
addCommandHandler ( "kick", kickPlayerHandler )
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

- kickPlayer

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
