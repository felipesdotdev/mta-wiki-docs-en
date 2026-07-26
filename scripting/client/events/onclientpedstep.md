---
doc_id: "mta-wiki:10975"
title: "OnClientPedStep"
source_title: "OnClientPedStep"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPedStep"
revision_id: 81208
language: "en"
categories: ["Client_events", "Changes_in_1.5.6"]
generated_at: "2026-07-26T16:16:19.364396+00:00"
---

# OnClientPedStep

This event is called when a peds foot has come on to the ground after jumping or taking a full step.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for peds that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
bool leftFoot
```

- **leftFoot**:  a [bool](mta://reference/misc/bool.md) representing if it was the left foot that moved.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](mta://reference/misc/ped.md) who stepped.

## Example

```
addEventHandler("onClientPedStep", localPlayer,
     function(leftFoot)
          if (leftFoot) then
               outputChatBox("Your left foot hit the ground.", 0, 255, 0)
          else
               outputChatBox("Your right foot hit the ground.", 0, 255, 0)
          end
     end
)
```

## See Also

### Client ped events

- [onClientPedDamage](mta://scripting/client/events/onclientpeddamage.md)

- [onClientPedHeliKilled](mta://scripting/client/events/onclientpedhelikilled.md)

- [onClientPedHitByWaterCannon](mta://scripting/client/events/onclientpedhitbywatercannon.md)

- [onClientPedVehicleEnter](mta://scripting/client/events/onclientpedvehicleenter.md)

- [onClientPedVehicleExit](mta://scripting/client/events/onclientpedvehicleexit.md)

- [onClientPedWasted](mta://scripting/client/events/onclientpedwasted.md)

- [onClientPedWeaponFire](mta://scripting/client/events/onclientpedweaponfire.md)

- onClientPedStep

- [onClientPedChoke](mta://scripting/client/events/onclientpedchoke.md)

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
