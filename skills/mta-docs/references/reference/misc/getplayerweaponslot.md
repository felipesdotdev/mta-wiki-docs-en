---
doc_id: "mta-wiki:2390"
title: "GetPlayerWeaponSlot"
source_title: "GetPlayerWeaponSlot"
source_url: "https://wiki.multitheftauto.com/wiki/GetPlayerWeaponSlot"
revision_id: 44590
language: "en"
categories: ["Deprecated"]
---

# GetPlayerWeaponSlot

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getPedWeaponSlot instead. |  |

This function gets the player's weapon slot.

## Syntax

```
int getPlayerWeaponSlot ( player thePlayer )
```

### Required Arguments

- **thePlayer**: the [player](https://wiki.multitheftauto.com/index.php?search=player) you want to get the weapon slot from.

### Optional Arguments

none

### Returns

Returns the weapon slot (as *number*) on success, returns *false* otherwise.

Weapon Slots

- **0:** WEAPONSLOT_TYPE_UNARMED

- **1:** WEAPONSLOT_TYPE_MELEE

- **2:** WEAPONSLOT_TYPE_HANDGUN

- **3:** WEAPONSLOT_TYPE_SHOTGUN

- **4:** WEAPONSLOT_TYPE_SMG (used for driveby's)

- **5:** WEAPONSLOT_TYPE_RIFLE

- **6:** WEAPONSLOT_TYPE_SNIPER

- **7:** WEAPONSLOT_TYPE_HEAVY

- **8:** WEAPONSLOT_TYPE_THROWN

- **9:** WEAPONSLOT_TYPE_SPECIAL

- **10:** WEAPONSLOT_TYPE_GIFT

- **11:** WEAPONSLOT_TYPE_PARACHUTE

- **12:** WEAPONSLOT_TYPE_DETONATOR

## Example

```
Pending.
```

## See Also

- [SetPlayerWeaponSlot](mta://scripting/shared/functions/setplayerweaponslot.md)
