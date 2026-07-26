---
doc_id: "mta-wiki:4559"
title: "IsPedDoingGangDriveby"
source_title: "IsPedDoingGangDriveby"
source_url: "https://wiki.multitheftauto.com/wiki/IsPedDoingGangDriveby"
revision_id: 62155
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:58.065179+00:00"
---

# IsPedDoingGangDriveby

This function checks if the ped is in the driveby state.

## Syntax

```
bool isPedDoingGangDriveby ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):isDoingGangDriveby(...)*

**Variable**: *.doingGangDriveby*

**Counterpart**: *[setPedDoingGangDriveby](mta://scripting/shared/functions/setpeddoinggangdriveby.md)*

### Required Arguments

- **thePed:** The [ped](mta://reference/misc/ped.md) element whose state is to be checked.

### Returns

Returns **true** if the driveby state is enabled, **false** otherwise.

## Example

Click to collapse [-]
Client

This example turns on driveby mode when the local player types *driveby* in the console.

```
function setDoingDriveby ( )
        -- we check if local player isn't currently doing a gang driveby
        if not isPedDoingGangDriveby ( localPlayer ) then
                -- if he got driveby mode off, turn it on
                setPedWeaponSlot ( localPlayer, 4 )
                setPedDoingGangDriveby ( localPlayer, true )
        else
                -- otherwise, turn it off
                setPedWeaponSlot ( localPlayer, 0 )
                setPedDoingGangDriveby ( localPlayer, false )
        end
end
addCommandHandler ( "driveby", setDoingDriveby )
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

- isPedDoingGangDriveby

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
