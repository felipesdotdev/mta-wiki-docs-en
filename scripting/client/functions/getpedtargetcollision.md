---
doc_id: "mta-wiki:3969"
title: "GetPedTargetCollision"
source_title: "GetPedTargetCollision"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedTargetCollision"
revision_id: 77182
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:18.185526+00:00"
---

# GetPedTargetCollision

This function allows retrieval of where a ped's target is blocked. It will only be blocked if there is an obstacle within a ped's target range.

## Syntax

```
float float float getPedTargetCollision ( ped targetingPed )
```

### Required Arguments

- **targetingPed:** This is the ped whose target collision you wish to retrieve

### Returns

Returns three floats, *x*,*y*,*z*, representing the position where the ped's target collides, or *false* if it was unsuccessful.

## Example

This Example draws a line from where the Ped´s Target Starts to the Point where the Targets Collision is.

```
function drawline()
   local x, y, z = getPedTargetStart(localPlayer) -- Gets the Point to start From.
   if (x) then -- Checks if there is a Point to start From.
      local sx, sy, sz = getPedTargetCollision(localPlayer) -- Gets the Point where the Targets Collision is.
      dxDrawLine3D(x, y, z, sx, sy, sz) -- Draws the Line
   end
end
addEventHandler("onClientPreRender", root, drawline) -- Adds the Handler.
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

- getPedTargetCollision

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
