---
doc_id: "mta-wiki:4838"
title: "Modules/SebasIRC/ircChangeNick"
source_title: "Modules/SebasIRC/ircChangeNick"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/ircChangeNick"
revision_id: 48377
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.005468+00:00"
---

# Modules/SebasIRC/ircChangeNick

|  | This function is provided by the external module SebasIRC . You must install this module to use this function. |
| --- | --- |
|  |  |

## **WARNING:** This function is disabled in the ml_irc-rewrite branch!

Changes the name of your bot.

## Syntax

```
bool ircChangeNick(string newNick)
```

### Required arguments

- **newNick:** How you want your bot to be called.

### Returns

Returns true if the nick was changed successfully, false otherwise.

## Example

```
-- Example here
```

## See also

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

- ircChangeNick

- [ircRaw](mta://reference/misc/modules-sebasirc-ircraw.md)
