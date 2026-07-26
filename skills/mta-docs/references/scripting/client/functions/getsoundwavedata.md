---
doc_id: "mta-wiki:7073"
title: "GetSoundWaveData"
source_title: "GetSoundWaveData"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundWaveData"
revision_id: 75916
language: "en"
categories: ["Client_functions", "Changes_in_1.3.2"]
---

# GetSoundWaveData

This function gets the wave form data for an audio stream which is a table of floats representing the current audio frame as a wave.
This allows things like visualisations.

If the element is a player, this function will use the players voice.

## Syntax

```
table getSoundWaveData ( element sound, int iSamples )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):getWaveData(...)*

### Required Arguments

- **sound:** a [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) that is created using [playSound](mta://scripting/client/functions/playsound.md) or [playSound3D](mta://scripting/client/functions/playsound3d.md). Streams are also supported

- **iSamples:** allowed samples are 256, 512, 1024, 2048, 4096, 8192 and 16384.

### Returns

Returns a [table](mta://reference/misc/table.md) of **iSamples** *floats* representing the current audio frame waveform.
Returns *false* if the sound is not playing yet or hasn't buffered in the
case of streams.

## Example

This example creates a sound visualizer on the top left corner of the screen.

Click to collapse [-]
Client

```
soundHandler = playSound ( "sound.wav" )

function onSoundPlayRender ( )
    if ( soundHandler ) then
        local waveData = getSoundWaveData ( soundHandler, 256 )
	if ( waveData ) then
            for i=0,255 do
                dxDrawRectangle ( i, 128, 1, waveData[i] * 128)
            end
        end
    end
end
addEventHandler ( "onClientRender", getRootElement(), onSoundPlayRender )
```

This example creates a sound viewer, but only with bars down.

Click to collapse [-]
Client

```
soundHandler = playSound ("audio.mp3")
local samples = 256

function renderWave ()
    if (isElement (soundHandler)) then
        local waveData = getSoundWaveData (soundHandler, samples)
        if (waveData) then -- Avoid NaN values.
            for i=0, samples-1 do
                dxDrawRectangle (i, 128, 1, math.abs (waveData[i]) * 128)
            end
        end
    end
end
addEventHandler ("onClientRender", root, renderWave)
```

This example creates a sound viewer, but only with bars up.

Click to collapse [-]
Client

```
soundHandler = playSound ("audio.mp3")
local samples = 256

function renderWave ()
    if (isElement (soundHandler)) then
        local waveData = getSoundWaveData (soundHandler, samples)
        if (waveData) then -- Avoid NaN values.
            for i=0, samples-1 do
                dxDrawRectangle (i, 128, 1, math.abs (waveData[i]) * -128)
            end
        end
    end
end
addEventHandler ("onClientRender", root, renderWave)
```

This example creates a sound viewer on the bottom right corner of the screen.

Click to collapse [-]
Client

```
soundHandler = playSound ("audio.mp3")
local x, y = guiGetScreenSize ()
local samples = 256

function renderWave ()
    if (isElement (soundHandler)) then
        local waveData = getSoundWaveData (soundHandler, samples)
        if (waveData) then -- Avoid NaN values.
            for i=0, samples-1 do
                dxDrawRectangle ((x-samples)+i, y-128, 1, waveData[i] * 128)
            end
        end
    end
end
addEventHandler ("onClientRender", root, renderWave)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.2 | Added player element to use a players voice |
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

- getSoundWaveData

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
