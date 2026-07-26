---
doc_id: "mta-wiki:4851"
title: "Modules/bIRC/ircConnect"
source_title: "Modules/bIRC/ircConnect"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircConnect"
revision_id: 44529
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:16:14.462077+00:00"
---

# Modules/bIRC/ircConnect

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function is used to connect an [ircbot](mta://reference/misc/modules-birc-ircbot.md) created with [ircCreateBot](mta://reference/misc/modules-birc-irccreatebot.md) to a server.  

**Note:** The maximum number of simultanuous connections is 5. There is no limit for ircbots but it is not possible to connect more than 5 bots at a time.

## Syntax

```
bool ircConnect ( ircbot theBot, string server, int port, [ string password ] )
```

### Required Arguments

- **theBot:** The ircbot which will be connected.

- **server:** The name of the server to which the bot will connect, eg. "irc.gtanet.com".

- **port:** The port number of the IRC server.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **password:** The password for the IRC server.

### Returns

Returns *true* if passed arguments were valid, *false* otherwise.  

**Note:** Does not return *true* if ircbot was successfully connected or *false* if the bot didn't connect. You can check if the bot connected by using callbacks [event_ircOnConnect](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnConnect&action=edit&redlink=1) and [event_ircOnFailedConnection](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnFailedConnection&action=edit&redlink=1).

## Example

This example creates an ircbot called *DummyBot* and makes it connect to irc.gtanet.com server on resource start.

```
function resourceStart()
    theBot = ircCreateBot ( "DummyBot" )
    ircConnect ( theBot, "irc.gtanet.com", 6667 )
end
addEventHandler ( "onResourceStart", getResourceRootElement (), resourceStart )
```

## See Also

### Bot functions

#### Creation

- [ircCreateBot](mta://reference/misc/modules-birc-irccreatebot.md)

- [ircDestroyBot](mta://reference/misc/modules-birc-ircdestroybot.md)

#### Connection

- ircConnect

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
