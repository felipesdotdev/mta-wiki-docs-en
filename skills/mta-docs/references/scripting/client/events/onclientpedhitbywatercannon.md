---
doc_id: "mta-wiki:6241"
title: "OnClientPedHitByWaterCannon"
source_title: "OnClientPedHitByWaterCannon"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPedHitByWaterCannon"
revision_id: 81117
language: "en"
categories: ["Client_events"]
---

# OnClientPedHitByWaterCannon

This event is fired when a ped is hit by a water cannon.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for peds that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
ped pedHit
```

- **pedHit:** the ped which got shot by the water cannon

## Source

The source of this event is the vehicle who shot the water cannon.

## Type

This event is a pre reaction event meaning it occurs before any game level reaction to the collision which include:

- Peds flying off

- Peds being knocked down

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the ped will not be knocked down

## Example

Click to collapse [-]
Client

This example says who got hit by a water cannon.

```
function outputPlayerHitByWater(thePed)
	if (getElementType(thePed) ~= "player") then
		return false -- This event is for peds and players but this example only wants players
	end
	local hitPed = getPlayerName(thePed)
	outputChatBox(hitPed.." got hit by a water cannon!", 255, 0, 0)
end
addEventHandler("onClientPedHitByWaterCannon", root, outputPlayerHitByWater)
```

## See Also

### Client ped events

- [onClientPedDamage](mta://scripting/client/events/onclientpeddamage.md)

- [onClientPedHeliKilled](mta://scripting/client/events/onclientpedhelikilled.md)

- onClientPedHitByWaterCannon

- [onClientPedVehicleEnter](mta://scripting/client/events/onclientpedvehicleenter.md)

- [onClientPedVehicleExit](mta://scripting/client/events/onclientpedvehicleexit.md)

- [onClientPedWasted](mta://scripting/client/events/onclientpedwasted.md)

- [onClientPedWeaponFire](mta://scripting/client/events/onclientpedweaponfire.md)

- [onClientPedStep](mta://scripting/client/events/onclientpedstep.md)

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
