---
doc_id: "mta-wiki:7725"
title: "GetEffectSpeed"
source_title: "GetEffectSpeed"
source_url: "https://wiki.multitheftauto.com/wiki/GetEffectSpeed"
revision_id: 50861
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:10.502198+00:00"
---

# GetEffectSpeed

This function gets the speed of a specified [effect](mta://reference/misc/effect.md).

## Syntax

```
float getEffectSpeed ( effect theEffect )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[effect](mta://reference/misc/effect.md):getSpeed(...)*

**Variable**: *.speed*

**Counterpart**: *[setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)*

### Required Arguments

- **theEffect:** The [effect](mta://reference/misc/effect.md) to get the speed of.

### Returns

Returns [float](mta://reference/misc/float.md) containing the effect's speed, *false* if invalid arguments were specified.

### Example

This example adds command *ges* that creates crate explosion effect at the player's position and outputs its speed to the chatbox.

```
addCommandHandler("ges", 
function (cmd)
   local x, y, z = getElementPosition(localPlayer)
   local effect = createEffect("explosion_crate", x, y, z)
   outputChatBox("The speed: " .. tostring(getEffectSpeed(effect)))
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

- getEffectSpeed

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
