---
doc_id: "mta-wiki:4929"
title: "Modules/SebasIRC/ircNotice"
source_title: "Modules/SebasIRC/ircNotice"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/ircNotice"
revision_id: 48372
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.093524+00:00"
---

# Modules/SebasIRC/ircNotice

|  | This function is provided by the external module SebasIRC . You must install this module to use this function. |
| --- | --- |
|  |  |

Sends a message to a Player

## Syntax

```
bool ircNotice(string user , string text)
```

### Required arguments

- **user:** Player name.

- **text:** The Text.

### Returns

True if joined, otherwise false.

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

- ircNotice

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
