---
doc_id: "mta-wiki:1557"
title: "CreatePickup"
source_title: "CreatePickup"
source_url: "https://wiki.multitheftauto.com/wiki/CreatePickup"
revision_id: 76824
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# CreatePickup

This function creates a pickup element, which is placed in the GTA world and can be picked up to retrieve a health, armour or a weapon.

## Syntax

```
pickup createPickup ( float x, float y, float z, int theType, int amount/weapon/model, [ int respawnTime = 30000, int ammo = 50 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Pickup(...)*

### Required Arguments

- **x**: A floating point number representing the X coordinate on the map.

- **y**: A floating point number representing the Y coordinate on the map.

- **z**: A floating point number representing the Z coordinate on the map.

- **theType**: This is an integer representing the type of pickup, representing the following types:

- **0**: Health Pickup

- **1**: Armour Pickup

- **2**: Weapon Pickup

- **3**: Custom Pickup

- **amount**: This is an integer representing the amount of Health points or Armour points a pickup has.

**OR**

- **weapon**: If the type is a Weapon pickup, then it represents the [weapon ID](https://wiki.multitheftauto.com/index.php?search=weapon%20ID) of the weapon pickup. When used with the weapon pickup type set, the ammo parameter can be used.

**OR**

- 

- **model**: If the pickup is a custom model, this is the model id to use. Many non-pickup models can be used, though some may cause crashes. The following is a list of models designed to be used as pickups.

- **1212:** Money (wad of cash)

- **1239:** Info icon

- **1240:** Health (heart)

- **1241:** Adrenaline

- **1242:** Armour

- **1247:** Bribe

- **1248:** GTA III sign

- **1252:** Bomb from GTA III

- **1253:** Photo op

- **1254:** Skull

- **1272:** House (blue)

- **1273:** House (green)

- **1274:** Money icon

- **1275:** Blue t-shirt

- **1276:** Tiki statue

- **1277:** Save disk

- **1279:** Drug bundle

- **1310:** Parachute (with leg straps)

- **1313:** 2 Skulls

- **1314:** 2 Players icon

- **1318:** Down arrow

**OR**
Other ID Object

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **respawnTime**: How long before the pickup respawns in milliseconds (**This parameter is ignored on the client!**)

- **ammo**: An integer representing the amount of ammo a pickup contains.  This is only valid when the pickup type is a weapon pickup.

### Returns

Returns [pickup](https://wiki.multitheftauto.com/index.php?search=pickup) [element](mta://reference/misc/element.md) if the pickup was created succesfully, otherwise returns *false*.

## Example

Click to collapse [-]
Server

This example creates a pickup after a player dies so that he drops his weapon.

```
function createDeathPickup ( totalammo, killer, killerweapon, bodypart ) --when a player dies
    x, y, z = getElementPosition ( source ) --get the position of the person who died and define it as x, y and z
    currentweapon = getPlayerWeapon ( source ) --get the current weapon of the dead person
    createPickup ( x, y, z, 2, currentweapon, 10000, totalammo )
end
addEventHandler ( "onPlayerWasted", root, createDeathPickup ) --add an event handler for onPlayerWasted
```

Click to expand [+]
Server

This example creates a custom pickup(money) after a player dies and sets it's value.

```
function createDeathPickup ( totalammo, killer, killerweapon, bodypart ) --when a player dies
    x, y, z = getElementPosition ( source ) --get the position of the person who died and define it as x, y and z
    local money=createPickup ( x, y, z, 3, 1212, 10000)
    local playermoney = getPlayerMoney(source) --get the amount of money the dead person has
    setElementData(money,"Amount",playermoney) --now let's set the value of the pickup
    takePlayerMoney(source,playermoney) --Let's take away all their money
end
addEventHandler ( "onPlayerWasted", root, createDeathPickup ) --add an event handler for onPlayerWasted
```

## See Also

- createPickup

- [getPickupAmmo](mta://scripting/shared/functions/getpickupammo.md)

- [getPickupAmount](mta://scripting/shared/functions/getpickupamount.md)

- [getPickupType](mta://scripting/shared/functions/getpickuptype.md)

- [setPickupType](mta://scripting/shared/functions/setpickuptype.md)

- [getPickupWeapon](mta://scripting/shared/functions/getpickupweapon.md)
