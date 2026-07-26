---
doc_id: "mta-wiki:5426"
title: "GetSoundMetaTags"
source_title: "GetSoundMetaTags"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundMetaTags"
revision_id: 80334
language: "en"
categories: ["Client_functions", "Utility_templates"]
---

# GetSoundMetaTags

Used to get the meta tags attached to a sound. These provide information about the sound, for instance the title or the artist.

| [[{{{image}}}\|link=\|]] | Note: This function does not work on remote WAV files |
| --- | --- |
|  |  |

## Syntax

```
table getSoundMetaTags ( element sound [, string format = "" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):getMetaTags(...)*

### Required Arguments

- **sound:** a [sound](https://wiki.multitheftauto.com/index.php?search=sound) element.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **format:** a filter [string](mta://reference/misc/string.md) to get a specific meta tag.

### Returns

Returns a [table](mta://reference/misc/table.md), but only a [string](mta://reference/misc/string.md) if **format** is given, with all data available (keys are listed below) for the sound if successful, *false* otherwise. If any data is unavailable then the associated key is not written to the table.

- **title**

- **artist**

- **album**

- **genre**

- **year**

- **comment**

- **track**

- **composer**

- **copyright**

- **subtitle**

- **album_artist**

- **stream_name**

- **stream_title**

## Example

```
addEventHandler("onClientSoundFinishedDownload",root,function(length)
	local meta = getSoundMetaTags(source)
	outputChatBox("The sound: "..(meta.title).." has finished in :"..length.."ms.")
        outputChatBox("The sound meta tags: Artist:"..(meta.artist).." Album:"..(meta.album).." Genre:"..(meta.genre).." Year:"..(meta.year).." Comment:"..(meta.comment).." Track:"..(meta.track).." Composer:"..(meta.composer).." Copyright:"..(meta.copyright).." SubTitle:"..(meta.subtitle).." Album Artist:"..(meta.album_artist)..".")
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

- getSoundMetaTags

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
