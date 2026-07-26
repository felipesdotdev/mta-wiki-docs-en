---
doc_id: "mta-wiki:3983"
title: "SetPedRotation"
source_title: "SetPedRotation"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedRotation"
revision_id: 80464
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated", "Changes_in_1.3.2"]
---

# SetPedRotation

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setElementRotation instead. |  |

This function allows you to set the current rotation of the specified ped.

## Syntax

```
bool setPedRotation ( ped thePed, float rotation [, bool conformPedRotation = false ] )
```

### Required Arguments

- **thePed:** The [ped](https://wiki.multitheftauto.com/index.php?search=ped) to set the rotation of

- **rotation:** A [float](mta://reference/misc/float.md) specifying the desired rotation in degrees.

### Optional Arguments

- **conformPedRotation:** A bool which should be set to *true* to ensure the ped rotation is correctly set in all circumstances. Failing to set this argument may result in the rotation being inverted when the ped is in the air and other inconsistencies. The default value of false is for backward compatibility with scripts which may depend upon the incorrect behaviour

### Returns

Returns *true* if successful, *false* otherwise.

## Example

Click to collapse [-]
Client

This example allows a player to type the command 'disco', which will result in the player being rotated to a random direction every 1 second, infinite times.

```
function discoTime ( )
     -- Randomly choose a new player rotation and set it
     newRotation = math.random ( 0, 360 )
     setPedRotation ( getLocalPlayer(), newRotation )
end

function initiateDiscoMode ( commandName )
     -- Trigger a random change in player rotation every second
     setTimer ( discoTime, 1000, 0 )
end
addCommandHandler ( "disco", initiateDiscoMode )
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.1-9.04680 | Added conformPedRotation argument |
| --- | --- |

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
