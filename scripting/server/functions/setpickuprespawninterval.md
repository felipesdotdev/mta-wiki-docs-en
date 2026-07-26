---
doc_id: "mta-wiki:3841"
title: "SetPickupRespawnInterval"
source_title: "SetPickupRespawnInterval"
source_url: "https://wiki.multitheftauto.com/wiki/SetPickupRespawnInterval"
revision_id: 80380
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:43.538754+00:00"
---

# SetPickupRespawnInterval

Sets the time it takes for a pickup to respawn after a player picked it up.

## Syntax

```
bool setPickupRespawnInterval ( pickup thePickup, int ms )
```

### Required Arguments

- **thePickup:** the pickup to set the respawn time of

- **ms:** the new respawn time in ms

### Returns

Returns *true* if the new respawn time was set successfully, *false* otherwise.

## Example

This example adds 3000ms to the current pickup respawn time.

```
addEventHandler("onPickUpHit",root,function(player)
	interval = getPickupRespawnInterval(source)
	setPickupRespawnInterval(source,interval + 3000)
	outputChatBox("That pickup isn't going to be there until "..tostring(interval).." is done.",player)
end)
```

## See Also

- [getPickupRespawnInterval](mta://scripting/server/functions/getpickuprespawninterval.md)

- [isPickupSpawned](mta://scripting/server/functions/ispickupspawned.md)

- setPickupRespawnInterval

- [usePickup](mta://scripting/server/functions/usepickup.md)
  

- **Shared**

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
