---
doc_id: "mta-wiki:12720"
title: "账户"
source_title: "账户"
source_url: "https://wiki.multitheftauto.com/wiki/%E8%B4%A6%E6%88%B7"
revision_id: 69285
language: "en"
categories: ["Translated/Scripting_Concepts"]
generated_at: "2026-07-26T16:16:58.275256+00:00"
---

# 账户

账户类表示[玩家](https://wiki.multitheftauto.com/index.php?title=%E7%8E%A9%E5%AE%B6&action=edit&redlink=1)的服务器帐户。您可以使用[getPlayerAccount](mta://scripting/server/functions/getplayeraccount.md)获取与任何客户端关联的账户对象.

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
