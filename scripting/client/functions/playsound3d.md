---
doc_id: "mta-wiki:4278"
title: "PlaySound3D"
source_title: "PlaySound3D"
source_url: "https://wiki.multitheftauto.com/wiki/PlaySound3D"
revision_id: 82676
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.5"]
generated_at: "2026-07-26T16:16:29.226460+00:00"
---

# PlaySound3D

Creates a [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) in the GTA world and plays it immediately after creation for the local player. [setElementPosition](mta://scripting/shared/functions/setelementposition.md) can be used to move the [sound](mta://reference/misc/sound.md) element around after it has been created. Remember to use [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) after creating the sound to play it outside of dimension 0.
Added the feature of playing WebM files.

| [[{{{image}}}\|link=\|]] | Note: The only supported audio formats are MP3, WAV, OGG, FLAC, RIFF, MOD, WEBM, XM, IT and S3M. For performance reasons, when using playSound3D for effects that will be played lots (i.e. weapon fire), it is recommend that you convert your audio file to a one channel (mono) WAV with sample rate of 22050 Hz or less. Also consider adding a limit on how often the effect can be played e.g. once every 50ms. |
| --- | --- |
|  |  |

## Syntax

```
element playSound3D ( string soundPath, float x, float y, float z, [ bool looped = false, bool throttled = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Sound3D](mta://reference/misc/sound.md)(...)*

### Required Arguments

- **soundPath:** raw data or [filepath](mta://reference/misc/filepath.md) to the sound file you want to play. (**Note:** Playing sound files from other resources requires the target resource to be in the running state)

- **soundURL:** the URL (http://, https:// or ftp://) of the sound file you want to play. (In this version the file does not have to be predefined in the [meta.xml](mta://reference/misc/meta-xml.md))

- **x:** a [floating](mta://reference/misc/float.md) point number representing the X coordinate on the map.

- **y:** a [floating](mta://reference/misc/float.md) point number representing the Y coordinate on the map.

- **z:** a [floating](mta://reference/misc/float.md) point number representing the Z coordinate on the map.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **looped:** a [boolean](mta://reference/misc/boolean.md) representing whether the sound will be looped. To loop the sound, use *true*.

- **throttled:** a [boolean](mta://reference/misc/boolean.md) representing whether the sound will be throttled (i.e. given reduced download bandwidth). To throttle the sound, use *true*.

### Returns

Returns a [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) if the sound was successfully created, *false* otherwise.

## Example

This example creates a looping sound within a pizza shop. It's located in San Fierro near Pier 69.

Click to collapse [-]
Example

```
function onResourceStart()
    playSound3D("sounds/song.mp3", 373.14, -125.21, 1001, true) 
end
addEventHandler("onClientResourceStart", resourceRoot, onResourceStart)
```

This example plays internet radio at Grove street.

Click to collapse [-]
Example 2

```
addEventHandler('onClientResourceStart', resourceRoot, function()
    local uSound = playSound3D('http://977music.com/itunes/80s.pls', 2498, -1659, 12)
    if isElement(uSound) then
        setSoundMaxDistance(uSound, 100)
    end
end)
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

- playSound3D

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
