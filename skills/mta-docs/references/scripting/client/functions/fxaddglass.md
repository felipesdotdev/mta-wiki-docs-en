---
doc_id: "mta-wiki:4195"
title: "FxAddGlass"
source_title: "FxAddGlass"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddGlass"
revision_id: 63044
language: "en"
categories: ["Client_functions", "Utility_templates"]
---

# FxAddGlass

Glass

This function creates a glass particle effect.

## Syntax

```
bool fxAddGlass ( float posX, float posY, float posZ [, int colorR = 255, int colorG = 0, int colorB = 0, int colorA = 255, float scale = 1.0, int count = 1 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](https://wiki.multitheftauto.com/index.php?search=Effect).addGlass(...)*

### Required Arguments

- **posX:** A float representing the **x** position of the glass

- **posY:** A float representing the **y** position of the glass

- **posZ:** A float representing the **z** position of the glass

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **colorR, colorG, colorB, colorA:** the color and alpha (transparency) of the glass effect.

- **scale:** A float representing the size of the particle effect, where **1** is the standard size.

- **count:** The density of the particle effect.

### Returns

Returns a true if the operation was successful, false otherwise.

## Examples

This example creates a glass particle effect at the position of the player who use /addGlass command.

```
function addGlassParticle(cmd,r,g,b,a,scale,count)
   if r and g and b then 
      local x,y,z = getElementPosition(localPlayer)
      fxAddGlass(x+3,y,z,r,g,b,255,1.0,5)
   end 
end
addCommandHandler("addGlass",addGlassParticle)
```

## See Also

- [createEffect](mta://scripting/client/functions/createeffect.md)

- [fxAddBlood](mta://scripting/client/functions/fxaddblood.md)

- [fxAddBulletImpact](mta://scripting/client/functions/fxaddbulletimpact.md)

- [fxAddBulletSplash](mta://scripting/client/functions/fxaddbulletsplash.md)

- [fxAddDebris](mta://scripting/client/functions/fxadddebris.md)

- [fxAddFootSplash](mta://scripting/client/functions/fxaddfootsplash.md)

- fxAddGlass

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
