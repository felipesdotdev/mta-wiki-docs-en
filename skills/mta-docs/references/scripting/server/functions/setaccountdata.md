---
doc_id: "mta-wiki:1802"
title: "SetAccountData"
source_title: "SetAccountData"
source_url: "https://wiki.multitheftauto.com/wiki/SetAccountData"
revision_id: 73903
language: "en"
categories: ["Server_functions"]
---

# SetAccountData

| [[{{{image}}}\|link=\|]] | Important Note: You MUST use the standard module.key naming for your keys, as shown in the example below. This prevents collisions between different scripts. |
| --- | --- |
|  |  |

This function sets a string to be stored in an [account](mta://reference/misc/account.md). This can then be retrieved using [getAccountData](mta://scripting/server/functions/getaccountdata.md). Data stored as account data is persistent across user's sessions and maps, unless they are logged into a guest account. Even if logged into a guest account, account data can be useful as a way to store a reference to your own account system, though it's persistence is equivalent to that of using [setElementData](mta://scripting/shared/functions/setelementdata.md) on the player's element.

## Syntax

```
bool setAccountData ( account theAccount, string key, var value )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):setData(...)*

**Counterpart**: *[getAccountData](mta://scripting/server/functions/getaccountdata.md)*

### Required Arguments

- **theAccount:** The account you wish to retrieve the data from.

- **key:** The key under which you wish to store the data

- **value:** The value you wish to store. Set to false to remove the data. **NOTE:** you cannot store tables as values, but you can use [toJSON](mta://scripting/shared/functions/tojson.md) strings.

### Returns

Returns a *true* if the account data was set, *false* if an invalid argument was specified.

## Example

For a pirate roleplaying gametype, the amount of money a player has is made persistent by storing it in his account. Note the code uses "piraterpg.money" as key instead of just "money", as the player may be participating in other gametypes that also save his money amount to his account. If both gametypes would use "money" as the account key, they'd overwrite each other's data.

```
function onPlayerQuit ( )
      -- when a player leaves, store his current money amount in his account data
      local playeraccount = getPlayerAccount ( source )
      if ( playeraccount ) and not isGuestAccount ( playeraccount ) then -- if the player is logged in
            local playermoney = getPlayerMoney ( source ) -- get the player money
            setAccountData ( playeraccount, "piraterpg.money", playermoney ) -- save it in his account
      end
end
 
function onPlayerLogin (_, playeraccount )
      -- when a player logins, retrieve his money amount from his account data and set it
      if ( playeraccount ) then
            local playermoney = getAccountData ( playeraccount, "piraterpg.money" )
            -- make sure there was actually a value saved under this key (check if playermoney is not false).
            -- this will for example not be the case when a player plays the gametype for the first time
            if ( playermoney ) then
                  setPlayerMoney ( source, playermoney )
            end
      end
end
 
addEventHandler ( "onPlayerQuit", root, onPlayerQuit )
addEventHandler ( "onPlayerLogin", root, onPlayerLogin )
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

- setAccountData

- [setAccountPassword](mta://scripting/server/functions/setaccountpassword.md)

- [getAccountByID](mta://scripting/server/functions/getaccountbyid.md)

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
