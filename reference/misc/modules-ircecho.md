---
doc_id: "mta-wiki:3582"
title: "Modules/IRCEcho"
source_title: "Modules/IRCEcho"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/IRCEcho"
revision_id: 36431
language: "en"
categories: ["Outdated_Pages"]
generated_at: "2026-07-26T16:16:12.777660+00:00"
---

# Modules/IRCEcho

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
| Reason: This module only works on DP2.3, use resource:irc for now |  |

| Module info |  |
| --- | --- |
| Name | MTASA IRC Echo |
| Version | 2.1 |
| Author | VRocker |
| Module website | Not available |
| Download link | Here |
| License | Unlicensed |
| Written in | C++ |
| Operating system | Cross-platform |
| Compatible with | DP2.3 |

MTASA IRC Echo is a module that provides an IRC echo for an MTASA server. It is available for both Windows and Linux.

## Installation

### Windows

Uncompress the file ml_ircecho.dll into your *%PROGRAMFILES%\MTA San Andreas\server\mods\deathmatch\modules\* directory.

Then, add the following line in mtaserver.conf:

```
<module src="ml_ircecho.dll" />
```

### Linux

Uncompress the file ml_ircecho.so into your *%MTASERVER%\mods\deathmatch\modules\* directory.

Then, add the following line in mtaserver.conf:

```
<module src="ml_ircecho.so" />
```

## Functions

- [ircInit](mta://reference/misc/modules-ircecho-ircinit.md)

- [ircOpen](mta://reference/misc/modules-ircecho-ircopen.md)

- [ircDisconnect](mta://reference/misc/modules-ircecho-ircdisconnect.md)

- [ircMessage](mta://reference/misc/modules-ircecho-ircmessage.md)

- [ircNotice](mta://reference/misc/modules-ircecho-ircnotice.md)

- [ircChangeNick](mta://reference/misc/modules-ircecho-ircchangenick.md)

- [ircJoin](mta://reference/misc/modules-ircecho-ircjoin.md)

- [ircPart](mta://reference/misc/modules-ircecho-ircpart.md)

- [ircRaw](mta://reference/misc/modules-ircecho-ircraw.md)

- [ircIsVoice](mta://reference/misc/modules-ircecho-ircisvoice.md)

- [ircIsHalfop](mta://reference/misc/modules-ircecho-ircishalfop.md)

- [ircIsOp](mta://reference/misc/modules-ircecho-ircisop.md)

- [ircIsSuper](mta://reference/misc/modules-ircecho-ircissuper.md)

- [ircIsOwner](mta://reference/misc/modules-ircecho-ircisowner.md)

- [ircGetStatus](mta://reference/misc/modules-ircecho-ircgetstatus.md)

## Callbacks

- [irc_onConnecting](mta://reference/misc/modules-ircecho-irc-onconnecting.md)

- [irc_onConnected](mta://reference/misc/modules-ircecho-irc-onconnected.md)

- [irc_onDisconnected](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onDisconnected&action=edit&redlink=1)

- [irc_onFailedConnection](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onFailedConnection&action=edit&redlink=1)

- [irc_onPrivMsg](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onPrivMsg&action=edit&redlink=1)

- [irc_onNotice](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onNotice&action=edit&redlink=1)

- [irc_onJoin](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onJoin&action=edit&redlink=1)

- [irc_onPart](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onPart&action=edit&redlink=1)

- [irc_onQuit](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onQuit&action=edit&redlink=1)

- [irc_onNickChange](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onNickChange&action=edit&redlink=1)

- [irc_onRaw](https://wiki.multitheftauto.com/index.php?title=Modules/IRCEcho/irc_onRaw&action=edit&redlink=1)
