---
doc_id: "mta-wiki:10523"
title: "IsPedWearingJetpack"
source_title: "IsPedWearingJetpack"
source_url: "https://wiki.multitheftauto.com/wiki/IsPedWearingJetpack"
revision_id: 81196
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.5"]
---

# IsPedWearingJetpack

Checks whether or not a ped is currently wearing a jetpack.

## Syntax

```
bool isPedWearingJetpack ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):isWearingJetpack(...)*

**Variable**: *.jetpack*

### Required Arguments

- **thePed:** the ped you want to check

### Returns

Returns *true* if the ped is carrying a jetpack, *false* if he is not or an invalid element was passed.

## Example

Click to collapse [-]
Server

**Example 1:** This examples adds a "jetpack" console command, which toggles a jetpack for the player.

```
addCommandHandler ( "jetpack",
    function ( player )
        setPedWearingJetpack ( player, not isPedWearingJetpack ( player ) )
    end
)
```

Click to collapse [-]
Server

**Example 2:** This example provides a check to see if players have a jetpack when they enter a particular marker.

```
function onWarpMarkerHit ( player )
   -- check whether the player has a jetpack
   if ( not isPedWearingJetpack ( player ) ) then
      -- warp the player to their destination
      setElementPosition ( player, 1337, 1337, 50 )
   else
      -- tell the player to remove their jetpack
      outputChatBox ( "You must remove your jetpack to use this marker!", player )
   end
end

-- create a marker and add the function above to its onMarkerHit event
addEventHandler ( "onMarkerHit", createMarker( 3180, 200, 27 ), onWarpMarkerHit )
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

- isPedWearingJetpack

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
