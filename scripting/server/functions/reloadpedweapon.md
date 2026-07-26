---
doc_id: "mta-wiki:4712"
title: "ReloadPedWeapon"
source_title: "ReloadPedWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/ReloadPedWeapon"
revision_id: 80374
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:31.764201+00:00"
---

# ReloadPedWeapon

This function makes a pedestrian reload their weapon.

## Syntax

```
bool reloadPedWeapon ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):reloadWeapon(...)*

### Required Arguments

- **thePed:** The [ped](mta://reference/misc/ped.md) who will reload their weapon.

### Returns

Returns *true* if the pedestrian was made to reload, or *false* if invalid arguments were passed or that pedestrian has a weapon which cannot be reloaded.

**Note:** this will fail but return true if

1) the ped is crouched and moving

2) the ped is using a weapon without clip ammo (or minigun/flamethrower/fire
extinguisher)

3) the ped is using his weapon (shooting/aiming)

4) the ped moved while crouching recently

Due to these circumstances causing problems with this function

## Example

This example adds a 'reloadgun' console command that lets players reload their weapon.

```
function reloadGun ( sourcePlayer, command )
    reloadPedWeapon ( sourcePlayer )
end
addCommandHandler ( "reloadgun", reloadGun )
```

## See Also

- [getPedGravity](mta://scripting/server/functions/getpedgravity.md)

- reloadPedWeapon

- [setPedChoking](mta://scripting/server/functions/setpedchoking.md)

- [setPedGravity](mta://scripting/server/functions/setpedgravity.md)

- [setPedWearingJetpack](mta://scripting/server/functions/setpedwearingjetpack.md)
  

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
