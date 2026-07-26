---
doc_id: "mta-wiki:4890"
title: "Modules/bIRC/ircGetUserHost"
source_title: "Modules/bIRC/ircGetUserHost"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircGetUserHost"
revision_id: 21096
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.787016+00:00"
---

# Modules/bIRC/ircGetUserHost

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function returns the hostmask of a specified user in format user@host. The specified [ircbot](mta://reference/misc/modules-birc-ircbot.md) has to be in one of the channels the specified user is in.

## Syntax

```
string ircGetUserHost ( ircbot theBot, string user )
```

### Required Arguments

- **theBot:** The ircbot which is in the channel

- **user:** The user whose hostmask you want to get

### Returns

Returns the host of specified user if it could be retrieved, or *false* if it failed or invalid arguments were passed.

## Example

This example creates an ircbot called *DummyBot* makes it connect to a server and join a channel. It also includes an IRC command '!ban' which can be used to ban users (unable to talk or join) from IRC without kicking them from the channel.

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
    if message:find( "!ban" ) then
        local params = split ( message, string.byte (' ') )
        -- params[1] has the string "!ban" which we don't need
        -- params[2] has the user name
        if ircIsInChannel ( theBot, channel, params[2] ) then
            local userHost = ircGetUserHost ( theBot, params[2] )
            if userHost then -- if user host was successfully received
                local hostMask = ircFormatHost ( params[2] .. "!" .. userHost )
                if hostMask then -- and if formatting was successful
                    ircSetChannelMode ( theBot, channel, "+b " .. hostMask )
                end
            else
                ircSendMessage ( theBot, channel, "Failed to retrieve user host!" )
            end
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

- ircGetUserHost

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
