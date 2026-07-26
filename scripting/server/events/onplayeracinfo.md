---
doc_id: "mta-wiki:8457"
title: "OnPlayerACInfo"
source_title: "OnPlayerACInfo"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerACInfo"
revision_id: 62622
language: "en"
categories: ["Server_Events"]
generated_at: "2026-07-26T16:16:24.418289+00:00"
---

# OnPlayerACInfo

This event is triggered when a player trips anti-cheat detections. It can be used to script a white/blacklist of custom d3d9.dll files, or a white/blacklist of players with certain anti-cheat codes. The relevant anti-cheat code has to be disabled (or not enabled) in the server [mtaserver.conf](mta://reference/misc/mtaserver-conf.md) to be of use here.

| [[{{{image}}}\|link=\|]] | Note: Any resource using this event should call resendPlayerACInfo for each player in onResourceStart |
| --- | --- |
|  |  |

## Parameters

```
table detectedACList, int d3d9Size, string d3d9MD5, string d3d9SHA256
```

- **detectedACList**: A table of [anti-cheat](mta://scripting/concepts/anti-cheat-guide.md) codes the player has triggered.

- **d3d9Size**: A number representing the file size of any custom d3d9.dll the player may have installed.

- **d3d9MD5**: A string containing the MD5 of any custom d3d9.dll the player may have installed.

- **d3d9SHA256**: A string containing the SHA256 of any custom d3d9.dll the player may have installed.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](mta://reference/misc/player.md)

## Example

This example prints all information into the chatbox

```
function handleOnPlayerACInfo( detectedACList, d3d9Size, d3d9MD5, d3d9SHA256 )
    outputChatBox( "ACInfo for " .. getPlayerName(source)
                .. " detectedACList:" .. table.concat(detectedACList,",")
                .. " d3d9Size:" .. d3d9Size
                .. " d3d9SHA256:" .. d3d9SHA256
                )
end
	
addEventHandler( "onPlayerACInfo", root, handleOnPlayerACInfo )

-- Ensure no one gets missed when the resource is (re)started
addEventHandler( "onResourceStart", resourceRoot,
    function()
        for _,plr in ipairs( getElementsByType("player") ) do
            resendPlayerACInfo( plr )
        end
    end
)
```

This example will notify all online admins when someone triggers a (suspicious) detection

```
function handleAC(detectedACList)
	for _, acCode in ipairs(detectedACList) do
		if acCode == 33 then -- SD #33 in this code example = NetLimiter software (possible lagswitch)
			local playerName = getPlayerName(source)
			warnAdmins(playerName, acCode)
		end
	end
end
addEventHandler("onPlayerACInfo", root, handleAC)

local staffACL = {
	[aclGetGroup("Admin")] = true,
	[aclGetGroup("Moderator")] = true
}

function warnAdmins(playerName, acCode)
	for _, p in ipairs(getElementsByType("player")) do
		local account = getPlayerAccount(p)
		if p and account then
			for group, _ in pairs(staffACL) do
				local name = getAccountName(account)
				if isObjectInACLGroup("user." .. name, group) then
					outputChatBox("The player " .. playerName .. " has triggered SD/AC #" .. acCode .. "! Keep an eye out!", p)
				end
			end
		end
	end
end

-- Ensure no one gets missed when the resource is (re)started
function onRestart()
	for _,p in ipairs (getElementsByType("player")) do
		resendPlayerACInfo(p)
	end
end
addEventHandler("onResourceStart", resourceRoot, onRestart)
```

This example allows player serial exceptions for SD #14 (virtual machines). In order for this to work, it's important that you **don't** add SD #14 detection into mtaserver.conf, as this is a custom re-implementation.

```
-- List of serials which are allowed to use virtual machines
allowVM = { ["0123456789012345601234567890123456"] = true,
            ["A123637892167367281632896790123456"] = true,
            ["E123456789012347839207878392123456"] = true }

function handleOnPlayerACInfo( detectedACList, d3d9Size, d3d9MD5, d3d9SHA256 )
    for _,acCode in ipairs( detectedACList ) do
        if acCode == 14 then
            local serial = getPlayerSerial(source)
            if not allowVM[serial] then
                kickPlayer( source, "This server does not allow virtual machines." )
            end
        end
    end
end
addEventHandler( "onPlayerACInfo", root, handleOnPlayerACInfo )

-- Ensure no one gets missed when the resource is (re)started
addEventHandler( "onResourceStart", resourceRoot,
    function()
        for _,plr in ipairs( getElementsByType("player") ) do
            resendPlayerACInfo( plr )
        end
    end
)
```

## See Also

### Player events

- onPlayerACInfo

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
