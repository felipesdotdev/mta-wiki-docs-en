---
doc_id: "mta-wiki:1814"
title: "IsGuestAccount"
source_title: "IsGuestAccount"
source_url: "https://wiki.multitheftauto.com/wiki/IsGuestAccount"
revision_id: 69872
language: "en"
categories: ["Server_functions"]
---

# IsGuestAccount

This function checks to see if an [account](mta://reference/misc/account.md) is a guest account. A guest account is an account automatically created for a user when they join the server and deleted when they quit or login to another account. Data stored in a guest account is not stored after the player has left the server. As a consequence, this function will check if a player is logged in or not.

## Syntax

```
bool isGuestAccount ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):isGuest(...)*

**Variable**: *.guest*

### Required Arguments

- **theAccount:** The account you want to check to see if it is a guest account.

### Returns

Returns *true* if the account is a guest account, *false* otherwise.

## Example

This example shows how you could create a *call_admin* function that only could be run by registered users.

```
function callAdmin ( playerSource )
    -- get the account of the user trying to use this function first
    sourceAccount = getPlayerAccount ( playerSource )
    -- if they're a guest
    if isGuestAccount ( sourceAccount ) then
        -- tell them to register
        outputConsole ( "Please register to use this function!", playerSource )
    else
        -- your code to call the admin would go here
    end
end
-- attach the function 'callAdmin' as a handler to the command "call_admin"
addCommandHandler ( "call_admin", callAdmin )
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

- isGuestAccount

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
