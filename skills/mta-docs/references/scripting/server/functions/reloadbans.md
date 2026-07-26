---
doc_id: "mta-wiki:6158"
title: "ReloadBans"
source_title: "ReloadBans"
source_url: "https://wiki.multitheftauto.com/wiki/ReloadBans"
revision_id: 81104
language: "en"
categories: ["Server_functions"]
---

# ReloadBans

This function will reload the server ban list file.

## Syntax

```
bool reloadBans()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Ban](mta://reference/misc/ban.md).reload(...)*

### Returns

Returns *true* if the ban list was reloaded successfully, *false* otherwise.

## Example

This example add command "reloadban" to reload the server ban list file.

```
function ReBan (player)
   if (reloadBans()) then
      outputChatBox("Bans has been reloaded successfully.",player)
   else
      outputChatBox("Failed to Reload Bans.",player)
   end
end
addCommandHandler("reloadban",ReBan)
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

- reloadBans

- [removeBan](mta://scripting/server/functions/removeban.md)
