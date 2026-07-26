---
doc_id: "mta-wiki:3650"
title: "BanSerial"
source_title: "BanSerial"
source_url: "https://wiki.multitheftauto.com/wiki/BanSerial"
revision_id: 44606
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# BanSerial

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use addBan instead. |  |

This function will ban the specified [serial](mta://reference/misc/serial.md) number from the server.

## Syntax

```
bool banSerial ( string theSerial )
```

### Required Arguments

- **theSerial:** The serial to ban from this server

### Returns

Returns *true* if the serial was banned succesfully, *false* if invalid arguments are specified.

## Example

This example lets a client (console or player) ban a serial if he has ACL rights.

```
--Add the "banserial" command handler
function banSerialCommand ( theClient, commandName, bannedSerial )

	-- Give the player a nice error if he doesn't have rights
	if ( hasObjectPermissionTo ( theClient, "function.banSerial" ) ) 

		--Ban the serial
		banSerial ( bannedSerial )
		outputChatBox ( "banserial: Serial " .. bannedSerial .. " successfully banned", theClient )
	else
		outputChatBox ( "banserial: You don't have enough permissions", theClient )
	end

end
addCommandHandler ( "banserial", banSerialCommand )
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
