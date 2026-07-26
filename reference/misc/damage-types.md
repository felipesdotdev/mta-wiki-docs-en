---
doc_id: "mta-wiki:5582"
title: "Damage Types"
source_title: "Damage Types"
source_url: "https://wiki.multitheftauto.com/wiki/Damage_Types"
revision_id: 77166
language: "en"
categories: ["ID_Lists"]
generated_at: "2026-07-26T16:11:26.054192+00:00"
---

# Damage Types

The following damage types are used by events like [onPlayerDamage](mta://scripting/server/events/onplayerdamage.md) or [onPlayerWasted](mta://scripting/server/events/onplayerwasted.md) for the **weapon** argument to describe the reason, why a [ped](mta://reference/misc/ped.md) has been damaged or died.  

When a player was shot by a weapon, the respective weapon ID is the damage type ID. The weapon IDs can be found [here](mta://reference/misc/weapons.md).

| ID | Damage type | Additional info |
| --- | --- | --- |
| 19 | Rocket | Actual damage type when damaged from a rocket launcher |
| 37 | Burnt | This is used by a damage by fire, even when the fire is created by a rocket explosion or a molotov |
| 49 | Rammed |  |
| 50 | Ranover | This is also called when damaged because of helicopter blades |
| 51 | Explosion | This may sometimes also be used at an indirect damage through an exploding rocket |
| 52 | Driveby | This is NOT used for a driveby kill with e.g. the 'realdriveby' resource |
| 53 | Drowned |  |
| 54 | Fall |  |
| 55 | Unknown | No known information about this damage type |
| 56 | Melee | Seems to be never called (?); for an actual melee damage, the fist weapon ID (0) is used (see here ) |
| 57 | Weapon | Seems to be never called (?) |
| 59 | Tank Grenade |  |
| 63 | Blown | Actual damage type when dying in a vehicle explosion |

Damage types in Lua table:

```
local damageTypes = {
	[19] = "Rocket",
	[37] = "Burnt",
	[49] = "Rammed",
	[50] = "Ranover/Helicopter Blades",
	[51] = "Explosion",
	[52] = "Driveby",
	[53] = "Drowned",
	[54] = "Fall",
	[55] = "Unknown",
	[56] = "Melee",
	[57] = "Weapon",
	[59] = "Tank Grenade",
	[63] = "Blown"
}
```
