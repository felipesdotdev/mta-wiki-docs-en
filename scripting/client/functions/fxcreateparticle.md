---
doc_id: "mta-wiki:14352"
title: "FxCreateParticle"
source_title: "FxCreateParticle"
source_url: "https://wiki.multitheftauto.com/wiki/FxCreateParticle"
revision_id: 79603
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0", "Utility_templates"]
generated_at: "2026-07-26T16:15:04.379051+00:00"
---

# FxCreateParticle

ADDED/UPDATED IN VERSION 1.6.0 [r22512](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22512):

Creates the given particles of the specified color. Can be useful for creating flares, toxic fumes, reward effects, etc. 

## Syntax

```
bool fxCreateParticle(string particle, float posX, float posY, float posZ, float dirX, float dirY, float dirZ, float r, float g, float b, float a [, bool randomizeColors = false, int count = 1, float brightness = 1.0, float size = 0.3, bool randomSizes = false, float life = 1.0 ])
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).createParticle(...)*

### Required Arguments

- **particle:** The name of the particle to create. See [particles](mta://reference/misc/particles.md) list.

- **posX, posY, posZ:** the world coordinates where the effect originates.

- **dirX, dirY, dirZ:** a direction vector indicating where the particles flies to.

- **r, g, b, a:** a particle color.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

 

Glass particles with base color *21, 78, 171* with randomizeColors set.

- **randomizeColors:** Specifies whether the color should be fixed (r,g,b) or randomly calculated for each particle based on the given color. This allows to create colorful effects.

- **count:** the number of flying particles to create. Depending on the particle, a very large count may cause the game to lag or freeze (50k+).

- **brightness:** the brightness. Ranges from 0 (almost black) to 1 (normal color).

- **size:** Particles size. If *randomSizes* is set then when 0 is specified the minimum size is 0.3.

- **randomSizes:** Specifies whether all particles should be the same fixed size or each particle should have a random size.

- **life:** the higher this value, the longer the particles survive before they disappear. This parameter may be ignored by some particles.

## Example

Click to collapse [-]
Client

This example creates a constant green, toxic fume over the biowell.

```
setTimer(function()
	fxCreateParticle("sand", 1271.76392, 295.11682, 20.65631, 0, 0, 1, 56, 191, 52, 255, false, 5, 1, 1, true)
end, 750, 0)
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

- [fxAddTankFire](mta://scripting/client/functions/fxaddtankfire.md)

- [fxAddTyreBurst](mta://scripting/client/functions/fxaddtyreburst.md)

- [fxAddWaterHydrant](mta://scripting/client/functions/fxaddwaterhydrant.md)

- [fxAddWaterSplash](mta://scripting/client/functions/fxaddwatersplash.md)

- [fxAddWood](mta://scripting/client/functions/fxaddwood.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22512](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22512):

- fxCreateParticle

- [getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
