---
doc_id: "mta-wiki:4849"
title: "Modules/bIRC/ircRegister"
source_title: "Modules/bIRC/ircRegister"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/bIRC/ircRegister"
revision_id: 44531
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:16:14.995928+00:00"
---

# Modules/bIRC/ircRegister

|  | This function is provided by the external module Basic IRC Module . You must install this module to use this function. |
| --- | --- |
|  |  |

This function is used to register an [ircbot](mta://reference/misc/modules-birc-ircbot.md) for specified resource. By registering an ircbot for a resource, you are able to use the callbacks called by that bot in that resource.

**Note:** It is required to register your ircbot to the module if you're willing to use callbacks with other resources than the one where specified ircbot was originally created. This function is automatically executed for that specific resource when creating a new ircbot using [ircCreateBot](mta://reference/misc/modules-birc-irccreatebot.md) so registering a newly created ircbot within same resource is not required.

## Syntax

```
bool ircRegister ( ircbot theBot, [ string resourceName = getResourceName ( getThisResource() ) ] )
```

### Required Arguments

- **theBot:** The ircbot which you want to call the callbacks.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **resourceName:** The name of resource to which the ircbot should be registered. The resource specified must be running. Defaults to current resource's name.

### Returns

Returns *true* if registering callbacks was succesful, *false* otherwise.

## Example

This example creates an ircbot called *DummyBot* on when resource **ircecho** starts. *DummyBot* is now able to call the callback function **event_ircOnText** inside resource **ircecho**.  

Once resource **ircecho2** starts, it checks if ircbot named *DummyBot* exists and if it does, it registers that bot's callbacks for resource **ircecho2**. Now *DummyBot* is able to call the callback function **event_ircOnText** also inside resource **ircecho2**.

Click to collapse [-]
Resource: ircecho

```
function resourceStart()
    theBot = ircCreateBot ( "DummyBot" )
    -- ircRegister ( theBot ) is automatically executed
end
addEventHandler ( "onResourceStart", getResourceRootElement (), resourceStart )

-- This function will be called!
function event_ircOnText ( theBot, channel, sender, message )
    if channel == ircGetName( theBot ) then
        outputServerLog ( "[IRC-ECHO] " .. ircGetName( theBot ) .. " received PM from " .. sender .. ": " .. message )
    else
        outputServerLog ( "[IRC-ECHO] " .. ircGetName( theBot ) .. " received text on " .. channel .. " from " .. sender .. ": " .. message )
    end
end
```

Click to collapse [-]
Resource: ircecho2

```
function resourceStart()
    if ircGetBotByName ( "DummyBot" ) then
        ircRegister ( ircGetBotByName ( "DummyBot" ) )
    end
end
addEventHandler ( "onResourceStart", getResourceRootElement (), resourceStart )

-- This function wouldn't be called if ircRegister wasn't executed!
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

- ircRegister

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
