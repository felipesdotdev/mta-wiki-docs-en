---
doc_id: "mta-wiki:7260"
title: "PlaySFX3D"
source_title: "PlaySFX3D"
source_url: "https://wiki.multitheftauto.com/wiki/PlaySFX3D"
revision_id: 73341
language: "en"
categories: ["Client_functions", "Changes_in_1.3.4", "Changes_in_1.4"]
generated_at: "2026-07-26T16:16:29.167602+00:00"
---

# PlaySFX3D

This function plays a sound in the GTA world from GTA's big sound containers.

| [[{{{image}}}\|link=\|]] | Note: There is a tool available which allows you to find bank and sound IDs easily: [ sfxBrowser:Download ]. |
| --- | --- |
|  |  |

|  | Warning: Many players use versions of GTA:SA (especially pirated versions) that have audio files full of zeros so that they can compresses better in their AUDIO\SFX\ folder. (They lack any data) In case of these invalid audio files, this function returns false . It also returns false when trying to play a track deleted in the recent GTA: SA Steam patches (and if the client is using a Steam GTA: SA copy). |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: PlaySFX sounds are MTA driven sounds, so MTA volume affects the volume. |
| --- | --- |
|  |  |

## Syntax

```
element playSFX3D ( string containerName, int bankId, int soundId, float x, float y, float z [, bool looped = false ] )
```

### Required Arguments

- **containerName:** The name of the audio container. Possible values are: "feet", "genrl", "pain_a", "script", "spc_ea", "spc_fa", "spc_ga", spc_na", "spc_pa"

- **bankId:** The audio bank id

- **soundId:** The sound id within the audio bank

- **x:** A floating point number representing the X coordinate on the map.

- **y:** A floating point number representing the Y coordinate on the map.

- **z:** A floating point number representing the Z coordinate on the map.

### Optional Arguments

- **looped:** A [boolean](mta://reference/misc/boolean.md) representing whether the sound will be looped

## Returns

Returns a [sound](mta://reference/misc/sound.md) element if the sound was successfully created, *false* otherwise.

## Syntax 2

```
element playSFX3D( string "radio", string radioStation, int trackId, float x, float y, float z [, bool looped = false ] )
```

### Required Arguments

- **radio:** The string "radio" (used to differentiate to the first syntax)

- **radioStation:** The radio station. Possible values are "Adverts", "Ambience", "Police", "Playback FM", "K-Rose", "K-DST", "Cutscene", "Beats", "Bounce FM", "SF-UR", "Radio Los Santos", "Radio X", "CSR 103.9", "K-Jah West", "Master Sounds 98.3", "WCTR".

- **trackId :** The radio track id within the radio station audio file

- **x:** A floating point number representing the X coordinate on the map.

- **y:** A floating point number representing the Y coordinate on the map.

- **z:** A floating point number representing the Z coordinate on the map.

### Optional Arguments

- **looped:** A [boolean](mta://reference/misc/boolean.md) representing whether the sound will be looped

## Returns

Returns a [sound](mta://reference/misc/sound.md) element if the sound was successfully created, *false* otherwise.

## Example

The following example plays a fire alarm sound near you (looped).

```
local x, y, z = getElementPosition(localPlayer)
if not playSFX3D("script", 7, 1, x + 10, y, z, true) then
    outputChatBox("You have to install some missing audio files to hear the sound")
end
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

- playSFX3D

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
