---
doc_id: "mta-wiki:2738"
title: "UnbanIP"
source_title: "UnbanIP"
source_url: "https://wiki.multitheftauto.com/wiki/UnbanIP"
revision_id: 25633
language: "en"
categories: ["Server_functions", "Deprecated", "Utility_templates"]
---

# UnbanIP

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions, but there should be a more generic way to perform what it does. |
| --- | --- |
|  |  |

Please use [removeBan](mta://scripting/server/functions/removeban.md)

This function will unban the specified IP.

## Syntax

```
bool unbanIP ( string ipToUnban, [player unbanningPlayer = nil] )
```

### Required Arguments

- **ipToUnban:** The IP that should be unbanned.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **unbanningPlayer:** The player who is unbanning the IP. Defaults to nil, meaning no one.

### Returns

Returns *true* if the unban was successful, *false* otherwise.

## Example

This example adds a unbanip command for only admins to use (uses a ACL permission check).

```
addCommandHandler( "unbanip", -- add a command handler to command 'unbanip'
   function ( thePlayer, command, ip )
      if ( hasObjectPermissionTo ( thePlayer, "command.unbanip", false ) ) then -- check if the player has access to the command (specified in ACL)
         if not ip then outputChatBox( "No IP specified.", thePlayer ) return end -- if no IP was specified, abort command
         if not findpattern( ip, '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', 1 ) then outputChatBox( "Given IP is not valid.", thePlayer ) return end -- if IP is not in correct format, abort command
         local success = unbanIP( ip, thePlayer ) -- see whether the function was a success
         if success then
            outputChatBox( "IP " .. ip .. " succesfully unbanned!", thePlayer ) -- if it was, tell that to player
         else
            outputChatBox( "Unbanning IP " .. ip .. " failed!", thePlayer ) -- if it wasn't, tell that to player
         end
      else
         outputChatBox( "You have no permission to use this command.", thePlayer ) -- tell player that he hasn't got right permission
      end
   end
)

-- specify the findpattern function used in the command handler
function findpattern(text, pattern, start)
	local found = string.find(text, pattern, start)
	if found ~= nil then
		return string.gsub(text, found)
	else return nil end
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
