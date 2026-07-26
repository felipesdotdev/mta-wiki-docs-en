---
doc_id: "mta-wiki:3981"
title: "SetPedWeaponSlot"
source_title: "SetPedWeaponSlot"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedWeaponSlot"
revision_id: 48751
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetPedWeaponSlot

This function changes the selected weapon slot of a [ped](https://wiki.multitheftauto.com/index.php?search=ped).

## Syntax

```
bool setPedWeaponSlot ( ped thePed, int weaponSlot )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):setWeaponSlot(...)*

**Variable**: *.weaponSlot*

**Counterpart**: *[getPedWeaponSlot](mta://scripting/shared/functions/getpedweaponslot.md)*

### Required Arguments

- **thePed:** the [ped](https://wiki.multitheftauto.com/index.php?search=ped) whose weapon slot you want to set. In a clientside script, this cannot be used on remote players.

- **weaponSlot:** the weapon slot to set.

Weapon Slots

- **0:** WEAPONSLOT_TYPE_UNARMED

- **1:** WEAPONSLOT_TYPE_MELEE

- **2:** WEAPONSLOT_TYPE_HANDGUN

- **3:** WEAPONSLOT_TYPE_SHOTGUN

- **4:** WEAPONSLOT_TYPE_SMG (used for driveby's)

- **5:** WEAPONSLOT_TYPE_RIFLE

- **6:** WEAPONSLOT_TYPE_SNIPER

- **7:** WEAPONSLOT_TYPE_HEAVY

- **8:** WEAPONSLOT_TYPE_THROWN

- **9:** WEAPONSLOT_TYPE_SPECIAL

- **10:** WEAPONSLOT_TYPE_GIFT

- **11:** WEAPONSLOT_TYPE_PARACHUTE

- **12:** WEAPONSLOT_TYPE_DETONATOR

### Returns

Returns *true* if successful in setting the ped's equipped weapon slot, *false* otherwise.

## Example

Click to collapse [-]
Server

This example allows the player to type the command 'giveweapons', which gives the player a weapon for every slot. Instead of equipping the last given weapon, the script randomly decides which weapon to equip after all the weapons are given.

```
local weaponIDs = {1,22,25,28,30,33,35,16,42,10,44,40} -- Weapon IDs

function givePlayerWeapons ( thePlayer, commandName )
   -- Give the player a weapon for each slot
   for i = 1 , #weaponIDs do
      giveWeapon (thePlayer,weaponIDs[i], 1 )
   end
   -- Randomly select which weapon to equip, slots 1 through 12
   setPedWeaponSlot ( thePlayer, math.random ( 1, 12) )
end
addCommandHandler ( "giveweapons", givePlayerWeapons )
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

- setPedWeaponSlot

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
