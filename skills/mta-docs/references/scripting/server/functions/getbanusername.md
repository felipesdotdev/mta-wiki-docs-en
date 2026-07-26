---
doc_id: "mta-wiki:4316"
title: "GetBanUsername"
source_title: "GetBanUsername"
source_url: "https://wiki.multitheftauto.com/wiki/GetBanUsername"
revision_id: 48718
language: "en"
categories: ["Deprecated", "Server_functions"]
---

# GetBanUsername

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getBanNick instead. |  |

This function will return the username of the specified [ban](mta://reference/misc/ban.md).

## Syntax

```
string getBanUsername ( ban theBan )
```

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) in which you wish to retrieve the username of.

### Returns

Returns a *string* of the username if everything was successful, *false* if invalid arguments are specified if there was no username specified for the [ban](mta://reference/misc/ban.md).

## Example

```
function retrieveBan(theBan)
    local ban = getBanUsername(theBan)
    if ban then
        outputChatBox("The following bans username is: "..ban, getRootElement(), 255,255,255, true)
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

- [removeBan](mta://scripting/server/functions/removeban.md)
