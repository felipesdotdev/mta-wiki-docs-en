---
doc_id: "mta-wiki:4603"
title: "SetPedAimTarget"
source_title: "SetPedAimTarget"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedAimTarget"
revision_id: 81905
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:41.819679+00:00"
---

# SetPedAimTarget

This function allows you to set a ped's aim target to a specific point. If a ped is within a certain range defined by [getPedTargetStart](mta://scripting/client/functions/getpedtargetstart.md) and [getPedTargetEnd](mta://scripting/client/functions/getpedtargetend.md) he will be targeted and shot.

*Note: If you wish to make a ped shoot you must use this in conjunction with an equipped weapon and [setPedControlState](mta://scripting/client/functions/setpedcontrolstate.md).  Also for akimbo weapons such as 22, 26, 28, 32 and the sniper rifle you must also set both aim_weapon and fire to true at least once.*

## Syntax

```
bool setPedAimTarget ( ped thePed, float x, float y, float z )
```

### Required Arguments

- **thePed:** The ped whose target you want to set. Only peds and remote players will work; this function has no effect on the local player.

- **x:** The x coordinate of the aim target point.

- **y:** The y coordinate of the aim target point.

- **z:** The z coordinate of the aim target point.

### Returns

Returns *true* if the function was successful, *false* otherwise.

## Example

**Example 1:** This example creates a ped in the middle of the map and sets its aim target to point north-east.

```
function createPedAndsetHisAimTarget ()
        local ped = createPed (0, 0, 0, 5 ) -- create a ped, who looks like cj, in the middle of the map
        setPedAimTarget ( ped, 10, 10, 5 ) -- set the ped's target to a point in North-East
end
```

**Example 2:** This example creates a ped at grove street that will shoot at anything that enters a certain marker.

```
local cj = createPed(0, 2498.5, -1684.0, 13.5, 20) -- create a ped at cjs house in grove street and give it an ak
givePedWeapon(cj, 30, 3000, true)

local marker = createMarker(2493.0, -1669.0, 13.5, "checkpoint", 3, 255, 0, 0, 128) -- create a marker and get its associated colshape for later use
local colshape = getElementColShape(marker)

function renderHandler()
	local intruder = getElementsWithinColShape(colshape)[2] -- get the second element found within the colshape, because the first one will normally be the marker itself
	if intruder then
		local x,y,z = getElementPosition(intruder) -- if an intruder exists, get its position and have the cj ped fire at it
		setPedAimTarget(cj, x, y, z)
		setPedControlState(cj, "fire", true)
		setPedControlState(cj, "aim_weapon", true) -- needed for akimbo weapons (22, 26, 28, 32) and the sniper rifle
	else
		setPedControlState(cj, "fire", false) -- otherwise stop shooting
		setPedControlState(cj, "aim_weapon", false)
	end
end
addEventHandler("onClientRender", root, renderHandler) -- add an event handler to go through the target acquisition procedure every frame
```

## See Also

- [canPedBeKnockedOffBike](mta://scripting/client/functions/canpedbeknockedoffbike.md)

- [getPedAnalogControlState](mta://scripting/client/functions/getpedanalogcontrolstate.md)

- [getPedAnimation](mta://scripting/client/functions/getpedanimation.md)

- [getPedBonePosition](mta://scripting/client/functions/getpedboneposition.md)

- [getPedCameraRotation](mta://scripting/client/functions/getpedcamerarotation.md)

- [getPedControlState](mta://scripting/client/functions/getpedcontrolstate.md)

- [getPedMoveState](mta://scripting/client/functions/getpedmovestate.md)

- [getPedOxygenLevel](mta://scripting/client/functions/getpedoxygenlevel.md)

- [getPedSimplestTask](mta://scripting/client/functions/getpedsimplesttask.md)

- [getPedTargetCollision](mta://scripting/client/functions/getpedtargetcollision.md)

- [getPedTargetEnd](mta://scripting/client/functions/getpedtargetend.md)

- [getPedTargetStart](mta://scripting/client/functions/getpedtargetstart.md)

- [getPedTask](mta://scripting/client/functions/getpedtask.md)

- [getPedVoice](mta://scripting/client/functions/getpedvoice.md)

- [getPedWeaponMuzzlePosition](mta://scripting/client/functions/getpedweaponmuzzleposition.md)

- [givePedWeapon](mta://scripting/client/functions/givepedweapon.md)

- [isPedBleeding](mta://scripting/client/functions/ispedbleeding.md)

- [isPedDoingTask](mta://scripting/client/functions/ispeddoingtask.md)

- [isPedTargetingMarkerEnabled](mta://scripting/client/functions/ispedtargetingmarkerenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21874](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21874):

- [resetPedVoice](mta://scripting/client/functions/resetpedvoice.md)

- setPedAimTarget

- [setPedAnalogControlState](mta://scripting/client/functions/setpedanalogcontrolstate.md)

- [setPedBleeding](mta://scripting/client/functions/setpedbleeding.md)

- [setPedCameraRotation](mta://scripting/client/functions/setpedcamerarotation.md)

- [setPedCanBeKnockedOffBike](mta://scripting/client/functions/setpedcanbeknockedoffbike.md)

- [setPedControlState](mta://scripting/client/functions/setpedcontrolstate.md)

- [setPedEnterVehicle](mta://scripting/client/functions/setpedentervehicle.md)

- [setPedExitVehicle](mta://scripting/client/functions/setpedexitvehicle.md)

- [IsPedFootBloodEnabled](mta://scripting/client/functions/ispedfootbloodenabled.md)

- [setPedFootBloodEnabled](mta://scripting/client/functions/setpedfootbloodenabled.md)

- [setPedLookAt](mta://scripting/client/functions/setpedlookat.md)

- [setPedOxygenLevel](mta://scripting/client/functions/setpedoxygenlevel.md)

- [setPedTargetingMarkerEnabled](mta://scripting/client/functions/setpedtargetingmarkerenabled.md)

- [setPedVoice](mta://scripting/client/functions/setpedvoice.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22997](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22997):

- [playPedVoiceLine](mta://scripting/client/functions/playpedvoiceline.md)

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
