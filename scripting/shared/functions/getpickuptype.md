---
doc_id: "mta-wiki:1503"
title: "GetPickupType"
source_title: "GetPickupType"
source_url: "https://wiki.multitheftauto.com/wiki/GetPickupType"
revision_id: 67674
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:18.935309+00:00"
---

# GetPickupType

This function retrieves the type of a pickup, either a health, armour or weapon pickup.

## Syntax

```
int getPickupType ( pickup thePickup )
```

### Required Arguments

- **thePickup:** The pickup you wish to retrieve the type of.

### Returns

Returns *false* if the pickup is invalid, or an integer of the type of the pickup, which include:

- **0:** Health pickup

- **1:** Armour pickup

- **2:** Weapon pickup

- **3:** Custom Pickup

## Example

This example outputs a text according on the pickup type and it's contents to the player who picks it up.

Click to collapse [-]
Server

```
function onPickupHitShow ( thePlayer )                        -- when someone hits a pickup
	local message = nil                                   -- define the 'message' variable
	local pickupType = getPickupType ( source )           -- get the pickup type and save it to the variable 'pickupType'
	if (pickupType == 0) then                             -- check the type of pickup, if it is a health pickup then...
		amount = getPickupAmount ( source )               -- get the amount of health in the pickup
		message = "You picked up " .. amount .. " health" -- save the message in the 'message' variable
	elseif (pickupType == 1) then                         -- if its a armour pickup then...
		amount = getPickupAmount(source)                  -- get the amount of amour in the pickup
		message = "You picked up " .. amount .. " armor"  -- save the message in the 'message' variable
	elseif (pickupType == 2) then                         -- if its a weapon pickup then..
		local weapon = getPickupWeapon ( source )         -- get the weapon id of the pickup
		local ammo = getPickupAmmo ( source )             -- get the ammo in the pickup
		message = "You picked up " .. getWeaponNameFromID(weapon) .. " with " .. ammo .. " ammo" -- save the message in the 'message' variable
	else
		message = "Unknown pickup type"      -- if it's neither of the above types, set the 'message' variable accordingly
	end
	outputChatBox ( message, thePlayer )             -- output the message to the player in the chatbox
end
addEventHandler ( "onPickupHit", root, onPickupHitShow ) -- add an event handler for onPickupHit
```

## See Also

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- getPickupType

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
