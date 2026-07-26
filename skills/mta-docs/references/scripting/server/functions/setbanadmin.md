---
doc_id: "mta-wiki:7840"
title: "SetBanAdmin"
source_title: "SetBanAdmin"
source_url: "https://wiki.multitheftauto.com/wiki/SetBanAdmin"
revision_id: 48709
language: "en"
categories: ["Server_functions"]
---

# SetBanAdmin

This function sets a new admin for a [ban](mta://reference/misc/ban.md).

## Syntax

```
bool setBanAdmin ( ban theBan, string theAdmin )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):setAdmin(...)*

**Variable**: *.admin*

**Counterpart**: *[getBanAdmin](mta://scripting/server/functions/getbanadmin.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) you want to change the admin of.

- **theAdmin:** The new admin.

### Returns

Returns *true* if changed, *false* otherwise.

## Example

This example changes the ban admin to the admin's IP (If it's a player), when someone gets banned.

```
function banHappened(theBan)
    if getElementType(source) == "player" then
        local adminIP = getPlayerIP(source)
        setBanAdmin(theBan,adminIP)
    end
end

addEventHandler( "onBan", getRootElement(), banHappened )
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

- setBanAdmin

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
