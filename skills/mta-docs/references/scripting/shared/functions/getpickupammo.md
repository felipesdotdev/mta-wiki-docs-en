---
doc_id: "mta-wiki:1561"
title: "GetPickupAmmo"
source_title: "GetPickupAmmo"
source_url: "https://wiki.multitheftauto.com/wiki/GetPickupAmmo"
revision_id: 67682
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetPickupAmmo

This function retrieves the amount of ammo in a weapon pickup.

## Syntax

```
int getPickupAmmo ( pickup thePickup )
```

### Required Arguments

- **thePickup:** The pickup in which you wish to retrieve the ammo of

### Returns

Returns an *integer* of the amount of ammo in the pickup, *false* if the pickup element is invalid, 0 if it's no weapon pickup.

## Example

This example outputs a message with the picked up weapon and ammo to the player.

Click to collapse [-]
Server

```
function onPickupHitFunction ( thePlayer )
	if getPickupType ( source ) ~= 2 then return end   -- if the pickup is no weapon, stop
	local ammo = getPickupAmmo ( source )              -- get the amount of ammo
	local weapon = getPickupWeapon ( source )          -- get the weapon of the pickup
	outputChatBox ( "You just picked up a " .. getWeaponNameFromID(weapon) .. " with " .. ammo .. " ammo", thePlayer ) -- output a message to the player
end
addEventHandler ( "onPickupHit", root, onPickupHitFunction ) -- add an event handler for onPickupHit
```

## See Also

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- getPickupAmmo

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
