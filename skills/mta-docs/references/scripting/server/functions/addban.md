---
doc_id: "mta-wiki:4311"
title: "AddBan"
source_title: "AddBan"
source_url: "https://wiki.multitheftauto.com/wiki/AddBan"
revision_id: 82142
language: "en"
categories: ["Server_functions", "Utility_templates"]
---

# AddBan

This function will add a [ban](mta://reference/misc/ban.md) for the specified IP/username/serial to the server.

| [[{{{image}}}\|link=\|]] | Note: One of the three: IP, Username or Serial have to be specified. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Don't forget to give admin rights to the resource, in which you are using addBan function or it won't work. |
| --- | --- |
|  |  |

## Syntax

```
ban addBan ( string IP, string Username, string Serial, [ player responsibleElement, string reason, int seconds = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Ban](mta://reference/misc/ban.md)(...)*

### Required Arguments

- **IP:** The IP to be banned. If you don't want to ban by IP, set this to *nil*.

- **Username:** The [MTA Community](http://community.mtasa.com/) username to be banned (now obsolete). If you don't want to ban by username, set this to *nil*.

- **Serial:** The serial to be banned. If you don't want to ban by serial, set this to *nil*.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **responsibleElement:** The element that is responsible for banning the IP/username/serial. This can be a player or the root ([getRootElement](mta://scripting/shared/functions/getrootelement.md)()).

- **reason:** The reason the IP/username/serial will be banned from the server.

- **seconds:** The amount of seconds the player will be banned from the server for. This can be 0 for an infinite amount of time.

### Returns

Returns the new [ban](mta://reference/misc/ban.md) if the IP/username/serial was banned successfully, *false* if invalid arguments are specified.

## Examples

This example bans a player's IP with the reason "Requested" when they type "/ban-me".

```
function banMe ( source, command ) -- The function header and where source is defined
	local ipToBan = getPlayerIP ( source ) -- Get the player's IP
	addBan ( ipToBan, nil, nil, source, "Requested" ) -- Ban him with the reason; Requested
end
addCommandHandler ( "ban-me", banMe ) -- Make it trigger when a player types "/ban-me"
```

This example add command to ban player serial.

```
function banSerial( source, command, noob, reason )
   if ( noob ) then
      local theNoob = getPlayerFromName( noob )
      if ( theNoob ) then
         local theNoobSerial = getPlayerSerial( theNoob )
         addBan( nil, nil, theNoobSerial, source, reason )
      end
   end
end
addCommandHandler( "ban-serial", banSerial )
```

## See Also

- addBan

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
