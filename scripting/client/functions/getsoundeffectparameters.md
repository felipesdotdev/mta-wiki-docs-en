---
doc_id: "mta-wiki:13277"
title: "GetSoundEffectParameters"
source_title: "GetSoundEffectParameters"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundEffectParameters"
revision_id: 81303
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:25.344658+00:00"
---

# GetSoundEffectParameters

This function gets the parameters of a [sound](mta://reference/misc/sound.md) effect.

## Syntax

```
table getSoundEffectParameters ( element sound, string effectName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):getEffectParameters(...)*

### Required Arguments

- **sound**: The [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) to get the sound effect parameters of.

- **effectName**: The name of the effect whose parameters you want to retrieve:

- **gargle**

- **compressor**

- **echo**

- **i3dl2reverb**

- **distortion**

- **chorus**

- **parameq**

- **reverb**

- **flanger**

### Returns

Returns a [table](mta://reference/misc/table.md) with the parameter names as the keys, and their values. If the specified effect name is not valid, *false* is returned.

### Effects Parameters

| Chorus |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_CHORUS.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| wetDryMix | float | 50 | 0-100 | Ratio of wet (processed) signal to dry (unprocessed) signal. |
| depth | float | 10 | 0-100 | Percentage by which the delay time is modulated by the low-frequency oscillator (LFO). |
| feedback | float | 25 | -99-99 | Percentage of output signal to feed back into the effect's input. |
| frequency | float | 1.1 | 0-10 | Frequency of the LFO. |
| waveform | int | 1 | 0-1 | Waveform of the LFO... 0 = triangle, 1 = sine . |
| delay | float | 16 | 0-20 (ms) | Number of milliseconds the input is delayed before it is played back. |
| phase | int | 1 | 0-4 | Phase differential between left and right LFOs. 0 : -180 1 : -90 2 : 0 3 : 90 4 : 180 |

| Compressor |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_COMPRESSOR.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| gain | float | 0 | -60-60 (dB) | Output gain of signal after compression. |
| attack | float | 10 | 0.01-500 (ms) | Time before compression reaches its full value. |
| release | float | 200 | 50-3000 (ms) | Speed at which compression is stopped after input drops below threshold. |
| threshold | float | -20 | -60-0 (dB) | Point at which compression begins. |
| ratio | float | 3 | 1-100 | Compression ratio. |
| predelay | int | 4 (ms) | 0-4 | Time after threshold is reached before attack phase is started. |

| Distortion |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_DISTORTION.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| gain | float | -18 | -60-0 (dB) | Amount of signal change after distortion. |
| edge | float | 15 | 0-100 | Percentage of distortion intensity. |
| postEQCenterFrequency | float | 2400 | 100-8000 (Hz) | Center frequency of harmonic content addition. |
| postEQBandwidth | float | 2400 | 100-8000 (Hz) | Width of frequency band that determines range of harmonic content addition. |
| preLowpassCutoff | float | 8000 | 100-8000 (Hz) | Filter cutoff for high-frequency harmonics attenuation. |

| Echo |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_ECHO.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| wetDryMix | float | 50 | 0-100 | Ratio of wet (processed) signal to dry (unprocessed) signal. |
| feedback | float | 50 | 0-100 | Percentage of output fed back into input. |
| leftDelay | float | 500 | 1-2000 (ms) | Delay for left channel. |
| rightDelay | float | 500 | 1-2000 (ms) | Delay for right channel. |
| panDelay | bool | false | false, true | Value that specifies whether to swap left and right delays with each successive echo. |

| Flanger |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_FLANGER.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| wetDryMix | float | 50 | 0-100 | Ratio of wet (processed) signal to dry (unprocessed) signal. |
| depth | float | 100 | 0-100 | Percentage by which the delay time is modulated by the low-frequency oscillator (LFO). |
| feedback | float | -50 | -99-99 | Percentage of output signal to feed back into the effect's input. |
| frequency | float | 0.25 | 0-10 | Frequency of the LFO. |
| waveform | int | 1 | 0-1 | Waveform of the LFO... 0 = triangle, 1 = sine . |
| delay | float | 2 | 0-4 (ms) | Number of milliseconds the input is delayed before it is played back. |
| phase | int | 2 | 0-4 | Phase differential between left and right LFOs. 0 : -180 1 : -90 2 : 0 3 : 90 4 : 180 |

| Gargle |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_GARGLE.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| rateHz | int | 20 | 1-1000 (Hz) | Rate of modulation. |
| waveShape | int | 0 | 0-1 | Shape of the modulation waveform... 0 = triangle, 1 = square . |

| I3DL2 Reverb |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_I3DL2REVERB.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| room | int | -1000 | -10000-0 (mB) | Attenuation of the room effect. |
| roomHF | int | -100 | -10000-0 (mB) | Attenuation of the room high-frequency effect. |
| roomRolloffFactor | float | 0 | 0-10 | Rolloff factor for the reflected signals. |
| decayTime | float | 1.49 | 0.1-20 (s) | Decay time. |
| decayHFRatio | int | 0.83 | 0.1-2 | Ratio of the decay time at high frequencies to the decay time at low frequencies. |
| reflections | int | -2602 | -10000-1000 (mB) | Attenuation of early reflections relative to room . |
| reflectionsDelay | float | 0.007 | 0-0.3 (s) | Delay time of the first reflection relative to the direct path. |
| reverb | int | 200 | -10000-2000 (mB) | Attenuation of late reverberation relative to room . |
| reverbDelay | float | 0.011 | 0-0.1 (s) | Time limit between the early reflections and the late reverberation relative to the time of the first reflection. |
| diffusion | float | 100 | 0-100 | Echo density in the late reverberation decay. |
| density | float | 100 | 0-100 | Modal density in the late reverberation decay. |
| HFReference | float | 5000 | 20-20000 (Hz) | Delay time of the first reflection relative to the direct path. |

| Parametric Equalizer |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_PARAMEQ.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| center | float | 0 | 80-16000 (Hz) | Center frequency. |
| bandwidth | float | 12 | 1-36 | Bandwidth, in semitones. |
| gain | float | 0 | -15-15 (dB) | Output gain of signal. |

| Reverb |  |  |  |  |
| --- | --- | --- | --- | --- |
| http://www.un4seen.com/doc/#bass/BASS_DX8_REVERB.html |  |  |  |  |
| Parameter | Type | Default value | Valid range | Description |
| inGain | float | 0 | -96-0 (dB) | Input gain of signal. |
| reverbMix | float | 0 | -96-0 (dB) | Reverb mix. |
| reverbTime | float | 1000 | 0.001-3000 (ms) | Reverb time. |
| highFreqRTRatio | float | 0.001 | 0.001-0.999 (ms) | High-frequency reverb time ratio. |

## Example

```
local sound = playSound ("music.mp3")
setSoundEffectEnabled (sound, "echo", true)

local echoParams = getSoundEffectParameters (sound, "echo")
print (echoParams.feedback) -- 50
iprint (echoParams)
--[[
{
  feedback = 50,
  leftDelay = 500,
  panDelay = false,
  rightDelay = 500,
  wetDryMix = 50
}
]]
```

## See Also

- [getRadioChannel](mta://scripting/client/functions/getradiochannel.md)

- [getRadioChannelName](mta://scripting/client/functions/getradiochannelname.md)

- [getSFXStatus](mta://scripting/client/functions/getsfxstatus.md)

- [getSoundBPM](mta://scripting/client/functions/getsoundbpm.md)

- [getSoundBufferLength](mta://scripting/client/functions/getsoundbufferlength.md)

- getSoundEffectParameters

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

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
