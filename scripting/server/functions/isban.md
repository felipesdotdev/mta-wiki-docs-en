---
doc_id: "mta-wiki:7653"
title: "IsBan"
source_title: "IsBan"
source_url: "https://wiki.multitheftauto.com/wiki/IsBan"
revision_id: 63269
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:53.430519+00:00"
---

# IsBan

This function checks whether the passed value is valid [ban](mta://reference/misc/ban.md) or not.

## Syntax

```
bool isBan ( ban theBan )
```

### Required Arguments

- **theBan:** The value to check

### Returns

Returns *true* if the value is a ban, *false* otherwise.

## Example

Click to collapse [-]
Example1

This example chechks if the passed argument is a ban or not.

```
function banRecieve ( ban )
	if ban and isBan(ban) then
		outputChatBox("this is a ban!")--Valid ban is recieved!
	else
		outputChatBox("this is not a ban, this is a "..getElementType(ban))--if the argument is not a ban, then checks its type and output it into the chat box.
	end
end

function onBan ( ban ) -- This function will be triggered every time a player is banned.
	banRecieve(ban)
end
addEventHandler ( "onPlayerBan", getRootElement(), onBan )

function sendWrongBanArguement()
	local vehicle = createVehicle(411,0,5,3)
	local object = createObject(2600,0,0,0)
	local ped = createPed(61,0,0,3)
	
	banRecieve(vehicle)--sends a vehicle as an argument.
	banRecieve(object)--sends an object as an argument.
	banRecieve(ped)--sends a ped as an argument.
end
addCommandHandler("sendWrongArgument",sendWrongBanArguement)
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

- isBan

- [kickPlayer](mta://scripting/server/functions/kickplayer.md)

- [setBanAdmin](mta://scripting/server/functions/setbanadmin.md)

- [setBanNick](mta://scripting/server/functions/setbannick.md)

- [setBanReason](mta://scripting/server/functions/setbanreason.md)

- [setUnbanTime](mta://scripting/server/functions/setunbantime.md)

- [reloadBans](mta://scripting/server/functions/reloadbans.md)

- [removeBan](mta://scripting/server/functions/removeban.md)
