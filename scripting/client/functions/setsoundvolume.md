---
doc_id: "mta-wiki:4285"
title: "SetSoundVolume"
source_title: "SetSoundVolume"
source_url: "https://wiki.multitheftauto.com/wiki/SetSoundVolume"
revision_id: 82678
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:45.091084+00:00"
---

# SetSoundVolume

This function is used to change the volume level of the specified [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md).
Use a player element to control a players voice with this function.

## Syntax

```
bool setSoundVolume ( element theSound/thePlayer, float volume )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):setVolume(...)*

**Variable**: *.volume*

**Counterpart**: *[getSoundVolume](mta://scripting/client/functions/getsoundvolume.md)*

### Required Arguments

- **theSound:** The [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) which volume you want to modify or a [player](mta://reference/misc/player.md) element which voice volume you want to modify.

- **volume:** A [floating](mta://reference/misc/float.md) point number representing the desired volume level. Range is from **0.0** to **1.0**. This can go above **1.0** for amplification.

### Returns

Returns *true* if the [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) volume was successfully changed, *false* otherwise.

## Example

```
function wasted (killer, weapon, bodypart)
    local sound = playSound("sounds/wasted.mp3") --Play wasted.mp3 from the sounds folder
    if isElement(sound) then
        setSoundVolume(sound, 0.5) -- set the sound volume to 50%
    end
end

addEventHandler("onClientPlayerWasted", localPlayer, wasted) --add the event handler
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

- [setSoundEffectEnabled](mta://scripting/client/functions/setsoundeffectenabled.md)

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

- setSoundVolume

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
