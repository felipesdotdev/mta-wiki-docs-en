---
doc_id: "mta-wiki:5424"
title: "SetSoundEffectEnabled"
source_title: "SetSoundEffectEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/SetSoundEffectEnabled"
revision_id: 71883
language: "en"
categories: ["Client_functions", "Changes_in_1.3.2"]
generated_at: "2026-07-26T16:16:44.771791+00:00"
---

# SetSoundEffectEnabled

Used to enable or disable specific [sound](mta://reference/misc/sound.md) effects.
Use a [player](mta://reference/misc/player.md) element to control a players voice with this function.

## Syntax

```
bool setSoundEffectEnabled ( element theSound/thePlayer, string effectName, bool bEnable )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):setEffectEnabled(...)*

### Required Arguments

- **sound:** a [sound](mta://reference/misc/sound.md) element or a [player](mta://reference/misc/player.md) element which will affect the [voice](mta://resources/voice.md) broadcast.

- **effectName:** the effect you want to enable or disable

- **gargle**

- **compressor**

- **echo**

- **i3dl2reverb**

- **distortion**

- **chorus**

- **parameq**

- **reverb**

- **flanger**

- **bEnable:** *true* if you want to enable the effect, *false* if you want to disable it.

### Returns

Returns *true* if the effect was set successfully, *false* otherwise.

## Example

This example creates a sound and set's the flanger sound effect enabled.

```
addCommandHandler("flanger", function(cmd, enabled)
	if isElement(waterSplashes) then
		setSoundEffectEnabled(waterSplashes, cmd, enabled)
	else
		waterSplashes = playSound("splashes.mp3", true)
		setSoundEffectEnabled(waterSplashes, cmd, enabled)
	end
end, true) --set it case sensitive as we are going to get the command name and use it in the setSoundEffectEnabled
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.2 | Added player element for voice control |
| --- | --- |

## See Also

- [getRadioChannel](mta://scripting/client/functions/getradiochannel.md)

- [getRadioChannelName](mta://scripting/client/functions/getradiochannelname.md)

- [getSFXStatus](mta://scripting/client/functions/getsfxstatus.md)

- [getSoundBPM](mta://scripting/client/functions/getsoundbpm.md)

- [getSoundBufferLength](mta://scripting/client/functions/getsoundbufferlength.md)

- [getSoundEffectParameters](mta://scripting/client/functions/getsoundeffectparameters.md)

- [getSoundEffects](mta://scripting/client/functions/getsoundeffects.md)

- [getSoundFFTData](mta://scripting/client/functions/getsoundfftdata.md)

- [getSoundLength](mta://scripting/client/functions/getsoundlength.md)

- [getSoundLevelData](mta://scripting/client/functions/getsoundleveldata.md)

- [getSoundMaxDistance](mta://scripting/client/functions/getsoundmaxdistance.md)

- [getSoundMetaTags](mta://scripting/client/functions/getsoundmetatags.md)

- [getSoundMinDistance](mta://scripting/client/functions/getsoundmindistance.md)

- [getSoundPan](mta://scripting/client/functions/getsoundpan.md)

- [getSoundPosition](mta://scripting/client/functions/getsoundposition.md)

- [getSoundProperties](mta://scripting/client/functions/getsoundproperties.md)

- [getSoundSpeed](mta://scripting/client/functions/getsoundspeed.md)

- [getSoundVolume](mta://scripting/client/functions/getsoundvolume.md)

- [getSoundWaveData](mta://scripting/client/functions/getsoundwavedata.md)

- [isSoundLooped](mta://scripting/client/functions/issoundlooped.md)

- [isSoundPanningEnabled](mta://scripting/client/functions/issoundpanningenabled.md)

- [isSoundPaused](mta://scripting/client/functions/issoundpaused.md)

- [playSFX3D](mta://scripting/client/functions/playsfx3d.md)

- [playSFX](mta://scripting/client/functions/playsfx.md)

- [playSound3D](mta://scripting/client/functions/playsound3d.md)

- [playSound](mta://scripting/client/functions/playsound.md)

- [setRadioChannel](mta://scripting/client/functions/setradiochannel.md)

- setSoundEffectEnabled

- [setSoundEffectParameter](mta://scripting/client/functions/setsoundeffectparameter.md)

- [setSoundLooped](mta://scripting/client/functions/setsoundlooped.md)

- [setSoundMaxDistance](mta://scripting/client/functions/setsoundmaxdistance.md)

- [setSoundMinDistance](mta://scripting/client/functions/setsoundmindistance.md)

- [setSoundPan](mta://scripting/client/functions/setsoundpan.md)

- [setSoundPanningEnabled](mta://scripting/client/functions/setsoundpanningenabled.md)

- [setSoundPaused](mta://scripting/client/functions/setsoundpaused.md)

- [setSoundPosition](mta://scripting/client/functions/setsoundposition.md)

- [setSoundProperties](mta://scripting/client/functions/setsoundproperties.md)

- [setSoundSpeed](mta://scripting/client/functions/setsoundspeed.md)

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
