---
doc_id: "mta-wiki:4277"
title: "GetBansXML"
source_title: "GetBansXML"
source_url: "https://wiki.multitheftauto.com/wiki/GetBansXML"
revision_id: 44616
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GetBansXML

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getBans instead. |  |

This function retrieves the root [xmlnode](mta://reference/misc/xmlnode.md) of the ban file (server/mods/deathmatch/banlist.xml).

## Syntax

```
xmlnode getBansXML ()
```

### Returns

Returns a [xmlnode](mta://reference/misc/xmlnode.md), *false* if something went wrong.

## Example

This example prints the amount of bans in the banfile to the chat when player uses command *banamount*.

```
function tellPlayerBanAmount ( thePlayer )
    local bansNode = getBansXML () -- get the root node of ban file
    local children = xmlNodeGetChildren ( bansNode ) -- get the children (bans) of the root xml node
    outputChatBox ( "There are " .. #children .. " bans in the ban file.", thePlayer ) -- print the size of children table to the chat
end
addCommandHandler ( "banamount", tellPlayerBanAmount )
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
