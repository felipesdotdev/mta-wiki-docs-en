---
doc_id: "mta-wiki:4613"
title: "Modules/SebasIRC/ircIsConnected"
source_title: "Modules/SebasIRC/ircIsConnected"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/ircIsConnected"
revision_id: 48361
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.060973+00:00"
---

# Modules/SebasIRC/ircIsConnected

|  | This function is provided by the external module SebasIRC . You must install this module to use this function. |
| --- | --- |
|  |  |

This function will check if the irc bot is connected.

## Syntax

```
bool ircIsConnected()
```

### Returns

True if connected, otherwise false.

## Example

```
addCommandHandler("connected",
  function()
    if ircIsConnected() then
      outputChatBox("-IRC- Connection is ok!")
    else
      outputChatBox("-IRC- Not connected!")
    end
  end
)
```

## See also

### Connection:

- [ircConnect](mta://reference/misc/modules-sebasirc-ircconnect.md)

- [ircDisconnect](mta://reference/misc/modules-sebasirc-ircdisconnect.md)

- ircIsConnected

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
