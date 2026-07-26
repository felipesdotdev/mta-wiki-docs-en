---
doc_id: "mta-wiki:10233"
title: "GetAccountByID"
source_title: "GetAccountByID"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountByID"
revision_id: 70150
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
---

# GetAccountByID

ADDED/UPDATED IN VERSION 1.5.5 [r12217](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=12217):

This function returns the account with the specific ID.

## Syntax

```
account getAccountByID ( int id )
```

### Required Arguments

- **id:** The ID to get account from

### Returns

Returns *[account](mta://reference/misc/account.md)* associated with specified ID. Returns *false* if invalid arguments were specified or there is no account with this ID.

## Example

This example adds command *getAccount* that outputs the account-name of the account with ID.

```
addCommandHandler("getAccount", 
	function (player, cmd, id)
                id = tonumber(id)
		local account = getAccountByID(id)
                if account then
		   outputChatBox("The name of the account with that ID is: "..getAccountName(account), player)
                else 
                   outputChatBox("There is no account with this ID.", player)
                end
	end)
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

- [removeAccount](mta://scripting/server/functions/removeaccount.md)

- [setAccountData](mta://scripting/server/functions/setaccountdata.md)

- [setAccountPassword](mta://scripting/server/functions/setaccountpassword.md)

- getAccountByID

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
