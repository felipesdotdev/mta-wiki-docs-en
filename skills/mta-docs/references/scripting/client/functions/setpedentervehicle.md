---
doc_id: "mta-wiki:12574"
title: "SetPedEnterVehicle"
source_title: "SetPedEnterVehicle"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedEnterVehicle"
revision_id: 82691
language: "en"
categories: ["Client_functions"]
---

# SetPedEnterVehicle

This function makes a [ped](https://wiki.multitheftauto.com/index.php?search=ped) enter a [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle), similar to the enter_exit control state.

| [[{{{image}}}\|link=\|]] | Note: This function only works on synced peds and vehicles (ie. created serverside). |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This function only works within the following limits: If forced to enter as a passenger, it doesn't work if all passenger seats are occupied. Only the driver seat can be jacked. If forced to enter as a driver, the ped can carjack the current driver. If the driver's door is blocked by something, the ped can use the opposite front door to reach the driver's seat, jacking the passenger in the process. If a vehicle is not specified: The ped will search for a vehicle door within 20 m. If the vehicle has a driver, the limit becomes 10 m. If a vehicle is specified: The vehicle has to be within 50 m. The doors aren't taken into account. It means that it doesn't work if the vehicle's door is in range but the vehicle itself is not. If the vehicle has a driver, the limit becomes 10 m. When entering, the ped will run toward a vehicle if it is less than 50 m away. The ped reserves the seat it is trying to use. It means nobody can enter the respective seat while the ped is running toward it. Exception: If the ped is forced to enter as a passenger and is going to use the front door, the ped can wait if someone is using it to go the driver seat. |
| --- | --- |
|  |  |

## Syntax

```
bool setPedEnterVehicle ( ped thePed [, vehicle theVehicle = nil, bool passenger = false ] )
```

### Required Arguments

- **thePed:** The [player](https://wiki.multitheftauto.com/index.php?search=player) or [ped](https://wiki.multitheftauto.com/index.php?search=ped) to enter the vehicle.

- *Note: The player must be the local player.*

- *Note: The ped must be synced by the client. Use [isElementSyncer](mta://scripting/client/functions/iselementsyncer.md) clientside to check if the client is syncing. Use [setElementSyncer](mta://scripting/server/functions/setelementsyncer.md) serverside to change the syncer manually.*

- **vehicle:** The [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) to enter. If no vehicle is set, the ped will enter the nearest vehicle within 20 m.

- **passenger:** If set to *true*, the ped will enter as passenger in the nearest available seat, otherwise he will enter as driver.

### Returns

Returns *true* if the function was successful, *false* otherwise.

When this function returns *true*, the client will ask server for permission to enter a vehicle. Actually entering can still fail in the following cases

- Another player or ped is already entering, exiting or jacking the same vehicle and seat.

- Movement input or damage can interrupt the task. Use [getPedTask](mta://scripting/client/functions/getpedtask.md) to monitor what the ped is doing.

This function returns *false* in the following cases

- Invalid arguments were parsed.

- Time passed since last enter/exit for this ped is less than 1500 ms.

- [onClientVehicleStartEnter](mta://scripting/client/events/onclientvehiclestartenter.md) was cancelled by a script.

- The ped has an active TASK_PRIMARY [task](https://wiki.multitheftauto.com/index.php?search=task). Use [getPedTask](mta://scripting/client/functions/getpedtask.md) to monitor what the ped is doing.

## Example

Make [ped](https://wiki.multitheftauto.com/index.php?search=ped) Sweet enter his car:

Click to collapse [-]
Server

```
local sweet = createPed (270, 0, 0, 3)
setElementID (sweet, "sweet")

local sweetscar = createVehicle (492, 3, 0, 3)
setElementID (sweetscar, "sweetscar")
```

Click to collapse [-]
Client

```
-- Code works only if client is syncing ped Sweet
addCommandHandler ("sweetentercar",
function()
    local sweet = getElementByID ("sweet")

    if isElementSyncer (sweet) then
        setPedEnterVehicle (sweet, getElementByID("sweetscar"), true)
    end
end)
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

- setPedEnterVehicle

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
