---
doc_id: "mta-wiki:3114"
title: "Client"
source_title: "Client"
source_url: "https://wiki.multitheftauto.com/wiki/Client"
revision_id: 40057
language: "en"
categories: ["Scripting_Concepts"]
---

# Client

The client class represents any client that is connected to the server. Therefore, clients are created and destroyed automatically by players' connections or disconnections. They usually are the MTA: SA copy that a [player](https://wiki.multitheftauto.com/index.php?search=player) is using (so it has more information about the world), but it can also be the [server console](mta://reference/misc/element-console.md).

All client-managing functions operate on both player and server console elements, so the element responsible for a kick can be the server console, for example. However, the server console is protected against some of that functions: it can't get kicked or banned.

The players' clients are also responsible of informing the server about the state of the elements that they're [syncing](mta://scripting/server/functions/setelementsyncer.md), so they're essential for accurate sync of peds and vehicles. They also receive data from other clients and the server.

## Related scripting functions

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
