---
doc_id: "mta-wiki:3404"
title: "LogIn"
source_title: "LogIn"
source_url: "https://wiki.multitheftauto.com/wiki/LogIn"
revision_id: 82751
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:04.928235+00:00"
---

# LogIn

This functions logs the given player in to the given [account](mta://reference/misc/account.md). You need to provide the password needed to log into that account.

## Syntax

```
bool logIn ( player thePlayer, account theAccount, string thePassword )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[player](mta://reference/misc/player.md):logIn(...)*

**Counterpart**: *[logOut](mta://scripting/server/functions/logout.md)*

### Required Arguments

- **thePlayer:** The player to log into an account

- **theAccount:** The account to log the player into

- **thePassword:** The password needed to sign into this account

### Returns

Returns *true* if the player was successfully logged into the given account. Returns *false* or *nil* if the log in failed for some reason, ie. the player was already logged in to some account (use [logOut](mta://scripting/server/functions/logout.md) first), if the account was already in use or if it failed for some other reason.

## Example

```
function loginPlayer ( thePlayer, command, username, password )
	local account = getAccount ( username, password ) -- Return the account
		if ( account ~= false ) then -- If the account exists.
			logIn ( thePlayer, account, password ) -- Log them in.
		else
			outputChatBox ( "Wrong username or password!", thePlayer, 255, 255, 0 ) -- Output they got the details wrong.
		end
end
addCommandHandler ( "log-in", loginPlayer ) -- Make it trigger for "/log-in", NOTE: /login is hardcored and cannot be used.
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

- logIn

- [logOut](mta://scripting/server/functions/logout.md)

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
