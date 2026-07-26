---
doc_id: "mta-wiki:4198"
title: "FxAddWood"
source_title: "FxAddWood"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddWood"
revision_id: 63042
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:04.354553+00:00"
---

# FxAddWood

Wood

Creates a wood splinter particle effect.

## Syntax

```
bool fxAddWood ( float posX, float posY, float posZ, float dirX, float dirY, float dirZ [, int count = 1, float brightness = 1.0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).addWood(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the effect originates.

- **dirX, dirY, dirZ:** a direction vector indicating where the wood splinters fly to.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **count:** the number of splinters to create.

- **brightness:** the brightness. Ranges from 0 (black) to 1 (normal color).

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

This example will create a Wood Effect next to you when typing */woodfx* in the Chatbox.

```
addCommandHandler("woodfx", function()
    local x, y, z = getElementPosition(localPlayer)
    local gz = getGroundPosition(x, y, z)
    fxAddWood(x, y, gz+0.4, 0, 0, 0, math.random(3, 6), 0.7)
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

- [fxAddTankFire](mta://scripting/client/functions/fxaddtankfire.md)

- [fxAddTyreBurst](mta://scripting/client/functions/fxaddtyreburst.md)

- [fxAddWaterHydrant](mta://scripting/client/functions/fxaddwaterhydrant.md)

- [fxAddWaterSplash](mta://scripting/client/functions/fxaddwatersplash.md)

- fxAddWood

ADDED/UPDATED IN VERSION 1.6.0 [r22512](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22512):

- [fxCreateParticle](mta://scripting/client/functions/fxcreateparticle.md)

- [getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
