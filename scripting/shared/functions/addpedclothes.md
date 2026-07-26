---
doc_id: "mta-wiki:4026"
title: "AddPedClothes"
source_title: "AddPedClothes"
source_url: "https://wiki.multitheftauto.com/wiki/AddPedClothes"
revision_id: 69187
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:10:51.534454+00:00"
---

# AddPedClothes

| [[{{{image}}}\|link=\|]] | Note: This function only works with peds using CJ skin (ID 0). |
| --- | --- |
|  |  |

This function is used to set the current clothes on a [ped](mta://reference/misc/ped.md).

## Syntax

```
bool addPedClothes ( ped thePed, string clothesTexture, string clothesModel, int clothesType )
```

 

CJ with a shirt.

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):addClothes(...)*

**Counterpart**: *[getPedClothes](mta://scripting/shared/functions/getpedclothes.md)*

### Required Arguments

- **thePed**: The [ped](mta://reference/misc/ped.md) whose clothes you want to change.

- **clothesTexture**: A string determining the clothes texture that will be added. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

- **clothesModel**: A string determining the clothes model that will be added. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

- **clothesType**: A integer representing the clothes slot/type the clothes should be added to. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

### Returns

This function returns *true* if the clothes were successfully added to the ped, *false* otherwise.

## Example

Click to collapse [-]
Server

This example adds a 'moto' helmet to a player when he gets on a nrg bike, and removes it when he gets off.

```
function onEnterVehicle ( theVehicle, seat, jacked )
    if getElementModel ( theVehicle ) == 522 then         -- if it's an nrg
        addPedClothes ( source, "moto", "moto", 16 )   -- add the helmet
    end
end
addEventHandler ( "onPlayerVehicleEnter", root, onEnterVehicle )

function onExitVehicle ( theVehicle, seat, jacked )
    if getElementModel ( theVehicle ) == 522 then      -- if it's an nrg
        removePedClothes ( source, 16 )              -- remove the helmet
    end
end
addEventHandler ( "onPlayerVehicleExit", root, onExitVehicle )
```

## See Also

- addPedClothes

- [getPedClothes](mta://scripting/shared/functions/getpedclothes.md)

- [removePedClothes](mta://scripting/shared/functions/removepedclothes.md)

- [createPed](mta://scripting/shared/functions/createped.md)

- [getPedAmmoInClip](mta://scripting/shared/functions/getpedammoinclip.md)

- [getPedArmor](mta://scripting/shared/functions/getpedarmor.md)

- [getPedFightingStyle](mta://scripting/shared/functions/getpedfightingstyle.md)

- [getPedOccupiedVehicle](mta://scripting/shared/functions/getpedoccupiedvehicle.md)

- [getPedOccupiedVehicleSeat](mta://scripting/shared/functions/getpedoccupiedvehicleseat.md)

- [getPedStat](mta://scripting/shared/functions/getpedstat.md)

- [getPedTarget](mta://scripting/shared/functions/getpedtarget.md)

- [getPedTotalAmmo](mta://scripting/shared/functions/getpedtotalammo.md)

- [getPedWalkingStyle](mta://scripting/shared/functions/getpedwalkingstyle.md)

- [getPedWeapon](mta://scripting/shared/functions/getpedweapon.md)

- [getPedWeaponSlot](mta://scripting/shared/functions/getpedweaponslot.md)

- [getPedContactElement](mta://scripting/shared/functions/getpedcontactelement.md)

- [getValidPedModels](mta://scripting/shared/functions/getvalidpedmodels.md)

- [isPedChoking](mta://scripting/shared/functions/ispedchoking.md)

- [isPedDead](mta://scripting/shared/functions/ispeddead.md)

- [isPedDoingGangDriveby](mta://scripting/shared/functions/ispeddoinggangdriveby.md)

- [isPedDucked](mta://scripting/shared/functions/ispedducked.md)

- [isPedHeadless](mta://scripting/shared/functions/ispedheadless.md)

- [isPedInVehicle](mta://scripting/shared/functions/ispedinvehicle.md)

- [isPedOnGround](mta://scripting/shared/functions/ispedonground.md)

- [isPedReloadingWeapon](mta://scripting/shared/functions/ispedreloadingweapon.md)

- [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md)

- [killPed](mta://scripting/shared/functions/killped.md)

- [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md)

- [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md)

- [setPedAnimationProgress](mta://scripting/shared/functions/setpedanimationprogress.md)

- [setPedAnimationSpeed](mta://scripting/shared/functions/setpedanimationspeed.md)

- [setPedArmor](mta://scripting/shared/functions/setpedarmor.md)

- [setPedDoingGangDriveby](mta://scripting/shared/functions/setpeddoinggangdriveby.md)

- [setPedFightingStyle](mta://scripting/shared/functions/setpedfightingstyle.md)

- [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md)

- [setPedStat](mta://scripting/shared/functions/setpedstat.md)

- [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
