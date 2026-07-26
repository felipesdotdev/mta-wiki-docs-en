---
doc_id: "mta-wiki:4206"
title: "FxAddDebris"
source_title: "FxAddDebris"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddDebris"
revision_id: 63045
language: "en"
categories: ["Client_functions", "Utility_templates"]
---

# FxAddDebris

Debris

Creates a debris particle effect (e.g. bits that fly off a car when ramming a wall).

## Syntax

```
bool fxAddDebris ( float posX, float posY, float posZ [, int colorR = 255, int colorG = 0, int colorB = 0, int colorA = 255, float scale = 1.0, int count = 1 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](https://wiki.multitheftauto.com/index.php?search=Effect).addDebris(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the debris originates.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **colorR, colorG, colorB, colorA:** the color and alpha (transparency) of the debris effect.

- **scale:** the size of the chunks.

- **count:** the number of chunks to create.

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

This example will create a Debris Effect next to you when typing */debris* in the Chatbox.

```
addCommandHandler("debris", function()
    local x, y, z = getElementPosition(localPlayer)
    local randomColor, randomAmount = math.random(0, 255), math.random(4, 8)
    fxAddDebris(x, y, z, randomColor, randomColor, randomColor, 255, 1.0, randomAmount)
end)
```

## See Also

- [createEffect](mta://scripting/client/functions/createeffect.md)

- [fxAddBlood](mta://scripting/client/functions/fxaddblood.md)

- [fxAddBulletImpact](mta://scripting/client/functions/fxaddbulletimpact.md)

- [fxAddBulletSplash](mta://scripting/client/functions/fxaddbulletsplash.md)

- fxAddDebris

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
