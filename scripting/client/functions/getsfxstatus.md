---
doc_id: "mta-wiki:7295"
title: "GetSFXStatus"
source_title: "GetSFXStatus"
source_url: "https://wiki.multitheftauto.com/wiki/GetSFXStatus"
revision_id: 80325
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:23.951236+00:00"
---

# GetSFXStatus

|  | Warning: Many players use versions of GTA:SA (especially pirated versions) that have audio files full of zeros so that they can compress better in their AUDIO\SFX\ folder. (They lack any data) In case of these invalid audio files, this function returns false . |
| --- | --- |
|  |  |

This function checks if a big sound container is available to use or not.

## Syntax

```
bool getSFXStatus ( string audioContainer )
```

### Required Arguments

- **audioContainer:** The container name. Possible values are:

- **feet**

- **genrl**

- **pain_a**

- **script**

- **spc_ea**

- **spc_fa**

- **spc_ga**

- **spc_na**

- **spc_pa**

## Returns

Returns **true** if the sound container is available, **false** otherwise.

## Example

```
if not getSFXStatus("spc_ea") then
   outputChatBox("Please install the missing audio files to enjoy the full gaming experience")
end
```

## See Also

- [getRadioChannel](mta://scripting/client/functions/getradiochannel.md)

- [getRadioChannelName](mta://scripting/client/functions/getradiochannelname.md)

- getSFXStatus

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

- [setSoundPosition](mta://scripting/client/functions/setsoundposition.md)

- [setSoundProperties](mta://scripting/client/functions/setsoundproperties.md)

- [setSoundSpeed](mta://scripting/client/functions/setsoundspeed.md)

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
