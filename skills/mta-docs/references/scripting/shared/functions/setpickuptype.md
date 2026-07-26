---
doc_id: "mta-wiki:1562"
title: "SetPickupType"
source_title: "SetPickupType"
source_url: "https://wiki.multitheftauto.com/wiki/SetPickupType"
revision_id: 67683
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# SetPickupType

This function allows changing the type of a pickup to a Weapon, Armour or Health pickup, and allows you to set the health points **or** the weapon and ammo that the pickup will give.

## Syntax

```
bool setPickupType ( pickup thePickup, int theType, int amount/weapon/model [, int ammo ] )
```

### Required Arguments

- **thePickup:** The pickup which you wish to change the settings of

- **theType**: An integer representing the type of pickup. You can choose from:

- **0**: Health Pickup

- **1**: Armour Pickup

- **2**: Weapon Pickup

- **3**: Custom Pickup

- **amount**: This is an integer representing the amount of Health points or Armour points a pickup has.

**OR**

- **weapon**: If the type is a Weapon pickup, then it represents the [weapon ID](https://wiki.multitheftauto.com/index.php?search=weapon%20ID) of the weapon pickup the 'ammo' field must be entered if the type is Weapon Pickup.

**OR**

- **model**: If the pickup is a custom model, this is the model id to use. Many non-pickup models can be used, though some may cause crashes. The following is a list of models designed to be used as pickups.

- **370:** Jetpack

- **1240:** Health (heart)

- **1242:** Armour

- **1272:** House (blue)

- **1273:** House (green)

- **1274:** Money (dollar symbol)

- **1277:** Save (floppy disk)

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **ammo**: An integer representing the amount of ammo a pickup contains. This argument is only valid when the pickup type is a Weapon Pickup, and must be specified in that case.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

This example changes the pickup time every time someone hits it

Click to collapse [-]
Server

```
function onPickupHit ( )                          -- when a pickup is hit
    local currenttype = getPickupType ( source )  -- get the current type of the pickup and store it in 'currenttype'
    if currenttype == 0 then                      -- if it is currently a health pickup
        setPickupType ( source, 1, 100 )          -- change it to an armour pickup with 100 hp
    elseif currenttype == 1 then                  -- else, if it is currently an armour pickup
        setPickupType ( source, 2, 29, 100 )      -- change it to an mp5 weapon pickup with 100 ammo
    elseif currenttype == 2 then                  -- lastly, if it is already a weapon
        setPickupType ( source, 0, 100 )           -- change it to a health pickup
    end
end
addEventHandler ( "onPickupHit", root, onPickupHit ) -- add an event handler for onPickupHit
```

This example changes a local player's pickup every time the spacebar key is pressed down

Click to collapse [-]
Client

```
function changeMyPickupType ( key, keyState )
    local currenttype = getPickupType ( myPickup )  -- get the current type of the pickup and store it in 'currenttype'
    if currenttype == 0 then                      -- if it is currently a health pickup
        setPickupType ( myPickup, 1, 100 )          -- change it to an armour pickup with 100 hp
    elseif currenttype == 1 then                  -- else, if it is currently an armour pickup
        setPickupType ( myPickup, 2, 29, 100 )      -- change it to an mp5 weapon pickup with 100 ammo
    elseif currenttype == 2 then                  -- lastly, if it is already a weapon
        setPickupType ( myPickup, 0, 100 )          -- change it to a health pickup
    end
end

function clientsideResourceStart ()
	myPickup = createPickup ( 10.0, 10.0, 3.11, 0, 100 ) -- create myPickup at resource start
	bindKey ( "space", "down", changeMyPickupType ) --bind spacebar to changeMyPickupType function
end
addEventHandler ( "onClientResourceStart", resourceRoot, clientsideResourceStart )
```

## See Also

- [createPickup](mta://scripting/shared/functions/createpickup.md)

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- setPickupType

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
