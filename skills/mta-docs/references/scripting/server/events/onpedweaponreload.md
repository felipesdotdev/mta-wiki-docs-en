---
doc_id: "mta-wiki:14611"
title: "OnPedWeaponReload"
source_title: "OnPedWeaponReload"
source_url: "https://wiki.multitheftauto.com/wiki/OnPedWeaponReload"
revision_id: 82384
language: "en"
categories: ["Server_Events"]
---

# OnPedWeaponReload

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909))

Event has been added.

This event is triggered when a ped reloads his weapons.

## Parameters

```
int weapon, int clip, int ammo
```

- **weapon**: an [int](mta://reference/misc/int.md) representing the [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) that has been reloaded.

- **clip**: an [int](mta://reference/misc/int.md) representing the [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) clip size.

- **ammo**: an [int](mta://reference/misc/int.md) representing the [weapon](https://wiki.multitheftauto.com/index.php?search=weapon) ammo.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](https://wiki.multitheftauto.com/index.php?search=ped) that reloaded his weapon.

## Example

This example outputs a line to the chat box whenever a ped reloads weapons.

```
function weaponReload(iWeaponID, iClip, iAmmo)
    outputChatBox("A ped reloaded "..getWeaponNameFromID(iWeaponID)..", clip: "..iClip..", ammo: "..iAmmo.."!");
end
addEventHandler("onPedWeaponReload", root, weaponReload);
```

## See Also

### Ped events

- [onPedDamage](mta://scripting/server/events/onpeddamage.md)

- [onPedVehicleEnter](mta://scripting/server/events/onpedvehicleenter.md)

- [onPedVehicleExit](mta://scripting/server/events/onpedvehicleexit.md)

- [onPedWasted](mta://scripting/server/events/onpedwasted.md)

- [onPedWeaponSwitch](mta://scripting/server/events/onpedweaponswitch.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909))

- onPedWeaponReload

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
