---
doc_id: "mta-wiki:4555"
title: "OnClientPedWasted"
source_title: "OnClientPedWasted"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPedWasted"
revision_id: 82031
language: "en"
categories: ["Client_events"]
---

# OnClientPedWasted

This event is triggered whenever a ped dies.

## Parameters

```
element killer, int weapon, int bodypart, mixed lossOrStealth
```

- **killer**: A [player](https://wiki.multitheftauto.com/index.php?search=player), [ped](https://wiki.multitheftauto.com/index.php?search=ped) or [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) [element](mta://reference/misc/element.md) representing the killer.

- **weapon**: An [integer](mta://reference/misc/int.md) representing the [killer weapon](mta://reference/misc/weapons.md) or the [damage types](mta://reference/misc/damage-types.md).

- **bodypart**: An [integer](mta://reference/misc/int.md) representing the bodypart the player was damaged.

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **lossOrStealth**: A [float](mta://reference/misc/float.md) representing the percentage of health the ped lost in the final "hit" (*only for client-side created peds.*) or a [boolean](mta://reference/misc/boolean.md) representing whether or not this was a stealth kill

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](https://wiki.multitheftauto.com/index.php?search=ped) that died.

## Example

Click to collapse [-]
Client

This example outputs a message every time a player kills another player.

```
-- define the event handler function
function onWasted(killer, weapon, bodypart)
    if ( killer and getElementType(killer) == "player" and getElementType(source) == "player" ) then
        outputChatBox(getPlayerName(killer).." has killed ".. getPlayerName(source) ..".") -- output the kill message to the chatbox.
    end
end

-- add the event handler
addEventHandler("onClientPedWasted", getRootElement(), onWasted)
```

## See Also

### Client ped events

- [onClientPedDamage](mta://scripting/client/events/onclientpeddamage.md)

- [onClientPedHeliKilled](mta://scripting/client/events/onclientpedhelikilled.md)

- [onClientPedHitByWaterCannon](mta://scripting/client/events/onclientpedhitbywatercannon.md)

- [onClientPedVehicleEnter](mta://scripting/client/events/onclientpedvehicleenter.md)

- [onClientPedVehicleExit](mta://scripting/client/events/onclientpedvehicleexit.md)

- onClientPedWasted

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
