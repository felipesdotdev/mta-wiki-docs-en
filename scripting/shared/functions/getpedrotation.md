---
doc_id: "mta-wiki:3939"
title: "GetPedRotation"
source_title: "GetPedRotation"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedRotation"
revision_id: 44607
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:15:18.003738+00:00"
---

# GetPedRotation

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use getElementRotation instead. |  |

Gets the rotation of a ped.

## Syntax

```
float getPedRotation ( ped thePed )
```

### Required Arguments

- **thePed:** the ped to retrieve the rotation of.

### Returns

Returns the rotation of the ped, in degrees: 0 means facing north, higher values go counter clockwise. Returns *false* if an invalid element was passed.

## Example

Click to collapse [-]
Server

This code adds a *getrot* command to get a player's current rotation.

```
function outputPlayerRotation ( sourcePlayer )
	-- if the command was triggered by an ingame player
	if ( sourcePlayer ) then
		-- if he is in a vehicle
		if isPedInVehicle ( sourcePlayer ) then
			-- store the vehicle element
			local playerVehicle = getPedOccupiedVehicle ( sourcePlayer )
			-- and output its rotation
			local x,y,z = getElementRotation ( playerVehicle )
			outputChatBox ( "Your vehicle's rotation is: " .. z, sourcePlayer )
		-- if he is on foot
		else
			-- output the player's rotation
			outputChatBox ( "Your rotation is: " .. getPedRotation ( sourcePlayer ), sourcePlayer )
		end
	end
end

-- register outputPlayerRotation as a handler for the getrot command
addCommandHandler ( "getrot", outputPlayerRotation )
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
