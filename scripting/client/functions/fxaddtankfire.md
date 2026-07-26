---
doc_id: "mta-wiki:4201"
title: "FxAddTankFire"
source_title: "FxAddTankFire"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddTankFire"
revision_id: 43850
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:04.276785+00:00"
---

# FxAddTankFire

Tank fire

This function creates a tank firing particle effect.

## Syntax

```
bool fxAddTankFire ( float posX, float posY, float posZ, float dirX, float dirY, float dirZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).addTankFire(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the effect originates.

- **dirX, dirY, dirZ:** a direction vector indicating where the tank fire is directed to.

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

This example will create a Tank Fire Effect at your weapon's muzzle position

```
addEventHandler("onClientPlayerWeaponFire", root, function(weapon, ammo, ammoInClip, hitX, hitY, hitZ, hitElement)
    if weapon == 0 then return end -- If the player is unarmed, return end.
    local mX, mY, mZ = getPedWeaponMuzzlePosition(localPlayer)
    fxAddTankFire(mX, mY, mZ, 0, 90, 0)
end)
```

## See Also

- [createEffect](mta://scripting/client/functions/createeffect.md)

- [fxAddBlood](mta://scripting/client/functions/fxaddblood.md)

- [fxAddBulletImpact](mta://scripting/client/functions/fxaddbulletimpact.md)

- [fxAddBulletSplash](mta://scripting/client/functions/fxaddbulletsplash.md)

- [fxAddDebris](mta://scripting/client/functions/fxadddebris.md)

- [fxAddFootSplash](mta://scripting/client/functions/fxaddfootsplash.md)

- [fxAddGlass](mta://scripting/client/functions/fxaddglass.md)

- [fxAddGunshot](mta://scripting/client/functions/fxaddgunshot.md)

- [fxAddPunchImpact](mta://scripting/client/functions/fxaddpunchimpact.md)

- [fxAddSparks](mta://scripting/client/functions/fxaddsparks.md)

- fxAddTankFire

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
