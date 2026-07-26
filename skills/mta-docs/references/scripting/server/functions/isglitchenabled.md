---
doc_id: "mta-wiki:4598"
title: "IsGlitchEnabled"
source_title: "IsGlitchEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsGlitchEnabled"
revision_id: 47021
language: "en"
categories: ["Server_functions", "Changes_in_1.6.0"]
---

# IsGlitchEnabled

This function retrieves whether San Andreas game glitches are enabled or not, set by using [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

## Syntax

```
bool isGlitchEnabled ( string glitchName )
```

### Required Arguments

- **glitchName:** the name of the property to set. Possible values are:

- **quickreload:** This is the glitch where switching weapons auto-reloads your weapon, without actually performing the reload animation.

- **fastmove:** This is the glitch that can be achieved by a certain key combinations whilst standing up after crouching, which allows you to move quickly with slow weapons (e.g. deagle). Side effect: also enables the "crouchslide" bug - use [the "NoCrouchSlide" resource](https://community.mtasa.com/index.php?p=resources&s=details&id=13368) to remedy this.

- **fastfire:** This is the glitch that can be achieved by cancelling the full fire animation, allowing you to shoot with slow-fire weapons (e.g. deagle) much faster.

- **crouchbug:** This is the glitch where the post shooting animation can be aborted by using the crouch key.

- **highcloserangedamage:** Enabling this removes the extremely high damage guns inflict when fired at very close range.

- **hitanim:** Enabling this allows 'hit by bullet' animations to interrupt player aiming.

- **fastsprint:** Enabling fastsprint allows players to tap space with a macro to boost their speed beyond normal speeds of GTASA.

- **baddrivebyhitbox:** This glitch leaves players invulnerable to gun fire when performing certain driveby animations.

- **quickstand:** This glitch allows players to quickly stand up by pressing the crouch, sprint or jump controls just after releasing the aim weapon button while using one and being ducked.

- **kickoutofvehicle_onmodelreplace:** This glitch enables the old behavior where players get warped out of a vehicle when the model is replaced.

- ADDED/UPDATED IN VERSION 1.6.0 [r23281](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23281):

**vehicle_rapid_stop:** This glitch enables the old behavior of vehicles (pre-high FPS fix, see PR: [#4243](https://github.com/multitheftauto/mtasa-blue/pull/4243) & [#2784](https://github.com/multitheftauto/mtasa-blue/pull/2784))

### Returns

Returns *true* if if the glitch was enabled, or *false* if it is disabled.

## Example

This example outputs weather the "fastmove" glitch is enabled or not.

```
setGlitchEnabled("fastmove",true) -- Enable the fastmove glitch at resource start.

function checkIsEnabled(thePlayer,command)
	if (isGlitchEnabled("fastmove")) then -- Check weather fastmove is enabled or not.
		outputChatBox("fastmove is enabled.",thePlayer,255,255,0) -- If so, output that it's enabled.
	else
		outputChatBox("fastmove is not enabled.",thePlayer,255,0,0) -- If not, output that it isn't enabled.
	end
end
addCommandHandler("glitch",checkIsEnabled)
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

- isGlitchEnabled

- [setGlitchEnabled](mta://scripting/server/functions/setglitchenabled.md)

- [setMaxPlayers](mta://scripting/server/functions/setmaxplayers.md)

- [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md)

- [setServerPassword](mta://scripting/server/functions/setserverpassword.md)

- [shutdown](mta://scripting/server/functions/shutdown.md)
