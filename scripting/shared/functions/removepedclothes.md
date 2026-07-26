---
doc_id: "mta-wiki:4033"
title: "RemovePedClothes"
source_title: "RemovePedClothes"
source_url: "https://wiki.multitheftauto.com/wiki/RemovePedClothes"
revision_id: 69078
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:32.461836+00:00"
---

# RemovePedClothes

This function is used to remove the current clothes of a certain type on a [ped](mta://reference/misc/ped.md). It will remove them if the clothesTexture and clothesModel aren't specified, or if they match the current clothes on that slot.

## Syntax

```
bool removePedClothes ( ped thePed, int clothesType [, string clothesTexture, string clothesModel ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):removeClothes(...)*

### Required Arguments

- **thePed**: The [ped](mta://reference/misc/ped.md) you want to remove clothes from.

- **clothesType**: the clothes slot/type to remove. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

### Optional Arguments

- **clothesTexture**: (Server only) A string determining the clothes texture that will be removed. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

- **clothesModel**: (Server only) A string determining the clothes model that will be removed. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

## Returns

This function returns *true* if the clothes were successfully removed from the ped, *false* otherwise.

## Example

Click to collapse [-]
Server

This example adds a 'moto' helmet to a player when he gets on a nrg bike, and removes it when he gets off.

```
function addHelmetOnEnter ( vehicleEntered, seat, jacked )
    if getElementModel ( vehicleEntered ) == 522 then      -- if it's a nrg
        addPedClothes ( source, "moto", "moto", 16 )       -- add the helmet
    end
end
addEventHandler ( "onPlayerVehicleEnter", root, addHelmetOnEnter )

function removeHelmetOnExit ( vehicleExited, seat, jacked )
    if getElementModel ( vehicleExited ) == 522 then       -- if it's a nrg
        removePedClothes ( source, 16, "moto", "moto" )    -- remove that helmet
    end
end
addEventHandler ( "onPlayerVehicleExit", root, removeHelmetOnExit )
```

## See Also

- [addPedClothes](mta://scripting/shared/functions/addpedclothes.md)

- [getPedClothes](mta://scripting/shared/functions/getpedclothes.md)

- removePedClothes

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
