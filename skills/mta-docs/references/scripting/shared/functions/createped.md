---
doc_id: "mta-wiki:3909"
title: "CreatePed"
source_title: "CreatePed"
source_url: "https://wiki.multitheftauto.com/wiki/CreatePed"
revision_id: 82711
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions", "Functions_and_events_with_issues"]
---

# CreatePed

Creates a Ped in the GTA world.

## Syntax

Click to collapse [-]
Server

```
ped createPed ( int modelid, float x, float y, float z [, float rot = 0.0, bool synced = true ] )
```

### Required Arguments

- **modelid:** A whole integer specifying the [GTASA skin ID](mta://reference/misc/character-skins.md).

- **x:** A floating point number representing the X coordinate on the map.

- **y:** A floating point number representing the Y coordinate on the map.

- **z:** A floating point number representing the Z coordinate on the map.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **rot:** A floating point number representing the rotation in degrees.

- **synced:** A boolean value representing whether or not the ped will be synced. Disabling the sync might be useful for frozen or static peds to increase the server performance.

Click to collapse [-]
Client

```
ped createPed ( int modelid, float x, float y, float z [, float rot = 0.0 ] )
```

### Required Arguments

- **modelid:** A whole integer specifying the [GTASA skin ID](mta://reference/misc/character-skins.md).

- **x:** A floating point number representing the X coordinate on the map.

- **y:** A floating point number representing the Y coordinate on the map.

- **z:** A floating point number representing the Z coordinate on the map.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **rot:** A floating point number representing the rotation in degrees.

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Ped](https://wiki.multitheftauto.com/index.php?search=Ped)(...)*

### Returns

Returns a ped element if it was successfully created.

## Example

Click to collapse [-]
Server

This example creates an ped when the resource starts:

```
function pedLoad ( name )
   createPed ( 120, 5540.6654, 1020.55122, 1240.545 )
end
addEventHandler ( "onResourceStart", getResourceRootElement(), pedLoad )
```

Click to collapse [-]
Client

This example creates a ped, and makes it damage proof:

```
thePed = createPed(120, 5540.6654, 1020.55122, 1240.545) -- Creates a ped
function cancelPedDamage()
	cancelEvent() -- Cancels the onClientPedDamage event
end
addEventHandler("onClientPedDamage", thePed, cancelPedDamage) -- When thePed is damaged, cancelPedDamage is called
```

## Issues

{{Issues|
|[#375](https://github.com/multitheftauto/mtasa-blue/issues/375)
|Sync distance of unoccupied vehicles and peds should match stream distance
|-
|[#605](https://github.com/multitheftauto/mtasa-blue/issues/605)
|Ped fireing Projectiles doesn't work
|-

## See Also

- [addPedClothes](mta://scripting/shared/functions/addpedclothes.md)

- [getPedClothes](mta://scripting/shared/functions/getpedclothes.md)

- [removePedClothes](mta://scripting/shared/functions/removepedclothes.md)

- createPed

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
