---
doc_id: "mta-wiki:10522"
title: "SetPedWearingJetpack"
source_title: "SetPedWearingJetpack"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedWearingJetpack"
revision_id: 80377
language: "en"
categories: ["Server_functions", "Changes_in_1.5.5"]
generated_at: "2026-07-26T16:16:43.458745+00:00"
---

# SetPedWearingJetpack

This function is used to give or take a jetpack from a ped, it won't work if the ped is in a vehicle.

As such, you should either expect it to fail sometimes, or repeatedly try to give a jetpack every second or so until [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md) returns true. Alternatively, you can force the ped into a 'safe' position (e.g. standing on the ground) before giving the jetpack, or use a [pickup](mta://reference/misc/pickup.md) to handle it.

## Syntax

```
bool setPedWearingJetpack ( ped thePed, bool state )
```

 

Player wearing a jetpack

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):setWearingJetpack(...)*

**Variable**: *.jetpack*

### Required Arguments

- **thePed:** The [ped](mta://reference/misc/ped.md) you want to give a jetpack to.

- **state:** A [boolean](mta://reference/misc/boolean.md) representing whether to give or take the jetpack.

### Returns

Returns *true* if a jetpack was successfully set for the ped, *false* if setting it failed.

## Example

This examples adds a "jetpack" console command, which toggles a jetpack for the player.

```
addCommandHandler ( "jetpack",
    function ( player )
        setPedWearingJetpack ( player, not isPedWearingJetpack ( player ) )
    end
)
```

## See Also

- [getPedGravity](mta://scripting/server/functions/getpedgravity.md)

- [reloadPedWeapon](mta://scripting/server/functions/reloadpedweapon.md)

- [setPedChoking](mta://scripting/server/functions/setpedchoking.md)

- [setPedGravity](mta://scripting/server/functions/setpedgravity.md)

- setPedWearingJetpack
  

- **Shared**

- [addPedClothes](mta://scripting/shared/functions/addpedclothes.md)

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
