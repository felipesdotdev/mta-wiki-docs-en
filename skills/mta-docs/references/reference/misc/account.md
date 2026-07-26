---
doc_id: "mta-wiki:1793"
title: "Account"
source_title: "Account"
source_url: "https://wiki.multitheftauto.com/wiki/Account"
revision_id: 82752
language: "en"
categories: ["Scripting_Concepts"]
---

# Account

The account class represents a [player](https://wiki.multitheftauto.com/index.php?search=player)'s server account. You can get the account object associated to any client using [getPlayerAccount](mta://scripting/server/functions/getplayeraccount.md).

Accounts are unique to each client and can be used to store information that is persistent across map changes and user sessions. Clients that join without an account are given a temporary 'guest' account. This can store information like any other account, but isn't saved across sessions.

When a user logs in or out, the account object assigned to them will change. As such, you must not assume that the account attached to a client remains constant during their session.

PHP code to check password hashes from the MTA server database is [here.](mta://reference/misc/account-php.md)

## Related scripting functions

### Server

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

- [getAccountsByIP](mta://scripting/server/functions/getaccountsbyip.md)

- [setAccountName](mta://scripting/server/functions/setaccountname.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [getAccountType](mta://scripting/server/functions/getaccounttype.md)
