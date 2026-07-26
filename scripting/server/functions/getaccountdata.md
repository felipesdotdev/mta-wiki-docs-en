---
doc_id: "mta-wiki:1801"
title: "GetAccountData"
source_title: "GetAccountData"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountData"
revision_id: 75069
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:06.165376+00:00"
---

# GetAccountData

| [[{{{image}}}\|link=\|]] | Important Note: You MUST use the standard module.key naming for your keys, as shown in the example below. This prevents collisions between different scripts. |
| --- | --- |
|  |  |

This function retrieves a string that has been stored using [setAccountData](mta://scripting/server/functions/setaccountdata.md). Data stored as account data is persistent across user's sessions and maps, unless they are logged into a guest account.

## Syntax

```
string getAccountData ( account theAccount, string key )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):getData(...)*

**Counterpart**: *[setAccountData](mta://scripting/server/functions/setaccountdata.md)*

### Required Arguments

- **theAccount:** The account you wish to retrieve the data from.

- **key:** The key under which the data is stored

### Returns

Returns a [string](mta://reference/misc/string.md) containing the stored data or *false* if no data was stored under that key.

## Example

For a pirate roleplaying gametype, the amount of money a player has is made persistent by storing it in his account. Note the code uses "piraterpg.money" as key instead of just "money", as the player may be participating in other gametypes that also save his money amount to his account. If both gametypes would use "money" as the account key, they'd overwrite each other's data.

```
function onPlayerQuit()
      local playerAccount = getPlayerAccount(source) -- get his account
      if (playerAccount) then -- if we got the account then
            local playerMoney = getPlayerMoney(source) -- get his money amount
            setAccountData(playerAccount, "piraterpg.money", playerMoney) -- store his current money amount in his account data
      end
end
addEventHandler("onPlayerQuit", root, onPlayerQuit) -- add an event handler

function onPlayerLogin(_,account)
    local playerMoney = getAccountData(account, "piraterpg.money") -- get the money amount was store in his account data
    -- make sure there was actually a value saved under this key (check if playerMoney is not false).
    -- this will for example not be the case when a player plays the gametype for the first time
    if (playerMoney) then
        setPlayerMoney(source, playerMoney)
    end
end
addEventHandler("onPlayerLogin", root, onPlayerLogin) -- add an event handler
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- getAccountData

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
