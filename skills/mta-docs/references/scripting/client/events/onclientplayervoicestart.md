---
doc_id: "mta-wiki:5810"
title: "OnClientPlayerVoiceStart"
source_title: "OnClientPlayerVoiceStart"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientPlayerVoiceStart"
revision_id: 82731
language: "en"
categories: ["Client_events"]
---

# OnClientPlayerVoiceStart

**Note**:  This event should only be used as a low-level function for advanced users.  For typical Voice scripting, please see the [Voice Resource](mta://resources/voice.md)

This event is triggered when a player starts talking through voice chat.

| [[{{{image}}}\|link=\|]] | Note: This event triggers inconsistently ( https://github.com/multitheftauto/mtasa-blue/issues/1700 ). You should use onPlayerVoiceStart and trigger a custom client-sided event to get similar results, minus the cancelEvent effect. |
| --- | --- |
|  |  |

## Parameters

No parameters.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the player [element](mta://reference/misc/element.md) that just started talking through voice chat.

## Cancel effect

- If the [source](mta://reference/misc/event-system.md) is the local player, the local player will not broadcast his voice chat to the server

- If the [source](mta://reference/misc/event-system.md) is a remote player, the player who started talking will not be heard.

## Example

This example outputs to the console the player that started talking.

Click to collapse [-]
Example 1

```
addEventHandler("onClientPlayerVoiceStart",root,function()
	outputConsole(getPlayerName(source).." has started talking.")
end)
```

This example prevents the function from running multiple times due to inconsistent event execution.

Click to collapse [-]
Example 2

```
local toggleFix = 0
addEventHandler('onClientPlayerVoiceStart', localPlayer,
	function()
		if toggleFix == 0 then
			outputConsole("You've started talking")
		end
	end
)

addEventHandler('onClientPlayerVoiceStop', localPlayer,
	function()
		if not getKeyState("z") then
			toggleFix = 0
			outputConsole("You've stopped talking")
		end
	end
)
```

## See Also

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

- onClientPlayerVoiceStart

- [onClientPlayerVoiceStop](mta://scripting/client/events/onclientplayervoicestop.md)

- [onClientPlayerWasted](mta://scripting/client/events/onclientplayerwasted.md)

- [onClientPlayerWeaponFire](mta://scripting/client/events/onclientplayerweaponfire.md)

- [onClientPlayerWeaponSwitch](mta://scripting/client/events/onclientplayerweaponswitch.md)
