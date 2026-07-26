---
doc_id: "mta-wiki:3842"
title: "IsPickupSpawned"
source_title: "IsPickupSpawned"
source_url: "https://wiki.multitheftauto.com/wiki/IsPickupSpawned"
revision_id: 80379
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:58.794432+00:00"
---

# IsPickupSpawned

This function checks if a pickup is currently spawned (is visible and can be picked up) or not (a player picked it up recently).

## Syntax

```
bool isPickupSpawned ( pickup thePickup )
```

### Required Arguments

- **thePickup:** the pickup you want to check.

### Returns

Returns *true* if the pickup is spawned, *false* if it's not spawned or an invalid pickup was specified.

## Example

This example outputs to the player that' using the pick that the pickup is either available/unavailable.

```
addEventHandler("onPickupUse",root,function(player)
	if(isPickupSpawned(source))then
		outputChatBox("The pickup your using is now available to use pick up again.",player)
	else
		outputChatBox("This pickup might be the last pickup to use ever again.",player)
	end
end)
```

## See Also

- [getPickupRespawnInterval](mta://scripting/server/functions/getpickuprespawninterval.md)

- isPickupSpawned

- [setPickupRespawnInterval](mta://scripting/server/functions/setpickuprespawninterval.md)

- [usePickup](mta://scripting/server/functions/usepickup.md)
  

- **Shared**

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
