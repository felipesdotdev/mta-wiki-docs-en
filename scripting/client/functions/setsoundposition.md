---
doc_id: "mta-wiki:4280"
title: "SetSoundPosition"
source_title: "SetSoundPosition"
source_url: "https://wiki.multitheftauto.com/wiki/SetSoundPosition"
revision_id: 71991
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:45.022607+00:00"
---

# SetSoundPosition

This function is used to change the seek position of the specified [sound](mta://reference/misc/sound.md) element.
Use a player element to control a players voice with this function.

| [[{{{image}}}\|link=\|]] | Note: To set position of a remote audio file, you must pause the sound within an onClientSoundStream event after creation, set the sound position and then unpause it again. The sound can also not be throttled (see playSound arguments) |
| --- | --- |
|  |  |

## Syntax

```
bool setSoundPosition ( element theSound, float pos )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):setPlaybackPosition(...)*

**Variable**: *.playbackPosition*

**Counterpart**: *[getSoundPosition](mta://scripting/client/functions/getsoundposition.md)*

### Required Arguments

- **theSound:** the [sound](mta://reference/misc/sound.md) element which seek position you want to modify.

- **pos:** a [float](mta://reference/misc/float.md) value representing the new seek position of the [sound](mta://reference/misc/sound.md) element in seconds.

### Returns

Returns *true* if the [sound](mta://reference/misc/sound.md) element's seek position was successfully changed, *false* otherwise.

## Example

This example allows the player to set how many milliseconds into the song he wants it to play from

```
theSound = playSound("music/song.mp3")
function setSongPos(cmd, tm)
    tm = tonumber(tm)
    local ssp = setSoundPosition(theSound,tm)
    if ssp then
        outputChatBox("Sound is now playing from: "..tostring(tm))
    else
        outputChatBox("An error has occured.")
    end
end
addCommandHandler("skipsong", setSongPos)
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

- setSoundPosition

- [setSoundProperties](mta://scripting/client/functions/setsoundproperties.md)

- [setSoundSpeed](mta://scripting/client/functions/setsoundspeed.md)

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
