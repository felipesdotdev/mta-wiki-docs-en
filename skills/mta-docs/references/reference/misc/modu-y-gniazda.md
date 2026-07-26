---
doc_id: "mta-wiki:13435"
title: "Moduły/Gniazda"
source_title: "Moduły/Gniazda"
source_url: "https://wiki.multitheftauto.com/wiki/Modu%C5%82y/Gniazda"
revision_id: 73384
language: "en"
categories: ["Modules"]
---

# Moduły/Gniazda

| Informacje o module |  |
| --- | --- |
| Nazwa | ml_sockets |
| Wersja | 1.4 |
| Autor | Gamesnert, x86 & MCvarial |
| Strona internetowa modułu | Tutaj |
| Link do pobrania | Windows 32 bit Windows 64 bit Linux 32 bit Linux 64 bit |
| Licencja | GPLv3 |
| Napisany w | C++ |
| System operacyjny | Wieloplatformowy |
| Kompatybilny z | 1.x |

Ten moduł udostępnia funkcje i zdarzenia związane z gniazdami dla MTA:SA.
Gniazda dają różne możliwości, takie jak otwieranie strony internetowej, łączenie się z irc itp.

## Instalacja

### Windows

**32 bit:** Skopiuj 32 bitowy plik ml_sockets.dll do katalogu **MTA San Andreas\server\mods\deathmatch\modules\**

**64 bit:** Skopiuj 64 bitowy plik ml_sockets.dll do katalogu **MTA San Andreas\server\x64\modules\**

Następnie dodaj poniższy wiersz do pliku konfiguracyjnego mtaserver.conf:

```
<module src="ml_sockets.dll" />
```

### GNU/Linux

**32 bit:** Skopiuj 32 bitowy plik ml_sockets.so do katalogu **mods/deathmatch/modules/**

**64 bit:** Skopiuj 64 bitowy plik ml_sockets.so do katalogu **x64/modules/**

Następnie dodaj poniższy wiersz do pliku konfiguracyjnego mtaserver.conf:

```
<module src="ml_sockets.so" />
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

### Inne moduły

- [irc](mta://resources/irc.md)
