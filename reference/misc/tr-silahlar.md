---
doc_id: "mta-wiki:14481"
title: "Tr/Silahlar"
source_title: "Tr/Silahlar"
source_url: "https://wiki.multitheftauto.com/wiki/Tr/Silahlar"
revision_id: 81094
language: "en"
categories: ["ID_Lists"]
generated_at: "2026-07-26T16:17:00.741432+00:00"
---

# Tr/Silahlar

Silah ID'si isteyen betik işlevleri, GTASA silah ID listesine atıfta bulunan bir tam sayı gerektirir. Aşağıda listelenmiştir.

| [[{{{image}}}\|link=\|]] | Note: Şarjör boyutu () çift elle kullanıldığında şarjör boyutunu belirtir. Bu belirtme olmayan silahlar çift elle kullanılan silahlar değildir. GTASA silah istatistikleri , hareketi, doğruluğu, hasarı ve çift elle kullanabilme yeteneğini etkiler. Bu istatistikleri değiştirmek için setPedStat komutuna bakın. Varsayılan MTA sunucu paketi, GTASA silah istatistiklerini 999 olarak ayarlayan "defaultStats" adlı bir kaynakla birlikte gelir. Daha fazla bilgi için silah istatistikleri bağlantısına bakın. Özellikle onPlayerWasted veya benzeri etkinlik işleyicilerindeki ölüm sebepleri için, Damage Types 'a da göz atın. Name şu işlevlerle uyumludur: getWeaponNameFromID , getWeaponIDFromName . |
| --- | --- |
|  |  |

| Slot | Type | Image | Name | ID | Model ID | Clip | Sharing slot ammo |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Hand |  | Fist | 0 | - | - | - |
|  | Brassknuckle | 1 | 331 | - |  |  |  |
| 1 | Melee |  | Golfclub | 2 | 333 | - | - |
|  | Nightstick | 3 | 334 | - |  |  |  |
|  | Knife | 4 | 335 | - |  |  |  |
|  | Bat | 5 | 336 | - |  |  |  |
|  | Shovel | 6 | 337 | - |  |  |  |
|  | Poolstick | 7 | 338 | - |  |  |  |
|  | Katana | 8 | 339 | - |  |  |  |
|  | Chainsaw | 9 | 341 | - |  |  |  |
| 2 | Handguns |  | Colt 45 | 22 | 346 | 17 (34) | No Replacing handgun resets slot 2 ammo |
|  | Silenced | 23 | 347 | 17 |  |  |  |
|  | Deagle | 24 | 348 | 7 |  |  |  |
| 3 | Shotguns |  | Shotgun | 25 | 349 | 1 | Yes |
|  | Sawed-off | 26 | 350 | 2 (4) |  |  |  |
|  | Combat Shotgun | 27 | 351 | 7 |  |  |  |
| 4 | Sub-Machine Guns |  | Uzi | 28 | 352 | 50 (100) | Yes |
|  | MP5 | 29 | 353 | 30 |  |  |  |
|  | Tec-9 | 32 | 372 | 50 (100) |  |  |  |
| 5 | Assault Rifles |  | AK-47 | 30 | 355 | 30 | Yes |
|  | M4 | 31 | 356 | 50 |  |  |  |
| 6 | Rifles |  | Rifle | 33 | 357 | 1 | No Replacing rifle resets slot 6 ammo |
|  | Sniper | 34 | 358 | 1 |  |  |  |
| 7 | Heavy Weapons |  | Rocket Launcher | 35 | 359 | 1 | No Replacing heavy weapon resets slot 7 ammo |
|  | Rocket Launcher HS | 36 | 360 | 1 |  |  |  |
|  | Flamethrower | 37 | 361 | 50 |  |  |  |
|  | Minigun | 38 | 362 | 500 |  |  |  |
| 8 | Projectiles |  | Grenade | 16 | 342 | 1 | No Replacing projectile resets slot 8 ammo |
|  | Teargas | 17 | 343 | 1 |  |  |  |
|  | Molotov | 18 | 344 | 1 |  |  |  |
|  | Satchel | 39 | 363 | 1 |  |  |  |
| 9 | Special 1 |  | Spraycan | 41 | 365 | 500 | No Replacing slot 9 weapon resets slot 9 ammo |
|  | Fire Extinguisher | 42 | 366 | 500 |  |  |  |
|  | Camera | 43 | 367 | 36 |  |  |  |
| 10 | Gifts |  | Dildo | 10 | 321 | - | - |
|  | Dildo | 11 | 322 | - |  |  |  |
|  | Vibrator | 12 | 323 | - |  |  |  |
|  | Flower | 14 | 325 | - |  |  |  |
|  | Cane | 15 | 326 | - |  |  |  |
| 11 | Special 2 |  | Nightvision | 44 | 368 | - | - |
|  | Infrared | 45 | 369 | - |  |  |  |
|  | Parachute | 46 | 371 | - |  |  |  |
| 12 | Satchel Detonator |  | Bomb | 40 | 364 | - | - |

Tüm silah kimliklerinin Lua tablosu.

```
local weaponsID = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33, 34, 35, 36, 37, 38, 16, 17, 18, 39, 41, 42, 43, 10, 11, 12, 14, 15, 44, 45, 46, 40}
```

Slot'a göre gruplandırılmış tüm silah kimliklerinin Lua tablosu.

```
local weaponsBySlot = {
	[0] = {0, 1}, -- Hand
	[1] = {2, 3, 4, 5, 6, 7, 8, 9},	-- Melee
	[2] = {22, 23, 24}, -- Handguns
	[3] = {25, 26, 27}, -- Shotguns
	[4] = {28, 29, 32}, -- Sub-Machine Guns
	[5] = {30, 31}, -- Assault Rifles
	[6] = {33, 34}, -- Rifles
	[7] = {35, 36, 37, 38}, -- Heavy Weapons
	[8] = {16, 17, 18, 39}, -- Projectiles
	[9] = {41, 42, 43}, -- Special 1
	[10] = {10, 11, 12, 14, 15}, -- Gifts
	[11] = {44, 45, 46}, -- Special 2
	[12] = {40}, -- Satchel Detonator
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
