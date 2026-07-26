---
doc_id: "mta-wiki:4199"
title: "FxAddTyreBurst"
source_title: "FxAddTyreBurst"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddTyreBurst"
revision_id: 43851
language: "en"
categories: ["Client_functions"]
---

# FxAddTyreBurst

Tyre burst

Creates a tyre burst particle effect (a small white smoke puff).

## Syntax

```
bool fxAddTyreBurst ( float posX, float posY, float posZ, float dirX, float dirY, float dirZ )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](https://wiki.multitheftauto.com/index.php?search=Effect).addTyreBurst(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the puff originates.

- **dirX, dirY, dirZ:** a vector indicating the movement direction of the effect.

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

This example will create a Tyre Burst Effect next to you when typing */tyreburst* in the Chatbox.

```
addCommandHandler("tyreburst", function()
    local x, y, z = getElementPosition(localPlayer)
    local gz = getGroundPosition(x, y, z)
    fxAddTyreBurst(x, y, gz, 0, 0, 0)
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

- fxAddTyreBurst

- [fxAddWaterHydrant](mta://scripting/client/functions/fxaddwaterhydrant.md)

- [fxAddWaterSplash](mta://scripting/client/functions/fxaddwatersplash.md)

- [fxAddWood](mta://scripting/client/functions/fxaddwood.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22512](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22512):

- [fxCreateParticle](mta://scripting/client/functions/fxcreateparticle.md)

- [getEffectDensity](mta://scripting/client/functions/geteffectdensity.md)

- [getEffectSpeed](mta://scripting/client/functions/geteffectspeed.md)

- [setEffectDensity](mta://scripting/client/functions/seteffectdensity.md)

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
