---
doc_id: "mta-wiki:2350"
title: "BanPlayer"
source_title: "BanPlayer"
source_url: "https://wiki.multitheftauto.com/wiki/BanPlayer"
revision_id: 76868
language: "en"
categories: ["Server_functions", "Changes_in_1.0", "Utility_templates"]
generated_at: "2026-07-26T16:10:25.899496+00:00"
---

# BanPlayer

| [[{{{image}}}\|link=\|]] | Note: Don't forget to give admin rights to the resource, in which you are using banPlayer function or it won't work. |
| --- | --- |
|  |  |

This function will ban the specified player by either IP, [serial](mta://reference/misc/serial.md) or username

## Syntax

```
ban banPlayer ( player bannedPlayer, [ bool IP = true, bool Username = false, bool Serial = false, player/string responsiblePlayer = nil, string reason = nil, int seconds = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):ban(...)*

### Required Arguments

- **bannedPlayer:** The player that will be banned from the server.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **IP:** Will player be banned by IP?

- **Username:** Will player be banned by [MTA Community](http://community.mtasa.com/) username (obsolete, set to *false*)?

- **Serial:** Will player be banned by serial?

- **responsibleElement:** The element that is responsible for banning the player. This can be a player or the root ([getRootElement](mta://scripting/shared/functions/getrootelement.md)()) (Maximum 30 characters if using a string).

- **reason:** The reason the player will be banned from the server.

- **seconds:** The amount of seconds the player will be banned from the server for. This can be 0 for an infinite amount of time.

### Returns

Returns a [ban](mta://reference/misc/ban.md) object if banned successfully, or *false* if unsuccessful.

## Example

This example lets a player ban anyone if he has ACL rights.

```
--Add the "ban" command handler
-- Example with the player
function banPlayerCommand ( theClient, commandName, bannedName, reason )

	-- Give the player a nice error if he doesn't have rights
	if ( hasObjectPermissionTo ( theClient, "function.banPlayer" ) ) then
		--Get player element from the name
		local bannedPlayer = getPlayerFromName ( bannedName )

		--Ban the player
		banPlayer ( bannedPlayer, theClient, reason )
		outputChatBox ( "ban: " .. bannedName .. " successfully banned", theClient )

	else
		outputChatBox ( "ban: You don't have enough permissions", theClient )
	end

end
addCommandHandler ( "ban", banPlayerCommand )

-- Example function with the root element. Here you would pass a player element to the function.
function banCheater(theCheater)
	banPlayer(theCheater, root, "You are banned because of cheating.")
end
```

This example is Firewall Account Player by serial on Login

```
Firewall = 
{
    [ 'AccountName' ] = 'SerialPlayer',
    [ '3ash8' ] = '9C9F3B55D9D7BB7135FF274D3BF444E4',
    [ 'test5' ] = '1D6F76CF8D7193792D13789849498452',
}
 
addEventHandler ( 'onPlayerLogin', root,
    function ( _, theCurrentAccount )
    local Serial = Firewall[getAccountName(theCurrentAccount)]
        if ( Serial ) then
            if Serial ~= getPlayerSerial ( source ) then
                banPlayer ( source, false, false, true, root, 'reason ban' )
            end
        end
    end
)
```

## See Also

- [addBan](mta://scripting/server/functions/addban.md)

- banPlayer

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
