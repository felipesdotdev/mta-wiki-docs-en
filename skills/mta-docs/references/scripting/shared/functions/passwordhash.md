---
doc_id: "mta-wiki:9312"
title: "PasswordHash"
source_title: "PasswordHash"
source_url: "https://wiki.multitheftauto.com/wiki/PasswordHash"
revision_id: 74671
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.4"]
---

# PasswordHash

| [[{{{image}}}\|link=\|]] | Note: Using passwordHash is the recommended way of storing passwords. |
| --- | --- |
|  |  |

This function creates a new password hash using a specified hashing algorithm.

| [[\|link=\|]] | Warning: It is strongly recommended to use the async version of the function (i.e. provide a callback function). Otherwise, you will experience short freezes due to the slow nature of the bcrypt algorithm |
| --- | --- |
|  |  |

## Syntax

```
string passwordHash ( string password, string algorithm, table options [, function callback ] )
```

### Required Arguments

- **password:** The password to hash.

- **algorithm:** The algorithm to use:

- *bcrypt*: use the bcrypt hashing algorithm. Hash length: 60 characters. Note that only the prefix *$2y$* is supported (older prefixes can cause security issues).

- **options:** table with options for the hashing algorithm, as detailed below.

### Optional Arguments

- **callback:** providing a callback will run this function asynchronously, the arguments to the callback are the same as the returned values below.

### Options for each hashing algorithm

- *bcrypt*:

