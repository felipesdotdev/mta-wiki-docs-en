---
doc_id: "mta-wiki:4888"
title: "Modules/bIRC/ircGetUserMode"
source_title: "Modules/bIRC/ircGetUserMode"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircGetUserMode"
revision_id: 21080
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.813423+00:00"
---

# Modules/bIRC/ircGetUserMode

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function returns the user mode of user in specified channel. The specified [ircbot](mta://reference/misc/modules-birc-ircbot.md) has to be in that channel.

## Syntax

```
string ircGetUserMode ( ircbot theBot, string channel, string user )
```

### Required Arguments

- **theBot:** The ircbot which is in the channel

- **channel:** The name of the channel which channel mode you want to get

- **user:** The name of the user whose user mode you want to return

### Returns

Returns a [string](mta://reference/misc/string.md) containing a series of symbols, each representing a user mode. Symbols are

- **+:** user is voiced in the channel

- **%:** user is a channel half-operator

- **@:** user is a channel operator

- **&:** user is a channel super-operator

- **~:** user is the channel owner

If user does not have any modes on that channel, returns an empty string or *false* if invalid arguments were passed.

## Example

This example creates a function which can be used to check whether a user is voiced in a channel.

```
function isUserVoiced( theBot, channel, user )
    local botName = ircGetName( theBot )
    if botName then -- if the bot given was valid (it has a name)
        if ircIsInChannel( theBot, channel, user ) then -- if the user is in channel
            local userMode = ircGetUserMode( theBot, channel, user )
            if userMode and userMode:find( "+" ) then -- if valid arguments were passed, and '+' symbol is found in the user mode
                return true
            end
        end
    end
    return false
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

- ircGetUserMode

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
