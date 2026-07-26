---
doc_id: "mta-wiki:4036"
title: "SetPedChoking"
source_title: "SetPedChoking"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedChoking"
revision_id: 80375
language: "en"
categories: ["Server_functions"]
---

# SetPedChoking

This function can be used to force the ped to do the choking (coughing) animation until he respawns or toggled off using this function. The animation can not be cancelled by a player it's applied to, and he will not loose health.

## Syntax

```
bool setPedChoking ( ped thePed, bool choking )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):setChoking(...)*

**Variable**: *.choking*

**Counterpart**: *[isPedChoking](mta://scripting/shared/functions/ispedchoking.md)*

### Required Arguments

- **thePed:** The ped whose choking status to toggle

- **choking:** *true* to make the ped choke, *false* to no longer force his choking animation

### Returns

Returns *true* if successful, *false* otherwise (e.g. player handle is invalid)

## Example

This script will make all players choke on resource start

```
-- Choke all the players when the resource starts

function onResourceStart()
    setPedChoking(root, true)
end
addEventHandler("onResourceStart", resourceRoot, onResourceStart)

-- Unchoke all the players when the resource stops

function onResourceStop()
    setPedChoking(root, false)
end
addEventHandler("onResourceStop", resourceRoot, onResourceStop)

-- Choke players spawning

function onPlayerSpawn()
    setPedChoking(source, true)
end
addEventHandler("onPlayerSpawn", root, onPlayerSpawn)
```

## See Also

- [getPedGravity](mta://scripting/server/functions/getpedgravity.md)

- [reloadPedWeapon](mta://scripting/server/functions/reloadpedweapon.md)

- setPedChoking

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
