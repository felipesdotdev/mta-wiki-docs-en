---
doc_id: "mta-wiki:4319"
title: "GetBanTime"
source_title: "GetBanTime"
source_url: "https://wiki.multitheftauto.com/wiki/GetBanTime"
revision_id: 48717
language: "en"
categories: ["Server_functions"]
---

# GetBanTime

This function will return the time the specified [ban](mta://reference/misc/ban.md) was created, in **seconds**.

## Syntax

```
int getBanTime ( ban theBan )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):getTime(...)*

**Variable**: *.time*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) of which you wish to retrieve the time of.

### Returns

- Returns an integer of the banning time in the format of seconds from the year 1970.  Use in conjunction with [getRealTime](mta://scripting/shared/functions/getrealtime.md) in order to retrieve detailed information.

- Returns **false** if invalid arguments were specified or if there was no banning time specified for the [ban](mta://reference/misc/ban.md).

## Example

```
function retrieveBan(theBan)
    local ban = getBanTime(theBan)
    if ban then
        outputChatBox("The time of the ban is: " .. ban, root, 255, 255, 255, false)
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

- getBanTime

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
