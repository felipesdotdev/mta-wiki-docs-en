---
doc_id: "mta-wiki:8266"
title: "SetBanNick"
source_title: "SetBanNick"
source_url: "https://wiki.multitheftauto.com/wiki/SetBanNick"
revision_id: 48713
language: "en"
categories: ["Server_functions", "Changes_in_1.4.1"]
---

# SetBanNick

This function sets a new nick for a [ban](mta://reference/misc/ban.md).

## Syntax

```
bool setBanNick ( ban theBan, string theNick )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ban](mta://reference/misc/ban.md):setNick(...)*

**Variable**: *.nick*

**Counterpart**: *[getBanNick](mta://scripting/server/functions/getbannick.md)*

### Required Arguments

- **theBan:** The [ban](mta://reference/misc/ban.md) you want to change the nick of.

- **theNick:** A string representing the nick you want to set the ban to.

### Returns

Returns *true* if changed, *false* otherwise.

## Example

```
-- this example looks if there is a ban with nick 'Steve', and if there is, it changes ban nick to 'Mike'
function changeBanNick()
   for i,ban in pairs(getBans()) do
      if getBanNick(ban) == "Steve" then
         setBanNick(ban,"Mike")
      end
   end
end
addCommandHandler("setbannick",changeBanNick)
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

- setBanNick

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
