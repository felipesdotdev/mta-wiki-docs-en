---
doc_id: "mta-wiki:4837"
title: "Modules/SebasIRC/ircDisconnect"
source_title: "Modules/SebasIRC/ircDisconnect"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/ircDisconnect"
revision_id: 48359
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:16:14.046971+00:00"
---

# Modules/SebasIRC/ircDisconnect

|  | This function is provided by the external module SebasIRC . You must install this module to use this function. |
| --- | --- |
|  |  |

This function disconnects the server from the IRC server it's connected to.

## Syntax

```
bool ircDisconnect( [ string reason = "MTABot" ] )
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **reason :** The quit reason.

### Returns

Returns *true* if successfully disconnected from the server, *false* otherwise.

## Example

```
-- Example here
```

## See also

### Connection:

- [ircConnect](mta://reference/misc/modules-sebasirc-ircconnect.md)

- ircDisconnect

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
