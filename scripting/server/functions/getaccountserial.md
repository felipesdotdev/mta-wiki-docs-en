---
doc_id: "mta-wiki:7643"
title: "GetAccountSerial"
source_title: "GetAccountSerial"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccountSerial"
revision_id: 75075
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:06.288815+00:00"
---

# GetAccountSerial

This function returns the last [serial](mta://reference/misc/serial.md) that logged onto the specified [account](mta://reference/misc/account.md).

## Syntax

```
string getAccountSerial ( account theAccount )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):getSerial(...)*

**Variable**: *.serial*

### Required Arguments

- **theAccount:** The [account](mta://reference/misc/account.md) to get serial from

### Returns

Returns *string* containing the serial, the string is empty if the account was never used. Returns *false* if invalid arguments were specified.

## Example

This example adds command *getaccserial* that outputs the given account's serial in the chat box.

```
addCommandHandler("getaccserial", 
   function (player, cmd, accountName)
      if accountName then 
	 local account = getAccount(accountName)
	 if (account) then
	     outputChatBox("Serial: " .. getAccountSerial(account))
	 else
	     outputChatBox("Account not found")
	 end
     end
 end
)
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- [getAccount](mta://scripting/server/functions/getaccount.md)

- [getAccountData](mta://scripting/server/functions/getaccountdata.md)

- [getAccountName](mta://scripting/server/functions/getaccountname.md)

- [getAccountPlayer](mta://scripting/server/functions/getaccountplayer.md)

- getAccountSerial

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
