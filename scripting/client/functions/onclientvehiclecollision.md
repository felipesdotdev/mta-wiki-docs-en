---
doc_id: "mta-wiki:6040"
title: "OnClientVehicleCollision"
source_title: "OnClientVehicleCollision"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientVehicleCollision"
revision_id: 82065
language: "en"
categories: ["Client_events", "Functions_and_events_with_issues"]
generated_at: "2026-07-26T16:16:20.506317+00:00"
---

# OnClientVehicleCollision

This event is triggered when a vehicle collides with an [element](mta://reference/misc/element.md) or a world object.

Note that the collision reported by this event doesn't always damage the vehicle by default (this event triggers when hitting lamp posts, but the vehicle isn't damaged by them automatically, for example). If you want to deal with real damage, please refer to [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md).

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for vehicles that are streamed in |
| --- | --- |
|  |  |

## Parameters

```
element theHitElement, float damageImpulseMag, int bodyPart, float collisionX, float collisionY, float collisionZ, float normalX, float normalY, float normalZ, float hitElementForce, int model
```

**Note:** *theHitElement* will be nil or false if it's a default SA object and it will trigger twice for vehicles because one vehicle hit another and one got hit by another.

- **theHitElement:** the other entity, or nil if the vehicle collided with the world

- **damageImpulseMag:** the impact magnitude (Note: this is NOT the damage it is a force value which is then multiplied by the vehicles collision damage multiplier. for an example of this see below)

- **bodyPart:** the bodypart that hit the other element

- **0:** Frame

- **2:** Trunk

- **3:** Hood

- **4:** Rear

- **5:** Front left door

- **6:** Front right door

- **7:** Rear left door

- **8:** Rear right door

- **13:** Front Left tyre

- **14:** Front Right tyre

- **15:** Back Left tyre

- **16:** Back Right tyre

(Other potential IDs haven't been documented yet and might depend on vehicle model)

- **collisionX:** the X coordinate of the position the collision took place

- **collisionY:** the Y coordinate of the position the collision took place

- **collisionZ:** the Z coordinate of the position the collision took place

- **normalX:** the X coordinate of the surface normal of the hit object

- **normalY:** the Y coordinate of the surface normal of the hit object

- **normalZ:** the Z coordinate of the surface normal of the hit object

- **hitElementForce:** 0 for non vehicles or the force of the other vehicle

- **model:** model of the hit element (useful to detect building collisions as hitElement will be nil)

## Type

This event is a pre reaction event meaning it occurs before any game level reaction to the collision which include:

- Bike knock off effect

- Collision particles

- All types of damage reaction such as broken wings, wind shields, engine damage, broken lights and so on

- Audio of the impact

## Source

The source of this event is the vehicle that collided with something.

## Issues

| Issue ID | Description |
| --- | --- |
| #522 | onClientVehicleCollision doesn't trigger when world objects are broken |
| #2320 | hitElement in onClientVehicleCollision returns nil for projectile |

## Example

```
addEventHandler("onClientVehicleCollision", root,
    function(collider, damageImpulseMag, bodyPart, x, y, z, nx, ny, nz)
         if ( source == getPedOccupiedVehicle(localPlayer) ) then
             -- force does not take into account the collision damage multiplier (this is what makes heavy vehicles take less damage than banshees for instance) so take that into account to get the damage dealt
             local fDamageMultiplier = getVehicleHandling(source).collisionDamageMultiplier
             -- Create a marker (Scaled down to 1% of the actual damage otherwise we will get huge markers)
             local m = createMarker(x, y, z, "corona", damageImpulseMag* fDamageMultiplier * 0.01, 0, 9, 231)
             -- Destroy the marker in 2 seconds
             setTimer(destroyElement, 2000, 1, m)
         end
    end
)
```

```
-- This code works because onClientVehicleCollision is triggered before any SA reaction to the collision, therefore we can update the knocked off bike status just before the collision and stop the falling off effect happening :)
addEventHandler("onClientVehicleCollision", root,
    function ( hit ) 
        -- firstly did we trigger this event
        if ( source == getPedOccupiedVehicle(localPlayer) ) then
            -- knock off defaults to false
            local knockOff = false 
            -- if our hit element is nil (we just hit an SA map object)
            if ( hit == nil ) then 
                -- set knockOff to true 
                knockOff = true 
            end 
  
            -- update our can be knocked off bike status accordingly
            setPedCanBeKnockedOffBike(localPlayer, knockOff) 
        end
    end
)
```

## See Also

### Client vehicle events

- [onClientTrailerAttach](mta://scripting/client/events/onclienttrailerattach.md)

- [onClientTrailerDetach](mta://scripting/client/events/onclienttrailerdetach.md)

- onClientVehicleCollision

- [onClientVehicleDamage](mta://scripting/client/events/onclientvehicledamage.md)

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
