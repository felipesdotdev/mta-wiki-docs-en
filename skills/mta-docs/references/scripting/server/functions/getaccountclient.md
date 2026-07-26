---
doc_id: "mta-wiki:1811"
title: "GetAccountClient"
source_title: "GetAccountClient"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountClient"
revision_id: 44574
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GetAccountClient

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getAccountPlayer instead. |  |

This function returns the client that is currently using a specified account, i.e. is logged into it. Only one client can use an account at a time.

## Syntax

```
client getAccountClient ( account theAccount )
```

### Required Arguments

- **theAccount:** The account you wish to get the client of.

### Returns

Returns a [client](mta://reference/misc/client.md) element if the account is currently in use, *false* otherwise.

## Example

This example checks if the user attached to an account is a player, and if so if they're alive.

```
function isAccountUserAlive ( theAccount )
    local theClient = getAccountClient ( theAccount )       -- get the client attached to the account
    if ( getElementType ( theClient ) == "player" ) then    -- see if it's a player (rather than an admin for example)
        if ( not isPlayerDead ( theClient ) ) then          -- if the player's health is greater than 0 
            return true
        end
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
