---
doc_id: "mta-wiki:3840"
title: "GetPickupRespawnInterval"
source_title: "GetPickupRespawnInterval"
source_url: "https://wiki.multitheftauto.com/wiki/GetPickupRespawnInterval"
revision_id: 80378
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:18.924443+00:00"
---

# GetPickupRespawnInterval

Returns the time it takes before a pickup respawns after a player picked it up. The time is specified in milliseconds.

## Syntax

```
int getPickupRespawnInterval ( pickup thePickup )
```

### Required Arguments

- **thePickup:** the pickup you want the respawn time of

### Returns

Returns the respawn time of the pickup if successful, *false* in case of failure.

## Example

This example outputs to the player that picked up the pickup, that it's not going to spawn again for another ... secs.

```
addEventHandler("onPickUpHit",root,function(player)
	outputChatBox("That pickup isn't going to be there until "..tostring(getPickupRespawnInterval(source)).." is done.",player)
end)
```

## See Also

- getPickupRespawnInterval

- [isPickupSpawned](mta://scripting/server/functions/ispickupspawned.md)

- [setPickupRespawnInterval](mta://scripting/server/functions/setpickuprespawninterval.md)

- [usePickup](mta://scripting/server/functions/usepickup.md)
  

- **Shared**

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
