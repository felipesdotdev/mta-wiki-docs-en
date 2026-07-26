---
doc_id: "mta-wiki:4519"
title: "Оружие"
source_title: "Оружие"
source_url: "https://wiki.multitheftauto.com/wiki/%D0%9E%D1%80%D1%83%D0%B6%D0%B8%D0%B5"
revision_id: 74857
language: "en"
categories: ["Списки_ID"]
generated_at: "2026-07-26T16:17:09.423992+00:00"
---

# Оружие

Функциям скриптинга, которые запрашивают ID оружия, требуется целое число, взятое из списка ID оружий GTA:SA. Они перечислены ниже.

| [[{{{image}}}\|link=\|]] | Примечание: Вместимость обоймы, указанная внутри "( )", указывает общую вместимость обойм, когда оружие находится в двух руках. Оружие без этой характеристики - не двуручное оружие. Навыки владения оружием GTA:SA влияют на передвижение, точность, урон и возможность брать оружие в две руки. Смотрите setPedStat , чтобы узнать как их изменять. Сервер MTA поставляется вместе с ресурсом "defaultStats", который устанавливает все навыки владения оружием GTA:SA на 999. Для получения информации по причинам смерти, в особенности при использовании обработчиков события onPlayerWasted и ему подобных, также взгляните на Причины смерти . Название совместимо с функциями getWeaponNameFromID , getWeaponIDFromName . |
| --- | --- |
|  |  |

| Слот | Тип | Изображение | Название | ID | ID модели | Боезапас | Общий боеприпас в слоте |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Рука |  | Fist | 0 | - | - | - |
|  | Brassknuckle | 1 | 331 | - |  |  |  |
| 1 | Ближний бой |  | Golfclub | 2 | 333 | - | - |
|  | Nightstick | 3 | 334 | - |  |  |  |
|  | Knife | 4 | 335 | - |  |  |  |
|  | Bat | 5 | 336 | - |  |  |  |
|  | Shovel | 6 | 337 | - |  |  |  |
|  | Poolstick | 7 | 338 | - |  |  |  |
|  | Katana | 8 | 339 | - |  |  |  |
|  | Chainsaw | 9 | 341 | - |  |  |  |
| 2 | Пистолеты |  | Colt 45 | 22 | 346 | 17 (34) | Нет Замена пистолета сбрасывает боезапас слота 2 |
|  | Silenced | 23 | 347 | 17 |  |  |  |
|  | Deagle | 24 | 348 | 7 |  |  |  |
| 3 | Дробовики |  | Shotgun | 25 | 349 | 1 | Да |
|  | Sawed-off | 26 | 350 | 2 (4) |  |  |  |
|  | Combat Shotgun | 27 | 351 | 7 |  |  |  |
| 4 | Пистолеты-пулемёты |  | Uzi | 28 | 352 | 50 (100) | Да |
|  | MP5 | 29 | 353 | 30 |  |  |  |
|  | Tec-9 | 32 | 372 | 50 (100) |  |  |  |
| 5 | Штурмовые винтовки |  | AK-47 | 30 | 355 | 30 | Да |
|  | M4 | 31 | 356 | 50 |  |  |  |
| 6 | Винтовки |  | Rifle | 33 | 357 | 1 | Нет Замена винтовки сбрасывает боезапас слота 6 |
|  | Sniper | 34 | 358 | 1 |  |  |  |
| 7 | Тяжёлое оружие |  | Rocket Launcher | 35 | 359 | 1 | Нет Замена тяжёлого оружия сбрасывает боезапас слота 7 |
|  | Rocket Launcher HS | 36 | 360 | 1 |  |  |  |
|  | Flamethrower | 37 | 361 | 50 |  |  |  |
|  | Minigun | 38 | 362 | 500 |  |  |  |
| 8 | Снаряды |  | Grenade | 16 | 342 | 1 | Нет Замена снаряда сбрасывает боезапас слота 8 |
|  | Teargas | 17 | 343 | 1 |  |  |  |
|  | Molotov | 18 | 344 | 1 |  |  |  |
|  | Satchel | 39 | 363 | 1 |  |  |  |
| 9 | Специальное 1 |  | Spraycan | 41 | 365 | 500 | Нет Замена специального 1 сбрасывает боезапас слота 9 |
|  | Fire Extinguisher | 42 | 366 | 500 |  |  |  |
|  | Camera | 43 | 367 | 36 |  |  |  |
| 10 | Подарки |  | Dildo | 10 | 321 | - | - |
|  | Dildo | 11 | 322 | - |  |  |  |
|  | Vibrator | 12 | 323 | - |  |  |  |
|  | Flower | 14 | 325 | - |  |  |  |
|  | Cane | 15 | 326 | - |  |  |  |
| 11 | Специальное 2 |  | Nightvision | 44 | 368 | - | - |
|  | Infrared | 45 | 369 | - |  |  |  |
|  | Parachute | 46 | 371 | - |  |  |  |
| 12 | Satchel детонатор |  | Bomb | 40 | 364 | - | - |

Lua-таблица всех ID оружия

