---
doc_id: "mta-wiki:2332"
title: "AddAccount"
source_title: "AddAccount"
source_url: "https://wiki.multitheftauto.com/wiki/AddAccount"
revision_id: 75060
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:10:25.571105+00:00"
---

# AddAccount

This function adds an account to the list of registered accounts of the current server.

## Syntax

```
account addAccount ( string name, string pass [, bool allowCaseVariations = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Account class.*

**Method**: *[Account](mta://reference/misc/account.md).add (...)*

### Required Arguments

- **name:** The name of the account you wish to make, this normally is the player's name.

- **pass:** The password to set for this account for future logins.

### Optional Arguments

- **allowCaseVariations:** Whether the username is case sensitive (if this is set to true, usernames "Bob" and "bob" will refer to different accounts)

### Returns

Returns an [account](mta://reference/misc/account.md) or *false* if the account already exists or an error occured.

### Limits

- **name:**

- Minimal account name length is 1 character.

- Account names are case-sensitive if allowCaseVariations is *true*.

- Account name can not be equal to "*****"

- **pass:**

- Minimal account password length is 1 character.

- Maximum account password length **was** 30 characters until version 1.5.4-11138. Currently there is no upper limit.

- Account password can not be equal to "*****"

## Example

**Example 1:** This enables players to register on your server by using /register <password> in the chat window.

```
function registerPlayer ( source, commandName, password )
	-- Check if the password field is blank or not (only blank if they didnt enter one)
	if ( password ~= "" and password ~= nil ) then
		--Attempt to add the account, and save its value in a var
		local accountAdded = addAccount( getPlayerName(source), password )
		if ( accountAdded ) then
			--  Tell the user all is done
			outputChatBox ( "Thank you " .. getPlayerName(source) .. ", you're now registed, you can login with /login", source )
		else
			-- There was an error making the account, tell the user
			outputChatBox ( "Error creating account, contact the server admin", source )
		end
	else
		-- There was an error in the syntax, tell the user the correct syntax.
		outputChatBox ( "Error creating account, correct syntax: /register <password>", source )
	end
end
addCommandHandler ( "register", registerPlayer ) -- add the command handler
```

**This code differs by allowing the user to change their username that they wish to use.**

**Example 2:** This enables players to register on your server by using /register <username> <password> in the chat window.

```
function registerPlayer ( source, commandName, username, password )
        if(password ~= "" and password ~= nil and username ~= "" and username ~= nil) then
                local accountAdded = addAccount(username,password)
                if(accountAdded) then
                        outputChatBox("Thank you " .. getPlayerName(source) .. ", you're now registed, you can login with /login",source)
                else
                        outputChatBox("Error creating account, contact the server admin.",source)
                end
        else
                outputChatBox("Error creating account, correct syntax: /register <nick> <pass>",source)
        end
end
addCommandHandler ( "register", registerPlayer ) -- add the command handler
```

**Example 3:** This code differs again so the user can only register once /register <username> <password>.

```
bRegisteredOnce = {}

function registerPlayer ( source, commandName, username, password )
        if(password ~= "" and password ~= nil and username ~= "" and username ~= nil and not bRegisteredOnce[source]) then
                local accountAdded = addAccount(username,password)
                if(accountAdded) then
                        outputChatBox("Thank you " .. getPlayerName(source) .. ", you're now registed, you can login with /login",source)
                        bRegisteredOnce[source] = true
                else
                        outputChatBox("Error creating account, contact the server admin.",source)
                end
        else
                if bRegisteredOnce[source] == true then
                    outputChatBox("You already registered on this server!",source)
                else
                    outputChatBox("Error creating account, correct syntax: /register <nick> <pass>",source)
                end
        end
end
```

## See Also

- addAccount

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
