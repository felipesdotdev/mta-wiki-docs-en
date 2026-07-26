---
doc_id: "mta-wiki:10234"
title: "GetAccountsByData"
source_title: "GetAccountsByData"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountsByData"
revision_id: 70143
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
---

# GetAccountsByData

ADDED/UPDATED IN VERSION 1.5.5 [r11747](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=11747):

This function returns a [table](mta://reference/misc/table.md) containing all accounts with specified dataName and value (set with setAccountData).

## Syntax

```
table getAccountsByData ( string dataName, string value )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Account class.*

**Method**: *Account.getAllByData(...)*

### Required Arguments

- **dataName:** The name of the data

- **value:** The value the dataName should have

### Returns

Returns *[table](mta://reference/misc/table.md)* containing the accounts associated with specified value at dataName. Returns *false* if invalid arguments were specified.

## Example

Useless example to show how it works.

```
addCommandHandler("accountsbydata", function (player)
   local account = getPlayerAccount(player)
   setAccountData(account, "test", "hello")
   local accounts = getAccountsByData("test", "hello")
   outputChatBox(getAccountName(accounts[1]), player)                
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

- [getAccountByID](mta://scripting/server/functions/getaccountbyid.md)

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- getAccountsByData

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
