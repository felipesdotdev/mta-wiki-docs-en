---
doc_id: "mta-wiki:1790"
title: "GetClientIP"
source_title: "GetClientIP"
source_url: "https://wiki.multitheftauto.com/wiki/GetClientIP"
revision_id: 44579
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GetClientIP

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPlayerIP instead. |  |

This function returns a string containing the IP address of the client.

## Syntax

```
string getClientIP ( client theClient )
```

### Required Arguments

- **theClient:** The client [element](mta://reference/misc/element.md) (player or admin) you want to get the IP of.

### Returns

Returns a string containing the requested client's IP, or *false* if the client passed to the function is invalid.

## Example

This example prints a player's IP to the chat.

```
function printIP ( thePlayer, command )
	outputChatBox ( getClientName ( thePlayer ) .. "'s IP is: " .. getClientIP ( thePlayer ) )
end
addCommandHandler ( "ip", printIP )
```

## See Also

BEFORE VERSION 1.0 :

- [getClientAccount](mta://scripting/server/functions/getclientaccount.md)

- getClientIP

- [getClientName](mta://scripting/server/functions/getclientname.md)

- [setClientName](mta://scripting/server/functions/setclientname.md)
