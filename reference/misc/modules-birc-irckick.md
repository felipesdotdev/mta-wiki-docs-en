---
doc_id: "mta-wiki:4893"
title: "Modules/bIRC/ircKick"
source_title: "Modules/bIRC/ircKick"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircKick"
revision_id: 21100
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:16:14.917950+00:00"
---

# Modules/bIRC/ircKick

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function can be used to kick user from the specified channel. The specified [ircbot](mta://reference/misc/modules-birc-ircbot.md) often needs to have suitable privileges in order for this to work.

## Syntax

```
bool ircKick ( ircbot theBot, string channel, string user, [ string reason = "" ] )
```

### Required Arguments

- **theBot:** The ircbot which is going to do the kicking

- **channel:** The channel where user should be kicked from

- **user:** The user who should be kicked

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **reason:** The reason for the kick

### Returns

Returns *true* if passed arguments were valid, *false* otherwise.  

**Note:** Does not return *true* if the user was successfully kicked or *false* if it failed. You can check if the user was kicked by using callback [event_ircOnKick](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/event_ircOnKick&action=edit&redlink=1).

## Example

This example creates an ircbot called *DummyBot*, makes it connect to a server and join a channel. It also includes an IRC command '!kick' which can be used to kick users from the channel.

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
    if message:find( "!kick" ) then
        local params = split ( message, string.byte (' ') )
        -- params[1] has the string "!kick" which we don't need
        -- params[2] has the user name
        if ircIsInChannel ( theBot, channel, params[2] ) then
            ircKick ( theBot, channel, params[2] )
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

- [ircSetChannelMode](mta://reference/misc/modules-birc-ircsetchannelmode.md)

- [ircSetChannelTopic](mta://reference/misc/modules-birc-ircsetchanneltopic.md)

#### User

- [ircGetUserHost](mta://reference/misc/modules-birc-ircgetuserhost.md)

- [ircGetUserMode](mta://reference/misc/modules-birc-ircgetusermode.md)

- [ircIsInChannel](mta://reference/misc/modules-birc-ircisinchannel.md)

#### Communication

- [ircBan](mta://reference/misc/modules-birc-ircban.md)

- [ircInviteUser](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircInviteUser&action=edit&redlink=1)

- ircKick

- [ircSendMessage](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendMessage&action=edit&redlink=1)

- [ircSendNotice](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendNotice&action=edit&redlink=1)

- [ircSendRaw](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendRaw&action=edit&redlink=1)

### Other

- [ircFormatHost](mta://reference/misc/modules-birc-ircformathost.md)

- [ircStrip](mta://reference/misc/modules-birc-ircstrip.md)
