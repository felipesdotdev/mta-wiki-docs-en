---
doc_id: "mta-wiki:11011"
title: "OnClientVehicleWeaponHit"
source_title: "OnClientVehicleWeaponHit"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientVehicleWeaponHit"
revision_id: 82088
language: "en"
categories: ["Client_events", "Changes_in_1.5.6"]
---

# OnClientVehicleWeaponHit

This event is called when a vehicle weapon hits an element or the world.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for elements that are streamed in |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Weapon Types: 0 : Invalid 1 : Water Canon 2 : Tank Gun - Not yet implemented. 3 : Rocket - Not yet implemented. 4 : Heat Seeking Rocket - Not yet implemented. |
| --- | --- |
|  |  |

## Parameters

```
int weaponType, element hitElement, float hitX, float hitY, float hitZ, int model, int materialID
```

- **weaponType**: The type of vehicle weapon. (See the list above)

- **hitElement**: The [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle), [ped](https://wiki.multitheftauto.com/index.php?search=ped) or [player](https://wiki.multitheftauto.com/index.php?search=player) that was hit by the weapon sometimes *false*.

- **hitX**: The X world co-ordinate of where the hit occured.

- **hitY**: The Y world co-ordinate of where the hit occured.

- **hitZ**: The Z world co-ordinate of where the hit occured.

- **model**: The model ID of the element that was hit.

- **materialID**: The material ID of the element that was hit.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that fired the weapon.

## Example

Click to collapse [-]
Client

```
addEventHandler("onClientVehicleWeaponHit", root,
     function(weaponType, hitElement, hitX, hitY, hitZ, model, materialID)
          outputChatBox(tostring(weaponType).." "..tostring(hitElement).." "..tostring(hitX).." "..tostring(hitY).." "..tostring(hitZ).." "..tostring(model).." "..tostring(materialID))
     end
)
```

## See Also

### Client vehicle events

- [onClientTrailerAttach](mta://scripting/client/events/onclienttrailerattach.md)

- [onClientTrailerDetach](mta://scripting/client/events/onclienttrailerdetach.md)

- [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md)

- [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md)

- [onClientVehicleEnter](mta://scripting/client/events/onclientvehicleenter.md)

- [onClientVehicleExit](mta://scripting/client/events/onclientvehicleexit.md)

- [onClientVehicleExplode](mta://scripting/client/events/onclientvehicleexplode.md)

- [onClientVehicleNitroStateChange](mta://scripting/client/events/onclientvehiclenitrostatechange.md)

- [onClientVehicleRespawn](mta://scripting/client/events/onclientvehiclerespawn.md)

- [onClientVehicleStartEnter](mta://scripting/client/events/onclientvehiclestartenter.md)

- [onClientVehicleStartExit](mta://scripting/client/events/onclientvehiclestartexit.md)

- onClientVehicleWeaponHit

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
