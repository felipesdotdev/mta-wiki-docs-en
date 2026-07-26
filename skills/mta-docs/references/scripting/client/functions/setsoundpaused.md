---
doc_id: "mta-wiki:4283"
title: "SetSoundPaused"
source_title: "SetSoundPaused"
source_url: "https://wiki.multitheftauto.com/wiki/SetSoundPaused"
revision_id: 63315
language: "en"
categories: ["Client_functions", "Changes_in_1.3.2"]
---

# SetSoundPaused

This function is used to either pause or unpause the playback of the specified [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md).

Use a player element to control a players voice with this function.

## Syntax

```
bool setSoundPaused ( element theSound, bool paused )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):setPaused(...)*

**Variable**: *.paused*

**Counterpart**: *[isSoundPaused](mta://scripting/client/functions/issoundpaused.md)*

### Required Arguments

- **theSound:** the [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) which you want to pause/unpause.

- **paused:** a [boolean](mta://reference/misc/boolean.md) value representing whether the sound should be paused or not. To pause the sound, use *true*.

### Returns

Returns *true* if the [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) was successfully paused, *false* otherwise.

## Example

This example will allow the user to toggle sounds from paused to playing, and from playing to paused

Click to collapse [-]
Client

```
theSound = playSound("music/song.mp3", true)
function togglePausedSound()
    if(isSoundPaused(theSound)) then --sound is paused, un-pause it
        setSoundPaused(theSound, false)
    else --sound is not paused, pause it
        setSoundPaused(theSound, true)
    end
end
addCommandHandler("pausesound", togglePausedSound)
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

- setSoundPaused

- [setSoundPosition](mta://scripting/client/functions/setsoundposition.md)

- [setSoundProperties](mta://scripting/client/functions/setsoundproperties.md)

- [setSoundSpeed](mta://scripting/client/functions/setsoundspeed.md)

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
