---
doc_id: "mta-wiki:5178"
title: "Modules/Sockets/sockWrite"
source_title: "Modules/Sockets/sockWrite"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Sockets/sockWrite"
revision_id: 73416
language: "en"
categories: []
---

# Modules/Sockets/sockWrite

|  | This function is provided by the external module Sockets . You must install this module to use this function. |
| --- | --- |
|  |  |

This function writes data to a socket.

## Syntax

```
bool sockWrite ( socket theSocket, string data)
```

### Required arguments

- **theSocket:** The socket to write the data to.

- **data:** The data you wanna send.

### Returns

Returns *a boolean* true if the data was send, false otherwise.

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

- sockWrite

- [sockClose](mta://reference/misc/modules-sockets-sockclose.md)

### Events

- [onSockOpened](mta://reference/misc/modules-sockets-onsockopened.md)

- [onSockData](mta://reference/misc/modules-sockets-onsockdata.md)

- [onSockClosed](mta://reference/misc/modules-sockets-onsockclosed.md)
