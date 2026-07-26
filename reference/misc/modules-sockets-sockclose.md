---
doc_id: "mta-wiki:5179"
title: "Modules/Sockets/sockClose"
source_title: "Modules/Sockets/sockClose"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Sockets/sockClose"
revision_id: 23394
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.277849+00:00"
---

# Modules/Sockets/sockClose

|  | This function is provided by the external module Sockets . You must install this module to use this function. |
| --- | --- |
|  |  |

This function destroys a socket.

## Syntax

```
bool sockClose ( socket theSocket )
```

### Required arguments

- **theSocket:** The socket to close

### Returns

Returns *a boolean* true if the socket was closed, false otherwise.

## Example

This piece of code connects to irc.gtanet.com, joins #mta and quits in 10 seconds.

```
local root = getRootElement()
local ircSocket = sockOpen("irc.gtanet.com",6667)

addEventHandler("onSockOpened",root,
   function (socket)
      if socket == ircSocket then
         sockWrite(socket,"USER mta mta * :Bot\r\n")
         sockWrite(socket,"NICK mta\r\n")
         sockWrite(socket,"JOIN #mta\r\n")

         outputServerLog("IRC: Connected!")
         setTimer(disconnect,10000,1)
      end
   end
)

addEventHandler("onSockData",root,
   function (socket,data)
      if socket == ircSocket then
         outputServerLog(data)
      end
   end
)

addEventHandler("onSockClosed",root,
   function (socket)
      if socket == ircSocket then
         outputServerLog("IRC: disconnected!")
      end
   end
)

function disconnect ()
   sockClose(ircSocket)
end
```

## See Also

### Functions

- [sockOpen](mta://reference/misc/modules-sockets-sockopen.md)

- [sockWrite](mta://reference/misc/modules-sockets-sockwrite.md)

- sockClose

### Events

- [onSockOpened](mta://reference/misc/modules-sockets-onsockopened.md)

- [onSockData](mta://reference/misc/modules-sockets-onsockdata.md)

- [onSockClosed](mta://reference/misc/modules-sockets-onsockclosed.md)
