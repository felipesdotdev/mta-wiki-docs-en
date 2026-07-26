---
doc_id: "mta-wiki:4619"
title: "BlendPedAnimation"
source_title: "BlendPedAnimation"
source_url: "https://wiki.multitheftauto.com/wiki/BlendPedAnimation"
revision_id: 73871
language: "en"
categories: ["Utility_templates", "Server_functions", "Client_functions", "Disabled_Functions_and_Events"]
generated_at: "2026-07-26T16:11:13.311577+00:00"
---

# BlendPedAnimation

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: This function doesn't exist. See the bugtracker for updates and more information. |  |

Sets the current animation of a player or ped.  Not specifying the type of animation will automatically cancel the current one.

Click to collapse [-]
Client

```
bool blendPedAnimation ( ped thePed [, string block, string name, float speed=1.0, float blendSpeed=1.0, float startTime=0.0, bool loop=true, bool updatePosition=true, bool interruptable=false, function callbackFunction=nil, var arguments, ... ] )
```

### Required Arguments

- **thePed:** the player or ped you want to apply an animation to.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **block:** the [animation](mta://reference/misc/animations.md) block's name.

- **anim:** the name of the [animation](mta://reference/misc/animations.md) within the block.

- **speed:** the speed at which the animation is played.

- **blendSpeed:** the speed at which the previous and current animation are blended.

- **startTime:** how far into the animation (in seconds) you want to skip

- **loop:** indicates whether or not the animation will loop.

- **updatePosition:** will change the actual coordinates of the ped according to the animation. Use this for e.g. walking animations.

- **interruptable:** If set to 'false', the animation will not be interrupted by other tasks (eg: falling)

- **callbackFunction:** A function that is called when the animation is finished

- **arguments:** Any arguments you want to pass to the callbackFunction, eg: animation name

### Returns

Returns *true* if succesful, *false* otherwise.

## Example

Click to collapse [-]
Client

This example creates a ped, rotates them, and makes them walk:

```
function makePed()
   ped1 = createPed(56, 1, 1, 4)
   setPedRotation(ped1, 315)
   blendPedAnimation(ped1, "ped", "WOMAN_walknorm")
end
addEventHandler("onClientResourceStart", getResourceRootElement(), makePed)
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

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
