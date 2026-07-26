---
doc_id: "mta-wiki:4038"
title: "SetPedGravity"
source_title: "SetPedGravity"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedGravity"
revision_id: 80376
language: "en"
categories: ["Server_functions"]
generated_at: "2026-07-26T16:16:42.918641+00:00"
---

# SetPedGravity

This function sets the gravity level of a ped.

## Syntax

```
bool setPedGravity ( ped thePed, float gravity )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):setGravity(...)*

**Variable**: *.gravity*

**Counterpart**: *[getPedGravity](mta://scripting/server/functions/getpedgravity.md)*

### Required Arguments

- **thePed**: The ped whose gravity to change.

- **level**: The level of gravity (default is 0.008).

### Returns

Returns *true* if the gravity was successfully set, *false* otherwise

## Example

This example allows the user to type a command to change their gravity:

```
function consoleSetPlayerGravity ( thePlayer, commandName, level )
	if thePlayer and level then
		local success = setPedGravity ( thePlayer, tonumber ( level ) )  -- Set the gravity
		if not success then                           -- Check if setPlayerGravity was false (not successful)
			outputConsole( "Failed to set ped gravity", thePlayer )  -- If success is false, meaning gravity could not be set, this message will show
		end
	end
end
addCommandHandler ( "setplayergravity", consoleSetPlayerGravity )
```

## See Also

- [getPedGravity](mta://scripting/server/functions/getpedgravity.md)

- [reloadPedWeapon](mta://scripting/server/functions/reloadpedweapon.md)

- [setPedChoking](mta://scripting/server/functions/setpedchoking.md)

- setPedGravity

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
