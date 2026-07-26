---
doc_id: "mta-wiki:4044"
title: "WarpPedIntoVehicle"
source_title: "WarpPedIntoVehicle"
source_url: "https://wiki.multitheftauto.com/wiki/WarpPedIntoVehicle"
revision_id: 73920
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates", "Functions_and_events_with_issues"]
---

# WarpPedIntoVehicle

This function is used to warp or force a ped into a vehicle.  There are no animations involved when this happens.

 

Vehicle seat ids

**Available client side from 1.3.1** (It will only work with client side vehicles and peds)

| [[{{{image}}}\|link=\|]] | Important Note: If you used setElementPosition to spawn the ped / player , this function will not work and returns false . |
| --- | --- |
|  |  |

## Syntax

```
bool warpPedIntoVehicle ( ped thePed, vehicle theVehicle, [ int seat=0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Set the variable to nil to execute [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md)*

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):warpIntoVehicle(...)*

**Variable**: *.vehicle*

**Counterpart**: *[getPedOccupiedVehicle](mta://scripting/shared/functions/getpedoccupiedvehicle.md)*

### Required Arguments

- **thePed:** The ped which you wish to force inside the vehicle

- **theVehicle:** The vehicle you wish to force the ped into

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **seat:** An integer representing the seat ID.

- **0:** Front-left

- **1:** Front-right

- **2:** Rear-left

- **3:** Rear-right

### Returns

Returns *true* if the operation is successful, *false* otherwise.

## Example

This example creates a vehicle and warps a ped inside immediately.

```
function setupForRace ( )
    local RacerPed = createPed ( 252, 0, 0, 3 )
    local RaceVehicle = createVehicle ( 411, 4, 0, 3 )            -- create a vehicle.
    warpPedIntoVehicle ( RacerPed, RaceVehicle )                  -- warp the ped straight into the vehicle
end
addCommandHandler ( "startrace", setupForRace )                   -- add a command to start race
```

## Issues

| Issue ID | Description |
| --- | --- |
| #475 | Network trouble when calling warpPedIntoVehicle on resourceStart |

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

- warpPedIntoVehicle
