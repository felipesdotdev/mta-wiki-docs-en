---
doc_id: "mta-wiki:3985"
title: "SetPedAnimation"
source_title: "SetPedAnimation"
source_url: "https://wiki.multitheftauto.com/wiki/SetPedAnimation"
revision_id: 79882
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates", "Functions_and_events_with_issues"]
generated_at: "2026-07-26T16:16:41.889333+00:00"
---

# SetPedAnimation

Sets the current [animation](mta://reference/misc/animations.md) of a [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md). Not specifying the type of animation will automatically cancel the current one.

| [[\|link=\|]] | Warning: It is possible that an animation will be cancelled if you use setElementFrozen on the ped, but this does not happen all the time. |
| --- | --- |
|  |  |

## Syntax

```
bool setPedAnimation ( ped thePed [, string block = nil, string anim = nil, int time = -1, bool loop = true, bool updatePosition = true,
                       bool interruptable = true, bool freezeLastFrame = true, int blendTime = 250, bool retainPedState = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](mta://reference/misc/ped.md):setAnimation(...)*

**Counterpart**: *[getPedAnimation](mta://scripting/client/functions/getpedanimation.md)*

### Required Arguments

- **thePed:** the [player](mta://reference/misc/player.md) or [ped](mta://reference/misc/ped.md) you want to apply an [animation](mta://reference/misc/animations.md) to.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **block:** the [animation](mta://reference/misc/animations.md) block's name.

- **anim:** the name of the [animation](mta://reference/misc/animations.md) within the block.

- **time:** how long the animation will run for in milliseconds.

- **loop:** indicates whether or not the animation will loop.

- **updatePosition:** will change the actual coordinates of the ped according to the animation. Use this for e.g. walking animations.

- **interruptable:** if set to *false* other tasks wont be able to interupt the animation. Setting this to 'false' also gives this function more power to override other animations that are running. For example, squatting after a jump can be terminated.

- **freezeLastFrame:** if set to *true* after animation the last frame will be frozen, otherwise the animation will end and controls will return.

- **blendTime:** how long the animation will mixed with the previous one in milliseconds.

- **retainPedState:** will restore the task which was playing before calling this function. Useful for restoring the crouch task after animation ends. This may be extended in the future to support other states/tasks.

### Returns

Returns *true* if succesful, *false* otherwise.

## Examples

Click to collapse [-]
Server

This example creates a ped, rotates him, and makes him walk:

```
function makePed()
	local thePed = createPed(56, 1, 1, 4, 315)
	setPedAnimation(thePed, "ped", "WOMAN_walknorm")
end
addCommandHandler("makemyped", makePed)
```

Click to collapse [-]
Server

This example makes the player sit down and stand up using the command /sit.

```
local playerSitState = {}

function toggleSit(thePlayer)
	local playerSitting = playerSitState[thePlayer]

	if (not playerSitting) then
		setPedAnimation(thePlayer, "ped", "seat_down", -1, false, false, false, false)
		playerSitState[thePlayer] = true -- store the player state in the table

		return true
	end

	setPedAnimation(thePlayer) -- if you use again this command then your character stand up
	playerSitState[thePlayer] = nil -- remove player sit state from table
end
addCommandHandler("sit", toggleSit)

function onPlayerQuitClearSitState()
	playerSitState[source] = nil -- clear state at player quit, to prevent memory leak
end
addEventHandler("onPlayerQuit", root, onPlayerQuitClearSitState)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.5.7-9.16632 | Added retainPedState argument |
| --- | --- |

## Issues

| Issue ID | Description |
| --- | --- |
| #1110 | retainPedState in setPedAnimation() does not work when latency reduction is set to 1 |
| #953 | setPedAnimation() "interrupt" and "time" has no effect in certain situations |
| #467 | Ped animations don't sync for new players |
| #463 | setPedAnimation() does not work when a ped is attached and floating in air |
| #1173 | setPedAnimation() removes player jetpack |
| #884 | setPedAnimation() messes up collisions of peds inside vehicles |

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

- setPedAnimation

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
