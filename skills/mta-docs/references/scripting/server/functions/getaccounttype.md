---
doc_id: "mta-wiki:14303"
title: "GetAccountType"
source_title: "GetAccountType"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountType"
revision_id: 79579
language: "en"
categories: ["Server_functions", "Changes_in_1.6.0"]
---

# GetAccountType

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

This function returns an [account](mta://reference/misc/account.md) type. 

## Syntax

```
string getAccountType ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Account class.*

**Method**: *Account.getType(...)*

### Required Arguments

- **theAccount:** An [account](mta://reference/misc/account.md) you want to get info from

### Returns

Returns *[string](mta://reference/misc/string.md)* containing the type of the account if the account is valid.

## Example

This example adds command *accountInfo* that outputs provided account info

Click to collapse [-]
Server

```
addCommandHandler("accountInfo", function(player, cmd, accountName)
    if not accountName then
        outputChatBox("You have to provide an account's name to get info from!", player)
        return
    end
    local acc = getAccount(accountName)
    if not acc then
        outputChatBox("That account doesn't exist!", player)
        return
    end
    local accName = getAccountName(acc)
    local accType = getAccountType(acc)
    outputChatBox('Account name: '..accName..', type: '..accType, player)
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

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- getAccountType
