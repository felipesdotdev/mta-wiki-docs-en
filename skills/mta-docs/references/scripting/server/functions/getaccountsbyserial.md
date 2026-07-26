---
doc_id: "mta-wiki:7644"
title: "GetAccountsBySerial"
source_title: "GetAccountsBySerial"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountsBySerial"
revision_id: 70049
language: "en"
categories: ["Server_functions"]
---

# GetAccountsBySerial

This function returns a [table](mta://reference/misc/table.md) containing all accounts that were logged onto from specified [serial](mta://reference/misc/serial.md). If the serial is empty string, it will return all accounts that were never logged onto.

## Syntax

```
table getAccountsBySerial ( string serial )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Account class.*

**Method**: *Account.getAllBySerial(...)*

### Required Arguments

- **serial:** The [serial](mta://reference/misc/serial.md) to get accounts from

### Returns

Returns *[table](mta://reference/misc/table.md)* containing the accounts associated with specified serial. Returns *false* if invalid arguments were specified.

## Example

This example adds command *getAccounts* that outputs the number of accounts a player has in the chat box.

```
addCommandHandler("getAccounts", 
	function (player, cmd)
		local serial = getPlayerSerial(player)
		local accounts = getAccountsBySerial(serial)
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

- getAccountsBySerial

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
