---
doc_id: "mta-wiki:1792"
title: "GetClientAccount"
source_title: "GetClientAccount"
source_url: "https://wiki.multitheftauto.com/wiki/GetClientAccount"
revision_id: 44571
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GetClientAccount

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPlayerAccount instead. |  |

This function returns the specified client's [account](mta://reference/misc/account.md) object.

## Syntax

```
account getClientAccount ( client theClient )
```

### Required Arguments

- **theClient:** The client [element](mta://reference/misc/element.md) (player or admin) you want to get the account of.

### Returns

Returns the client's account object, or *false* if the client passed to the function is invalid.

## Example

This example sets a player's money and also stores the value is his account.

```
function setMoney ( thePlayer, key, amount )
	setPlayerMoney ( thePlayer, amount )
	account = getClientAccount ( thePlayer )
	if ( account ) then
		setAccountData ( account, "money", amount )
	end
end
addCommandHandler ( "setmoney", setMoney )
```

## See Also

BEFORE VERSION 1.0 :

- getClientAccount

- [getClientIP](mta://scripting/server/functions/getclientip.md)

- [getClientName](mta://scripting/server/functions/getclientname.md)

- [setClientName](mta://scripting/server/functions/setclientname.md)
