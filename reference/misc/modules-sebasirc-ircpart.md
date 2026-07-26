---
doc_id: "mta-wiki:4612"
title: "Modules/SebasIRC/ircPart"
source_title: "Modules/SebasIRC/ircPart"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/SebasIRC/ircPart"
revision_id: 48365
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:16:14.110725+00:00"
---

# Modules/SebasIRC/ircPart

|  | This function is provided by the external module SebasIRC . You must install this module to use this function. |
| --- | --- |
|  |  |

This function will part the bot from a channel

## Syntax

```
bool ircPart ( string channel [, string reason = "" ] )
```

### Required arguments

- **channel:** The channel name to part.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **reason:** The part reason.

### Returns

Returns true, otherwise false when giving wrong arguments.

## Example

```
local bot = nil

addEventHandler("onResourceStart", getResourceRootElement(),
  function()
    if ircConnect("irc.mtasa.com", 6667, "echoBot") then
      bot = true
      ircJoin("#mta.echo")
    end
  end
)

addCommandHandler("part",
  function(thePlayer, command, channel)
    if channel == nil then return end
    
    if bot and ircIsConnected() then
      ircPart(tostring(channel))
      outputChatBox("-IRC- Parted: "..tostring(channel).."!")
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

- [ircJoin](mta://reference/misc/modules-sebasirc-ircjoin.md)

- ircPart

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