```
local weapons = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 23, 24, 25, 26, 27, 28, 29, 32, 30, 31, 33, 34, 35, 36, 37, 38, 16, 17, 18, 39, 41, 42, 43, 10, 11, 12, 14, 15, 44, 45, 46, 40}
```

Lua-таблица всех ID оружия, сгруппированных по слотам

```
local weapons = {
	[0] = {0, 1},			-- Рука
	[1] = {2, 3, 4, 5, 6, 7, 8, 9},	-- Ближний бой
	[2] = {22, 23, 24},		-- Пистолеты
	[3] = {25, 26, 27},		-- Дробовики
	[4] = {28, 29, 32},		-- Пистолеты-пулемёты
	[5] = {30, 31},			-- Штурмовые винтовки
	[6] = {33, 34},			-- Винтовки
	[7] = {35, 36, 37, 38},		-- Тяжёлое оружие
	[8] = {16, 17, 18, 39},		-- Снаряды
	[9] = {41, 42, 43},		-- Специальное 1
	[10] = {10, 11, 12, 14, 15},	-- Подарки
	[11] = {44, 45, 46},		-- Специальное 2
	[12] = {40}			-- Satchel детонатор
}
```

## Смотрите также

- [Списки ID](https://wiki.multitheftauto.com/wiki/RU/Id)

### Функции сервера

#### Серверные функции

- [giveWeapon](https://wiki.multitheftauto.com/wiki/RU/giveWeapon) - *дает указанное оружие игроку или пешеходу*

- [takeAllWeapons](https://wiki.multitheftauto.com/wiki/RU/takeAllWeapons) - *удаляет всё оружие с указанного игрока или пешехода*

- [takeWeapon](https://wiki.multitheftauto.com/wiki/RU/takeWeapon) - *удаляет указанное оружие или боеприпасы с игрока или пешехода*

ДО ВЕРСИИ 1.3.1 :

- [takeWeaponAmmo](https://wiki.multitheftauto.com/wiki/RU/takeWeaponAmmo) - *удаляет определённое кол-во боеприпасов у игрока для указанного оружия*

- [giveWeaponAmmo](https://wiki.multitheftauto.com/index.php?title=RU/giveWeaponAmmo&action=edit&redlink=1) - *даёт определённое кол-во боеприпасов игроку для указанного оружия*

#### Клиентские функции

#### Общие функции

- [getOriginalWeaponProperty](https://wiki.multitheftauto.com/index.php?title=RU/getOriginalWeaponProperty&action=edit&redlink=1) - *получает исходное свойство указанного типа оружия*

- [getPickupWeapon](https://wiki.multitheftauto.com/index.php?title=RU/getPickupWeapon&action=edit&redlink=1) - *получает ID оружия из указанного пикапа*

- [getSlotFromWeapon](https://wiki.multitheftauto.com/wiki/RU/getSlotFromWeapon) - *получает слот к которому принадлежит оружие*

- [getWeaponIDFromName](https://wiki.multitheftauto.com/wiki/RU/getWeaponIDFromName) - *получает ID оружия из его названия*

- [getWeaponNameFromID](https://wiki.multitheftauto.com/wiki/RU/getWeaponNameFromID) - *получает название оружия или причину смерти из его ID*

- [getWeaponProperty](https://wiki.multitheftauto.com/index.php?title=RU/getWeaponProperty&action=edit&redlink=1) - *получает свойство указанного оружия*

- [setWeaponAmmo](https://wiki.multitheftauto.com/wiki/RU/setWeaponAmmo) - *устанавливает определенное кол-во боеприпасов для указанного оружия*

- [setWeaponProperty](https://wiki.multitheftauto.com/index.php?title=RU/setWeaponProperty&action=edit&redlink=1) - *устанавливает свойство указанного типа оружия*

### Функции клиента

### Общие функции

- [getOriginalWeaponProperty](https://wiki.multitheftauto.com/index.php?title=RU/getOriginalWeaponProperty&action=edit&redlink=1) - *получает исходное свойство указанного типа оружия*

- [getPickupWeapon](https://wiki.multitheftauto.com/index.php?title=RU/getPickupWeapon&action=edit&redlink=1) - *получает ID оружия из указанного пикапа*

- [getSlotFromWeapon](https://wiki.multitheftauto.com/wiki/RU/getSlotFromWeapon) - *получает слот к которому принадлежит оружие*

- [getWeaponIDFromName](https://wiki.multitheftauto.com/wiki/RU/getWeaponIDFromName) - *получает ID оружия из его названия*

- [getWeaponNameFromID](https://wiki.multitheftauto.com/wiki/RU/getWeaponNameFromID) - *получает название оружия или причину смерти из его ID*

- [getWeaponProperty](https://wiki.multitheftauto.com/index.php?title=RU/getWeaponProperty&action=edit&redlink=1) - *получает свойство указанного оружия*

- [setWeaponAmmo](https://wiki.multitheftauto.com/wiki/RU/setWeaponAmmo) - *устанавливает определенное кол-во боеприпасов для указанного оружия*

- [setWeaponProperty](https://wiki.multitheftauto.com/index.php?title=RU/setWeaponProperty&action=edit&redlink=1) - *устанавливает свойство указанного типа оружия*
