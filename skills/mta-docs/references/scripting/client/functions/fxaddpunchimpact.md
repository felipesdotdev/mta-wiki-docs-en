---
doc_id: "mta-wiki:4204"
title: "FxAddPunchImpact"
source_title: "FxAddPunchImpact"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddPunchImpact"
revision_id: 43848
language: "en"
categories: ["Client_functions"]
---

# FxAddPunchImpact

Punch impact

Creates a punch impact particle effect (a small dust cloud).

## Syntax

```
bool fxAddPunchImpact ( float posX, float posY, float posZ, float dirX, float dirY, float dirZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](https://wiki.multitheftauto.com/index.php?search=Effect).addPunchImpact(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the effect originates.

- **dirX, dirY, dirZ:** a vector indicating the movement direction of the effect.

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

This example will create a Punch Impact Effect next to you when typing */pimpact* in the Chatbox.

```
addCommandHandler("pimpact", function()
    local x, y, z = getElementPosition(localPlayer)
    local gz = getGroundPosition(x, y, z)
    fxAddPunchImpact(x, y, gz, 0, 0, 0)
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

- fxAddPunchImpact

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
