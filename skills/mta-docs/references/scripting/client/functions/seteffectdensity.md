---
doc_id: "mta-wiki:7728"
title: "SetEffectDensity"
source_title: "SetEffectDensity"
source_url: "https://wiki.multitheftauto.com/wiki/SetEffectDensity"
revision_id: 52066
language: "en"
categories: ["Client_functions", "Changes_in_1.4"]
---

# SetEffectDensity

This function sets the density of a specified [effect](https://wiki.multitheftauto.com/index.php?search=effect).

|  | Warning: Upper density limit of this function depends on client FX Quality setting. The limit is 1 for Low, 1.5 for Medium, and 2 for High/Very high. |
| --- | --- |
|  |  |

## Syntax

```
bool setEffectDensity ( effect theEffect, float density )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[effect](https://wiki.multitheftauto.com/index.php?search=effect):setDensity(...)*

**Variable**: *.density*

**Counterpart**: *[getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)*

### Required Arguments

- **theEffect:** The [effect](https://wiki.multitheftauto.com/index.php?search=effect) to change the speed of.

- **density:** The level of density (from 0 to 2).

### Returns

Returns *true* if the density was succesfully changed, *false* otherwise.

### Example

This example adds command *sed* that creates spray effect at the player's position and sets its density to 2.

```
addCommandHandler("sed", 
function (cmd)
   local x, y, z = getElementPosition(localPlayer)
   local effect = createEffect("spraycan", x, y, z)
   setEffectDensity(effect, 2)
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

- [getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- setEffectDensity

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
