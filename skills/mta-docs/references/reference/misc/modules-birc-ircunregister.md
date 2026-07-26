---
doc_id: "mta-wiki:4850"
title: "Modules/bIRC/ircUnregister"
source_title: "Modules/bIRC/ircUnregister"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircUnregister"
revision_id: 44530
language: "en"
categories: ["Utility_templates"]
---

# Modules/bIRC/ircUnregister

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function is used to unregister an [ircbot](mta://reference/misc/modules-birc-ircbot.md) for a resource. It is the opposite function for [ircRegister](mta://reference/misc/modules-birc-ircregister.md).

## Syntax

```
bool ircUnregister ( ircbot theBot, [ string resourceName = getResourceName ( getThisResource() ) ] )
```

### Required Arguments

- **theBot:** The ircbot which you want to stop calling the callbacks.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **resourceName:** The name of resource from which the ircbot should be unregistered. The resource specified must be running. Defaults to current resource's name.

### Returns

Returns *true* if unregistering callbacks was succesful, *false* otherwise.

## Example

This example creates an ircbot called *DummyBot* on when resource **ircecho** starts and makes it unable to call the callback functions inside the resource.

Click to collapse [-]
Resource: ircecho

```
function resourceStart()
    theBot = ircCreateBot ( "DummyBot" )
    ircUnregister ( theBot )
end
addEventHandler ( "onResourceStart", getResourceRootElement (), resourceStart )

-- This callback function will never be called!
function event_ircOnText ( theBot, channel, sender, message )
    if channel == ircGetName( theBot ) then
        outputServerLog ( "[IRC-ECHO] " .. ircGetName( theBot ) .. " received PM from " .. sender .. ": " .. message )
    else
        outputServerLog ( "[IRC-ECHO] " .. ircGetName( theBot ) .. " received text on " .. channel .. " from " .. sender .. ": " .. message )
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

- ircUnregister

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
