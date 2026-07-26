---
doc_id: "mta-wiki:1841"
title: "OnVehicleStartExit"
source_title: "OnVehicleStartExit"
source_url: "https://wiki.multitheftauto.com/wiki/OnVehicleStartExit"
revision_id: 67860
language: "en"
categories: ["Server_Events"]
---

# OnVehicleStartExit

This event is triggered when a player or ped starts to exit a vehicle. This event can be used to cancel exit, if necessary.

## Parameters

```
ped exitingPed, int seat, ped jacked, int door
```

- **exitingPed**: a [player](https://wiki.multitheftauto.com/index.php?search=player) or [ped](https://wiki.multitheftauto.com/index.php?search=ped) element who is starting to exit a vehicle.

- **seat**: an [int](mta://reference/misc/int.md) representing the seat in which the ped is exiting from.

- **jacked**: a [player](https://wiki.multitheftauto.com/index.php?search=player) or [ped](https://wiki.multitheftauto.com/index.php?search=ped) element representing who is jacking.

- **door**: an [int](mta://reference/misc/int.md) representing the door that the ped is using to leave.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) in which a ped began to exit.

### Canceling

If this event is [canceled](mta://reference/misc/event-system.md), the ped will not exit the vehicle.

## Example

This example locks a player inside a police vehicle if he is a policeman.

```
local policeVehicles = {[598] = true,[596] = true,[597] = true,[599] = true } -- Police vehicle IDs
local policeSkins = {[280] = true,[281] = true,[282] = true,[283] = true,[284] = true,[285] = true,[286] = true } -- Police Skins
 
function exitVehicle ( thePlayer, seat, jacked ) 
   if (policeVehicles[getElementModel (source)]) and (policeSkins[getElementModel(thePlayer)]) then 
      outputChatBox ( "You're the cop! Don't exit the car!", thePlayer )  
      cancelEvent()
   end
end
addEventHandler ( "onVehicleStartExit", getRootElement(), exitVehicle)
```

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

- [onVehicleDamage](mta://scripting/server/events/onvehicledamage.md)

- [onVehicleEnter](mta://scripting/server/events/onvehicleenter.md)

- [onVehicleExit](mta://scripting/server/events/onvehicleexit.md)

- [onVehicleExplode](mta://scripting/server/events/onvehicleexplode.md)

- [onVehicleRespawn](mta://scripting/server/events/onvehiclerespawn.md)

- [onVehicleStartEnter](mta://scripting/server/events/onvehiclestartenter.md)

- onVehicleStartExit

### Event functions

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
