---
doc_id: "mta-wiki:5177"
title: "Modules/Sockets/sockOpen"
source_title: "Modules/Sockets/sockOpen"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Sockets/sockOpen"
revision_id: 73391
language: "en"
categories: []
generated_at: "2026-07-26T16:11:19.697907+00:00"
---

# Modules/Sockets/sockOpen

|  | This function is provided by the external module Sockets . You must install this module to use this function. |
| --- | --- |
|  |  |

This function creates a socket.

## Syntax

```
socket sockOpen ( string hostname, int port )
```

### Required arguments

- **hostname:** The DNS or IP to connect to e.g. "www.google.com"

- **port:** The port to bind the socket to e.g. 80

### Returns

Returns *userdata* that represents the socket if you correct arguments were given, *false* otherwise.

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

- sockOpen

- [sockWrite](mta://reference/misc/modules-sockets-sockwrite.md)

- [sockClose](mta://reference/misc/modules-sockets-sockclose.md)

### Events

- [onSockOpened](mta://reference/misc/modules-sockets-onsockopened.md)

- [onSockData](mta://reference/misc/modules-sockets-onsockdata.md)

- [onSockClosed](mta://reference/misc/modules-sockets-onsockclosed.md)
