---
doc_id: "mta-wiki:13326"
title: "OnPedDamage"
source_title: "OnPedDamage"
source_url: "https://wiki.multitheftauto.com/wiki/OnPedDamage"
revision_id: 81482
language: "en"
categories: ["Server_Events"]
---

# OnPedDamage

This event is triggered when a ped is damaged. For player damage, use [onPlayerDamage](mta://scripting/server/events/onplayerdamage.md) instead.

| [[{{{image}}}\|link=\|]] | Note: This event is not triggered prior to r21247. |
| --- | --- |
|  |  |

## Parameters

```
float loss
```

- **loss**: an [int](mta://reference/misc/int.md) representing the percentage of health the ped lost.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [ped](https://wiki.multitheftauto.com/index.php?search=ped) that got damaged.

## Cancel Effect

Canceling this event has no effect. Cancel the client-side event [onClientPedDamage](mta://scripting/client/events/onclientpeddamage.md) instead.

## Example

This example outputs a message to the console when a specific ped is damaged.

```
local ped1 = createPed(112, 0, 0, 0) -- create our ped

function pedDamaged(loss)
    outputConsole("ped1 damaged! loss: " .. tostring(loss))
end

addEventHandler("onPedDamage", ped1, pedDamaged) -- triggered only when ped1 gets damaged
```

## See Also

### Ped events

- onPedDamage

- [onPedVehicleEnter](mta://scripting/server/events/onpedvehicleenter.md)

- [onPedVehicleExit](mta://scripting/server/events/onpedvehicleexit.md)

- [onPedWasted](mta://scripting/server/events/onpedwasted.md)

- [onPedWeaponSwitch](mta://scripting/server/events/onpedweaponswitch.md)

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
