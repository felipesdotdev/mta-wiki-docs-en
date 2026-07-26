---
doc_id: "mta-wiki:4243"
title: "IsPedHeadless"
source_title: "IsPedHeadless"
source_url: "https://wiki.multitheftauto.com/wiki/IsPedHeadless"
revision_id: 71553
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# IsPedHeadless

With this function, you can check if a ped has a head or not.

## Syntax

```
bool isPedHeadless(ped thePed)
```

### Required Arguments

- **thePed**: The [ped](https://wiki.multitheftauto.com/index.php?search=ped) to check.

### Returns

Returns *true* if the ped is headless, *false* otherwise.

## Example

Click to collapse [-]
Client

Add a command to check whether the player is a zombie or not

```
function checkZombie(commandName)
   local player = getLocalPlayer()
   -- check whether the player is headless (a zombie)
   local message = isPedHeadless(player) and "Yes, you are a zombie!" or "No, you aren't a zombie yet!"
   outputChatBox(message)
end

addCommandHandler("zombie", checkZombie)
```

Click to collapse [-]
Server

Add a command to check whether a player is a zombie or not

```
function checkZombie(playerSource, commandName, playerTargetNick)
   local playerTarget = getPlayerFromName(playerTargetNick)
   if (not playerTarget) then return outputChatBox("Player not online!", playerSource, 255, 0, 0) end

   -- check whether the playerTarget is headless (a zombie)
   local message = isPedHeadless(playerTarget) and "This Player is a zombie!" or "This player is not a zombie!"
   outputChatBox(message, playerSource)
end

addCommandHandler("zombie", checkZombie)
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

- isPedHeadless

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
