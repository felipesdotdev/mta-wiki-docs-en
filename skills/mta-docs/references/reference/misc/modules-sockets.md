---
doc_id: "mta-wiki:4894"
title: "Modules/Sockets"
source_title: "Modules/Sockets"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Sockets"
revision_id: 73383
language: "en"
categories: ["Modules"]
---

# Modules/Sockets

| Module info |  |
| --- | --- |
| Name | ml_sockets |
| Version | 1.4 |
| Author | Gamesnert, x86 & MCvarial |
| Module website | Here |
| Download link | Windows 32 bit Windows 64 bit Linux 32 bit Linux 64 bit |
| License | GPLv3 |
| Written in | C++ |
| Operating system | Cross-platform |
| Compatible with | 1.x |

This module provides socket related functions and events for MTA:SA.
Sockets provide various possibilities such as opening a webpage, connecting to irc etc.

## Installation

### Windows

**32 bit:** Copy 32 bit ml_sockets.dll into the **MTA San Andreas\server\mods\deathmatch\modules\** directory.

**64 bit:** Copy 64 bit ml_sockets.dll into the **MTA San Andreas\server\x64\modules\** directory.

Then, add the following line in mtaserver.conf:

```
<module src="ml_sockets.dll" />
```

### GNU/Linux

**32 bit:** Copy 32 bit ml_sockets.so into the **mods/deathmatch/modules/** directory.

**64 bit:** Copy 64 bit ml_sockets.so into the **x64/modules/** directory.

Then, add the following line in mtaserver.conf:

```
<module src="ml_sockets.so" />
```

## See Also

### Functions

- [sockOpen](mta://reference/misc/modules-sockets-sockopen.md)

- [sockWrite](mta://reference/misc/modules-sockets-sockwrite.md)

- [sockClose](mta://reference/misc/modules-sockets-sockclose.md)

### Events

- [onSockOpened](mta://reference/misc/modules-sockets-onsockopened.md)

- [onSockData](mta://reference/misc/modules-sockets-onsockdata.md)

- [onSockClosed](mta://reference/misc/modules-sockets-onsockclosed.md)

### Resources

- [resource:irc](mta://resources/irc.md)
