---
doc_id: "mta-wiki:7726"
title: "GetEffectDensity"
source_title: "GetEffectDensity"
source_url: "https://wiki.multitheftauto.com/wiki/GetEffectDensity"
revision_id: 50860
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:10.481950+00:00"
---

# GetEffectDensity

This function gets the density of certain [effect](mta://reference/misc/effect.md).

## Syntax

```
float getEffectDensity ( effect theEffect )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[effect](mta://reference/misc/effect.md):getDensity(...)*

**Variable**: *.density*

**Counterpart**: *[setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)*

### Required Arguments

- **theEffect:** The [effect](mta://reference/misc/effect.md) to get density of.

### Example

```
addCommandHandler("ses", 
function (cmd)
   local density = 4
   local x, y, z = getElementPosition (localPlayer)
   local effect = createEffect ("cement", x, y, z)
   setEffectDensity (effect, density)
   getEffectDensity (effect)
end)
```

## See also

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

- [fxAddTankFire](mta://scripting/client/functions/fxaddtankfire.md)

- [fxAddTyreBurst](mta://scripting/client/functions/fxaddtyreburst.md)

- [fxAddWaterHydrant](mta://scripting/client/functions/fxaddwaterhydrant.md)

- [fxAddWaterSplash](mta://scripting/client/functions/fxaddwatersplash.md)

- [fxAddWood](mta://scripting/client/functions/fxaddwood.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22512](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22512):

- [fxCreateParticle](mta://scripting/client/functions/fxcreateparticle.md)

- getEffectDensity

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
