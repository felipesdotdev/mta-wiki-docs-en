---
doc_id: "mta-wiki:3965"
title: "GetPedTarget"
source_title: "GetPedTarget"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedTarget"
revision_id: 50893
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:18.155925+00:00"
---

# GetPedTarget

This function is used to get the element a [ped](mta://reference/misc/ped.md) is currently targeting.

## Syntax

```
element getPedTarget ( ped thePed )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):getTarget(...)*

### Required Arguments

- **thePed:** The [ped](mta://reference/misc/ped.md) whose target you want to retrieve.

### Returns

Returns the [element](mta://reference/misc/element.md) that's being targeted, or *false* if there isn't one.

This is only effective on physical GTA elements, namely:

- Players

- Peds

- Vehicles

- Objects

## Example

Click to collapse [-]
Server

This example blows up any vehicle a player targets (aims at).

```
function playerTargetCheck ( )
    local target
    for i, thePlayer in ipairs ( getElementsByType("player") ) do  -- iterate over all players
        target = getPedTarget ( thePlayer )                        -- get the target of the current player
        if ( target ) then                                         -- if there was a target
            if ( getElementType ( target ) == "vehicle" ) then     -- and the target is a vehicle
                blowVehicle ( target )                             -- blow it up
            end
        end
    end
end
setTimer ( playerTargetCheck, 1000, 0 )                            -- call the check function every second
```

*Note: A more efficient way to do this would be to use the [onPlayerTarget](mta://scripting/server/events/onplayertarget.md) event.*

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

- getPedTarget

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
