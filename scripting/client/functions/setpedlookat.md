---
doc_id: "mta-wiki:4188"
title: "SetPedLookAt"
source_title: "SetPedLookAt"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedLookAt"
revision_id: 82744
language: "en"
categories: ["Client_functions", "Functions_and_events_with_issues"]
generated_at: "2026-07-26T16:16:42.971741+00:00"
---

# SetPedLookAt

| [[{{{image}}}\|link=\|]] | Note: Avoid calling setPedLookAt every frame as this can cause bugs like being invincible to burning. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Important Note: For remote players, you have to use setPedAimTarget before setPedLookAt. |
| --- | --- |
|  |  |

Makes a ped turn his head and look at a specific world position or element.

## Syntax

```
bool setPedLookAt ( ped thePed, float x, float y, float z [, int time = 3000 [, int blend = 1000 ], element target = nil ] )
```

### Required Arguments

- **thePed:** the ped to change the lookat of.

- **x:** the x coordinate of the world position to look at.

- **y:** the y coordinate of the world position to look at.

- **z:** the z coordinate of the world position to look at.

### Optional Arguments

- **time:** the time, in milliseconds, during which the ped will look at the target. Once this time has elapsed, he will look ahead again like before the function was applied. A time of 0 will immediately stop any lookat. A negative time will make the ped look at the target indefinitely.

- **blend:** the time, in milliseconds, during which the look will blend.

- **target:** if this argument is specified, the position arguments will be mean offsets relative to the target and the ped's gaze will follow the specified element instead. Can be a player, a vehicle, another ped etc.

## Example

This example makes the local player look at where the camera points at. If you want to sync this effect with other players you can use [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md) and [triggerLatentClientEvent](mta://scripting/server/functions/triggerlatentclientevent.md) functions.

```
local screenSize_X, screenSize_Y = guiGetScreenSize()

function pedLookAt()
   local x, y, z = getWorldFromScreenPosition(screenSize_X / 2, screenSize_Y / 2, 15)
   setPedLookAt(localPlayer, x, y, z, -1, 0)
end
setTimer(pedLookAt, 120, 0)
```

This example makes remote players heads move based on what direction their camera is facing.

```
function remotePlayerHeadMoving()
	local x, y, z = getElementPosition(localPlayer)
	for i, player in pairs(getElementsWithinRange(x, y, z, 35, "player")) do
		if (player ~= localPlayer and isElementOnScreen(player)) then
			local rot = getPedCameraRotation(player)
			local x, y, z = getElementPosition(player)
			local vx = x + math.sin(math.rad(rot)) * 10
			local vy = y + math.cos(math.rad(rot)) * 10
			-- To fix remote player's head bug + check to avoid setPedAimTarget movement lag while aiming with gun
			if (getPedTask(player, "secondary", 0) ~= "TASK_SIMPLE_USE_GUN") then
				if (player ~= localPlayer) then
					setPedAimTarget(player, vx, vy, z) -- head bug fix
				end
				setPedLookAt(player, vx, vy, z, -1, 0)
			end
		end
    end
end
setTimer(remotePlayerHeadMoving, 100, 0)
```

## Issues

| Issue ID | Description |
| --- | --- |
| #509 | setPedLookAt does not work for remote players |
| #626 | setPedLookAt cancels damage done by any sort of fire |

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

- [setPedAimTarget](mta://scripting/client/functions/setpedaimtarget.md)

- [setPedAnalogControlState](mta://scripting/client/functions/setpedanalogcontrolstate.md)

- [setPedBleeding](mta://scripting/client/functions/setpedbleeding.md)

- [setPedCameraRotation](mta://scripting/client/functions/setpedcamerarotation.md)

- [setPedCanBeKnockedOffBike](mta://scripting/client/functions/setpedcanbeknockedoffbike.md)

- [setPedControlState](mta://scripting/client/functions/setpedcontrolstate.md)

- [setPedEnterVehicle](mta://scripting/client/functions/setpedentervehicle.md)

- [setPedExitVehicle](mta://scripting/client/functions/setpedexitvehicle.md)

- [IsPedFootBloodEnabled](mta://scripting/client/functions/ispedfootbloodenabled.md)

- [setPedFootBloodEnabled](mta://scripting/client/functions/setpedfootbloodenabled.md)

- setPedLookAt

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
