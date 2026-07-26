---
doc_id: "mta-wiki:2335"
title: "SetAccountPassword"
source_title: "SetAccountPassword"
source_url: "https://wiki.multitheftauto.com/wiki/SetAccountPassword"
revision_id: 70122
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:37.839769+00:00"
---

# SetAccountPassword

This function sets the password of the specified [account](mta://reference/misc/account.md).

| [[{{{image}}}\|link=\|]] | Note: Don't forget to give admin rights to the resource, in which you are using setAccountPassword function or it won't work. |
| --- | --- |
|  |  |

## Syntax

```
bool setAccountPassword ( account theAccount, string password )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[account](mta://reference/misc/account.md):setPassword(...)*

**Variable**: *.password*

### Required Arguments

- **theAccount:** the account whose password you want to set

- **password:** the password

| [[{{{image}}}\|link=\|]] | Note: The password will always be encrypted with sha256 , other types are no longer supported. See CAccountPassword for more information. |
| --- | --- |
|  |  |

### Returns

Returns *true* if the password was set correctly, *false* otherwise.

### Limits

The following limits apply:

- Minimum account password length is 1 character.

- Maximum account password length is 30 characters.

- Account password can not be equal to "*****"

## Example

This example allows a user to change their password with a command.

```
function ChangePlayerPassword(player, command, oldpass, newpass)
	-- get the account the player is currently logged into
	local account = getPlayerAccount(player)
	if (account) then
		-- if its only a guest account, do not allow the password to be changed
		if (isGuestAccount(account)) then
			outputChatBox("You must be logged into an account to change your password.", player) 
			-- end the function
			return
		end
		
		-- check that the old password is correct
		local password_check = getAccount(getAccountName(account), oldpass)
		if (password_check) then
			-- check the length of the new password
			if (string.len(newpass)>=5) then
				setAccountPassword(account,newpass)
			else
				outputChatBox("Your new password must be at least 5 characters long.", player)
			end
		else
			outputChatBox("Old password invalid.", player)
		end
	end
end
addCommandHandler("changepass", ChangePlayerPassword)
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

- setAccountPassword

- [getAccountByID](mta://scripting/server/functions/getaccountbyid.md)

- [getAccountID](mta://scripting/server/functions/getaccountid.md)

- [getAccountIP](mta://scripting/server/functions/getaccountip.md)

- [getAccountsByData](mta://scripting/server/functions/getaccountsbydata.md)

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
