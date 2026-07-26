---
doc_id: "mta-wiki:4867"
title: "Modules/bIRC/ircGetChannelUsers"
source_title: "Modules/bIRC/ircGetChannelUsers"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircGetChannelUsers"
revision_id: 20932
language: "en"
categories: []
generated_at: "2026-07-26T16:16:14.688042+00:00"
---

# Modules/bIRC/ircGetChannelUsers

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function can be used to list out all the users a specified channel.

## Syntax

```
table ircGetChannelUsers ( ircbot theBot, string channel )
```

### Required Arguments

- **theBot:** The ircbot which is connected to the channel

- **channel:** The channel which users you want to get

### Returns

Returns a [table](mta://reference/misc/table.md) over all channel users. Returns an empty table if there's no users on that channel or *false* if invalid arguments were passed.

## Example

This example adds a command *listusers* which can be used to print out all users in the specified channel to the console.

```
function printOutUsers ( thePlayer, commandName, name, channel )
    local theBot = ircGetBotByName ( name )
    if not theBot then
        outputConsole ( "There's no ircbot called " .. name .. "!", thePlayer )
    else
        if ircIsInChannel ( theBot, channel ) then
           local users = ircGetChannelUsers ( theBot, channel )
           if #users == 0 then
               outputConsole ( "There's no users on " .. channel .. "!", thePlayer )
           else
               outputConsole ( "There is " .. #users .. " on " .. channel .. ":", thePlayer ) 
               for key, value in ipairs ( users ) do
                   outputConsole ( "- " .. value, thePlayer )
               end
           end
        else
            outputConsole ( name .. " is not on " .. channel .. "!", thePlayer )
        end
    end
end
addCommandHandler ( "listusers", printOutUsers )
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

- ircGetChannelUsers

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
