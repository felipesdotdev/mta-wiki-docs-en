---
doc_id: "mta-wiki:5433"
title: "GetValidPedModels"
source_title: "GetValidPedModels"
source_url: "https://wiki.multitheftauto.com/wiki/GetValidPedModels"
revision_id: 80799
language: "en"
categories: ["Utility_templates", "Changes_in_1.6.0", "Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:26.652352+00:00"
---

# GetValidPedModels

This function returns all valid ped models. The syntax is different for server and client sides.

## Syntax

Click to collapse [-]
Client

```
table getValidPedModels ( [ bool includeCustom = true ] )
```

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

ADDED/UPDATED IN VERSION 1.6.0 [r22780](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22780):

- **includeCustom:** Specifies if the table returned should contain custom model IDs allocated with [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md).

### Returns

Returns a [table](mta://reference/misc/table.md) with all valid ped models that exist on the client, containing the custom model IDs unless **includeCustom** is false.

Click to collapse [-]
Server

```
table getValidPedModels ( )
```

### Returns

Returns a [table](mta://reference/misc/table.md) with all valid ped models that exist on the server.

## Examples

This example will check if the specified skin ID is a valid skin via a command.

```
function isValidSkin( thePlayer, command, specifiedSkin )
    specifiedSkin = tonumber ( specifiedSkin )
    if ( specifiedSkin ) then -- If skin specified
        local allSkins = getValidPedModels ( ) -- Get valid skin IDs
        local result = false -- Define result, it is currently false
        for _, skin in ipairs( allSkins ) do -- Check all skins
            if skin == specifiedSkin then -- If skin equals specified one, it is valid
                result = true -- So set it as result
                break -- stop looping through a table after we found the skin
            end
        end
        if ( result ) then -- If we got results
            outputChatBox( specifiedSkin .. " is a valid skin ID.", thePlayer, 0, 255, 0 ) -- It is valid, output it
        else -- If we didn't get results
            outputChatBox( specifiedSkin .. " is not a valid skin ID.", thePlayer, 0, 255, 0 ) -- No result, it is not valid
        end
    else
        outputChatBox( "Please specify a valid number to check!", thePlayer, 255, 0, 0 )
    end
end
addCommandHandler("checkskin",isValidSkin) -- bind 'checkskin' command to 'isValidSkin' function
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

- getValidPedModels

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
