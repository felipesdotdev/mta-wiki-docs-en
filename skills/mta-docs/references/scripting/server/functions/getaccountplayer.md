---
doc_id: "mta-wiki:4443"
title: "GetAccountPlayer"
source_title: "GetAccountPlayer"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountPlayer"
revision_id: 75073
language: "en"
categories: ["Server_functions"]
---

# GetAccountPlayer

This function returns the [player](https://wiki.multitheftauto.com/index.php?search=player) element that is currently using a specified [account](mta://reference/misc/account.md), i.e. is logged into it. Only one player can use an account at a time.

## Syntax

```
player getAccountPlayer ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):getPlayer(...)*

**Variable**: *.player*

### Required Arguments

- **theAccount:** The [account](mta://reference/misc/account.md) you wish to get the [player](https://wiki.multitheftauto.com/index.php?search=player) of.

### Returns

Returns a [player](https://wiki.multitheftauto.com/index.php?search=player) element if the account is currently in use, *false* otherwise.

## Example

This example checks if the user attached to an account is a player, and if so if they're alive.

```
function isAccountUserAlive ( theAccount )
    local thePlayer = getAccountPlayer ( theAccount )       -- get the client attached to the account
    if ( getElementType ( thePlayer ) == "player" ) then    -- see if it really is a player (rather than a console admin for example)
        return not isPedDead(thePlayer)             -- if the player's health is greater than 0 
    end
    return false
end
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- [getAccountName](mta://scripting/server/functions/getaccountname.md)

- getAccountPlayer

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
