---
doc_id: "mta-wiki:2395"
title: "Weapons"
source_title: "Weapons"
source_url: "https://wiki.multitheftauto.com/wiki/Weapons"
revision_id: 82103
language: "en"
categories: ["ID_Lists"]
generated_at: "2026-07-26T16:17:06.859207+00:00"
---

# Weapons

Scripting functions that ask for a weapon ID need an integer that refers to the GTASA weapon ID list. They are listed below.

| [[{{{image}}}\|link=\|]] | Note: Clip size () denotes clip size when the weapon is dual wielded. Weapons without this specification are not dual wield weapons. GTASA weapon stats will affect movement, accuracy, damage, and dual wield capability. See setPedStat to change these stats. The default MTA server package comes with a resource called "defaultStats" that sets GTASA weapon stats to 999. See the weapon stats link for more info. For death reasons, especially in event handlers for onPlayerWasted or similar, also have a look at the Damage Types . Name is compatible with functions getWeaponNameFromID , getWeaponIDFromName . Bullet Sync refers to whether they are triggered by the OnPlayerWeaponFire event. |
| --- | --- |
|  |  |

| Slot | Type | Image | Name | ID | Model ID | Clip | Sharing slot ammo | Bullet Sync |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hand |  | Fist | 0 | - | - | - | No |
|  | Brassknuckle | 1 | 331 | - |  |  |  |  |
| 1 | Melee |  | Golfclub | 2 | 333 | - | - | No |
|  | Nightstick | 3 | 334 | - |  |  |  |  |
|  | Knife | 4 | 335 | - |  |  |  |  |
|  | Bat | 5 | 336 | - |  |  |  |  |
|  | Shovel | 6 | 337 | - |  |  |  |  |
|  | Poolstick | 7 | 338 | - |  |  |  |  |
|  | Katana | 8 | 339 | - |  |  |  |  |
|  | Chainsaw | 9 | 341 | - |  |  |  |  |
| 2 | Handguns |  | Colt 45 | 22 | 346 | 17 (34) | No Replacing handgun resets slot 2 ammo | Yes |
|  | Silenced | 23 | 347 | 17 |  |  |  |  |
|  | Deagle | 24 | 348 | 7 |  |  |  |  |
| 3 | Shotguns |  | Shotgun | 25 | 349 | 1 | Yes | Yes |
|  | Sawed-off | 26 | 350 | 2 (4) |  |  |  |  |
|  | Combat Shotgun | 27 | 351 | 7 |  |  |  |  |
| 4 | Sub-Machine Guns |  | Uzi | 28 | 352 | 50 (100) | Yes | Yes |
|  | MP5 | 29 | 353 | 30 |  |  |  |  |
|  | Tec-9 | 32 | 372 | 50 (100) |  |  |  |  |
| 5 | Assault Rifles |  | AK-47 | 30 | 355 | 30 | Yes | Yes |
|  | M4 | 31 | 356 | 50 |  |  |  |  |
| 6 | Rifles |  | Rifle | 33 | 357 | 1 | No Replacing rifle resets slot 6 ammo | Yes |
|  | Sniper | 34 | 358 | 1 |  |  |  |  |
| 7 | Heavy Weapons |  | Rocket Launcher | 35 | 359 | 1 | No Replacing heavy weapon resets slot 7 ammo | No |
|  | Rocket Launcher HS | 36 | 360 | 1 |  |  |  |  |
|  | Flamethrower | 37 | 361 | 50 |  |  |  |  |
|  | Minigun | 38 | 362 | 500 |  |  |  |  |
| 8 | Projectiles |  | Grenade | 16 | 342 | 1 | No Replacing projectile resets slot 8 ammo | No |
|  | Teargas | 17 | 343 | 1 |  |  |  |  |
|  | Molotov | 18 | 344 | 1 |  |  |  |  |
|  | Satchel | 39 | 363 | 1 |  |  |  |  |
| 9 | Special 1 |  | Spraycan | 41 | 365 | 500 | No Replacing slot 9 weapon resets slot 9 ammo | No |
|  | Fire Extinguisher | 42 | 366 | 500 |  |  |  |  |
|  | Camera | 43 | 367 | 36 |  |  |  |  |
| 10 | Gifts |  | Dildo | 10 | 321 | - | - | No |
|  | Purple Dildo | 11 | 322 | - |  |  |  |  |
|  | Vibrator | 12 | 323 | - |  |  |  |  |
|  | Silver Vibrator | 13 | 324 | - |  |  |  |  |
|  | Flower | 14 | 325 | - |  |  |  |  |
|  | Cane | 15 | 326 | - |  |  |  |  |
| 11 | Special 2 |  | Nightvision | 44 | 368 | - | - | No |
|  | Infrared | 45 | 369 | - |  |  |  |  |
|  | Parachute | 46 | 371 | - |  |  |  |  |
| 12 | Satchel Detonator |  | Bomb | 40 | 364 | - | - | No |

Lua tables with weapons:

```
local weaponsID = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33, 34, 35, 36, 37, 38, 16, 17, 18, 39, 41, 42, 43, 10, 11, 12, 13, 14, 15, 44, 45, 46, 40}
local weaponsBySlot = {
	[0] = {0, 1}, -- hand
	[1] = {2, 3, 4, 5, 6, 7, 8, 9},	-- melee
	[2] = {22, 23, 24}, -- handguns
	[3] = {25, 26, 27}, -- shotguns
	[4] = {28, 29, 32}, -- sub-machine guns
	[5] = {30, 31}, -- assault rifles
	[6] = {33, 34}, -- rifles
	[7] = {35, 36, 37, 38}, -- heavy weapons
	[8] = {16, 17, 18, 39}, -- projectiles
	[9] = {41, 42, 43}, -- special 1
	[10] = {10, 11, 12, 13, 14, 15}, -- gifts
	[11] = {44, 45, 46}, -- special 2
	[12] = {40}, -- satchel detonator
}
```

## Functions

- [giveWeapon](mta://scripting/server/functions/giveweapon.md)

- [takeAllWeapons](mta://scripting/server/functions/takeallweapons.md)

- [takeWeapon](mta://scripting/server/functions/takeweapon.md)
  

- **Shared**

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

## See Also

- [Ids](mta://reference/misc/id--474ae526.md)
