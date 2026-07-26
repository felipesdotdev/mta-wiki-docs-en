---
doc_id: "mta-wiki:4037"
title: "SetPedFightingStyle"
source_title: "SetPedFightingStyle"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedFightingStyle"
revision_id: 81018
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
---

# SetPedFightingStyle

Changes a ped's fighting style. Most styles only change the 'special attack' which is done using the Aim and Enter keys.
Function also added client-side.

## Syntax

```
bool setPedFightingStyle ( ped thePed, int style )
```

### Required Arguments

- **thePed:** The ped whose fighting style to change.

- **style:** The fighting style ID to apply.

**Fighting Styles:**

| Fighting Style | ID |
| --- | --- |
| STYLE_STANDARD | 4 |
| STYLE_BOXING | 5 |
| STYLE_KUNG_FU | 6 |
| STYLE_KNEE_HEAD | 7 |
| STYLE_GRAB_KICK | 15 |
| STYLE_ELBOWS | 16 |

### Returns

Returns *true* in case of success, *false* otherwise.

## Example

This example sets the player's fighting style to the desired style when he types "setstyle" followed by a number from 4 to 16 in console.

```
function consoleSetFightingStyle ( thePlayer, commandName, id )
	if thePlayer and id then                                                     -- If player and ID are specified
		local status = setPedFightingStyle ( thePlayer, tonumber(id) )       -- set the fighting style
		if not status then                                                   -- if that failed
			outputConsole ( "Failed to set fighting style.", thePlayer ) -- show a message
		end
	end
end
addCommandHandler ( "setstyle",  consoleSetFightingStyle )
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

- setPedFightingStyle

- [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md)

- [setPedStat](mta://scripting/shared/functions/setpedstat.md)

- [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
