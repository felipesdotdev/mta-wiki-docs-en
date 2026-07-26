---
doc_id: "mta-wiki:4886"
title: "Modules/bIRC/ircSetChannelMode"
source_title: "Modules/bIRC/ircSetChannelMode"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircSetChannelMode"
revision_id: 21074
language: "en"
categories: []
generated_at: "2026-07-26T16:16:15.021295+00:00"
---

# Modules/bIRC/ircSetChannelMode

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function can be used to set a channel mode the specified channel. The specified [ircbot](mta://reference/misc/modules-birc-ircbot.md) often needs to have suitable privileges in order for the change to have an effect.

## Syntax

```
bool ircSetChannelMode ( ircbot theBot, string channel, string mode )
```

### Required Arguments

- **theBot:** The ircbot which is in the channel

- **channel:** The name of the channel on which you want to set a channel mode

- **mode:** The channel mode string

### Returns

Returns *true*.  

**Note:** Does not return *true* if a channel mode was successfully set or *false* if it wasn't set. You can check if the channel mode was set by using callback [event_ircOnChannelMode](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnChannelMode&action=edit&redlink=1).

## Example

This example creates an ircbot called *DummyBot* makes it connect to a server and join a channel. It also includes an IRC command '!limitusers' which can used to change the channel's maximum user limit.

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
    if message:find( "!limitusers" ) then
        local params = split ( message, string.byte (' ') )
        -- params[1] has the string "!limitusers" which we don't need
        -- params[2] has the user count
        if tonumber( params[2] ) then -- check if it's a number, but don't convert it to a number
            ircSetChannelMode ( theBot, channel, "+l " .. params[2] )
        elseif params[2] == "off" then -- if user passes 'off' as the number, remove the limit
            ircSetChannelMode ( theBot, channel, "-l" )
        end
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

- ircSetChannelMode

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
