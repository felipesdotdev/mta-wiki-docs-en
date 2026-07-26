---
doc_id: "mta-wiki:3960"
title: "DoesPedHaveJetPack"
source_title: "DoesPedHaveJetPack"
source_url: "https://wiki.multitheftauto.com/wiki/DoesPedHaveJetPack"
revision_id: 60576
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# DoesPedHaveJetPack

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use isPedWearingJetpack instead. |  |

Checks whether or not a ped currently has a jetpack.

## Syntax

```
bool doesPedHaveJetPack ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):doesHaveJetpack(...)*

### Required Arguments

- **thePed:** the ped you want to check

### Returns

Returns *true* if the ped is carrying a jetpack, *false* if he is not or an invalid element was passed.

## Example

Click to collapse [-]
Server

**Example 1:** This examples adds a "jetpack" console command, which gives or removes a jetpack from the player.

```
-- Checks whether or not the player has a jetpack, and gives or removes it from the player
function consoleJetPack ( thePlayer, commandName )
   if ( not doesPedHaveJetPack ( thePlayer ) ) then            -- if the player doesn't have a jetpack
      local status = givePedJetPack ( thePlayer )              -- give him one
      if ( not status ) then
         outputConsole ( "Failed to give jetpack.", thePlayer )   -- tell him if it failed
      end
   else
      local status = removePedJetPack ( thePlayer )            -- remove his jetpack
      if ( not status ) then
         outputConsole ( "Failed to remove jetpack.", thePlayer ) -- tell him if it failed
      end
   end
end

-- add the function above to handle the "jetpack" command
addCommandHandler ( "jetpack", consoleJetPack )
```

Click to collapse [-]
Server

**Example 2:** This example provides a check to see if players have a jetpack when they enter a particular marker.

```
function onWarpMarkerHit ( thePlayer, matchingDimension )
   -- check whether the player has a jetpack and store it in the hasJetPack flag
   local hasJetPack = doesPedHaveJetPack ( thePlayer )
   if ( not hasJetPack ) then
      -- warp the player to their destination
      setElementPosition ( thePlayer, 1337, 1337, 50 )
   else
      -- tell the player to remove their jetpack
      outputChatBox ( "You must remove your jetpack to use this marker!", thePlayer )
   end
end

-- create a marker and add the function above to its onMarkerHit event
addEventHandler ( "onMarkerHit", createMarker(3180, 200, 27), onWarpMarkerHit )
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
