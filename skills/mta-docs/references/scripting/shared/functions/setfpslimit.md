---
doc_id: "mta-wiki:4018"
title: "SetFPSLimit"
source_title: "SetFPSLimit"
source_url: "https://wiki.multitheftauto.com/wiki/SetFPSLimit"
revision_id: 82191
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetFPSLimit

This function sets the maximum [FPS (Frames per second)](http://en.wikipedia.org/wiki/Frame_rate) that players on the server can run their game at.

| [[{{{image}}}\|link=\|]] | Note: When set client side, the actual limit used is the lowest of both the server and client set values. Starting from version [ r21313 ] and above fpsLimit range is 25-32767 . In older MTA releases it was 25-100 . |
| --- | --- |
|  |  |

## Syntax

```
bool setFPSLimit ( int fpsLimit )
```

### Required Arguments

- **fpsLimit:** An integer value representing the maximum FPS. Refer to the note above for possible values. You can also pass **0** or **false**, in which case the FPS limit will be the one set in the client settings (by default **100 FPS** and the client fps limit should also be manually changed via "**fps_limit=0**" in console or **MTA San Andreas\MTA\config\coreconfig.xml**).

### Returns

Returns *true* if successful, or *false* if it was not possible to set the limit or an invalid value was passed.

## Issues when increasing FPS

Note: with "very high" FPS, any FPS limit over 74 is meant.
It is recommended to set a conservative FPS limit (between 40-60 and 74 highest) because high FPS can break some GTA internal calculations, causing various bugs. The higher the FPS the more of a problem these become:

74 FPS is the breaking point that opens the door to various more severe GTA bugs related to FPS and physics.

- Physics of vehicles is effected, both high and low FPSes may bring their own set of unfair advantages. Speaking about the consequences of high FPS in this context, up to 70 or 74 FPS is considered safe (as any differences in physics, if they do exist to begin with as they theoretically should, are so tiny that they are unmeasurable and thus wouldn't affect racing results in practise). Anything beyond 74 FPS may cause impactful discrepancies.

- Pressing the horn button to turn on and off sirens gets really hard at very high FPS. For instance, at 100 FPS, you are more likely to hit the regular horn 3 times (inconsistent) before eventually triggering the siren, besides taking a similar amount of tries to turn off the siren.

- At very high FPS, climbing over certain objects will result in instant death. Example at: 2520.108, -1681.407, 19.406, 266 - [you can use this Lua code to fix it.](https://wiki.multitheftauto.com/wiki/SetFPSLimit#Fix_for_climbing_over_certain_objects)

- The higher your FPS, the more of a penalty in satchel throwing distance (up to ~10% at very high FPS) will apply.

For a full list of FPS-related GTA bugs (that are much less likely to impact gameplay in a meaningful way) and MTA developers' progress in tackling them, see the [Framerate issues tracker](https://github.com/multitheftauto/mtasa-blue/projects/14) github project.

## Example

This example allows players to limit their own FPS using a command.

Click to collapse [-]
Client

```
function fpsFunction(commandName, fpsLimit)
	local newFPS = tonumber(fpsLimit)

	if not newFPS then
		outputChatBox("Syntax: /" .. commandName .. " [FPS] - to limit your own FPS.")
		return false
	end

	if newFPS < minFPS or newFPS > maxFPS then
		outputChatBox("Please enter a value between " .. minFPS .. " and " .. maxFPS .. ".")
		return false
	end

	local currentLimit = getFPSLimit()
	local setNewFPS = (newFPS ~= currentLimit)

	if (setNewFPS) then
		outputChatBox("Your FPS have been limited to: " .. newFPS .. ".")
		setFPSLimit(newFPS)
	end
end
addCommandHandler("fpslimit", fpsFunction)
```

## Fix for climbing over certain objects

You can use this small code to fix one of high FPS issues, specifically the one which would instantly kill player climbing over some objects.

Click to collapse [-]
Client

```
function onClientPlayerDamage(attackerElement, damageType, bodyPart)
	local fallDamage = (damageType == 54)

	if (not fallDamage) then
		return false
	end

	local playerTask = getPedSimplestTask(localPlayer)
	local playerClimbing = (playerTask == "TASK_SIMPLE_CLIMB")

	if (playerClimbing) then
		cancelEvent()
	end
end
addEventHandler("onClientPlayerDamage", localPlayer, onClientPlayerDamage)
```

## See Also

- [getMaxPlayers](mta://scripting/server/functions/getmaxplayers.md)

- [getServerConfigSetting](mta://scripting/server/functions/getserverconfigsetting.md)

- [getServerHttpPort](mta://scripting/server/functions/getserverhttpport.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIpFromMasterServer](mta://scripting/server/functions/getserveripfrommasterserver.md)

- [getServerName](mta://scripting/server/functions/getservername.md)

- [getServerPassword](mta://scripting/server/functions/getserverpassword.md)

- [getServerPort](mta://scripting/server/functions/getserverport.md)

- [isGlitchEnabled](mta://scripting/server/functions/isglitchenabled.md)

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
