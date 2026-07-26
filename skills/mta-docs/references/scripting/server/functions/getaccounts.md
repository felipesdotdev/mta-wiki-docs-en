---
doc_id: "mta-wiki:4294"
title: "GetAccounts"
source_title: "GetAccounts"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccounts"
revision_id: 70045
language: "en"
categories: ["Server_functions"]
---

# GetAccounts

This function returns a table over all the [accounts](mta://reference/misc/account.md) that exist in the server internal.db file. (Note: accounts.xml is no longer used after version 1.0.4)

## Syntax

```
table getAccounts ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Account class.*

**Method**: *[Account](mta://reference/misc/account.md).getAll(...)*

### Returns

A [table](mta://reference/misc/table.md) over the accounts that exist in the server internal.db file. This table might be empty.

## Example

```
function printAmountOfAccounts ( thePlayer )
    local accountTable = getAccounts () -- return the table over accounts
    if #accountTable == 0 then -- if the table is empty
        outputChatBox( "There are no accounts. :(", thePlayer )
    else -- table isn't empty
        outputChatBox( "There are " .. #accountTable .. " accounts in this server!", thePlayer )
    end
end
addCommandHandler( "accountcount", printAmountOfAccounts ) -- add a command handler for command 'accountcount'
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- [getAccountName](mta://scripting/server/functions/getaccountname.md)

- [getAccountPlayer](mta://scripting/server/functions/getaccountplayer.md)

- [getAccountSerial](mta://scripting/server/functions/getaccountserial.md)

- getAccounts

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
