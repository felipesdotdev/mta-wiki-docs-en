---
doc_id: "mta-wiki:4618"
title: "OnClientPedChoke"
source_title: "OnClientPedChoke"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPedChoke"
revision_id: 82040
language: "en"
categories: ["Client_events", "Needs_Checking"]
generated_at: "2026-07-26T16:16:19.293035+00:00"
---

# OnClientPedChoke

|  | This article needs checking. |
| --- | --- |
| Reason(s): Event is never triggered |  |

This event is fired when a ped chokes due to the effect of a weapon such as tear gas grenades, fire extinguishers and spray cans.

## Parameters

```
int weaponID, ped responsiblePed
```

- **weaponID:** an [int](mta://reference/misc/int.md) representing the ID of the weapon which caused the choking.

- **responsiblePed:** the ped responsible for causing the choking, possiblly nil.

## Source

The source of this event is the ped who is choking.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the ped will not be choked.

## Example

Click to collapse [-]
Client

This example disables choking effects from the tear gas grenades.

```
addEventHandler( "onClientPedChoke", getRootElement( ),
    function ( )
        cancelEvent( );
    end
);
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

- [onClientPedStep](mta://scripting/client/events/onclientpedstep.md)

- onClientPedChoke

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
