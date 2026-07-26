---
doc_id: "mta-wiki:3536"
title: "GetPlayerAccount"
source_title: "GetPlayerAccount"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerAccount"
revision_id: 70058
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:18.982315+00:00"
---

# GetPlayerAccount

This function returns the specified player's [account](mta://reference/misc/account.md) object.

## Syntax

```
account getPlayerAccount ( player thePlayer )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Static method [Account](mta://reference/misc/account.md).getFromPlayer() can also be used*

**Method**: *[player](mta://reference/misc/player.md):getAccount(...)*

**Variable**: *.account*

### Required Arguments

- **thePlayer:** The [player](mta://reference/misc/player.md) element you want to get the [account](mta://reference/misc/account.md) of.

### Returns

Returns the player's account object, or *false* if the player passed to the function is invalid.

## Example

This example sets a player's money and also stores the value is his account.

```
function setMoney(thePlayer,key,amount)
    local account = getPlayerAccount(thePlayer)
    if account and tonumber(amount) then
        setPlayerMoney (thePlayer,amount)
        setAccountData(account,"money",amount)
    end
end
addCommandHandler("setmoney",setMoney)
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

- getPlayerAccount

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
