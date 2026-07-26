---
doc_id: "mta-wiki:7510"
title: "SetAccountName"
source_title: "SetAccountName"
source_url: "https://wiki.multitheftauto.com/wiki/SetAccountName"
revision_id: 70147
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:16:37.818546+00:00"
---

# SetAccountName

ADDED/UPDATED IN VERSION 1.5.5 [r11747](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=11747):

This function sets the name of an [account](mta://reference/misc/account.md).

## Syntax

```
bool setAccountName ( account theAccount, string name [, bool allowCaseVariations = false] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):setName(...)*

**Variable**: *.name*

**Counterpart**: *[getAccountName](mta://scripting/server/functions/getaccountname.md)*

### Required Arguments

- **theAccount:** The account you wish to change the name.

- **name:** The new name.

### Optional Arguments

- **allowCaseVariations:** Whether the username is case sensitive (if this is set to true, usernames "Bob" and "bob" will refer to different accounts)

### Returns

Returns a *true* if the account name was set, *false* if an invalid argument was specified.

## Example

Change the name of an account.

```
addCommandHandler("changeaccountname", function(player, _, oldname, newname)
    if not oldname or not newname then
        return
    end
    local account = getAccount(oldname)
    if not account then
        return 
    end
    setAccountName(account, newname)
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

- setAccountName

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
