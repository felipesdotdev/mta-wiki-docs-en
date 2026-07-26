---
doc_id: "mta-wiki:10768"
title: "SetPedAnimationSpeed"
source_title: "SetPedAnimationSpeed"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedAnimationSpeed"
revision_id: 78673
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.5", "Changes_in_1.5.7"]
---

# SetPedAnimationSpeed

Sets the speed of a currently running animation for a particular player or ped.

## Syntax

```
bool setPedAnimationSpeed ( ped thePed [, string anim = "", float speed = 1.0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):setAnimationSpeed(...)*

### Required Arguments

- **thePed:** the [player](https://wiki.multitheftauto.com/index.php?search=player) or [ped](https://wiki.multitheftauto.com/index.php?search=ped) you want to change animation speed of.

### Optional Arguments

- **anim:** the animation name it will affect.

- **speed:** a [float](mta://reference/misc/float.md) containing the speed between 0.0–1.0 you want to apply to the animation. *This limitation may be adjusted in the future, so do not provide speeds outside this boundary.* The limit is now 0.0 to 10.0.

| [[\|link=\|]] | Warning: Setting speed higher than 1 can cause issues with some animations. |
| --- | --- |
|  |  |

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Server

In this example we give the animation of dancing to the player and after 5 seconds it becomes 0.2s slower.

```
addCommandHandler('dance',
  function( player, cmd )
      setPedAnimation( player, 'DANCING', 'DAN_Down_A', -1 )
      setTimer(function(plr)
          if isElement(plr) then setPedAnimationSpeed( plr, 'DAN_Down_A', 0.2 ) end
      end,5000,1,player)
   end
)
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

- setPedAnimationSpeed

- [setPedArmor](mta://scripting/shared/functions/setpedarmor.md)

- [setPedDoingGangDriveby](mta://scripting/shared/functions/setpeddoinggangdriveby.md)

- [setPedFightingStyle](mta://scripting/shared/functions/setpedfightingstyle.md)

- [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md)

- [setPedStat](mta://scripting/shared/functions/setpedstat.md)

- [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
