---
doc_id: "mta-wiki:4314"
title: "GetBanIP"
source_title: "GetBanIP"
source_url: "https://wiki.multitheftauto.com/wiki/GetBanIP"
revision_id: 48711
language: "en"
categories: ["Server_functions"]
---

# GetBanIP

This function will return the IP of the specified [ban](mta://reference/misc/ban.md).

## Syntax

```
string getBanIP ( ban theBan )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):getIP(...)*

**Variable**: *.ip*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) in which you want to return the IP of.

### Returns

Returns a *string* of the IP if everything was successful, *false* if invalid arguments are specified if there was no IP specified for the [ban](mta://reference/misc/ban.md).

## Example

This example will show the user who banned a player the IP adress of that banned player.

```
function banPlayerCommand ( thisPlayer, commandName, bannedName, reason )
    if ( hasObjectPermissionTo ( thisPlayer, "function.banPlayer" ) ) then -- If the command user has the rights
        local bannedPlayer = getPlayerFromNick ( bannedName ) -- Get the ID from the player who gets banned
        if getElementType ( bannedPlayer ) == "player" then -- If it's a player
            local theBan = banPlayer ( bannedPlayer, thisPlayer, reason ) -- Ban the player
            outputChatBox ( "ban: " .. bannedName .. " successfully banned", thisPlayer ) -- Send the banner a succes message
            outputChatBox ( "At IP Adress: " ..getBanIP ( theBan ), thisPlayer ) -- And send him the IP adress of the banned player
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

- getBanIP

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
