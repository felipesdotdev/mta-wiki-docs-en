---
doc_id: "mta-wiki:5432"
title: "GetPedMoveState"
source_title: "GetPedMoveState"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedMoveState"
revision_id: 75315
language: "en"
categories: ["Client_functions", "Changes_in_1.7.0"]
generated_at: "2026-07-26T16:15:17.884207+00:00"
---

# GetPedMoveState

This function returns the current move state for the specified [ped](mta://reference/misc/ped.md).

## Syntax

```
string getPedMoveState ( ped thePed )
```

### Required Arguments

- **thePed:** The [ped](mta://reference/misc/ped.md) whose move state you want to know

### Returns

Returns a [string](mta://reference/misc/string.md) indicating the ped's move state, or *false* if the ped is not streamed in, the movement type is unknown, the ped is in a vehicle or the ped is invalid.

- **stand**: The ped is standing still.

- **walk**: The ped is walking.

- **powerwalk**: The ped is walking quickly.

- **jog**: The ped is jogging.

- **sprint**: The ped is sprinting.

- **crouch**: The ped is crouching still.

- **crawl**: The ped is crawling (moving and ducked).

- **jump**: The ped is jumping into the air.

- **fall**: The ped is falling to the ground.

- **climb**: The ped is climbing onto an object.

ADDED/UPDATED IN VERSION 1.7.0 [r25351](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25351):

**swim:** The ped is swimming. 

ADDED/UPDATED IN VERSION 1.7.0 [r25351](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25351):

**walk_to_point:** The ped is walking to a vehicle door. 

ADDED/UPDATED IN VERSION 1.7.0 [r25351](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25351):

**ascent_jetpack:** The ped is ascending with jetpack. 

ADDED/UPDATED IN VERSION 1.7.0 [r25351](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25351):

**descent_jetpack:** The ped is descending with jetpack. 

ADDED/UPDATED IN VERSION 1.7.0 [r25351](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25351):

**jetpack_flying:** The ped is flying with jetpack. 

ADDED/UPDATED IN VERSION 1.7.0 [r25351](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25351):

**roll:** The ped is rolling. 

ADDED/UPDATED IN VERSION 1.7.0 [r25371](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25371):

**hanging:** The ped is hanging onto a wall. 

## Example

Click to collapse [-]

**Example 1:** This example shows how you can output a players current movestate.

```
function getMoveState( command, playerName )
-- If the player name exists we will have our 'player'
	local player = getPlayerFromName( playerName )
	-- If the player does not exist, the script will stop.
	if not player then 
		outputChatBox( "No player named " .. playerName .. " was found.", 250, 0, 0, true )
		return false
	end
	-- If we found the player from the name, we can get his movestate.
	local moveState = getPedMoveState( player )
	-- If a player and a movestate is found, the script will output it to the chatbox.
	outputChatBox( playerName .. "'s current moveState is: " .. moveState, 0, 150, 0, true )
end
addCommandHandler( "getMoveState", getMoveState ) -- To execute this command, simply write: /getMoveState playerName
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
