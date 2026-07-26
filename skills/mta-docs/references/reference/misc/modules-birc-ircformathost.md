---
doc_id: "mta-wiki:4856"
title: "Modules/bIRC/ircFormatHost"
source_title: "Modules/bIRC/ircFormatHost"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircFormatHost"
revision_id: 20930
language: "en"
categories: ["Utility_templates"]
---

# Modules/bIRC/ircFormatHost

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function can be used to change a ban host mask to specified wildcard format.

## Syntax

```
string ircFormatHost ( string host, [ int formatType = 2 ] )
```

### Required Arguments

- **host:** The host address that will be reformatted. It needs to be in format "nick!user@host".

**Note:** If you're using this function along with [ircGetUserHost](mta://reference/misc/modules-birc-ircgetuserhost.md), please remember to add the nick! part yourself to the host as ircGetUserHost only returns the user@host part.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **formatType:** The way the host is going to be formatted. Valid values are

- 0: *!user@host

- 1: *!*user@host

- 2: *!*@host

- 3: *!*user@*.host

- 4: *!*@*.host

- 5: nick!user@host

- 6: nick!*user@host

- 7: nick!*@host

- 8: nick!*user@*.host

- 9: nick!*@*.host

You can also specify a type of 10 to 19 which correspond to masks 0 to 9, but instead of using only * wildcard to replace portions of the host, also ? wildcards are used to replace the numbers in the address (host part).

### Returns

Returns a formatted version of the string of the specified host if arguments were valid, *false* otherwise.

## Example

This example creates an ircbot called *DummyBot* makes it connect to a server and join a channel. It also includes an IRC command '!formathost <name> <type>' which formats specified users host to specified type if the user is actually in the channel.

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
    if message:find( "!formathost" ) then
        local params = split ( message, string.byte (' ') )
        -- params[1] has the string "!formathost" which we don't need
        -- params[2] has the name of the user
        -- params[3] has the type of the format
        if ircIsInChannel ( theBot, channel, params[2] ) then
            local host = ircGetUserHost ( theBot, params[2] )
            host = ircFormatHost ( params[2] .. "!" .. host, tonumber(params[3]) )
            ircSendMessage ( theBot, channel, params[2] .. "'s formatted host is " .. tostring(host) )
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

- [ircKick](mta://reference/misc/modules-birc-irckick.md)

- [ircSendMessage](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendMessage&action=edit&redlink=1)

- [ircSendNotice](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendNotice&action=edit&redlink=1)

- [ircSendRaw](https://wiki.multitheftauto.com/index.php?title=Modules/bIRC/ircSendRaw&action=edit&redlink=1)

### Other

- ircFormatHost

- [ircStrip](mta://reference/misc/modules-birc-ircstrip.md)
