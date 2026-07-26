---
doc_id: "mta-wiki:4593"
title: "OnPedWeaponSwitch"
source_title: "OnPedWeaponSwitch"
source_url: "https://wiki.multitheftauto.com/wiki/OnPedWeaponSwitch"
revision_id: 59512
language: "en"
categories: ["Server_Events"]
---

# OnPedWeaponSwitch

This event is triggered when a ped switches weapons.

## Parameters

```
int previousWeaponID, int currentWeaponID
```

- **previousWeaponID**: an [int](mta://reference/misc/int.md) representing the [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) that was switched from.

- **currentWeaponID**: an [int](mta://reference/misc/int.md) representing the [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) that was switched to.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](https://wiki.multitheftauto.com/index.php?search=ped) that switched his weapon.

## Example

This example outputs a line to the chat box whenever a ped changes weapons.

```
function weaponSwitch ( previousWeaponID, currentWeaponID )

outputChatBox("A ped switched weapons from " .. previousWeaponID .. " to " .. currentWeaponID .. "!")

end

addEventHandler ( "onPedWeaponSwitch", getRootElement(), weaponSwitch )
```

## See Also

### Ped events

- [onPedDamage](mta://scripting/server/events/onpeddamage.md)

- [onPedVehicleEnter](mta://scripting/server/events/onpedvehicleenter.md)

- [onPedVehicleExit](mta://scripting/server/events/onpedvehicleexit.md)

- [onPedWasted](mta://scripting/server/events/onpedwasted.md)

- onPedWeaponSwitch

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909))

- [onPedWeaponReload](mta://scripting/server/events/onpedweaponreload.md)

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
