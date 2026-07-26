---
doc_id: "mta-wiki:6602"
title: "GetSoundProperties"
source_title: "GetSoundProperties"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundProperties"
revision_id: 72764
language: "en"
categories: ["Client_functions", "Changes_in_1.3.0"]
generated_at: "2026-07-26T16:15:25.585656+00:00"
---

# GetSoundProperties

This function gets the properties of a specific [sound](mta://reference/misc/sound.md).

## Syntax

```
float, float, float, bool getSoundProperties( element sound )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):getProperties(...)*

**Counterpart**: *[setSoundProperties](mta://scripting/client/functions/setsoundproperties.md)*

### Required Arguments

- **sound:** a [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) that is created using [playSound](mta://scripting/client/functions/playsound.md) or [playSound3D](mta://scripting/client/functions/playsound3d.md)

### Returns

This function returns 3 [floats](mta://reference/misc/float.md) and a [boolean](mta://reference/misc/boolean.md) value:

The first float is the sound's [sample rate](http://en.wikipedia.org/wiki/Sampling_rate), the second one the sound's [tempo](http://en.wikipedia.org/wiki/Tempo), and the third one the [pitch](http://en.wikipedia.org/wiki/Pitch_%28music%29) of the sound. The boolean representing whether the sound is reversed or not.

## Example

**Example 1:** This example would return three float values representing the sample rate, tempo, pitch and a boolean value representing whether the sound is reversed or not, every 5 seconds.

```
local sound 
local timer

addCommandHandler("playsound",
function () 
    sound = playSound("wasted.mp3")
    timer = setTimer(function() soundProperties(sound) end, 5000, 0)
end
)

function soundProperties(sound)
    local sampleRate, tempo, pitch, isReversed = getSoundProperties(sound) --gets the sample rate, tempo, pitch and a boolean value representing whether the sound is reversed or not.
    outputChatBox(sampleRate.." "..tempo.." "..pitch.." "..tostring(isReversed))
end
```

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

- getSoundProperties

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

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
