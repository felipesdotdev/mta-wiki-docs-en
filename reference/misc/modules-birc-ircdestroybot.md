---
doc_id: "mta-wiki:4848"
title: "Modules/bIRC/ircDestroyBot"
source_title: "Modules/bIRC/ircDestroyBot"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircDestroyBot"
revision_id: 44532
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.512174+00:00"
---

# Modules/bIRC/ircDestroyBot

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function is used to destroy a created [ircbot](mta://reference/misc/modules-birc-ircbot.md). After deletion, the ircbot pointer will nolonger be valid. If ircbot is connected, it will be disconnected from the server.

## Syntax

```
bool ircDestroyBot ( ircbot theBot )
```

### Required Arguments

- **theBot:** The ircbot which will be destroyed.

### Returns

Returns *true* if ircbot was successfully destroyed, *false* otherwise.

## Example

This example creates an ircbot called *DummyBot* on resource start and destroys the bot once the resource has stopped.

```
function resourceStart()
    theBot = ircCreateBot ( "DummyBot" )
end
addEventHandler ( "onResourceStart", getResourceRootElement (), resourceStart )

function resourceStop()
    if theBot then
        ircDestroyBot ( theBot )
    end
end
addEventHandler ( "onResourceStop", getResourceRootElement (), resourceStop )
```

## See Also

### Bot functions

#### Creation

- [ircCreateBot](mta://reference/misc/modules-birc-irccreatebot.md)

- ircDestroyBot

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
