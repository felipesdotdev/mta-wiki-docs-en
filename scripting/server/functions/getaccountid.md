---
doc_id: "mta-wiki:10230"
title: "GetAccountID"
source_title: "GetAccountID"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountID"
revision_id: 70149
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:15:06.215673+00:00"
---

# GetAccountID

ADDED/UPDATED IN VERSION 1.5.5 [r12217](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=12217):

This function retrieves the ID of an [account](mta://reference/misc/account.md).

## Syntax

```
int getAccountID ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):getID(...)*

**Variable**: *.id*

### Required Arguments

- **theAccount:** The account you wish to get the ID of.

### Returns

Returns a int containing the account's ID, *false* if the account does not exist or an invalid argument was passed to the function.

## Example

This example announces into the console when a player logs into his account.

```
function outputOnLogin(previous_account, current_account, auto_login) --when a player logs in
	outputConsole("[" .. getAccountID(previous_account) .. "] " .. getAccountName(previous_account) .. " Logged into ["..getAccountID(current_account) .. "]" .. getAccountName(current_account)) -- announce it into the console
end
addEventHandler("onPlayerLogin", root, outputOnLogin) --add an event handler
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

- [getAccountByID](mta://scripting/server/functions/getaccountbyid.md)

- getAccountID

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
