---
doc_id: "mta-wiki:5181"
title: "Modules/Sockets/onSockData"
source_title: "Modules/Sockets/onSockData"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Sockets/onSockData"
revision_id: 23445
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.192008+00:00"
---

# Modules/Sockets/onSockData

|  | This function is provided by the external module Sockets . You must install this module to use this function. |
| --- | --- |
|  |  |

This event is triggered when data is received on a socket.

### Parameters

```
userdata socket, string data
```

- **socket**: userdata representing a socket.

- **data**: a string with the data that was received.

### Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](mta://reference/misc/root-element.md).

## Example

This piece of code connects to irc.gtanet.com, joins #mta and quits in 10 seconds.

```
local root = getRootElement()
local ircSocket = sockOpen("irc.gtanet.com",6667)

addEventHandler("onSockOpened",root,
   function (socket)
      if socket == ircSocket then
         sockWrite(socket,"USER mta mta * :MCvarial & Gamesnert\r\n")
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

- [sockClose](mta://reference/misc/modules-sockets-sockclose.md)

### Events

- [onSockOpened](mta://reference/misc/modules-sockets-onsockopened.md)

- onSockData

- [onSockClosed](mta://reference/misc/modules-sockets-onsockclosed.md)
