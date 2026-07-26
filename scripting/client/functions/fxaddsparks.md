---
doc_id: "mta-wiki:4208"
title: "FxAddSparks"
source_title: "FxAddSparks"
source_url: "https://wiki.multitheftauto.com/wiki/FxAddSparks"
revision_id: 63041
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:04.257059+00:00"
---

# FxAddSparks

Sparks

Creates a number of sparks originating from a point or along a line.

## Syntax

```
bool fxAddSparks ( float posX, float posY, float posZ, float dirX, float dirY, float dirZ [, float force = 1.0, int count = 1,
                   float acrossLineX = 0.0, float acrossLineY = 0.0, float acrossLineZ = 0.0, bool blur = false, float spread = 1.0, float life = 1.0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Effect](mta://reference/misc/effect.md).addSparks(...)*

### Required Arguments

- **posX, posY, posZ:** the world coordinates where the sparks originate.

- **dirX, dirY, dirZ:** a direction vector indicating where the sparks fly to. The longer this vector is, the faster the sparks fly.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **force:** speed factor: the higher this value, the faster and further the sparks fly.

- **count:** the number of effects to create.

- **acrossLineX, acrossLineY, acrossLineZ:** a vector starting at the **pos** coordinates. If specified, the sparks will be created along a line going from **pos** to **pos - acrossLine**. If not specified, all sparks originate from the point at **pos**.

- **blur:** if *false*, creates standard bullet impact-like sparks. If *true*, adds motion blur to the sparks.

- **spread:** determines how strongly the particles deviate from each other. With low values the particles will stay quite close together, high values will make them fly in all directions. Also affects their speed.

- **life:** the higher this value, the longer the sparks survive before they disappear.

### Returns

Returns a true if the operation was successful, false otherwise.

## Example

Click to collapse [-]
Client

This example will add Fire Bins to all locations added in the table.

```
fires = {
    {0, 0, 3} --Middle of SA
}

for i = 1, #fires do
    bin = createObject(1362, fires[i][1], fires[i][2], fires[i][3]-0.5)
    torch = createObject(3461, fires[i][1]-0.1, fires[i][2]-0.1, fires[i][3]-2)
    light = createMarker(fires[i][1], fires[i][2], fires[i][3]+0.2, "corona", 1, 255, 170, 0, 80, root)
    fireCol = createColSphere(fires[i][1], fires[i][2], fires[i][3]+0.5, 0.8)
    setTimer(fxAddSparks, math.random(4000, 5000), 0, fires[i][1]+math.random(0.1, 0.3), fires[i][2]+math.random(0.1, 0.2), fires[i][3]+0.2, 1, 1, 1)         
            
    addEventHandler("onClientColShapeHit", fireCol, 
    function(theElement)
        if (getElementType(theElement) == "player") then
            setPedOnFire(theElement, true)
        end
    end)
            
end
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

- fxAddSparks

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
