---
doc_id: "mta-wiki:4315"
title: "GetBanSerial"
source_title: "GetBanSerial"
source_url: "https://wiki.multitheftauto.com/wiki/GetBanSerial"
revision_id: 48716
language: "en"
categories: ["Server_functions"]
---

# GetBanSerial

This function will return the [serial](mta://reference/misc/serial.md) of the specified [ban](mta://reference/misc/ban.md).

## Syntax

```
string getBanSerial ( ban theBan )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):getSerial(...)*

**Variable**: *.serial*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) you want to retrieve the serial of.

### Returns

Returns a *string* of the serial if everything was successful, *false* if invalid arguments are specified or if there was no serial specified for the [ban](mta://reference/misc/ban.md).

## Example

This example will show the user who banned a player the serial of that banned player.

```
function banPlayerCommand ( thisPlayer, commandName, bannedName, reason )
    if ( hasObjectPermissionTo ( thisPlayer, "function.banPlayer" ) ) then -- If the command user has the rights
        local bannedPlayer = getPlayerFromName ( bannedName ) -- Get the ID from the player who gets banned
        if getElementType ( bannedPlayer ) == "player" then -- If it's a player
            local theBan = banPlayer ( bannedPlayer, thisPlayer, reason ) -- Ban the player
            outputChatBox ( "ban: " .. bannedName .. " successfully banned", thisPlayer ) -- Send the banner a succes message
            outputChatBox ( "At Serial: " ..getBanSerial ( theBan ), thisPlayer ) -- And send him the serial of the banned player
        end
    else
        outputChatBox ( "ban: You don't have enough permissions", thisPlayer ) -- If the command user doesn't have the permissions
    end
end
addCommandHandler ( "ban", banPlayerCommand )
```

## See Also

- [addBan](mta://scripting/server/functions/addban.md)

- [banPlayer](mta://scripting/server/functions/banplayer.md)

- [getBanAdmin](mta://scripting/server/functions/getbanadmin.md)

- [getBanIP](mta://scripting/server/functions/getbanip.md)

- [getBanNick](mta://scripting/server/functions/getbannick.md)

- [getBanReason](mta://scripting/server/functions/getbanreason.md)

- getBanSerial

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
