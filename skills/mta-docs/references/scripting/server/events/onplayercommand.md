---
doc_id: "mta-wiki:5585"
title: "OnPlayerCommand"
source_title: "OnPlayerCommand"
source_url: "https://wiki.multitheftauto.com/wiki/OnPlayerCommand"
revision_id: 82046
language: "en"
categories: ["Server_Events"]
---

# OnPlayerCommand

This event is triggered when a player issues a command.

| [[{{{image}}}\|link=\|]] | Note: This event triggers regardless of whether the command exists in a script or is hardcoded. Also, typing anything in chat will execute the internal command "say", so this event will be triggered on every chat message as well. Therefore you should avoid excessive use of this function on busy servers, out of performance considerations. |
| --- | --- |
|  |  |

## Parameters

```
string command
```

- **command:** a [string](mta://reference/misc/string.md) containing the name of the command executed.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) who tried to execute a command.

## Canceling

The command will not be executed. (Only server-side commands can be canceled.)

## Example

Click to collapse [-]
Server

This example implements an anti-flood protection timer for commands.
**Be sure to give the resource a function.kickPlayer right.**
Also, note, that if the server freezes for a frame and a player executes a command 2x he/she'll get kicked, because those 2 commands will be processed after each other, with very little delay****

```
local CMD_INTERVAL        = 200 --// The interval that needs to pass before the player can execute another cmd
local KICK_AFTER_INTERVAL = 50  --// Kick the player if they execute more than 20 cmds/sec

local executions = setmetatable({}, { --// Metatable for non-existing indexes
    __index = function(t, player)
        return getTickCount()-CMD_INTERVAL
    end
})

addEventHandler("onPlayerCommand", root,
    function()
        if (executions[source]-getTickCount()<=CMD_INTERVAL) then
            if (executions[source]-getTickCount()<=KICK_AFTER_INTERVAL) then 
                kickPlayer(source, "Anti-Flood", "Don't flood")
            end 
            cancelEvent()
        end
        executions[source] = getTickCount()
    end
)
```

This example disables the hardcoded command 'whois'

```
addEventHandler("onPlayerCommand",root,
    function(command)
	if (command == "whois") then
	    cancelEvent()
	end
end)
```

Click to collapse [-]
Server

Time limit specific commands.

```
local LIMITED_COMMANDS = {
    -- ["COMMAND_NAME"] = TIME_LIMIT_IN_SEC
    ["something"] = 5,  -- Can use this command only once in every 5 sec
    ["spam"]      = 10, -- Can use this command only once in every 10 sec
}

local EXEC = {}

addEventHandler("onPlayerCommand", root, function(cmd)
    local limit_sec = LIMITED_COMMANDS[cmd]
    if not limit_sec then return end

    local tick = getTickCount()

    if not EXEC[source]      then EXEC[source] = {}     end
    if not EXEC[source][cmd] then EXEC[source][cmd] = 0 end

    if EXEC[source][cmd] + (limit_sec * 1000) > tick then
        cancelEvent()
        return outputChatBox("#FF0000[ANTISPAM]#FFFFFF You can use this command once, in every "..limit_sec.." sec.", source, 255, 255, 255, true)
    end
    EXEC[source][cmd] = tick
end)

addEventHandler("onPlayerQuit", root, function()
    EXEC[source] = nil
end)
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

- onPlayerCommand

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
