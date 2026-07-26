---
doc_id: "mta-wiki:1813"
title: "GetAccountName"
source_title: "GetAccountName"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountName"
revision_id: 82648
language: "en"
categories: ["Server_functions"]
---

# GetAccountName

This function retrieves the name of an [account](mta://reference/misc/account.md).

## Syntax

```
string getAccountName ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):getName(...)*

**Variable**: *.name*

### Required Arguments

- **theAccount:** The account you wish to get the name of.

### Returns

Returns a string containing the account's name, *false* if the account does not exist or an invalid argument was passed to the function.

## Example

This example announces into the console when a player logs into his account.

```
function outputOnLogin ( previous_account, current_account, auto_login ) --when a player logs in
    outputConsole(getAccountName(previous_account).." Logged into "..getAccountName(current_account)) -- announce it into the console
end
addEventHandler("onPlayerLogin",root,outputOnLogin ) --add an event handler
```

This example shows the account you are logged into.

```
addCommandHandler("mylogin", function(source)
    local account = getPlayerAccount(source)
    if account and not isGuestAccount(account) then
        local accountName = getAccountName(account)
        outputChatBox("Your login is: "..accountName, source)
    else
        outputChatBox("You are not logged in!", source)
    end
end)
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- getAccountName

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
