---
doc_id: "mta-wiki:7602"
title: "CreateEffect"
source_title: "CreateEffect"
source_url: "https://wiki.multitheftauto.com/wiki/CreateEffect"
revision_id: 82252
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.5.5"]
---

# CreateEffect

Creates an [effect](mta://reference/misc/element-effect.md) on specified position.

| [[{{{image}}}\|link=\|]] | Note: Not all effects support rotation (e.g. the "fire" - effect doesn't). |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: All effects have their own duration. |
| --- | --- |
|  |  |

## Syntax

```
effect createEffect ( string name, float x, float y, float z [, float rX, float rY, float rZ, float drawDistance = 0, bool soundEnable = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](https://wiki.multitheftauto.com/index.php?search=Effect)(...)*

### Required Arguments

- **name:** A string contains [effect name](mta://reference/misc/element-effect.md).

- **x:** A floating point number representing the X coordinate on the map.

- **y:** A floating point number representing the Y coordinate on the map.

- **z:** A floating point number representing the Z coordinate on the map.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **rX:** A floating point number representing the rotation about the X axis in degrees.

- **rY:** A floating point number representing the rotation about the Y axis in degrees.

- **rZ:** A floating point number representing the rotation about the Z axis in degrees.

- **drawDistance:** A floating point number between 1 and 8191 which represents the draw distance of the effect, or 0 to use the default draw distance.

- **soundEnable:** to enable the sound of the effect.

### Returns

Returns the [effect](mta://reference/misc/element-effect.md) element if creation was successful, *false* otherwise.

## Example

This example allows you to create effect by using 'B' key (use mouse scroll up/down to switch effect).

```
local effectSwitchUpKey = "mouse_wheel_up"
local effectSwitchDownKey = "mouse_wheel_down"
local effectCreateKey = "b"

local effectNames = {
	"blood_heli", "boat_prop", "camflash", "carwashspray", "cement", "cloudfast", "coke_puff", "coke_trail", "cigarette_smoke",
	"explosion_barrel", "explosion_crate", "explosion_door", "exhale", "explosion_fuel_car", "explosion_large", "explosion_medium",
	"explosion_molotov", "explosion_small", "explosion_tiny", "extinguisher", "flame", "fire", "fire_med", "fire_large", "flamethrower",
	"fire_bike", "fire_car", "gunflash", "gunsmoke", "insects", "heli_dust", "jetpack", "jetthrust", "nitro", "molotov_flame",
	"overheat_car", "overheat_car_electric", "prt_blood", "prt_boatsplash", "prt_bubble", "prt_cardebris", "prt_collisionsmoke",
	"prt_glass", "prt_gunshell", "prt_sand", "prt_sand2", "prt_smokeII_3_expand", "prt_smoke_huge", "prt_spark", "prt_spark_2",
	"prt_splash", "prt_wake", "prt_watersplash", "prt_wheeldirt", "petrolcan", "puke", "riot_smoke", "spraycan", "smoke30lit", "smoke30m",
	"smoke50lit", "shootlight", "smoke_flare", "tank_fire", "teargas", "teargasAD", "tree_hit_fir", "tree_hit_palm", "vent", "vent2",
	"water_hydrant", "water_ripples", "water_speed", "water_splash", "water_splash_big", "water_splsh_sml", "water_swim", "waterfall_end",
	"water_fnt_tme", "water_fountain", "wallbust", "WS_factorysmoke"
}

local effectID = 1
local effectName = effectNames[effectID]
local effectCount = (#effectNames) -- there are 82 effects

outputChatBox("Effect set to: #ffa500"..effectName.."#ffffff (ID: #ffa500"..effectID.."#ffffff)", 255, 255, 255, true)

local function createEffectManually()
	local playerX, playerY, playerZ = getElementPosition(localPlayer)
	local effectX, effectY, effectZ = playerX, playerY, (playerZ + 2)
	local effectRX, effectRY, effectRZ = 0, 0, 0
	local effectDrawDistance = 300
	local effectSoundEnable = false

	outputChatBox("Created effect: #ffa500"..effectName.."#ffffff (ID: #ffa500"..effectID.."#ffffff)", 255, 255, 255, true)
	createEffect(effectName, effectX, effectY, effectZ, effectRX, effectRY, effectRZ, effectDrawDistance, effectSoundEnable)
end
bindKey(effectCreateKey, "down", createEffectManually)

local function switchEffect(keyName)
	local effectSwitchUp = (keyName == effectSwitchUpKey)
	local effectSwitchFactor = (effectSwitchUp and 1 or -1)
	local effectSwitchTempID = (effectID + effectSwitchFactor)
	local effectSwitchID = (effectSwitchTempID > effectCount and 1 or effectSwitchTempID < 1 and effectCount or effectSwitchTempID)

	effectID = effectSwitchID
	effectName = effectNames[effectID]

	outputChatBox("Effect set to: #ffa500"..effectName.."#ffffff (ID: #ffa500"..effectID.."#ffffff)", 255, 255, 255, true)
end
bindKey(effectSwitchDownKey, "down", switchEffect)
bindKey(effectSwitchUpKey, "down", switchEffect)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.4.0-9.06892 | Added drawDistance argument |
| --- | --- |

| 1.5.4-9.11631 | Added soundEnable argument |
| --- | --- |

## See Also

- createEffect

- [fxAddBlood](mta://scripting/client/functions/fxaddblood.md)

- [fxAddBulletImpact](mta://scripting/client/functions/fxaddbulletimpact.md)

- [fxAddBulletSplash](mta://scripting/client/functions/fxaddbulletsplash.md)

- [fxAddDebris](mta://scripting/client/functions/fxadddebris.md)

- [fxAddFootSplash](mta://scripting/client/functions/fxaddfootsplash.md)

- [fxAddGlass](mta://scripting/client/functions/fxaddglass.md)

- [fxAddGunshot](mta://scripting/client/functions/fxaddgunshot.md)

- [fxAddPunchImpact](mta://scripting/client/functions/fxaddpunchimpact.md)

- [fxAddSparks](mta://scripting/client/functions/fxaddsparks.md)

- [fxAddTankFire](mta://scripting/client/functions/fxaddtankfire.md)

- [fxAddTyreBurst](mta://scripting/client/functions/fxaddtyreburst.md)

- [fxAddWaterHydrant](mta://scripting/client/functions/fxaddwaterhydrant.md)

- [fxAddWaterSplash](mta://scripting/client/functions/fxaddwatersplash.md)

- [fxAddWood](mta://scripting/client/functions/fxaddwood.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22512](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22512):

- [fxCreateParticle](mta://scripting/client/functions/fxcreateparticle.md)

- [getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
