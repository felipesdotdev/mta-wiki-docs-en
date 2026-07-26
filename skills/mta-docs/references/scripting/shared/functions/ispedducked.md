---
doc_id: "mta-wiki:3979"
title: "IsPedDucked"
source_title: "IsPedDucked"
source_url: "https://wiki.multitheftauto.com/wiki/IsPedDucked"
revision_id: 55781
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# IsPedDucked

This function checks if the specified [ped](https://wiki.multitheftauto.com/index.php?search=ped) is ducked (crouched) or not.

## Syntax

```
bool isPedDucked ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):isDucked(...)*

**Variable**: *.ducked*

### Required Arguments

- **thePed**: The [ped](https://wiki.multitheftauto.com/index.php?search=ped) to check.

### Returns

Returns *true* if the ped is ducked, *false* otherwise.

## Example

Click to collapse [-]
Client

This example checks if a random player is ducked or not, and if so displays a message in the chat box.

```
local players = getElementsByType ( "player" )
local randomPlayer = players[math.random(#players)]
if isPedDucked ( randomPlayer ) then
	outputChatBox ( getPlayerName ( randomPlayer ) .. " is currently crouching." )
end
```

This example creates a function that lets you toggle the crouching state of a ped.

```
function setPedDucked(ped, bool)
	local alreadyDucked = isPedDucked(ped)
	if (alreadyDucked and not bool) then
		setPedControlState(ped, "crouch", true)
		setTimer(setPedControlState, 50, 1, ped, "crouch", false)
		return true
	elseif (not alreadyDucked and bool) then
		setPedControlState(ped, "crouch", true)
		setTimer(setPedControlState, 50, 1, ped, "crouch", false)
		return true
	end
	return false
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

- isPedDucked

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
