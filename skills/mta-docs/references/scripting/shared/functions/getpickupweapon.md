---
doc_id: "mta-wiki:1559"
title: "GetPickupWeapon"
source_title: "GetPickupWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/GetPickupWeapon"
revision_id: 73731
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetPickupWeapon

This function retrieves the weapon ID of a weapon pickup.

## Syntax

```
int getPickupWeapon ( pickup thePickup )
```

### Required Arguments

- **thePickup:** The pickup of which you wish to retrieve the weapon

### Returns

Returns the [Weapon ID](mta://reference/misc/weapons.md) of the pickup, or *false* if the pickup is invalid.

## Example

This example gives extra ammo to a player if a pickup only has a small amount of ammo.

Click to collapse [-]
Server

```
function onPickupHitFunc ( thePlayer )                  -- when a pickup is hit
    if getPickupType ( source ) == 2 then               -- check if it's a weapon pickup
        local ammo = getPickupAmmo ( source )           -- get the pickup ammo
        if ammo < 50 then                               -- if ammo is less than 50
            local weapon = getPickupWeapon ( source )   -- store pickup weapon
            giveWeaponAmmo ( thePlayer, weapon, 50 )    -- give an extra 50 ammo
        end
    end
end
addEventHandler ( "onPickupHit", root, onPickupHitFunc )    -- add the function as handler for onPickupHit
```

## See Also

**GTASA IDs (vehicles, weapons, weathers, characters, colors):** [http://info.vces.net/](https://web.archive.org/web/20100427013910/http://www.vces.net/info/index.php) (Special thanks to Brophy and Ratt for making these lists)

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- getPickupWeapon
