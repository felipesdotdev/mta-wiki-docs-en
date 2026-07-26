---
doc_id: "mta-wiki:11747"
title: "SetPedArmor"
source_title: "SetPedArmour"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedArmour"
revision_id: 81017
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
generated_at: "2026-07-26T16:16:41.980241+00:00"
---

# SetPedArmor

This function allows you to set the armor value of a [ped](mta://reference/misc/ped.md).
Function also added client-side.

## Syntax

```
bool setPedArmor ( ped thePed, float armor )
```

 

Armor bar on the hud

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):setArmor(...)*

**Variable**: *.armor*

**Counterpart**: *[getPedArmor](mta://scripting/shared/functions/getpedarmor.md)*

### Required Arguments

- **thePed**: the [ped](mta://reference/misc/ped.md) whose armor you want to modify.

- **armor**: the amount of armor you want to set on the ped. Valid values are from 0 to 100.

### Returns

Returns *true* if the armor was changed succesfully. Returns *false* if an invalid ped was specified, or the armor value specified is out of acceptable range.

## Example

This example removes the armor of a player.

```
function armor (player, command)
   if command == "addarmor" then 
      setPedArmor ( player, 100 )    -- Set player's armor to 100 when he types the command 'addarmor'
   elseif command == "removearmor" then 
      setPedArmor ( player, 0 )      -- Set player's armor to 0 when he types the command 'removearmor'
   end 
end
addCommandHandler ("addarmor", armor)
addCommandHandler ("removearmor", armor)
```

In this, adds an amount of armor that the player defined in command 'addarmor'.

```
function givePlayerArmor( player, command, amount )
   if getPedArmor(player) == 100 then
      outputChatBox("Your armor already is complete!", player, 220, 0, 0 ) -- Inform the player if your armor already is complete.
      return
   end

   if amount and tonumber(amount) >= 1 or tonumber(amount) <= 100 then -- If amount is between 1 and 100.
      setPedArmor(player, tonumber(amount))    -- Set amount armor that player chosen on the command.
   else
      outputChatBox( "Syntax: /addarmor [armor-amount] the amount should be between 1 and 100", player, 220, 0, 0 ) -- Inform the player if 'amount' argument is missing.
   end
end
addCommandHandler( "addarmor", givePlayerArmor )
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

- setPedArmor

- [setPedDoingGangDriveby](mta://scripting/shared/functions/setpeddoinggangdriveby.md)

- [setPedFightingStyle](mta://scripting/shared/functions/setpedfightingstyle.md)

- [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md)

- [setPedStat](mta://scripting/shared/functions/setpedstat.md)

- [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
