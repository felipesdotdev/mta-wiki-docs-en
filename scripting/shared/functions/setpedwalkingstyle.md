---
doc_id: "mta-wiki:4230"
title: "SetPedWalkingStyle"
source_title: "SetPedWalkingStyle"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedWalkingStyle"
revision_id: 44902
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:43.394743+00:00"
---

# SetPedWalkingStyle

Sets the walking style of a ped. A walking style consists of a set of animations that are used for walking, running etc.

## Syntax

```
bool setPedWalkingStyle ( ped thePed, int style )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):setWalkingStyle(...)*

**Variable**: *.walkingStyle*

**Counterpart**: *[getPedWalkingStyle](mta://scripting/shared/functions/getpedwalkingstyle.md)*

### Required Arguments

- **thePed:** the ped whose walking style to change.

- **style:** the walking style to set.

The possible walking styles are:

| MOVE_DEFAULT | 0 |
| --- | --- |
| MOVE_PLAYER | 54 |
| MOVE_PLAYER_FAT | 55 |
| MOVE_PLAYER_MUSCULAR | 56 |
| MOVE_ROCKET | 57 |
| MOVE_ROCKET_FAT | 58 |
| MOVE_ROCKET_MUSCULAR | 59 |
| MOVE_ARMED | 60 |
| MOVE_ARMED_FAT | 61 |
| MOVE_ARMED_MUSCULAR | 62 |
| MOVE_BASEBALLBAT | 63 |
| MOVE_BASEBALLBAT_FAT | 64 |
| MOVE_BASEBALLBAT_MUSCULAR | 65 |
| MOVE_CHAINSAW | 66 |
| MOVE_CHAINSAW_FAT | 67 |
| MOVE_CHAINSAW_MUSCULAR | 68 |
| MOVE_SNEAK | 69 |
| MOVE_JETPACK | 70 |
| MOVE_MAN | 118 |
| MOVE_SHUFFLE | 119 |
| MOVE_OLDMAN | 120 |
| MOVE_GANG1 | 121 |
| MOVE_GANG2 | 122 |
| MOVE_OLDFATMAN | 123 |
| MOVE_FATMAN | 124 |
| MOVE_JOGGER | 125 |
| MOVE_DRUNKMAN | 126 |
| MOVE_BLINDMAN | 127 |
| MOVE_SWAT | 128 |
| MOVE_WOMAN | 129 |
| MOVE_SHOPPING | 130 |
| MOVE_BUSYWOMAN | 131 |
| MOVE_SEXYWOMAN | 132 |
| MOVE_PRO | 133 |
| MOVE_OLDWOMAN | 134 |
| MOVE_FATWOMAN | 135 |
| MOVE_JOGWOMAN | 136 |
| MOVE_OLDFATWOMAN | 137 |
| MOVE_SKATE | 138 |

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Client example

Changes the walking style of the player to Drunkman when the resource is started

```
function onClientResourceStart()
	setPedWalkingStyle(localPlayer,126) 
end
addEventHandler("onClientResourceStart",resourceRoot, onClientResourceStart)
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

- setPedWalkingStyle

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
