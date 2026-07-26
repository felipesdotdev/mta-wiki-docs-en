---
doc_id: "mta-wiki:1870"
title: "CopyAccountData"
source_title: "CopyAccountData"
source_url: "https://wiki.multitheftauto.com/wiki/CopyAccountData"
revision_id: 75061
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:36.300687+00:00"
---

# CopyAccountData

This function copies all of the data from one [account](mta://reference/misc/account.md) to another.

## Syntax

```
bool copyAccountData ( account theAccount, account fromAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):copyDataTo(...)*

### Required Arguments

- **theAccount:** The account you wish to copy the data *to*.

- **fromAccount:** The account you wish to copy the data *from*.

### Returns

Returns a *true* if the accounts were valid, *false* otherwise.

## Example

This example copies the account data from the 'guest' to a registered account when they login

```
function copyDataOnLogin ( previousAccount, currentAccount )
  copyAccountData ( currentAccount, previousAccount )
end
addEventHandler ( "onPlayerLogin", getRootElement(), copyDataOnLogin )
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- copyAccountData

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

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
