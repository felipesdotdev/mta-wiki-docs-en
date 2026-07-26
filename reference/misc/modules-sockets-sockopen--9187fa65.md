---
doc_id: "mta-wiki:5176"
title: "Modules/sockets/sockOpen"
source_title: "Modules/sockets/sockOpen"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/sockets/sockOpen"
revision_id: 23045
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.344192+00:00"
---

# Modules/sockets/sockOpen

|  | This function is provided by the external module Sockets . You must install this module to use this function. |
| --- | --- |
|  |  |

This function creates a socket.

## Syntax

```
socket sockOpen ( string hostname, int port)
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
         sockWrite(socket,"USER mta mta * MCvarial & Gamesnert")
         sockWrite(socket,"NICK mta")
         sockWrite(socket,"JOIN #mta")

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

## See also

- [sockOpen](mta://reference/misc/modules-sockets-sockopen.md)

- [sockWrite](mta://reference/misc/modules-sockets-sockwrite.md)

- [sockClose](mta://reference/misc/modules-sockets-sockclose.md)