- *cost* (int), default: 10.  Visit [this link](http://security.stackexchange.com/questions/17207/recommended-of-rounds-for-bcrypt) to determine the number of rounds appropriate for your server.

- *salt* (string), default: empty string

- an empty string will automatically generate a salt with the *cost* provided

- **deprecated**: if a string is provided, it will be used as a salt (**do not do this!**)

- the provided string should be longer than or equal to 22 characters

### Returns

Returns the hash as a string if hashing was successful, *false* otherwise. If a callback was provided, the aforementioned values are arguments to the callback, and this function will always return *true*.

## Example

| [[\|link=\|]] | Warning: If you will be using "Example 1" then you will have to save account data "hash_password" after server restart, otherwise this script will no longer work. |
| --- | --- |
|  |  |

This example makes use of [passwordHash](https://wiki.multitheftauto.com/wiki/PasswordHash) and [passwordVerify](https://wiki.multitheftauto.com/wiki/PasswordVerify) in account creation and account login to boost up security.

Click to collapse [-]
Example 1

- Use **/accountCreate [username] [password]** to create an account.

- Use **/accountLogin [username] [password]** to login in account.

```
-- lets add command handler that will handle the account creation
addCommandHandler("accountCreate",function(source,cmd,username,password)
	if (username and password) then
		local hashedPassword = passwordHash(password,"bcrypt",{}) -- create new hash for password
		if (hashedPassword) then -- check if hash has been generated
			local account = addAccount(username,hashedPassword) -- now lets add account with new hash what we got when we made it for password.
			if (account) then
				setAccountData(account,"hash_password",hashedPassword) -- store accounts password hash in order to verify it when it's needed.
				outputChatBox("Account successfuly created! Now please login. Syntax </accountLogin [username] [password]>",source,20,160,20)
			else
				outputChatBox("Account already exists! Please try again with different username.",source,20,160,20)
			end
		else
			outputChatBox("Securing your password failed! Please try again or contact an administrator.",source,160,20,20)
		end
	else
		outputChatBox("Wrong parameters! Correct Syntax </accountCreate [username] [password]>",source,160,20,20)
	end
end);

-- lets add command handler that will handle the account login
addCommandHandler("accountLogin",function(source,cmd,username,password)
	if (username and password) then
		local account = getAccount(username) -- get entered account
		if (account) then -- check if entered account exists
			local hashedPassword = getAccountData(account,"hash_password") -- lets get hashed password
			if (passwordVerify(password,hashedPassword)) then -- check if hash and entered password matches
				if logIn(source,account,hashedPassword) then -- now lets login player into account
					outputChatBox("Login successfull. Welcome, "..getAccountName(account).."!",source,20,160,20)
				end
			else
				outputChatBox("Password is incorrect!",source,160,20,20)
			end
		else
			outputChatBox("Account doesn't exist! Please try again with different account.",source,160,20,20)
		end
	else
		outputChatBox("Wrong parameters! Correct Syntax </accountLogin [username] [password]>",source,160,20,20)
	end
end);
```

## See Also

- [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- [decodeString](mta://scripting/shared/functions/decodestring.md)

- [encodeString](mta://scripting/shared/functions/encodestring.md)

- [fromJSON](mta://scripting/shared/functions/fromjson.md)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- [getColorFromString](mta://scripting/shared/functions/getcolorfromstring.md)

- [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md)

- [getDistanceBetweenPoints2D](mta://scripting/shared/functions/getdistancebetweenpoints2d.md)

- [getDistanceBetweenPoints3D](mta://scripting/shared/functions/getdistancebetweenpoints3d.md)

- [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md)

- [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md)

- [getNetworkUsageData](mta://scripting/shared/functions/getnetworkusagedata.md)

- [getPerformanceStats](mta://scripting/shared/functions/getperformancestats.md)

- [getRealTime](mta://scripting/shared/functions/getrealtime.md)

- [getTickCount](mta://scripting/shared/functions/gettickcount.md)

- [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md)

- [getTimers](mta://scripting/shared/functions/gettimers.md)

- [getFPSLimit](mta://scripting/shared/functions/getfpslimit.md)

- [getUserdataType](mta://scripting/shared/functions/getuserdatatype.md)

- [getVersion](mta://scripting/shared/functions/getversion.md)

- [gettok](mta://scripting/shared/functions/gettok.md)

- [isTransferBoxVisible](mta://scripting/shared/functions/istransferboxvisible.md)

- [setTransferBoxVisible](mta://scripting/shared/functions/settransferboxvisible.md)

- [hash](mta://scripting/shared/functions/hash.md)

- [inspect](mta://scripting/shared/functions/inspect.md)

- [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md)

- [iprint](mta://scripting/shared/functions/iprint.md)

- [isOOPEnabled](mta://scripting/shared/functions/isoopenabled.md)

- [isTimer](mta://scripting/shared/functions/istimer.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22701](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22701):

- [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md)

- [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md)

- [killTimer](mta://scripting/shared/functions/killtimer.md)

- [md5](mta://scripting/shared/functions/md5.md)

- passwordHash

- [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

- [pregFind](https://wiki.multitheftauto.com/index.php?search=pregFind)

- [pregMatch](mta://scripting/shared/functions/pregmatch.md)

- [pregReplace](mta://scripting/shared/functions/pregreplace.md)

- [removeDebugHook](mta://scripting/shared/functions/removedebughook.md)

- [resetTimer](mta://scripting/shared/functions/resettimer.md)

- [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md)

- [setFPSLimit](mta://scripting/shared/functions/setfpslimit.md)

- [setTimer](mta://scripting/shared/functions/settimer.md)

- [ref](mta://scripting/shared/functions/ref.md)

- [deref](mta://scripting/shared/functions/deref.md)

- [sha256](mta://scripting/shared/functions/sha256.md)

- [split](mta://scripting/shared/functions/split.md)

- [teaDecode](mta://scripting/shared/functions/teadecode.md)

- [teaEncode](mta://scripting/shared/functions/teaencode.md)

- [toJSON](mta://scripting/shared/functions/tojson.md)

- [tocolor](mta://scripting/shared/functions/tocolor.md)

- [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md)

- [utfChar](mta://scripting/shared/functions/utfchar.md)

- [utfCode](mta://scripting/shared/functions/utfcode.md)

- [utfLen](https://wiki.multitheftauto.com/index.php?search=utfLen)

- [utfSeek](mta://scripting/shared/functions/utfseek.md)

- [utfSub](mta://scripting/shared/functions/utfsub.md)

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
