---
doc_id: "mta-wiki:13442"
title: "Moduły/Gniazda/sockWrite"
source_title: "Moduły/Gniazda/sockWrite"
source_url: "https://wiki.multitheftauto.com/wiki/Modu%C5%82y/Gniazda/sockWrite"
revision_id: 73415
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.429817+00:00"
---

# Moduły/Gniazda/sockWrite

|  | Ta funkcja/zdarzenie jest dostarczana przez zewnętrzny moduł Gniazd . Musisz go zainstalować aby jej używać. |
| --- | --- |
|  |  |

Ta funkcja wysyła dane do gniazda.

## Składnia

```
bool sockWrite ( socket gniazdo, string data)
```

### Wymagane argumenty

- **gniazdo:** Gniazdo, do którego chcesz wysłać dane.

- **data:** Dane, które chcesz wysłać.

### Zwraca

Zwraca wartość true, jeśli dane zostały wysłane, w przeciwnym razie zwraca false.

## Przykład

Poniższy kod łączy się z serwerem IRC "irc.gtanet.com", wchodzi na kanał #mta i wychodzi po 10 sekundach.

```
local gniazdo = sockOpen('irc.gtanet.com',6667)

addEventHandler('onSockOpened',root,function(socket)
   if socket == gniazdo then
      sockWrite(socket,'USER mta mta * :Bot\r\n')
      sockWrite(socket,'NICK mta\r\n')
      sockWrite(socket,'JOIN #mta\r\n')

      outputServerLog('Połączono z serwerem IRC!')
      setTimer(sockClose,10000,1,gniazdo)
   end
end)

addEventHandler('onSockData',root,function(socket, data)
   if socket == gniazdo then
      outputServerLog('Dane z socketu:',data)
   end
end)

addEventHandler('onSockClosed',root,function(socket)
   if socket == gniazdo then
      outputServerLog('Rozłączono z serwerem IRC!')
   end
end)
```

## Zobacz także

### Funkcje

- [sockOpen](https://wiki.multitheftauto.com/wiki/PL/Modules/Sockets/sockOpen)

- [sockWrite](https://wiki.multitheftauto.com/wiki/PL/Modules/Sockets/sockWrite)

- [sockClose](https://wiki.multitheftauto.com/wiki/PL/Modules/Sockets/sockClose)

### Zdarzenia

- [onSockOpened](https://wiki.multitheftauto.com/index.php?title=PL/Modules/Sockets/onSockOpened&action=edit&redlink=1)

- [onSockData](https://wiki.multitheftauto.com/index.php?title=PL/Modules/Sockets/onSockData&action=edit&redlink=1)

- [onSockClosed](https://wiki.multitheftauto.com/index.php?title=PL/Modules/Sockets/onSockClosed&action=edit&redlink=1)
