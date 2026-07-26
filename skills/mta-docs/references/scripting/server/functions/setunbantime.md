---
doc_id: "mta-wiki:7842"
title: "SetUnbanTime"
source_title: "SetUnbanTime"
source_url: "https://wiki.multitheftauto.com/wiki/SetUnbanTime"
revision_id: 48763
language: "en"
categories: ["Server_functions"]
---

# SetUnbanTime

This function sets a new unban time of a given [ban](mta://reference/misc/ban.md) using unix timestamp (seconds since Jan 01 1970).

## Syntax

```
bool setUnbanTime( ban theBan, int theTime )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):setUnbanTime(...)*

**Variable**: *.unbanTime*

**Counterpart**: *[getUnbanTime](mta://scripting/server/functions/getunbantime.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) of which to change the unban time of

- **theTime:** the new unban time

### Returns

Returns *true* if changed successfully, *false* otherwise.

## Example

```
addCommandHandler("banMe",
function (player)
local ban = banPlayer(player)
setUnbanTime(ban, 500)
end
)
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

- setUnbanTime

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
