---
doc_id: "mta-wiki:4887"
title: "Modules/bIRC/ircSetChannelTopic"
source_title: "Modules/bIRC/ircSetChannelTopic"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircSetChannelTopic"
revision_id: 21073
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.046375+00:00"
---

# Modules/bIRC/ircSetChannelTopic

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function can be used to change the topic of specified channel. The specified [ircbot](mta://reference/misc/modules-birc-ircbot.md) has to be in that channel and often it needs to have suitable privileges.

## Syntax

```
bool ircSetChannelTopic ( ircbot theBot, string channel, string topic )
```

### Required Arguments

- **theBot:** The ircbot which is in the channel

- **channel:** The name of the channel which channel topic you want to change

- **topic:** The new topic of the channel

### Returns

Returns *true* if passed arguments were valid, *false* otherwise.  

**Note:** Does not return *true* if the channel topic was successfully changed or *false* if it wasn't changed. You can check if the channel topic was changed by using callback [event_ircOnTopic](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnTopic&action=edit&redlink=1).

## Example

This example creates an ircbot called *DummyBot* makes it connect to a server and join a channel. It also includes an IRC command '!settopic' which can used change the current channel topic.

```
function resourceStart ( )
    theBot = ircCreateBot ( "DummyBot" )
    ircConnect ( theBot, "irc.gtanet.com", 6667 )
end
addEventHandler ( "onResourceStart", getResourceRootElement ( getThisResource() ), resourceStart )

function event_ircOnConnect ( theBot )
    setTimer ( ircJoinChannel, 2000, 1, theBot, "#testchannel" )
end

function event_ircOnText ( theBot, channel, sender, message )
    if message:find( "!settopic" ) then
        local topic = message:sub( 11 ) -- subtract "!settopic " from the message
        ircSetChannelTopic ( theBot, channel, topic )
    end

end
```

## See Also

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

- ircSetChannelTopic

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
