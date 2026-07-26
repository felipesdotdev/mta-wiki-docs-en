---
doc_id: "mta-wiki:12568"
title: "OnClientPedsProcessed"
source_title: "OnClientPedsProcessed"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPedsProcessed"
revision_id: 82086
language: "en"
categories: ["Client_events"]
---

# OnClientPedsProcessed

This event is triggered after GTA updates bone transformations for all peds. This event can be used for updating bones.

| [[\|link=\|]] | Warning: This event will trigger whatever function it is attached to with every frame. Depending on the server's maximum FPS and what your computer might handle - you might end up triggering the function 30-60 times per second . As a result, this event may cause severe lag and/or even crashes if not used cautiously. |
| --- | --- |
|  |  |

## Parameters

None.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the client's [root element](https://wiki.multitheftauto.com/index.php?search=root%20element).

## Example

```
addEventHandler("onClientPedsProcessed",root,function() -- add the event
    for i,v in ipairs(getElementsByType('player',root,true)) do  -- loop all players
        
        -- just an exmaple anim
        setElementBoneRotation(v, 33, 0, 295.2, 0)
        setElementBoneRotation(v, 23, 0, 298.8, 0)
        setElementBoneRotation(v, 4, 0, 46.8, 0)
        setElementBoneRotation(v, 2, 0, 0, 32.4)

        updateElementRpHAnim(v) -- Update ped bones animations

    end 
end)
```

This example makes the localPlayer handcuffed. The player can still run/walk/jump/crouch/shoot, use [toggleControl](mta://scripting/shared/functions/togglecontrol.md) to disable them.

```
addEventHandler("onClientPedsProcessed", root, function()
    -- Left
    setElementBoneRotation(localPlayer, 32, 26.574, 61.3375, 59.2065)
    setElementBoneRotation(localPlayer, 33, 27.844, 15.364, 46.406)
    setElementBoneRotation(localPlayer, 34, -81.0185, 342.875, 326.118)
    -- Right
    setElementBoneRotation(localPlayer, 22, 338.839, 53.4935, 298.452)
    setElementBoneRotation(localPlayer, 23, 307.687, 22.11, 313.594)
    setElementBoneRotation(localPlayer, 24, 96.0475, 357.883, 56.739)

    updateElementRpHAnim(localPlayer)
end)
```

## See Also

### [Game Processing Order](mta://reference/misc/game-processing-order.md)

### Other client events

- [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)

- [onClientExplosion](mta://scripting/client/events/onclientexplosion.md)

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

- [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md)

- [onClientMinimize](mta://scripting/client/events/onclientminimize.md)

- [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md)

- onClientPedsProcessed

- [onClientPlayerNetworkStatus](mta://scripting/client/events/onclientplayernetworkstatus.md)

- [onClientPreRender](mta://scripting/client/events/onclientprerender.md)

- [onClientRender](mta://scripting/client/events/onclientrender.md)

- [onClientRestore](mta://scripting/client/events/onclientrestore.md)

- [onClientTransferBoxProgressChange](mta://scripting/client/events/onclienttransferboxprogresschange.md)

- [onClientTransferBoxVisibilityChange](mta://scripting/client/events/onclienttransferboxvisibilitychange.md)

- [onClientWorldSound](mta://scripting/client/events/onclientworldsound.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
