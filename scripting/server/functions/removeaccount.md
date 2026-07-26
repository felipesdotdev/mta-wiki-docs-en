---
doc_id: "mta-wiki:2333"
title: "RemoveAccount"
source_title: "RemoveAccount"
source_url: "https://wiki.multitheftauto.com/wiki/RemoveAccount"
revision_id: 70112
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:31.820800+00:00"
---

# RemoveAccount

This function is used to delete existing player [accounts](mta://reference/misc/account.md).

## Syntax

```
bool removeAccount ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):remove(...)*

### Required Arguments

- **theAccount:** The account you wish to remove

### Returns

Returns *true* if account was successfully removed, *false* if the account does not exist.

## Example

This example does...

```
function onCmdDeregister ( playerSource, commandName )
	-- grab the account
	local sourceAccount = getPlayerAccount ( playerSource )
	if sourceAccount then
		removeAccount ( sourceAccount )
		outputChatBox ( "Account deregistered for " .. getPlayerName ( playerSource ) )
	else 
		outputChatBox ( "Unable to get your account, make sure you are logged in", playerSource )
	end
end
 
addCommandHandler("deregister",onCmdDeregister)
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

- [logOut](mta://scripting/server/functions/logout.md)

- removeAccount

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
