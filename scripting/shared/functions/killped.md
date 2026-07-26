---
doc_id: "mta-wiki:4032"
title: "KillPed"
source_title: "KillPed"
source_url: "https://wiki.multitheftauto.com/wiki/KillPed"
revision_id: 73892
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.3"]
generated_at: "2026-07-26T16:16:03.845270+00:00"
---

# KillPed

This function kills the specified ped.

From v1.5.3 onwards this function is now available client side. Only works on client side peds.

## Syntax

```
bool killPed ( ped thePed, [ ped theKiller = nil, int weapon=255, int bodyPart=255, bool stealth = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):kill(...)*

### Required Arguments

- **thePed:** The [ped](mta://reference/misc/ped.md) to kill

### Optional Arguments

- **theKiller:** The ped responsible for the kill

- **weapon:** The ID of the [weapon](mta://reference/misc/weapon.md) or [Damage Types](mta://reference/misc/damage-types.md) that should appear to have killed the ped (doesn't affect how they die)

- **bodyPart:** The ID of the body part that should appear to have been hit by the weapon (doesn't affect how they die)

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **stealth:** Boolean value, representing whether or not this a stealth kill

### Returns

Returns *true* if the ped was killed, *false* if the ped specified could not be killed or is invalid.

## Example

**Example 1:** This simple example adds a **kill** command to commit suicide.

```
function commitSuicide ( sourcePlayer )
	-- kill the player and make him responsible for it
	killPed ( sourcePlayer, sourcePlayer )
end
-- attach our handler to the "kill" command
addCommandHandler ( "kill", commitSuicide )
```

**Example 2:** This example enables 1 hit kills if a player is shot in the head.

```
function headshotKill ( attacker, attackerweapon, bodypart, loss )
	if bodypart == 9 then --if the bodypart is the head
		--kill the player, emulating the correct killer, weapon and bodypart.
		killPed ( source, attacker, attackerweapon, bodypart )
	end
end
addEventHandler ( "onPlayerDamage", getRootElement(), headshotKill )
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

- killPed

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
