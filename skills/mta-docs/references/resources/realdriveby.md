---
doc_id: "mta-wiki:3825"
title: "Resource : Realdriveby"
source_title: "Resource:Realdriveby"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ARealdriveby"
revision_id: 19772
language: "en"
categories: ["Resource"]
---

# Resource : Realdriveby

Introduction

RealDriveby is a fully customisable resource which allows a flexible driveby system for your server.

All of GTA's driveby compatible weapons, including the shotguns,pistols,M4 and AK-47 are supported by this resource. Shot delays for weapons such as pistols are fixed to their normal rate.

Users can switch weapons by default using the "Vehicle Look Left" and "Vehicle Look Right" keys while in driveby mode.

However, it is completely up to the admin how he or she wants drivebys to be: Using MTA's settings system, shot delays for weapons can be modified; the weapons which a driver can driveby with are customisable; the weapons a passenger can driveby with are customisable.

There are also options available to disable steering whilst in driveby mode, or disable drivebys altogether for certain vehicles.

On top of this, RealDriveby provides clientside scripting functions so that users can modify these attributes on a player-basis, allowing different players the ability to driveby different weapons and different delays.

## Settings

All settings can be modified using MTA's set() functions, modifying the meta.xml of the resource, or modifying the settings.xml.

### Driver weapons

- **Setting name:** *driveby_driver*

