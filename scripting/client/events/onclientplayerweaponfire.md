---
doc_id: "mta-wiki:2556"
title: "OnClientPlayerWeaponFire"
source_title: "OnClientPlayerWeaponFire"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerWeaponFire"
revision_id: 82105
language: "en"
categories: ["Client_events", "Changes_in_1.3.1"]
generated_at: "2026-07-26T16:16:20.189719+00:00"
---

# OnClientPlayerWeaponFire

This event is called when a player fires a weapon.  This event does not trigger for melee weapons. Projectile weapons or the camera will only trigger the event if fired by the local player.

| [[{{{image}}}\|link=\|]] | Note: This event is only triggered for players that are streamed in |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This does not trigger for any player's melee weapons or for remote player's projectile weapons or cameras |
| --- | --- |
|  |  |

## Parameters

```
int weapon, int ammo, int ammoInClip, float hitX, float hitY, float hitZ, element hitElement, float startX, float startY, float startZ
```

- **weapon**:  an [int](mta://reference/misc/int.md) representing [weapon](mta://reference/misc/weapons.md) used for firing a shot.

- **ammo**: an [int](mta://reference/misc/int.md) amount of ammo left for this weapon type.

- **ammoInClip**: an [int](mta://reference/misc/int.md) amount of ammo left for this weapon type in clip.

- **hitX**: [float](mta://reference/misc/float.md) world X coordinate representing the hit point.

- **hitY**: [float](mta://reference/misc/float.md) world Y coordinate representing the hit point.

- **hitZ**: [float](mta://reference/misc/float.md) world Z coordinate representing the hit point.

- **hitElement**: an [element](mta://reference/misc/element.md) which was hit by a shot.

- **startX**: [float](mta://reference/misc/float.md) world X coordinate representing the start of the bullet. Note: This is not the gun muzzle.

- **startY**: [float](mta://reference/misc/float.md) world Y coordinate representing the start of the bullet.

- **startZ**: [float](mta://reference/misc/float.md) world Z coordinate representing the start of the bullet.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the streamed in [player](mta://reference/misc/player.md) who fired the weapon.

## Example

This example implements custom gunshot sounds.

```
local playerWeaponSounds = {
	[22] = "sounds/weap/colt45.wav",
	[23] = "sounds/weap/silenced.wav",
	[24] = "sounds/weap/deagle.wav",
	[25] = "sounds/weap/shotgun.wav",
	[26] = "sounds/weap/sawed-off.wav",
	[27] = "sounds/weap/combat shotgun.wav",
	[28] = "sounds/weap/uzi.wav",
	[30] = "sounds/weap/ak-47.wav",
	[31] = "sounds/weap/m4.wav",
	[32] = "sounds/weap/tec9.wav",
	[34] = "sounds/weap/sniper.wav",
}

local function playCustomWeaponSound(weaponID)
	local playerWeaponSoundPath = playerWeaponSounds[weaponID]

	if (not playerWeaponSoundPath) then
		return false
	end

	local playerMuzzleX, playerMuzzleY, playerMuzzleZ = getPedWeaponMuzzlePosition(source)
	local playerWeaponSound = playSound3D(playerWeaponSoundPath, playerMuzzleX, playerMuzzleY, playerMuzzleZ)

	if (not playerWeaponSound) then
		return false
	end

	setSoundMaxDistance(playerWeaponSound, 90)
	setSoundVolume(playerWeaponSound, 0.6)
end
addEventHandler("onClientPlayerWeaponFire", root, playCustomWeaponSound)
```

This example sends a warning to the local player if they shoot another player with a minigun.

```
--First, we create a function for the event handler to use.
function onClientPlayerWeaponFireFunc(weapon, ammo, ammoInClip, hitX, hitY, hitZ, hitElement )
    if weapon == 38 and getElementType(hitElement)=="player" then -- If the player shoots with a minigun, and hits another player...
         outputChatBox ( "Don't kill people with minigun, it's lame!", 255, 0, 0 ) -- We output a warning to him.
    end
end
-- Add this as a handler so that the function will be triggered every time the local player fires.
addEventHandler ( "onClientPlayerWeaponFire", localPlayer, onClientPlayerWeaponFireFunc )
```

This example makes the Shotgun fire explosive rounds.

```
function onClientPlayerWeaponFireFunc(weapon, ammo, ammoInClip, hitX, hitY, hitZ, hitElement)
    if (weapon == 25) then -- If the player shoots with a shotgun
        createExplosion(hitX, hitY, hitZ, 12, true, 0, true) -- Creates a tiny explosion where the bullet hit.
    end
end
-- Add this as a handler so that the function will be triggered every time a player fires.
addEventHandler("onClientPlayerWeaponFire", root, onClientPlayerWeaponFireFunc)
```

## See Also

### Client player events

- [onClientPlayerChangeNick](mta://scripting/client/events/onclientplayerchangenick.md)

- [onClientPlayerChoke](mta://scripting/client/events/onclientplayerchoke.md)

- [onClientPlayerDamage](mta://scripting/client/events/onclientplayerdamage.md)

- [onClientPlayerHeliKilled](mta://scripting/client/events/onclientplayerhelikilled.md)

- [onClientPlayerHitByWaterCannon](mta://scripting/client/events/onclientplayerhitbywatercannon.md)

- [onClientPlayerJoin](mta://scripting/client/events/onclientplayerjoin.md)

- [onClientPlayerPickupHit](mta://scripting/client/events/onclientplayerpickuphit.md)

- [onClientPlayerPickupLeave](mta://scripting/client/events/onclientplayerpickupleave.md)

- [onClientPlayerQuit](mta://scripting/client/events/onclientplayerquit.md)

- [onClientPlayerRadioSwitch](mta://scripting/client/events/onclientplayerradioswitch.md)

- [onClientPlayerSpawn](mta://scripting/client/events/onclientplayerspawn.md)

- [onClientPlayerStealthKill](mta://scripting/client/events/onclientplayerstealthkill.md)

- [onClientPlayerStuntFinish](mta://scripting/client/events/onclientplayerstuntfinish.md)

- [onClientPlayerStuntStart](mta://scripting/client/events/onclientplayerstuntstart.md)

- [onClientPlayerTarget](mta://scripting/client/events/onclientplayertarget.md)

- [onClientPlayerVehicleEnter](mta://scripting/client/events/onclientplayervehicleenter.md)

- [onClientPlayerVehicleExit](mta://scripting/client/events/onclientplayervehicleexit.md)

- [onClientPlayerVoicePause](mta://scripting/client/events/onclientplayervoicepause.md)

- [onClientPlayerVoiceResumed](mta://scripting/client/events/onclientplayervoiceresumed.md)

- [onClientPlayerVoiceStart](mta://scripting/client/events/onclientplayervoicestart.md)

- [onClientPlayerVoiceStop](mta://scripting/client/events/onclientplayervoicestop.md)

- [onClientPlayerWasted](mta://scripting/client/events/onclientplayerwasted.md)

- onClientPlayerWeaponFire

- [onClientPlayerWeaponSwitch](mta://scripting/client/events/onclientplayerweaponswitch.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
