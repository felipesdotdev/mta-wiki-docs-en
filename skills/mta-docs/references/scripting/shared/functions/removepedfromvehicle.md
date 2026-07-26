---
doc_id: "mta-wiki:4045"
title: "RemovePedFromVehicle"
source_title: "RemovePedFromVehicle"
source_url: "https://wiki.multitheftauto.com/wiki/RemovePedFromVehicle"
revision_id: 54530
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# RemovePedFromVehicle

This function removes a ped from a vehicle immediately. This works for drivers and passengers. Note that this removes the ped from the vehicle and puts him in the exact position where the command was initiated.

**Available client side from 1.3.1** (It will only work with client side vehicles and peds)

## Syntax

```
bool removePedFromVehicle ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Set the variable to nil to execute this function*

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):removeFromVehicle(...)*

**Variable**: *.vehicle*

### Required Arguments

- **thePed:** The ped you wish to remove from a vehicle

### Returns

Returns *true* if the operation was successful, *false* if the specified ped is not valid or if it isn't in a vehicle.

## Example

Small example to show how to remove a ped from any vehicle it's in.

```
function setupForRace( )
	RacerPed = createPed( 252, 0, 0, 3 ) -- create a ped into the variable "RacerPed"
	local RaceVehicle = createVehicle( 411, 4, 0, 3 ) -- create a vehicle.
	warpPedIntoVehicle( RacerPed, RaceVehicle ) -- warp the ped straight into the vehicle
	setTimer( removeThePed, 5000, 1 ) -- Setup a timer which will remove the ped from the vehicle after 5 seconds.
end
addCommandHandler( "startrace", setupForRace ) -- add a command to start race

function removeThePed( )
	removePedFromVehicle( RacerPed ) -- Removes the ped from any vehicle. 
end
```

## See Also

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

- removePedFromVehicle

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
