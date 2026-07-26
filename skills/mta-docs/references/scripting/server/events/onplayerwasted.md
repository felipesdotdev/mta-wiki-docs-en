---
doc_id: "mta-wiki:1722"
title: "OnPlayerWasted"
source_title: "OnPlayerWasted"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerWasted"
revision_id: 82052
language: "en"
categories: ["Server_Events", "Changes_in_1.6.0"]
---

# OnPlayerWasted

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

This event is triggered when a player is killed or dies.

## Parameters

```
int totalAmmo, element killer, int killerWeapon, int bodypart, bool stealth, int animGroup, int animID
```

- **totalAmmo**: an [int](mta://reference/misc/int.md) representing the total ammo the victim had when they died.

- **killer**: an [element](mta://reference/misc/element.md) representing the [player](https://wiki.multitheftauto.com/index.php?search=player), [ped](https://wiki.multitheftauto.com/index.php?search=ped), [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) or [object](https://wiki.multitheftauto.com/index.php?search=object) who was the killer. Deaths resulting from fall damage provide the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) or [object](https://wiki.multitheftauto.com/index.php?search=object) landed on as the killer. If there is no killer this is *false*.

- **killerWeapon**: an [int](mta://reference/misc/int.md) representing the [killer weapon](mta://reference/misc/weapons.md) or the [damage type](mta://reference/misc/damage-types.md).

- **bodypart**: an [int](mta://reference/misc/int.md) representing the bodypart ID the victim was hit on when they died.

- **3:** Torso

- **4:** Ass

- **5:** Left Arm

- **6:** Right Arm

- **7:** Left Leg

- **8:** Right Leg

- **9:** Head

- **stealth**: a [boolean](mta://reference/misc/boolean.md) value representing whether or not this was a stealth kill.

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **animGroup**: an [integer](mta://reference/misc/int.md) representing the player's current animation group.

ADDED/UPDATED IN VERSION 1.6.0 [r22620](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22620):

- **animID**: an [integer](mta://reference/misc/int.md) representing the player's current animation ID.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) that died or got killed.

## Example

This example prints the killer and bodypart to the chat when a player dies.

```
-- register player_Wasted as a handler for onPlayerWasted
function player_Wasted ( ammo, attacker, weapon, bodypart )
	-- if there was an attacker
	if ( attacker ) then
		-- we declare our variable outside the following checks
		local tempString
		-- if the element that killed him was a player,
		if ( getElementType ( attacker ) == "player" ) then
			-- put the attacker, victim and weapon info in the string
			tempString = getPlayerName ( attacker ).." killed "..getPlayerName ( source ).." ("..getWeaponNameFromID ( weapon )..")"
		-- else, if it was a vehicle,
		elseif ( getElementType ( attacker ) == "vehicle" ) then
			-- we'll get the name from the attacker vehicle's driver
			tempString = getPlayerName ( getVehicleController ( attacker ) ).." killed "..getPlayerName ( source ).." ("..getWeaponNameFromID ( weapon )..")"
		end
		-- if the victim was shot in the head, append a special message
		if ( bodypart == 9 ) then
			tempString = tempString.." (HEADSHOT!)"
		-- else, just append the bodypart name
		else
			tempString = tempString.." ("..getBodyPartName ( bodypart )..")"
		end
		-- display the message
		outputChatBox ( tempString )
	-- if there was no attacker,
	else
		-- output a death message without attacker info
		outputChatBox ( getPlayerName ( source ).." died. ("..getWeaponNameFromID ( weapon )..") ("..getBodyPartName ( bodypart )..")" )
	end
end
addEventHandler ( "onPlayerWasted", root, player_Wasted )
```

And another example, this will spawn you in the middle of GTA SA world (x=0, y=0, z=3) after 2 seconds of your death

```
addEventHandler( "onPlayerWasted", root,
	function()
		setTimer( spawnPlayer, 2000, 1, source, 0, 0, 3 )
	end
)
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

- [onPlayerDamage](mta://scripting/server/events/onplayerdamage.md)

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

- onPlayerWasted

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
