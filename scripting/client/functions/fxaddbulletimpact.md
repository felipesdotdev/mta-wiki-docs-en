---
doc_id: "mta-wiki:4202"
title: "FxAddBulletImpact"
source_title: "FxAddBulletImpact"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddBulletImpact"
revision_id: 63046
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:04.081879+00:00"
---

# FxAddBulletImpact

Bullet impact

Creates a bullet impact particle effect, consisting of a small smoke cloud and a number of sparks.

## Syntax

```
bool fxAddBulletImpact ( float posX, float posY, float posZ, float dirX, float dirY, float dirZ [, int smokeSize = 1, int sparkCount = 1, float smokeIntensity = 1.0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).addBulletImpact(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the effect originates.

- **dirX, dirY, dirZ:** a vector indicating the direction of the effect.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **smokeSize:** the size of the smoke cloud.

- **sparkCount:** the number of sparks to create.

- **smokeIntensity:** the amount/transparency of smoke, ranges from 0 to 1.

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

This example will create a Bullet Impact Effect on the position of the bullet impact.

```
addEventHandler("onClientPlayerWeaponFire", root, function(weapon, ammo, ammoInClip, hitX, hitY, hitZ, hitElement)
    if weapon == 0 then return end -- If the player is unarmed, return end.
    fxAddBulletImpact(hitX, hitY, hitZ, 0, 0, 0, math.random(1, 2), math.random(2, 5), 1.0)
end)
```

## See Also

- [createEffect](mta://scripting/client/functions/createeffect.md)

- [fxAddBlood](mta://scripting/client/functions/fxaddblood.md)

- fxAddBulletImpact

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
