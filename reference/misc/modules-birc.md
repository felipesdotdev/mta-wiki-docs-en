---
doc_id: "mta-wiki:4841"
title: "Modules/bIRC"
source_title: "Modules/bIRC"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC"
revision_id: 49251
language: "en"
categories: ["Outdated_Pages"]
generated_at: "2026-07-26T16:16:14.408011+00:00"
---

# Modules/bIRC

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
| Reason: Development for this module seems to have halted, use resource:irc for now. |  |

| Module info |  |
| --- | --- |
| Name | ml_birc |
| Version | 1.0 |
| Author | Awwu <awwugta@gmail.com> |
| Module website | None |
| Download link | Soon |
| License | Unlicensed |
| Written in | Unknown |
| Operating system | Windows only |
| Compatible with | 1.0 |

Basic IRC module (bIRC) provides a fully functional server IRC echo for MTA:SA. It is currently available only for Windows servers on MTA:SA 1.0 (other versions untested).

## Installation

Uncompress the file ml_birc.dll into your *server\mods\deathmatch\modules\* directory.

### mtaserver.conf

Add the following line in your mtaserver.conf:

```
<module src="ml_birc" />
```

## Provided scripting functionality

### Bot functions

#### Creation

- [ircCreateBot](mta://reference/misc/modules-birc-irccreatebot.md)

- [ircDestroyBot](mta://reference/misc/modules-birc-ircdestroybot.md)

#### Connection

- [ircConnect](mta://reference/misc/modules-birc-ircconnect.md)

- [ircIsConnected](mta://reference/misc/modules-birc-ircisconnected.md)

- [ircRegister](mta://reference/misc/modules-birc-ircregister.md)

- [ircUnregister](mta://reference/misc/modules-birc-ircunregister.md)

- [ircQuit](mta://reference/misc/modules-birc-ircquit.md)

#### Other

- [ircGetBotByName](mta://reference/misc/modules-birc-ircgetbotbyname.md)

- [ircGetBots](mta://reference/misc/modules-birc-ircgetbots.md)

- [ircGetBotState](mta://reference/misc/modules-birc-ircgetbotstate.md)

- [ircGetName](mta://reference/misc/modules-birc-ircgetname.md)

- [ircGetQuitMessage](mta://reference/misc/modules-birc-ircgetquitmessage.md)

- [ircSetName](mta://reference/misc/modules-birc-ircsetname.md)

- [ircSetQuitMessage](mta://reference/misc/modules-birc-ircsetquitmessage.md)

### IRC functions

#### Channel

- [ircGetChannelMode](mta://reference/misc/modules-birc-ircgetchannelmode.md)

- [ircGetChannelTopic](mta://reference/misc/modules-birc-ircgetchanneltopic.md)

- [ircGetChannelUsers](mta://reference/misc/modules-birc-ircgetchannelusers.md)

- [ircGetConnectedChannels](mta://reference/misc/modules-birc-ircgetconnectedchannels.md)

- [ircJoinChannel](mta://reference/misc/modules-birc-ircjoinchannel.md)

- [ircPartChannel](mta://reference/misc/modules-birc-ircpartchannel.md)

- [ircSetChannelMode](mta://reference/misc/modules-birc-ircsetchannelmode.md)

- [ircSetChannelTopic](mta://reference/misc/modules-birc-ircsetchanneltopic.md)

#### User

- [ircGetUserHost](mta://reference/misc/modules-birc-ircgetuserhost.md)

- [ircGetUserMode](mta://reference/misc/modules-birc-ircgetusermode.md)

- [ircIsInChannel](mta://reference/misc/modules-birc-ircisinchannel.md)

#### Communication

- [ircBan](mta://reference/misc/modules-birc-ircban.md)

- [ircInviteUser](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircInviteUser&action=edit&redlink=1)

- [ircKick](mta://reference/misc/modules-birc-irckick.md)

- [ircSendMessage](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendMessage&action=edit&redlink=1)

- [ircSendNotice](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendNotice&action=edit&redlink=1)

- [ircSendRaw](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendRaw&action=edit&redlink=1)

### Other

- [ircFormatHost](mta://reference/misc/modules-birc-ircformathost.md)

- [ircStrip](mta://reference/misc/modules-birc-ircstrip.md)

### Callbacks

- [event_ircOnAction](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnAction&action=edit&redlink=1)

- [event_ircOnCTCP](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnCTCP&action=edit&redlink=1)

- [event_ircOnChannelMode](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnChannelMode&action=edit&redlink=1)

- [event_ircOnConnect](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnConnect&action=edit&redlink=1)

- [event_ircOnDisconnect](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnDisconnect&action=edit&redlink=1)

- [event_ircOnFailedConnection](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnFailedConnection&action=edit&redlink=1)

- [event_ircOnInvite](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnInvite&action=edit&redlink=1)

- [event_ircOnJoinChannel](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnJoinChannel&action=edit&redlink=1)

- [event_ircOnKick](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnKick&action=edit&redlink=1)

- [event_ircOnLostConnection](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnLostConnection&action=edit&redlink=1)

- [event_ircOnNickChange](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnNickChange&action=edit&redlink=1)

- [event_ircOnNotice](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnNotice&action=edit&redlink=1)

- [event_ircOnPartChannel](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnPartChannel&action=edit&redlink=1)

- [event_ircOnPing](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnPing&action=edit&redlink=1)

- [event_ircOnQuit](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnQuit&action=edit&redlink=1)

- [event_ircOnRaw](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnRaw&action=edit&redlink=1)

- [event_ircOnText](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnText&action=edit&redlink=1)

- [event_ircOnTopic](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnTopic&action=edit&redlink=1)
