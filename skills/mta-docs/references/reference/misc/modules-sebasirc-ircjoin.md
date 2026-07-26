---
doc_id: "mta-wiki:4551"
title: "Modules/SebasIRC/ircJoin"
source_title: "Modules/SebasIRC/ircJoin"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/ircJoin"
revision_id: 48363
language: "en"
categories: []
---

# Modules/SebasIRC/ircJoin

|  | This function is provided by the external module SebasIRC . You must install this module to use this function. |
| --- | --- |
|  |  |

This function joins the bot a channel (, with a password).

## Syntax

```
bool ircJoin(string channel [, string password])
```

### Required arguments

- **channel:** The channel name.

### Optional Arguments

- **password:** The channel password.

### Returns

*True* if joined, otherwise *false*.

## Example

```
addEventHandler("onResourceStart", getResourceRootElement(),
  function()
    local connect = ircConnect("irc.mtasa.com", 6667, "MTABot")
    if connect then
      ircJoin("#mta.test")
    end
  end
)
```

## See also

### Connection:

- [ircConnect](mta://reference/misc/modules-sebasirc-ircconnect.md)

- [ircDisconnect](mta://reference/misc/modules-sebasirc-ircdisconnect.md)

- [ircIsConnected](mta://reference/misc/modules-sebasirc-ircisconnected.md)

### Channel:

- ircJoin

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
