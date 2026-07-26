---
doc_id: "mta-wiki:13436"
title: "Moduły/Gniazda/sockOpen"
source_title: "Moduły/Gniazda/sockOpen"
source_url: "https://wiki.multitheftauto.com/wiki/Modu%C5%82y/Gniazda/sockOpen"
revision_id: 73389
language: "en"
categories: []
---

# Moduły/Gniazda/sockOpen

|  | Ta funkcja/zdarzenie jest dostarczana przez zewnętrzny moduł Gniazd . Musisz go zainstalować aby jej używać. |
| --- | --- |
|  |  |

Ta funkcja tworzy gniazdo (tzw *socket*)

## Składnia

```
socket sockOpen ( string host, int port )
```

### Wymagane argumenty

- **host:** Nazwa DNS lub adres IP, z którym chcesz się połączyć np. "www.google.com" lub "192.168.0.101"

- **port:** Port do powiązania gniazda np. 80

### Zwraca

Zwraca *userdatę*, która reprezentuje gniazdo jeśli podano poprawne argumenty. W przeciwnym wypadku zwróci *fałsz*.

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
