---
doc_id: "mta-wiki:2396"
title: "PlaySound"
source_title: "PlaySound"
source_url: "https://wiki.multitheftauto.com/wiki/PlaySound"
revision_id: 82675
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.5"]
---

# PlaySound

Creates a [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) and plays it immediately after creation for the local player.
Added the feature of playing WebM files.

| [[{{{image}}}\|link=\|]] | Note: The only supported audio formats are MP3, WAV, OGG, FLAC, RIFF, MOD, WEBM, XM, IT, S3M and PLS (e.g. Webstream). For performance reasons, when using playSound for effects that will be played lots (i.e. weapon fire), it is recommend that you convert your audio file to a one channel (mono) WAV with sample rate of 22050 Hz or less. Also consider adding a limit on how often the effect can be played e.g. once every 50ms. |
| --- | --- |
|  |  |

## Syntax

```
element playSound ( string soundPath, [ bool looped = false, bool throttled = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Sound](https://wiki.multitheftauto.com/index.php?search=Sound)(...)*

### Required Arguments

- **soundPath:** [filepath](mta://reference/misc/filepath.md), raw data or URL (http://, https:// or ftp://) of the sound file you want to play. (**Note:** Playing sound files from other resources requires the target resource to be in the running state)

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **looped:** a [boolean](mta://reference/misc/boolean.md) representing whether the sound will be looped. To loop the sound, use *true*. Loop is not available for streaming sounds, only for sound files.

- **throttled:** a [boolean](mta://reference/misc/boolean.md) representing whether the sound will be throttled (i.e. given reduced download bandwidth). To throttle the sound, use *true*. Sounds will be throttled per default and only for URLs.

### Returns

Returns a [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) if the sound was successfully created, *false* otherwise.

## Example

```
function wasted (killer, weapon, bodypart) 
    local sound = playSound("sounds/wasted.mp3") -- Play wasted.mp3 from the sounds folder
    if isElement(sound) then
        setSoundVolume(sound, 0.5) -- Set the sound volume to 50%
    end
end

addEventHandler("onClientPlayerWasted", localPlayer, wasted) -- Add the event handler
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

- playSound

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
