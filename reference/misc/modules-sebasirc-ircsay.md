---
doc_id: "mta-wiki:4835"
title: "Modules/SebasIRC/ircSay"
source_title: "Modules/SebasIRC/ircSay"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/ircSay"
revision_id: 48368
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.142175+00:00"
---

# Modules/SebasIRC/ircSay

|  | This function is provided by the external module SebasIRC . You must install this module to use this function. |
| --- | --- |
|  |  |

Sends a message to the channel or a nickname

## Syntax

```
bool ircSay(string to, string message)
```

### Required arguments

- **to:** The channel name, or a nickname.

- **message:** The message to send..

### Returns

Returns true, otherwise false when giving wrong arguments.

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

- ircSay

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
