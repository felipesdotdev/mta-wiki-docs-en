---
doc_id: "mta-wiki:5955"
title: "SetWeaponProperty"
source_title: "SetWeaponProperty"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponProperty"
revision_id: 81036
language: "en"
categories: ["Changes_in_1.3", "Changes_in_1.4", "Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:49.759303+00:00"
---

# SetWeaponProperty

Click to collapse [-]
Server

This function sets the weapon property of the specified weapons specified weapon type. See lower down the page for documentation related to weapon creation.

## Syntax

```
bool setWeaponProperty ( int weaponID/string weaponName, string weaponSkill, string property, int/float theValue )
```

## Required Arguments

- **weaponID:** The ID or name of the [weapon](mta://reference/misc/weapons.md) you want to set a property of. Names can be:

- grenade

- teargas

- molotov

- colt 45

- silenced

- deagle

- shotgun

- sawed-off

- combat shotgun

- uzi

- mp5

- ak-47

- m4

- tec-9

- rifle

- sniper

- rocket launcher

- rocket launcher hs

- flamethrower

- minigun

- satchel

- bomb

- spraycan

- fire extinguisher

- camera

- **weaponSkill:** Either: "pro", "std" or "poor". The player must have this skill level set to have the effect.

- **property:** The property you want to set the value of:

- "weapon_range" - *float*

- "target_range" - *float* - **Max targeting range**

- "accuracy" - *float*

- "damage" - *int* - **Note: Changing the standard M4 stat will change how much damage vehicle guns (e.g: Rustler) do.**

- "maximum_clip_ammo" - *int*

- "move_speed" - *float* - **How fast player can move with weapon**

- "flags" - *int* - **(specify a flag to toggle it on/off) See [Weapon Flags](mta://reference/misc/weapon-flags.md)**

- "flag_aim_no_auto" - *bool* - **Disable auto up/down for non-aimed firing**

- "flag_aim_arm" - *bool* - **Uses other arm for aiming**

- "flag_aim_1st_person" - *bool* - **Uses 1st person aim**

- "flag_aim_free" - *bool* - **Can only use free aiming**

- "flag_move_and_aim" - *bool* - **Can move and aim at same time**

- "flag_move_and_shoot" - *bool* - **Can move and fire at same time**

- "flag_type_throw" - *bool* - **Is a throwing weapon**

- "flag_type_heavy" - *bool* - **Can't jump**

- "flag_type_constant" - *bool* - **Fires every frame within loop (ie paint spray)**

- "flag_type_dual" - *bool* - **Can use 2x guns at same time**

- "flag_anim_reload" - *bool* - **Weapon has reload anims**

- "flag_anim_crouch" - *bool* - **Has crouching anims**

- "flag_anim_reload_loop" - *bool* - **Loop from end of reload to fire loop start**

- "flag_anim_reload_long" - *bool* - **Force a longer reload time**

- "flag_shot_slows" - *bool* - **Slows down (area effect)**

- "flag_shot_rand_speed" - *bool* - **Random speed (area effect)**

- "flag_shot_anim_abrupt" - *bool* - **Force the anim to finish player after aim/fire rather than blending out (area effect)**

- "flag_shot_expands" - *bool* - **Expands (area effect)**

- "anim_loop_start" - *float* - **Start of aimed firing animation loop**

- "anim_loop_stop" - *float* - **End of aimed firing animation loop (Reduce to increase firing rate)**

- "anim_loop_bullet_fire" - *float* - **Time in aimed firing animation when weapon should be fired (Must be between Start and End)**

- "anim2_loop_start" - *float* - **Start of non-aimed firing animation2 loop**

- "anim2_loop_stop" - *float* - **End of non-aimed firing animation2 loop (Reduce to increase crouch firing rate)**

- "anim2_loop_bullet_fire" - *float* - **Time in non-aimed firing animation2 when weapon should be fired (Must be between Start and End)**

- "anim_breakout_time" - *float* - **Time after which player can break out of attack and run off**

- **theValue:** The value to set the property to.

## Returns

On success:

**bool:** Returns true if the weapon property was successfully set

On failure:

**bool:** Returns false if the weapon property was unable to be set

Click to collapse [-]
Client

The client side function only applies to custom weapons created client sided.

## Syntax

```
bool setWeaponProperty ( weapon theWeapon, string strProperty, value theValue )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[weapon](mta://reference/misc/element-weapon.md):setProperty(...)*

**Counterpart**: *[getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)*

## Required Arguments

- **theWeapon:** the weapon to change the property of.

- **strProperty:** the property to edit:

- "weapon_range" - float

- "target_range" - float

- "accuracy" - float

- "damage" - int

ADDED/UPDATED IN VERSION 1.4 [r6693](http://code.google.com/p/mtasa-blue/source/detail?r=6693):

- "fire_rotation" - vector - *For aligning fire direction with model*

- **theValue:** The value to set the property to.

## Returns

Returns *true* if the property was set.

## Example

Click to collapse [-]
Server

This example sets the weapon range of the M4 at poor skill level to 75

```
local rangeSet = setWeaponProperty(31, "poor", "weapon_range", 75)
if (rangeSet) then
    outputChatBox("M4 range at poor skill is set now 75!")
end
```

This example makes the silenced pistol dual wielded at pro skill level

```
setWeaponProperty(23, "pro", "flags", 0x000800) -- Warning - Depends on the current flag setting
setWeaponProperty(23, "pro", "flags", 0x000002) -- Warning - Depends on the current flag setting
setWeaponProperty(23, "pro", "maximum_clip_ammo", 34)
```

This examples doubles the range of the colt 45 hand gun

```
setWeaponProperty(22, "poor", "weapon_range", 70)
setWeaponProperty(22, "std", "weapon_range", 70)
setWeaponProperty(22, "pro", "weapon_range", 70)
```

This example makes the minigun able to fire all its ammo without the short reload time

```
setWeaponProperty("minigun", "pro", "maximum_clip_ammo", 1000)
```

This example turns off auto aim for all weapons

```
function setAutoAimForAllWeapons( bEnable )
    weaponList = { "colt 45", "silenced", "deagle", "shotgun", "sawed-off", "combat shotgun", "uzi", "mp5", "ak-47", "m4", "tec-9", "rifle", "sniper", "minigun" }
    for _,weapon in ipairs( weaponList ) do
        for _,skill in ipairs( { "poor", "std", "pro" } ) do
            setWeaponPropertyFlag( weapon, skill, 0x0001, not bEnable )
        end
    end
end

-- Set or clear an individual weapon flag bit
function setWeaponPropertyFlag( weapon, skill, flagBit, bSet )
    local bIsSet = bitAnd( getWeaponProperty(weapon, skill, "flags"), flagBit ) ~= 0
    if bIsSet ~= bSet then
        setWeaponProperty(weapon, skill, "flags", flagBit)
    end
end

-- Turn off auto aim
setAutoAimForAllWeapons( false )
```

## Changelog

| Version | Description |
| --- | --- |

| 1.4.0-9.06339 | Added 'fire_rotation' property |
| --- | --- |

## See also

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- setWeaponProperty
