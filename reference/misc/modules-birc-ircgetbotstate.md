---
doc_id: "mta-wiki:4861"
title: "Modules/bIRC/ircGetBotState"
source_title: "Modules/bIRC/ircGetBotState"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircGetBotState"
revision_id: 20923
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.591194+00:00"
---

# Modules/bIRC/ircGetBotState

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function is used to retrieve the current state of specified [ircbot](mta://reference/misc/modules-birc-ircbot.md).

## Syntax

```
string ircGetBotState ( ircbot theBot )
```

### Required Arguments

- **theBot:** The ircbot which current state you want to get

### Returns

Returns a string of the ircbot's current state. Possible values are:

- **disconnected**

- **connecting**

- **connected**

If invalid arguments were passed, it returns *false*.

## Example

This example creates an ircbot called *DummyBot* and makes it connect to a server. During the connection progress bot's current states are printed out to the server log.

```
function resourceStart ()
    dummyBot = ircCreateBot ( "DummyBot" )
    outputServerLog ( "DummyBot is now " .. ircGetBotState ( dummyBot ) ) -- "disconnected"
    ircConnect ( dummyBot, "irc.gtanet.com", 6667 )
    outputServerLog ( "DummyBot is now " .. ircGetBotState ( dummyBot ) ) -- "connecting"
end
addEventHandler ( "onResourceStart", getResourceRootElement ( getThisResource() ), resourceStart )

function event_ircOnConnect ( theBot )
    outputServerLog ( ircGetName ( theBot ) .. " is now " .. ircGetBotState ( theBot ) ) -- "connected"
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

- ircGetBotState

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
