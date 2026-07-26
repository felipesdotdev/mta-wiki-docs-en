---
doc_id: "mta-wiki:4847"
title: "Modules/bIRC/ircbot"
source_title: "Modules/bIRC/ircbot"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircbot"
revision_id: 20888
language: "en"
categories: []
---

# Modules/bIRC/ircbot

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

The ircbots are the main "elements" of the Basic IRC module. They are used in almost every function the module provides and they do the echoing between IRC and MTA server. There are various functions and callbacks to manipulate their actions. This way the server controller will have a full control over the IRC echoing system.

The ircbots can be created with function [ircCreateBot](mta://reference/misc/modules-birc-irccreatebot.md) and can be destroyed using function [ircDestroyBot](mta://reference/misc/modules-birc-ircdestroybot.md).

## Related Scripting Functions

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