- **Description:** Sets the weapons that a driver can driveby with.  To disable driver drivebys, just pass an empty table.  See [here](mta://resources/realdriveby.md) for compatible weapons.

- **XML Example:** 

```
<setting name="driveby_driver" value="[[ 22,23,24,26,28,29,32 ]]"/>
```

### Passenger weapons

- **Setting name:** *driveby_passenger*

- **Description:** Sets the weapons that a passenger can driveby with.  To disable passenger drivebys, just pass an empty table.  See [here](mta://resources/realdriveby.md) for compatible weapons.

- **XML Example:** 

```
<setting name="driveby_passenger" value="[[ 22,23,24,25,26,28,29,32,30,31,33 ]]"/>
```

### Shot delay

- **Setting name:** *driveby_shot_delay*

- **Description:** Sets the delay between each individual shot for the specified weapons.  Unspecified weapons have GTA's default driveby fire rate.  The setting is in the format of a table where the key is a **string** of the weapon ID, and the value is the delay in milliseconds.

- **XML Example:** 

```
<setting name="driveby_shot_delay" value="[{ '22':300,'23':300,'24':800,'26':700 }]"/>
```

### Blocked vehicles

- **Setting name:** *driveby_blocked_vehicles*

- **Description:** Sets the vehicles which driveby mode cannot be accessed in.  Useful to block strange effects such as drivebys in tanks.  In the format of an array of vehicle IDs.

- **XML Example:** 

```
<setting name="driveby_blocked_vehicles" value="[[ 432,601,437,431,592,553,577,488,497,548,563,512,476,447,425,519,520,460,417,469,487,513,441,464,501,465,564,538,449,537,539,570472,473,493,595,484,430,453,452,446,454,606,591,607,611,610,590,569,611,435,608,584,450 ]]"/>
```

### Steer Cars while in driveby mode

- **Setting name:** *driveby_steer_cars*

- **Description:** Sets whether drivers can steer left or right while in driveby mode for vehicles besides bikes.   The setting is in the format of a bool, where *true* allows steering.

- **XML Example:** 

```
<setting name="driveby_steer_cars" value="[true]"/>
```

### Steer Bikes while in driveby mode

- **Setting name:** *driveby_steer_bikes*

- **Description:** Sets whether drivers can steer left or right while in driveby mode for bikes/bicycles.  If set to false, it allows extra realism.  The setting is in the format of a bool, where *true* allows steering.

- **XML Example:** 

```
<setting name="driveby_steer_bikes" value="[true]"/>
```

### Auto-equip driveby weapon

- **Setting name:** *driveby_auto_equip*

- **Description:** Sets whether driveby mode will be enabled automatically when a player enters a vehicle.

- **XML Example:** 

```
<setting name="driveby_auto_equip" value="[false]"/>
```

### Toggle driveby mode key

- **Setting name:** *driveby_toggle_mode*

- **Description:** Sets the [key](mta://reference/misc/key-names.md) which will be used to toggle driveby mode.

- **XML Example:** 

```
<setting name="driveby_toggle_mode" value="mouse2"/>
```

### Next driveby weapon key

- **Setting name:** *driveby_next_weapon*

- **Description:** Sets the [key](mta://reference/misc/key-names.md) which will be used to change to the next driveby weapon (if there is one).

- **XML Example:** 

```
<setting name="driveby_next_weapon" value="vehicle_look_right"/>
```

### Previous driveby weapon key

- **Setting name:** *driveby_prev_weapon*

- **Description:** Sets the [key](mta://reference/misc/key-names.md) which will be used to change to the previous driveby weapon (if there is one).

- **XML Example:** 

```
<setting name="driveby_prev_weapon" value="vehicle_look_left"/>
```

## Scripting functions

All scripting functions are **clientside** and therefore only affect the **local player**.  All functions must be called using the [call](mta://scripting/shared/functions/call.md) function, e.g.

```
call(getResourceFromName("realdriveby"),"setWeaponShotDelay",22,300)
```

### setDriverDrivebyAbility

This function allows you to set what weapons the local player can use while a driver of a vehicle.

```
bool setDriverDrivebyAbility ( table weapons )
```

- **weapons:** An an array/table containing weapon IDs that the driver may use.  See [here](mta://resources/realdriveby.md) for compatible weapons.

### getDriverDrivebyAbility

This function allows you to retrive what weapons the local player can use while a driver of a vehicle.

```
table getDriverDrivebyAbility ()
```

Returns a table of the weapons that can be used as a driver.

### setPassengerDrivebyAbility

This function allows you to set what weapons the local player can use while a passenger of a vehicle.

```
bool setPassengerDrivebyAbility ( table weapons )
```

- **weapons:** An an array/table containing weapon IDs that the passenger may use.  See [here](mta://resources/realdriveby.md) for compatible weapons.

### getPassengerDrivebyAbility

This function allows you to retrive what weapons the local player can use while a passenger of a vehicle.

```
table getPassengerDrivebyAbility ()
```

Returns a table of the weapons that can be used as a passenger.

### setWeaponShotDelay

This function allows setting of a certain weapon's shot delay for the local player

```
bool setWeaponShotDelay(int weaponID, int delay)
```

- **weaponID:** An integer representing the [weapon ID](mta://reference/misc/weapons.md) of the delay that you wish to set.

- **delay:** An integer representing the delay in between each shot, in **milliseconds**.

### getWeaponShotDelay

This function allows retrieving of a certain weapon's shot delay for the local player

```
int getWeaponShotDelay(int weaponID)
```

- **weaponID:** An integer representing the [weapon ID](mta://reference/misc/weapons.md) of the delay that you wish to retrieve.

Returns an integer representing the weapon delay in between each shot.

### setDrivebySteeringAbility

This function allows setting of whether the local player can steer while in driveby mode.

```
bool setDrivebySteeringAbility( bool otherVehicles, bool bikes )
```

- **otherVehicles:** A bool representing whether steering is enabled while in any vehicle besides a bike/bicycle, where *true* represents enabled steering and *false* represents disabled steering.

- **bikes :** A bool representing whether steering is enabled while in a bike/bicycle, where *true* represents enabled steering and *false* represents disabled steering.

### getDrivebySteeringAbility

This function allows retrieving of whether the local player can steer while in driveby mode.

```
bool getDrivebySteeringAbility( string drivebyType )
```

- **drivebyType :** A string which can either be "**bike**", representing bikes/bicycles, or "**car**" representing all other vehicles.

Returns a bool of the ability of the specified type of driveby, where *true* is enabled and *false* is disabled.

### setDrivebyAutoEquip

This function allows setting of whether driveby mode is enabled automatically upon entering a vehicle, for the local player.

```
bool setDrivebyAutoEquip( bool enabled )
```

- **enabled :** A bool whether auto-equip should be enabled

### getDrivebyAutoEquip

This function allows retrieving of whether driveby mode is enabled automatically upon entering a vehicle, for the local player.

```
bool getDrivebyAutoEquip()
```

Returns a bool of whether auto-equipping is enabled.

## GTA Driveby Compatible weapons

These are weapons that are compatible with GTA/MTA's driveby mode, and can be used by this script.

| Name | ID |  | Name | ID |
| --- | --- | --- | --- | --- |
| Pistol | 22 |  | Silenced Pistol | 23 |
| Desert Eagle | 24 |  | Chrome Shotgun | 25 |
| Sawn-Off Shotgun | 26 |  | Combat Shotgun | 27 |
| Uzi | 28 |  | MP5 | 29 |
| Tec-9 | 32 |  | AK-47 | 30 |
| M4 | 31 |  | Country Rifle | 33 |
| Minigun | 38 |  |  |  |
