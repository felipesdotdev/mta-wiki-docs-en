---
doc_id: "mta-wiki:4143"
title: "GetPedAnimation"
source_title: "GetPedAnimation"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedAnimation"
revision_id: 82135
language: "en"
categories: ["Client_functions", "Changes_in_1.5.7"]
generated_at: "2026-07-26T16:15:16.777572+00:00"
---

# GetPedAnimation

Gets the animation of a player or ped that was set using [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md).

| [[{{{image}}}\|link=\|]] | Note: Use getPedTask to monitor what movements the player is currently doing. |
| --- | --- |
|  |  |

## Syntax

BEFORE VERSION 1.5.7 [r20450](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=20450):

```
string, string getPedAnimation ( ped thePed )
```

```
string, string, int, int, bool, bool, bool, int, bool getPedAnimation ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):getAnimation(...)*

**Counterpart**: *[setPedAnimation](mta://scripting/shared/functions/setpedanimation.md)*

### Required Arguments

- **thePed:** the [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) you want to get the [animation](mta://reference/misc/animations.md) of.

### Returns

BEFORE VERSION 1.5.7 [r20450](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=20450):

Returns two [strings](mta://reference/misc/string.md): the first is the name of the block, the second is the name of the animation. Returns *false* if there was an error or if the ped is not doing an animation.

The function returns 9 values in the same order as required by [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md):

```
string block, string anim, int time, bool loop, bool updatePosition, bool interruptable, bool freezeLastFrame, int blendTime, bool restoreTaskOnAnimEnd
```

## Examples

This example adds a command that allows you to copy the animation being used by another player using /copyanim theirName

```
function CopyAnimation(theCommand, thePlayer) -- The Command Function
	if thePlayer then -- If a player name entered then
		thePlayerToCopyFrom = getPlayerFromName(thePlayer) -- get player from his name
		block, anim = getPedAnimation(thePlayerToCopyFrom) -- get the player animation
		if block then -- if got the animation successfully then
			setPedAnimation(localPlayer, block, anim) -- set my animation the same
			outputChatBox("* Copied Successfully !") -- output chat message
		end
	else	
		outputChatBox("* Please Enter a Player Name To Copy From !") -- if you didnt entered a player name , then output a chat box message
	end
end
addCommandHandler("copyanim", CopyAnimation) --  adding the Command Handler
```

This example shows what block and animation your player is currently performing. Note this will return "N/A" if you did not set an animation with [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md). If you want to see what the player ped is doing as you control them that is [getPedTask](mta://scripting/client/functions/getpedtask.md).

```
addEventHandler("onClientPreRender",root,
	function ()
    local block, animation = getPedAnimation(localPlayer)
	dxDrawText ( "CURRENT ANIMATION INFO...", 100, 300 )
	if not block then block = "N/A" end
	if not animation then animation = "N/A" end
	dxDrawText ( "Block = "..block.." Animation = "..animation, 100, 315 )
end )
```

## See Also

- [canPedBeKnockedOffBike](mta://scripting/client/functions/canpedbeknockedoffbike.md)

- [getPedAnalogControlState](mta://scripting/client/functions/getpedanalogcontrolstate.md)

- getPedAnimation

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
