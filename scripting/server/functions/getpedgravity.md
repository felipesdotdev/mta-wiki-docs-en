---
doc_id: "mta-wiki:4029"
title: "GetPedGravity"
source_title: "GetPedGravity"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedGravity"
revision_id: 80373
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:15:17.525505+00:00"
---

# GetPedGravity

This function returns the current gravity for the specified [ped](mta://reference/misc/ped.md). The default gravity is 0.008.

## Syntax

```
float getPedGravity ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):getGravity(...)*

**Variable**: *.gravity*

**Counterpart**: *[setPedGravity](mta://scripting/server/functions/setpedgravity.md)*

### Required Arguments

- **thePed:** The [ped](mta://reference/misc/ped.md) whose gravity you want to check.

### Returns

Returns a [float](mta://reference/misc/float.md) indicating the ped's gravity, or *false* if the ped is invalid. Default value is 0.008.

## Example

This example outputs the gravity of the player who entered the 'showGravity' command.

```
function showGravity ( thePlayer )
	local gravity = getPedGravity ( thePlayer )
	outputChatBox ( "Your gravity: " .. tostring(gravity), thePlayer )
end
addCommandHandler ( "showGravity", showGravity )
```

## See Also

- getPedGravity

- [reloadPedWeapon](mta://scripting/server/functions/reloadpedweapon.md)

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
