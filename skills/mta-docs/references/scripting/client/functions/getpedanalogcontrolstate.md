---
doc_id: "mta-wiki:7433"
title: "GetPedAnalogControlState"
source_title: "GetPedAnalogControlState"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedAnalogControlState"
revision_id: 81186
language: "en"
categories: ["Client_functions", "Changes_in_1.5.7"]
---

# GetPedAnalogControlState

This function retrieves the analog control state of a [ped](https://wiki.multitheftauto.com/index.php?search=ped), as set by [setPedAnalogControlState](mta://scripting/client/functions/setpedanalogcontrolstate.md).

## Syntax

```
float getPedAnalogControlState ( ped thePed, string controlName [, bool rawValue ] )
```

### Required Arguments

- **thePed:** The ped you wish to retrieve the control state of.

- **controlName:** The control. See [control names](mta://reference/misc/control-names.md) for a list of possible controls.

### Optional Arguments

- **rawValue:** A [bool](https://wiki.multitheftauto.com/index.php?search=bool) indicating if it should return the raw player input value (will always return script value for non-player peds).

### Returns

Returns a [float](mta://reference/misc/float.md) between 0 (full release) and 1 (full push) indicating the amount the control is pushed.

## Example

This exmaple creating a ped can drive with command **/drive**

```
local ped = createPed(0, 0,0,3)
local vehicle = createVehicle(554,0,0,3)
warpPedIntoVehicle(ped, vehicle)

addCommandHandler("drive",function()
    isDriving = getPedAnalogControlState ( ped, "accelerate" ) -- get the analaog state of (accelerate)
    if isDriving==1 then -- checks if equals 1 that means is driving
        outputChatBox("Ped is driving stoping..")
        setPedAnalogControlState( ped, "accelerate", 0 ) -- set the analaog (accelerate) to 0 
    else 
        outputChatBox("Starting drive")
        setPedAnalogControlState( ped, "accelerate", 1 ) -- set the analaog (accelerate) to 1 
    end 
end)
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
