---
doc_id: "mta-wiki:4205"
title: "FxAddBulletSplash"
source_title: "FxAddBulletSplash"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddBulletSplash"
revision_id: 43843
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:04.113483+00:00"
---

# FxAddBulletSplash

Bullet splash

This function creates a bullet splash particle effect, normally created when shooting into water.

## Syntax

```
bool fxAddBulletSplash ( float posX, float posY, float posZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).addBulletSplash(...)*

### Required Arguments

- **posX:** A float representing the **x** position of the splash

- **posY:** A float representing the **y** position of the splash

- **posZ:** A float representing the **z** position of the splash

### Returns

Returns a true if the operation was successful, false otherwise.

### Example

Click to collapse [-]
Client

This example will add a Bullet Splash Effect next to your player when typing */bsplash* in the Chatbox.

```
addCommandHandler("bsplash", function()
    local x, y, z = getElementPosition(localPlayer)
    local gz = getGroundPosition(x, y, z)
    fxAddBulletSplash(x, y, gz)
end)
```

## See Also

- [createEffect](mta://scripting/client/functions/createeffect.md)

- [fxAddBlood](mta://scripting/client/functions/fxaddblood.md)

- [fxAddBulletImpact](mta://scripting/client/functions/fxaddbulletimpact.md)

- fxAddBulletSplash

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
