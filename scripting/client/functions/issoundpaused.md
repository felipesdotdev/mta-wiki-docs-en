---
doc_id: "mta-wiki:4284"
title: "IsSoundPaused"
source_title: "IsSoundPaused"
source_url: "https://wiki.multitheftauto.com/wiki/IsSoundPaused"
revision_id: 71836
language: "en"
categories: ["Client_functions", "Changes_in_1.3.2"]
generated_at: "2026-07-26T16:16:00.433966+00:00"
---

# IsSoundPaused

This function is used to return the current pause state of the specified [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md).

If the element is a [player](mta://reference/misc/player.md), this function will use the players voice.

## Syntax

```
bool isSoundPaused ( element theSound )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):isPaused(...)*

**Variable**: *.paused*

**Counterpart**: *[setSoundPaused](mta://scripting/client/functions/setsoundpaused.md)*

### Required Arguments

- **theSound:** the [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) which pause state you want to return.

### Returns

Returns *true* if the [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) is paused, *false* if unpaused or invalid arguments were passed.

## Example

This example will check and see if the sound is paused or not, and tell the player.

Click to collapse [-]
Client

```
theSound = playSound("music/song.mp3")
function checkSongPause()
    local pause = isSoundPaused(theSound)
    if(pause == true) then
        outputChatBox("The sound is paused!")
    else
        outputChatBox("The sound is not paused!")
    end
end
addCommandHandler("checkpause", checkSongPause)
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

- [getSoundWaveData](mta://scripting/client/functions/getsoundwavedata.md)

- [isSoundLooped](mta://scripting/client/functions/issoundlooped.md)

- [isSoundPanningEnabled](mta://scripting/client/functions/issoundpanningenabled.md)

- isSoundPaused

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
