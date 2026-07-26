---
doc_id: "mta-wiki:10231"
title: "GetAccountsByIP"
source_title: "GetAccountsByIP"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountsByIP"
revision_id: 72699
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:15:06.361855+00:00"
---

# GetAccountsByIP

This function returns a [table](mta://reference/misc/table.md) containing all accounts that were logged onto from specified IP-address.

## Syntax

```
table getAccountsByIP ( string ip )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Account class.*

**Method**: *Account.getAllByIP(...)*

### Required Arguments

- **ip:** The IP to get accounts from.

### Returns

Returns *[table](mta://reference/misc/table.md)* containing the accounts associated with specified IP-address. Returns *false* if invalid arguments were specified.

## Example

This example adds command *getAccounts* that outputs the number of accounts a player has in the chatbox:

```
addCommandHandler("getAccounts", 
	function (player, cmd)
		local ip = getPlayerIP(player)
		local accounts = getAccountsByIP(ip)
		outputChatBox("You have " .. #accounts .. " accounts.", player)
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

- getAccountsByIP

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
