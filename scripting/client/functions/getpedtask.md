---
doc_id: "mta-wiki:3963"
title: "GetPedTask"
source_title: "GetPedTask"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedTask"
revision_id: 82244
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:18.290408+00:00"
---

# GetPedTask

This function is used to get any simple or complex [task](mta://reference/misc/task.md) of a certain type for a ped.

It can provide feedback on all tasks relating to a ped. For example, while jumping, [getPedSimplestTask](mta://scripting/client/functions/getpedsimplesttask.md) will return TASK_SIMPLE_IN_AIR. If you wanted to know specifically if the player has jumped, you would use this function. If you did you will discover that while jumping Primary task 3 is TASK_COMPLEX_JUMP.

## Syntax

```
string, string, string, string getPedTask ( ped thePed, string priority, int taskType )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):getTask(...)*

### Required Arguments

- **thePed**: The [ped](mta://reference/misc/ped.md) whose task you want to retrieve.

- **priority**: A string determining which set of tasks you want to retrieve it from. This must be either "primary" or "secondary".

- **taskType**: An integer value representing the task type (or slot) you want to get the task from. Types can be:

- **PRIMARY TASKS**

- **0:** TASK_PHYSICAL_RESPONSE

- **1:** TASK_EVENT_RESPONSE_TEMP

- **2:** TASK_EVENT_RESPONSE_NONTEMP

- **3:** TASK_PRIMARY

- **4:** TASK_DEFAULT

- **SECONDARY TASKS**

- **0:** TASK_SECONDARY_ATTACK

- **1:** TASK_SECONDARY_DUCK

- **2:** TASK_SECONDARY_SAY

- **3:** TASK_SECONDARY_FACIAL_COMPLEX

- **4:** TASK_SECONDARY_PARTIAL_ANIM

- **5:** TASK_SECONDARY_IK

### Returns

Returns the name of the most complex task. See [list of player tasks](mta://reference/misc/list-of-player-tasks.md) for valid strings. Returns *false* if invalid arguments are specified or if there is no task of the type specified.
  

Returns between 1 and 4 strings. The first string contains the name of the most complex task, with simpler sub-tasks being named in the following strings. See [list of player tasks](mta://reference/misc/list-of-player-tasks.md) for valid strings. Returns *false* if invalid arguments are specified or if there is no task of the type specified.

## Example

This example draws the active primary and secondary tasks (including task hierarchy in 1.1) as your local player moves around the world.

```
local function renderPlayerTasks()
	local textX, textY = 100, 200

	for taskType = 0, 4 do
		local a, b, c, d = getPedTask(localPlayer, "primary", taskType)

		dxDrawText("Primary task #"..taskType.." is "..tostring(a).." -> "..tostring(b).." -> "..tostring(c).." -> "..tostring(d).." -> ", textX, textY)

		textY = (textY + 15)
	end

	textY = (textY + 15)

	for taskType = 0, 5 do
		local a, b, c, d = getPedTask(localPlayer, "secondary", taskType)

		dxDrawText("Secondary task #"..taskType.." is "..tostring(a).." -> "..tostring(b).." -> "..tostring(c).." -> "..tostring(d).." -> ", textX, textY)

		textY = (textY + 15)
	end
end
addEventHandler("onClientRender", root, renderPlayerTasks)
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

- getPedTask

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
