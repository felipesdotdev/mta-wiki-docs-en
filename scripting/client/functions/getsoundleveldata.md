---
doc_id: "mta-wiki:6771"
title: "GetSoundLevelData"
source_title: "GetSoundLevelData"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundLevelData"
revision_id: 81144
language: "en"
categories: ["Client_functions", "Changes_in_1.3.2"]
generated_at: "2026-07-26T16:15:25.438826+00:00"
---

# GetSoundLevelData

This function gets the left/right level from a [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md).
If the element is a player, this function will use the players voice.

## Syntax

```
int, int getSoundLevelData ( element theSound )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):getLevelData(...)*

### Required Arguments

- **theSound:** the [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) which level data you want to return.

### Returns

Returns a two *integers* in range from 0 to 32768.

## Example

```
local soundHandler = playSound ( "sound.wav" )

function onSoundPlayRender ( )
    if ( soundHandler ) then
        local leftData, rightData = getSoundLevelData ( soundHandler )
	if ( leftData ) then
            dxDrawRectangle ( 0, 0, 64, leftData / 32768 * 256, tocolor ( 255, 0, 0 ) )
            dxDrawRectangle ( 64, 0, 64, rightData / 32768 * 256, tocolor ( 0, 0, 255 ) )
        end
    end
end
addEventHandler ( "onClientRender", root, onSoundPlayRender )
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

- getSoundLevelData

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
