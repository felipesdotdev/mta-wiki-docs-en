---
doc_id: "mta-wiki:4027"
title: "GetPedClothes"
source_title: "GetPedClothes"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedClothes"
revision_id: 59281
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetPedClothes

This function is used to get the current clothes texture and model of a certain type on a [ped](https://wiki.multitheftauto.com/index.php?search=ped).

## Syntax

```
string, string getPedClothes ( ped thePed, int clothesType )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):getClothes(...)*

**Counterpart**: *[addPedClothes](mta://scripting/shared/functions/addpedclothes.md)*

### Required Arguments

- **thePed:** The [ped](https://wiki.multitheftauto.com/index.php?search=ped) whose clothes you want to retrieve.

- **clothesType:** The type/slot of clothing you want to get.

Clothing Types

- **0:** SHIRT

- **1:** HEAD

- **2:** TROUSERS

- **3:** SHOES

- **4:** TATTOOS_LEFT_UPPER_ARM

- **5:** TATTOOS_LEFT_LOWER_ARM

- **6:** TATTOOS_RIGHT_UPPER_ARM

- **7:** TATTOOS_RIGHT_LOWER_ARM

- **8:** TATTOOS_BACK

- **9:** TATTOOS_LEFT_CHEST

- **10:** TATTOOS_RIGHT_CHEST

- **11:** TATTOOS_STOMACH

- **12:** TATTOOS_LOWER_BACK

- **13:** NECKLACE

- **14:** WATCH

- **15:** GLASSES

- **16:** HAT

- **17:** EXTRA

### Returns

This function returns 2 [strings](mta://reference/misc/string.md), the clothes texture and model. The first return value will be *false* if this player's clothes type is empty or an invalid player was specified.

## Example

Click to collapse [-]
Server

This example prints the model and texture of the current clothing on the player who enters the "clothes" command. For example: "clothes 3" for the shoes.

```
function getClothes ( source, key, clothesType )
    local texture, model = getPedClothes ( source, clothesType )
    if ( texture and model ) then
        outputChatBox ( getPlayerName(source) .. " is wearing " .. texture .. " " .. model ..
                        " on his " .. getClothesTypeName(clothesType), source )
    else
        outputChatBox ( "Invalid input.", source )
    end
end
addCommandHandler ( "clothes", getClothes )
```

## See Also

- [addPedClothes](mta://scripting/shared/functions/addpedclothes.md)

- getPedClothes

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
