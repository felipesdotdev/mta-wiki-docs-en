---
doc_id: "mta-wiki:3356"
title: "GetAccount"
source_title: "GetAccount"
source_url: "https://wiki.multitheftauto.com/wiki/GetAccount"
revision_id: 75066
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:06.087900+00:00"
---

# GetAccount

This function returns an [account](mta://reference/misc/account.md) for a specific user.

## Syntax

```
account getAccount ( string username [, string password, bool caseSensitive = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Account](mta://reference/misc/account.md)(...)*

### Required Arguments

- **username:** The username of the account you want to retrieve

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **password:** The password for the account. If this argument is not specified, you can get the account whatever password it is, otherwise the password must match the account's.

- **caseSensitive**: Specifies whether to ignore the case when searching for an account.

### Returns

Returns an [account](mta://reference/misc/account.md) or *false* if an account matching the username specified (and password, if specified) could not be found.

## Example

Click to collapse [-]
Server example 1

This function checks if the account mentioned exists in the internal.db database file.

```
addCommandHandler("checkaccount",
	function(player, cmd, account)
		if hasObjectPermissionTo(player, "function.banPlayer" ) then -- if the player typing /checkaccount command has permission to banPlayer
			if account and account ~= "" then -- if the account name was mentioned
				if getAccount(account) then -- if the account exists
					outputChatBox("Account "..account.." exists in the database!", player, 0, 255, 0)
				else -- if the account doesn't exist
					outputChatBox("Account "..account.." does not exist in database", player, 0, 255, 0)
				end
			else
			outputChatBox("Syntax is /checkaccount [account name]", player, 255, 0, 0)
			end
		end
	end
)
```

## See Also

- [addAccount](mta://scripting/server/functions/addaccount.md)

- [copyAccountData](mta://scripting/server/functions/copyaccountdata.md)

- getAccount

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
