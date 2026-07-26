---
doc_id: "mta-wiki:4030"
title: "GivePedJetPack"
source_title: "GivePedJetPack"
source_url: "https://wiki.multitheftauto.com/wiki/GivePedJetPack"
revision_id: 73886
language: "en"
categories: ["Server_functions", "Deprecated"]
---

# GivePedJetPack

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedWearingJetpack instead. |  |

This function is used to give a ped a jetpack, it won't work if the ped is in a vehicle.

As such, you should either expect it to fail sometimes, or repeatedly try to give a jetpack every second or so until [doesPedHaveJetPack](mta://scripting/shared/functions/doespedhavejetpack.md) returns true. Alternatively, you can force the ped into a 'safe' position (e.g. standing on the ground) before giving the jetpack, or use a [pickup](https://wiki.multitheftauto.com/index.php?search=pickup) to handle it.

## Syntax

```
bool givePedJetPack ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):giveJetPack(...)*

### Required Arguments

- **thePed:** The [ped](https://wiki.multitheftauto.com/index.php?search=ped) you want to give a jetpack to.

### Returns

Returns *true* if a jetpack was successfully given to the ped, *false* if it could not be given.

## Example

This examples adds a "jetpack" console command, which gives or removes a jetpack from the player.

```
-- Checks whether or not the player has a jetpack, and gives or removes it from the player
function consoleJetPack ( thePlayer, commandName )
   if not doesPedHaveJetPack ( thePlayer ) then                   -- if the player doesn't have a jetpack
      local status = givePedJetPack ( thePlayer )                 -- give him one
      if not status then
         outputConsole ( "Failed to give jetpack.", thePlayer )   -- tell him if it failed
      end
   else
      local status = removePedJetPack ( thePlayer )               -- remove his jetpack
      if ( not status ) then
         outputConsole ( "Failed to remove jetpack.", thePlayer ) -- tell him if it failed
      end
   end
end

-- add the function above to handle the "jetpack" command
addCommandHandler ( "jetpack", consoleJetPack )
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
