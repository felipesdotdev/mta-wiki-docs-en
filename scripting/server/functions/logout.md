---
doc_id: "mta-wiki:3405"
title: "LogOut"
source_title: "LogOut"
source_url: "https://wiki.multitheftauto.com/wiki/LogOut"
revision_id: 70105
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:04.942232+00:00"
---

# LogOut

This function logs the given player out of his current [account](mta://reference/misc/account.md).

## Syntax

```
bool logOut ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):logOut(...)*

### Required Arguments

- **thePlayer:** The player to log out of his current account

### Returns

Returns *true* if the player was successfully logged out, *false* or *nil* if it failed for some reason, ie. the player was never logged in.

## Example

This example logs every player out of their account when the resource is (re)started. This would be handy for resources that show a login screen onClientResourceStart.

```
function logoutAll ()
	local players = getElementsByType ( "player" ) -- Get every player
		for k, player in ipairs ( players ) do -- For every player do the following...
			account = getPlayerAccount ( player ) -- Get every player's account
				if ( not isGuestAccount ( account ) ) then -- For every player that's logged in....
					logOut ( player ) -- Log them out.
				end
		end
end
 -- Trigger it when the resource (re)starts
addEventHandler ( "onResourceStart", getResourceRootElement(), logoutAll )
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- [getAccountName](mta://scripting/server/functions/getaccountname.md)

- [getAccountPlayer](mta://scripting/server/functions/getaccountplayer.md)

- [getAccountSerial](mta://scripting/server/functions/getaccountserial.md)

- [getAccounts](mta://scripting/server/functions/getaccounts.md)

- [getAccountsBySerial](mta://scripting/server/functions/getaccountsbyserial.md)

- [getAllAccountData](mta://scripting/server/functions/getallaccountdata.md)

- [getPlayerAccount](mta://scripting/server/functions/getplayeraccount.md)

- [isGuestAccount](mta://scripting/server/functions/isguestaccount.md)

- [logIn](mta://scripting/server/functions/login.md)

- logOut

- [removeAccount](mta://scripting/server/functions/removeaccount.md)

- [setAccountData](mta://scripting/server/functions/setaccountdata.md)

- [setAccountPassword](mta://scripting/server/functions/setaccountpassword.md)

- [getAccountByID](mta://scripting/server/functions/getaccountbyid.md)

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
