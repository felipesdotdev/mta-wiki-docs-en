---
doc_id: "mta-wiki:6587"
title: "SetSoundProperties"
source_title: "SetSoundProperties"
source_url: "https://wiki.multitheftauto.com/wiki/SetSoundProperties"
revision_id: 62320
language: "en"
categories: ["Client_functions", "Changes_in_1.3.0", "Utility_templates"]
generated_at: "2026-07-26T16:16:45.046718+00:00"
---

# SetSoundProperties

This function edits the properties of a specific [sound](mta://reference/misc/sound.md).

| [[{{{image}}}\|link=\|]] | Note: Streams are not supported. |
| --- | --- |
|  |  |

## Syntax

```
bool setSoundProperties(element sound, float fSampleRate, float fTempo, float fPitch [, bool bReverse = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):setProperties(...)*

**Counterpart**: *[getSoundProperties](mta://scripting/client/functions/getsoundproperties.md)*

### Required Arguments

- **sound:** a [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) that is created using [playSound](mta://scripting/client/functions/playsound.md) or [playSound3D](mta://scripting/client/functions/playsound3d.md)

- **fSampleRate:** a [float](mta://reference/misc/float.md) that defines the new sound's [sample rate](http://en.wikipedia.org/wiki/Sampling_rate)

- **fTempo:** a [float](mta://reference/misc/float.md) that defines the new sound [tempo](http://en.wikipedia.org/wiki/Tempo)

- **fPitch:** a [float](mta://reference/misc/float.md) that defines the new sound [pitch](http://en.wikipedia.org/wiki/Pitch_%28music%29)

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **bReverse:** a [boolean](mta://reference/misc/boolean.md) representing whether the sound will be reversed or not.

### Returns

Returns *true* if the properties sucessfully set, *false* otherwise.

## Example

Click to collapse [-]
Client

```
function editSongSound()
	local sound = playSound("song.wav", false) -- Play the file 'song.wav' and make it play only once
	setSoundProperties(sound, 48000.0, 128.00, 440.0, false) -- Set its samplerate to 48,000 Hz, tempo to 128.00, pitch to 440 Hz and not reversed
end
addEventHandler("onClientResourceStart", resourceRoot, editSongSound) -- Execute the function when the resource is started
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

- setSoundProperties

- [setSoundSpeed](mta://scripting/client/functions/setsoundspeed.md)

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
