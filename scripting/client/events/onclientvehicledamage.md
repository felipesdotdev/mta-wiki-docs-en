---
doc_id: "mta-wiki:7331"
title: "OnClientVehicleDamage"
source_title: "OnClientVehicleDamage"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientVehicleDamage"
revision_id: 64751
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.525984+00:00"
---

# OnClientVehicleDamage

This event is triggered when a vehicle is damaged.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for vehicles that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
element theAttacker, int theWeapon, float loss, float damagePosX, float damagePosY, float damagePosZ, int tireID
```

- **theAttacker**: An element if there was an attacker.

- **theWeapon**: An integer specifying the [weapon ID](mta://reference/misc/weapons.md) if a weapon was used. Otherwise [Damage Type ID](mta://reference/misc/damage-types.md) is used.

- **loss**: A float representing the amount of damage taken.

- **damagePosX**: A float representing the X co-ordinate of where the damage took place.

- **damagePosY**: A float representing the Y co-ordinate of where the damage took place.

- **damagePosZ**: A float representing the Z co-ordinate of where the damage took place.

- **tireID**: A number representing the tire which took damage, if there is one.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](mta://reference/misc/vehicle.md) that got damaged.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the vehicle health won't be reduced. Physical damage to the vehicle will remain.

## Example

This example makes every SWAT tank immune from all weapon attacks.

Click to collapse [-]
Client

```
function handleVehicleDamage(attacker, weapon, loss, x, y, z, tire)
    if (weapon and getElementModel(source) == 601) then
        -- A weapon was used and the vehicle model ID is that of the SWAT tank so cancel the damage.
        cancelEvent()
    end
end
addEventHandler("onClientVehicleDamage", root, handleVehicleDamage)
```

This example allows the Rhino to take damage from bullets even though they're bullet proof, this example doesn't work with explosions though.

Click to collapse [-]
Client

```
-- Only let these weapons damage a Rhino
local weaponsToDamageRhino = {
	[38] = true, -- minigun
	[33] = true, -- country rifle
	[34] = true, -- sniper rifle
	[30] = true, -- AK-47
	[31] = true, -- M4
}

function handleRhinoDamage(attacker, weapon, loss, x, y, z, tire)
	if (weapon and getElementModel(source) == 432 and loss > 0) then
		if (weaponsToDamageRhino[weapon]) then
			setElementHealth(source, getElementHealth(source) - loss)
		end
	end
end
addEventHandler("onClientVehicleDamage", root, handleRhinoDamage)
```

This example will makes all vehicle Fireproof.

Click to collapse [-]
Client

```
function fireproofvehicle(theAttacker, theWeapon)
	if(theWeapon == 37) then
		cancelEvent()
	end
end
addEventHandler("onClientVehicleDamage", getRootElement(), fireproofvehicle)
```

## See Also

### Client vehicle events

- [onClientTrailerAttach](mta://scripting/client/events/onclienttrailerattach.md)

- [onClientTrailerDetach](mta://scripting/client/events/onclienttrailerdetach.md)

- [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md)

- onClientVehicleDamage

- [onClientVehicleEnter](mta://scripting/client/events/onclientvehicleenter.md)

- [onClientVehicleExit](mta://scripting/client/events/onclientvehicleexit.md)

- [onClientVehicleExplode](mta://scripting/client/events/onclientvehicleexplode.md)

- [onClientVehicleNitroStateChange](mta://scripting/client/events/onclientvehiclenitrostatechange.md)

- [onClientVehicleRespawn](mta://scripting/client/events/onclientvehiclerespawn.md)

- [onClientVehicleStartEnter](mta://scripting/client/events/onclientvehiclestartenter.md)

- [onClientVehicleStartExit](mta://scripting/client/events/onclientvehiclestartexit.md)

- [onClientVehicleWeaponHit](mta://scripting/client/events/onclientvehicleweaponhit.md)

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
