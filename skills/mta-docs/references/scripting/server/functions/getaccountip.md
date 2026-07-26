---
doc_id: "mta-wiki:10232"
title: "GetAccountIP"
source_title: "GetAccountIP"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountIP"
revision_id: 70141
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
---

# GetAccountIP

ADDED/UPDATED IN VERSION 1.5.5 [r11747](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=11747):

This function retrieves the IP address of an [account](mta://reference/misc/account.md).

## Syntax

```
string getAccountIP ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):getIP(...)*

**Variable**: *.ip*

### Required Arguments

- **theAccount:** The [account](mta://reference/misc/account.md) you wish to get the IP of.

### Returns

Returns a string containing the account's IP, *false* if the account does not exist or an invalid argument was passed to the function.

## Example

This example announces into the debugscript when a player logs into his account.

```
function outputOnLogin ( previous_account, current_account, auto_login ) --when a player logs in
	outputDebugString(getPlayerName(source) .. " logged into his account with IP " .. getAccountIP(current_account)) -- announce it into the debugscript
end
addEventHandler("onPlayerLogin", getRootElement(), outputOnLogin) --add an event handler
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

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- getAccountIP

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
