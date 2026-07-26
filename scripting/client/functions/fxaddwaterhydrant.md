---
doc_id: "mta-wiki:4197"
title: "FxAddWaterHydrant"
source_title: "FxAddWaterHydrant"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddWaterHydrant"
revision_id: 45722
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:04.315631+00:00"
---

# FxAddWaterHydrant

Water hydrant

This function creates a water hydrant particle effect.

## Syntax

```
bool fxAddWaterHydrant ( float posX, float posY, float posZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).addWaterHydrant(...)*

### Required Arguments

- **posX:** A float representing the **x** position of the hydrant

- **posY:** A float representing the **y** position of the hydrant

- **posZ:** A float representing the **z** position of the hydrant

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

This example will create 20 water hydrant effects around the players position when they use the command: hydrantmania.

```
function createHydrants()
	local x, y, z = getElementPosition(localPlayer) -- Get your location.
	for i=0, 20 do -- 20 Hydrants.
		fxAddWaterHydrant(x + math.random(-5,5), y + math.random(-5,5), z) -- Using math.random, and your current location 20 water hydrants are created.
	end
end
addCommandHandler("hydrantmania", createHydrants)
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

- fxAddWaterHydrant

- [fxAddWaterSplash](mta://scripting/client/functions/fxaddwatersplash.md)

- [fxAddWood](mta://scripting/client/functions/fxaddwood.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22512](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22512):

- [fxCreateParticle](mta://scripting/client/functions/fxcreateparticle.md)

- [getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
