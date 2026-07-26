---
doc_id: "mta-wiki:7723"
title: "SetEffectSpeed"
source_title: "SetEffectSpeed"
source_url: "https://wiki.multitheftauto.com/wiki/SetEffectSpeed"
revision_id: 50863
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:39.559026+00:00"
---

# SetEffectSpeed

This function sets the speed of a specified [effect](mta://reference/misc/effect.md).

## Syntax

```
bool setEffectSpeed ( effect theEffect, float speed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[effect](mta://reference/misc/effect.md):setSpeed(...)*

**Variable**: *.speed*

**Counterpart**: *[getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)*

### Required Arguments

- **theEffect:** The [effect](mta://reference/misc/effect.md) to change the speed of.

- **speed:** The speed to set.

### Returns

Returns *true* if the effect speed was succesfuly changed, *false* otherwise.

### Example

This example adds command *ses* that creates effect of a smoke at player's position and sets its speed to 5.

```
addCommandHandler("ses", 
function (cmd)
   local x, y, z = getElementPosition(localPlayer)
   local effect = createEffect("smoke30lit", x, y, z)
   setEffectSpeed(effect, 5)
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

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- setEffectSpeed
