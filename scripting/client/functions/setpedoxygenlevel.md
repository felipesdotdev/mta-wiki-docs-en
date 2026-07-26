---
doc_id: "mta-wiki:6821"
title: "SetPedOxygenLevel"
source_title: "SetPedOxygenLevel"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedOxygenLevel"
revision_id: 43087
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:43.180500+00:00"
---

# SetPedOxygenLevel

This function allows you to set the oxygen level of a [ped](mta://reference/misc/ped.md).

## Syntax

```
bool setPedOxygenLevel ( ped thePed, float oxygen )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):setOxygenLevel(...)*

**Variable**: *.oxygenLevel*

**Counterpart**: *[getPedOxygenLevel](mta://scripting/client/functions/getpedoxygenlevel.md)*

### Required Arguments

- **thePed**: the [ped](mta://reference/misc/ped.md) whose oxygen level you want to modify.

- **oxygen**: the amount of oxygen you want to set on the [ped](mta://reference/misc/ped.md). Native values are from 0 to 1000. Each of the stamina (22) and underwater stamina (225) [stat](https://wiki.multitheftauto.com/wiki/Template:Stats) maximum adds a bonus of 1500. So the maximum oxygen level is 4000.

### Returns

Returns *true* if the oxygen level was changed succesfully. Returns *false* if an invalid ped and/or oxygen level was specified.

## Example

This example fills the local player's oxygen.

```
function fillOxygen ( command )
	local maxOxygen = math.floor ( 1000 + getPedStat ( localPlayer, 22 ) * 1.5 + getPedStat ( localPlayer, 225 ) * 1.5 )
	setPedOxygenLevel ( localPlayer, maxOxygen )
end
addCommandHandler ( "filloxygen", fillOxygen )
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

- setPedOxygenLevel

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
