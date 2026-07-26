---
doc_id: "mta-wiki:6674"
title: "GetSoundFFTData"
source_title: "GetSoundFFTData"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundFFTData"
revision_id: 80330
language: "en"
categories: ["Client_functions"]
---

# GetSoundFFTData

This function gets the fast fourier transform data for an audio stream which is a table of floats representing the current audio frame. This allows things like visualisations.
A fast fourier transform generates a table of all the frequencies of the current audio frame which starts at the bass end of the spectrum to mids to highs in that order.
Should you have any problems there is an example resource located on the resources repository:
[Visualiser](https://github.com/multitheftauto/mtasa-resources/tree/master/%5Bgameplay%5D/visualiser)

Just type "startmusic mystreamurl" in your console and it will play on the cinema billboard near A51. If the element is a player, this function will use the players voice.

## Syntax

```
table getSoundFFTData ( element sound, int iSamples [, int iBands = 0 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):getFFTData(...)*

### Required Arguments

- **sound:** a sound element that is created using [playSound](mta://scripting/client/functions/playsound.md) or [playSound3D](mta://scripting/client/functions/playsound3d.md). Streams are also supported

- **iSamples:** allowed samples are 256, 512, 1024, 2048, 4096, 8192 and 16384.

### Optional Arguments

- **iBands:** post processing option allows you to split the samples into the desired amount of bands or bars so if you only need 5 bars this saves a lot of cpu power compared to trying to do it in Lua.

### Returns

Returns a table of **iSamples**/2 (or **iBands** if **iBands** is used) *floats* representing the current audio frame.
Returns *false* if the sound is not playing yet or hasn't buffered in the
case of streams.

## Example

Click to collapse [-]
Client

```
soundHandler = playSound ( "sound.wav" )

function onSoundPlayRender ( )
    if ( soundHandler ) then
        local soundFFT = getSoundFFTData ( soundHandler, 2048, 256 )
	if ( soundFFT ) then
            for i = 0, 255 do -- Data starts from index 0
                dxDrawRectangle ( i, 0, 1, math.sqrt ( soundFFT[i] ) * 256 )
            end
        end
    end
end
addEventHandler ( "onClientRender", getRootElement(), onSoundPlayRender )
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

- getSoundFFTData

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
