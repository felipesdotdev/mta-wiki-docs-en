---
doc_id: "mta-wiki:3806"
title: "UsePickup"
source_title: "UsePickup"
source_url: "https://wiki.multitheftauto.com/wiki/UsePickup"
revision_id: 80901
language: "en"
categories: ["Server_functions"]
---

# UsePickup

This function is used to simulate the player using a pickup

## Syntax

```
bool usePickup ( pickup thePickup, player thePlayer )
```

### Required Arguments

- **thePickup**: The pickup element to be picked up/used.

- **thePlayer**: The player to use the pickup.

## Example

Click to collapse [-]
Server

This example gives a random player 100% armor by using a pickup.

```
local pickup = createPickup(3,3,3,1,100) -- Create a pickup for 100% armor
usePickup(pickup,getRandomPlayer()) -- Make a random player use the pickup (shall recieve 100% armor)
```

## See Also

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
