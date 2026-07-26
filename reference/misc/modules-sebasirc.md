---
doc_id: "mta-wiki:4514"
title: "Modules/SebasIRC"
source_title: "Modules/SebasIRC"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC"
revision_id: 48389
language: "en"
categories: ["Outdated_Pages"]
generated_at: "2026-07-26T16:16:13.978644+00:00"
---

# Modules/SebasIRC

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
| Reason: Development for this module has stopped, use resource:irc instead. |  |

| Module info |  |
| --- | --- |
| Name | ml_irc |
| Version | 1.0 |
| Author | x86 <sebasdevelopment@gmx.com> |
| Module website | Here |
| Download link | Here |
| License | Unlicensed |
| Written in | C++ |
| Operating system | Windows |
| Compatible with | MTA SA 1.x.x |

This ml_irc is a module for your MTA:SA 1.x Windows server, that provides IRC echo.

- **Note:** The bot can't join multiple servers.

## Installation

### Windows

Uncompress the file ml_irc.dll into your *server\mods\deathmatch\modules\* directory.

### mtaserver.conf

Add the following line in your mtaserver.conf:

```
<module src="ml_irc" />
```

## See Also

### Functions

### Connection:

- [ircConnect](mta://reference/misc/modules-sebasirc-ircconnect.md)

- [ircDisconnect](mta://reference/misc/modules-sebasirc-ircdisconnect.md)

- [ircIsConnected](mta://reference/misc/modules-sebasirc-ircisconnected.md)

### Channel:

- [ircJoin](mta://reference/misc/modules-sebasirc-ircjoin.md)

- [ircPart](mta://reference/misc/modules-sebasirc-ircpart.md)

- [ircSay](mta://reference/misc/modules-sebasirc-ircsay.md)

- [ircNotice](mta://reference/misc/modules-sebasirc-ircnotice.md)

- [ircInvite](https://wiki.multitheftauto.com/index.php?title=Modules/SebasIRC/ircInvite&action=edit&redlink=1)

- [ircSetChannelMode](mta://reference/misc/modules-sebasirc-ircsetchannelmode.md)

- [ircGetChannelModes](https://wiki.multitheftauto.com/index.php?title=Modules/SebasIRC/ircGetChannelModes&action=edit&redlink=1)

- [ircSetChannelTopic](https://wiki.multitheftauto.com/index.php?title=Modules/SebasIRC/ircSetChannelTopic&action=edit&redlink=1)

- [ircGetChannelTopic](https://wiki.multitheftauto.com/index.php?title=Modules/SebasIRC/ircGetChannelTopic&action=edit&redlink=1)

### Bot:

- [ircSetMode](https://wiki.multitheftauto.com/index.php?title=Modules/SebasIRC/ircSetMode&action=edit&redlink=1)

- [ircGetModes](https://wiki.multitheftauto.com/index.php?title=Modules/SebasIRC/ircGetModes&action=edit&redlink=1)

- [ircChangeNick](mta://reference/misc/modules-sebasirc-ircchangenick.md)

- [ircRaw](mta://reference/misc/modules-sebasirc-ircraw.md)

### Events

- [onIRCRaw](mta://reference/misc/modules-sebasirc-onircraw.md)

**There are no more events, more events are made in lua with onIRCRaw so that you can create your own syntax.**
