---
doc_id: "mta-wiki:1826"
title: "OnPlayerDamage"
source_title: "OnPlayerDamage"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerDamage"
revision_id: 73901
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.764715+00:00"
---

# OnPlayerDamage

This event is triggered when a player is damaged, in any way.

- This event is not triggered when attacked by a team member if friendly fire is enabled.

- Canceling this event has no effect. Cancel the client-side event [onClientPlayerDamage](mta://scripting/client/events/onclientplayerdamage.md) instead.

- onPlayerDamage doesn't trigger if the damage kills the player, [onPlayerWasted](mta://scripting/server/events/onplayerwasted.md) is called instead.

## Parameters

```
player attacker, int damage_causing, int bodypart, float loss
```

- **attacker**: a [player](mta://reference/misc/player.md) element representing the player who was the attacker.  If there was no attacker this returns false.

- **damage_causing**: an [int](mta://reference/misc/int.md) representing the cause of damage, either a [attacker weapon](mta://reference/misc/weapons.md), or some other [types of damage](mta://reference/misc/damage-types.md).

- **bodypart**: an [int](mta://reference/misc/int.md) representing the bodypart ID the player was hit on when he got damaged.

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **loss**: a [float](mta://reference/misc/float.md) representing the percentage of health the player lost.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md) who was damaged.

## Example

This example causes an instant kill when a player is shot in the head, and announces it in the chatbox.

```
function playerDamage_text ( attacker, weapon, bodypart, loss ) --when a player is damaged
	if ( bodypart == 9 and attacker and attacker ~= source ) then -- if the body part is 9 (head) and there is an attacker and it wasn't self damage
            outputChatBox ( "Headshot!", attacker, 255, 170, 0 ) --output "Headshot" into the chatbox
	    killPed ( source, attacker, weapon, bodypart ) -- and kill the player
	end
end
addEventHandler ( "onPlayerDamage", root, playerDamage_text ) --add an event handler for the onPlayerDamage event
```

## See Also

### Player events

- [onPlayerACInfo](mta://scripting/server/events/onplayeracinfo.md)

- [onPlayerBan](mta://scripting/server/events/onplayerban.md)

- [onPlayerChangeNick](mta://scripting/server/events/onplayerchangenick.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22790](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22790))

- [onPlayerChangesWorldSpecialProperty](mta://scripting/server/events/onplayerchangesworldspecialproperty.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22790](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22790))

- [onPlayerChangesProtectedData](mta://scripting/server/events/onplayerchangesprotecteddata.md)

- [onPlayerChat](mta://scripting/server/events/onplayerchat.md)

- [onPlayerClick](mta://scripting/server/events/onplayerclick.md)

- [onPlayerCommand](mta://scripting/server/events/onplayercommand.md)

- [onPlayerConnect](mta://scripting/server/events/onplayerconnect.md)

- [onPlayerContact](mta://scripting/server/events/onplayercontact.md)

- onPlayerDamage

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22293](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22293))

- [onPlayerDetonateSatchels](mta://scripting/server/events/onplayerdetonatesatchels.md)

- [onPlayerJoin](mta://scripting/server/events/onplayerjoin.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r20463](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=20463))

- [onPlayerDiscordJoin](mta://scripting/server/events/onplayerdiscordjoin.md)

- [onPlayerLogin](mta://scripting/server/events/onplayerlogin.md)

- [onPlayerLogout](mta://scripting/server/events/onplayerlogout.md)

- [onPlayerMarkerHit](mta://scripting/server/events/onplayermarkerhit.md)

- [onPlayerMarkerLeave](mta://scripting/server/events/onplayermarkerleave.md)

- [onPlayerModInfo](mta://scripting/server/events/onplayermodinfo.md)

- [onPlayerMute](mta://scripting/server/events/onplayermute.md)

- [onPlayerNetworkStatus](mta://scripting/server/events/onplayernetworkstatus.md)

- [onPlayerPickupHit](mta://scripting/server/events/onplayerpickuphit.md)

- [onPlayerPickupLeave](mta://scripting/server/events/onplayerpickupleave.md)

- [onPlayerPickupUse](mta://scripting/server/events/onplayerpickupuse.md)

- [onPlayerPrivateMessage](mta://scripting/server/events/onplayerprivatemessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22293](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22293))

- [onPlayerProjectileCreation](mta://scripting/server/events/onplayerprojectilecreation.md)

- [onPlayerQuit](mta://scripting/server/events/onplayerquit.md)

- [onPlayerScreenShot](mta://scripting/server/events/onplayerscreenshot.md)

- [onPlayerSpawn](mta://scripting/server/events/onplayerspawn.md)

- [onPlayerStealthKill](mta://scripting/server/events/onplayerstealthkill.md)

- [onPlayerTarget](mta://scripting/server/events/onplayertarget.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22447](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22447))

- [onPlayerTeamChange](mta://scripting/server/events/onplayerteamchange.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22313](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22313))

- [onPlayerTriggerEventThreshold](mta://scripting/server/events/onplayertriggereventthreshold.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22459](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22459))

- [onPlayerTriggerInvalidEvent](mta://scripting/server/events/onplayertriggerinvalidevent.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22930](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22930))

- [onPlayerTeleport](mta://scripting/server/events/onplayerteleport.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22909](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22909))

- [onPlayerWeaponReload](mta://scripting/server/events/onplayerweaponreload.md)

- [onPlayerUnmute](mta://scripting/server/events/onplayerunmute.md)

- [onPlayerVehicleEnter](mta://scripting/server/events/onplayervehicleenter.md)

- [onPlayerVehicleExit](mta://scripting/server/events/onplayervehicleexit.md)

- [onPlayerVoiceStart](mta://scripting/server/events/onplayervoicestart.md)

- [onPlayerVoiceStop](mta://scripting/server/events/onplayervoicestop.md)

- [onPlayerWasted](mta://scripting/server/events/onplayerwasted.md)

- [onPlayerWeaponFire](mta://scripting/server/events/onplayerweaponfire.md)

- [onPlayerWeaponSwitch](mta://scripting/server/events/onplayerweaponswitch.md)

### Event functions

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
