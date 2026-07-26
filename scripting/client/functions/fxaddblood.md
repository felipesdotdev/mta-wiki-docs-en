---
doc_id: "mta-wiki:4194"
title: "FxAddBlood"
source_title: "FxAddBlood"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddBlood"
revision_id: 63047
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:04.060832+00:00"
---

# FxAddBlood

Blood splatter

Creates a blood splatter particle effect.

## Syntax

```
bool fxAddBlood ( float posX, float posY, float posZ, float dirX, float dirY, float dirZ [, int count = 1, float brightness = 1.0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).addBlood(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the effect originates.

- **dirX, dirY, dirZ:** a direction vector indicating where the blood flies to.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **count:** the number of flying droplets to create.

- **brightness:** the brightness. Ranges from 0 (almost black) to 1 (normal color).

## Example

Click to collapse [-]
Client

This example creates blood effects when a player gets shot.

```
function BloodonDamage( attacker, weapon, bodypart, loss )
   if loss > 25 then -- if the player loses more than 25 hp, then...
      local x, y, z = getElementPosition( source ) -- get player's position for adding blood
      local randombloodamount = math.random( 1, 3 ) -- random blood amount 1-3
      fxAddBlood ( x, y, z-2, 0.00000, 0.00000, 0.00000, randombloodamount, 1 )
      -- this adds blood to player's current position
   end
end
addEventHandler( "onClientPlayerDamage", root, BloodonDamage ) -- calls the function when a player loses hp
```

## See Also

- [createEffect](mta://scripting/client/functions/createeffect.md)

- fxAddBlood

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

- [setEffectSpeed](mta://scripting/client/functions/seteffectspeed.md)
