---
doc_id: "mta-wiki:4310"
title: "GetPedOccupiedVehicleSeat"
source_title: "GetPedOccupiedVehicleSeat"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedOccupiedVehicleSeat"
revision_id: 55417
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetPedOccupiedVehicleSeat

This function gets the seat that a specific ped is sitting in in a vehicle.

 

Vehicle seat ids

## Syntax

```
int getPedOccupiedVehicleSeat ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Prior to 1.5, the variable was .occupiedVehicleSeat*

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):getOccupiedVehicleSeat(...)*

**Variable**: *.vehicleSeat*

### Required Arguments

- **thePed**: The [ped](https://wiki.multitheftauto.com/index.php?search=ped) whose vehicle seat you're looking up.

### Returns

- Returns an integer containing the number of the seat that the ped is currently in:

- **0:** Front-left

- **1:** Front-right

- **2:** Rear-left

- **3:** Rear-right

Returns *false* if the ped is on foot, or the ped doesn't exist.

## Example

This example finds what seat a random player is sitting in and outputs it to the chat box.

```
thePed = getRandomPlayer()
theVehicle = getPedOccupiedVehicle ( thePed )
if ( theVehicle ) then
    outputChatBox ( getPlayerName(thePed).." is in a vehicle in seat number " .. getPedOccupiedVehicleSeat ( thePed ) .. "." )
else
    outputChatBox ( getPlayerName(thePed).." is not in a vehicle." )
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

- getPedOccupiedVehicleSeat

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
