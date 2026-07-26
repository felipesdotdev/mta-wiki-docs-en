---
doc_id: "mta-wiki:7673"
title: "SetSoundPanningEnabled"
source_title: "SetSoundPanningEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/SetSoundPanningEnabled"
revision_id: 72686
language: "en"
categories: ["Client_functions", "Changes_in_1.4.0"]
---

# SetSoundPanningEnabled

This function toggles the panning of a sound (hearing it closer to the left or right side of the speakers due to the camera position). By default a sound has its panning enabled.

## Syntax

```
bool setSoundPanningEnabled ( element sound, bool enable )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *The method name was incorrect (setPann**n**ingEnabled) before version **1.5.8 r20761**.*

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):setPanningEnabled(...)*

**Variable**: *.panningEnabled*

**Counterpart**: *[isSoundPanningEnabled](mta://scripting/client/functions/issoundpanningenabled.md)*

### Required arguments

- **sound:** a [sound](https://wiki.multitheftauto.com/index.php?search=sound) element to change the panning of.

- **enable:** *true* to enable the panning, *false* otherwise.

### Returns

Returns *true* if the sound is valid and good arguments were passed, *false* if not.

If the sound is not 3D, this function will return *true* as well, but [isSoundPanningEnabled](mta://scripting/client/functions/issoundpanningenabled.md) will always return *true* after this (so it has no effect).

## Example

This example creates a sound at the center of the map when the resource which cointains it starts and adds a command called /soundpanning, which changes the panning of the sound.

```
local panned = true
local sound = playSFX3D("script", 7, 1, 0, 0, 20, true)

function changePanning()
    if sound then
        setSoundPanningEnabled(sound, not panned)
        panned = not panned
        outputChatBox("Sound panning changed to " .. tostring(panned))
    else
        outputDebugString("Looks that your GTA was ripped.")
    end
end
addCommandHandler("soundpanning", changePanning)
```

## See also

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

- setSoundPanningEnabled

- [setSoundPaused](mta://scripting/client/functions/setsoundpaused.md)

- [setSoundPosition](mta://scripting/client/functions/setsoundposition.md)

- [setSoundProperties](mta://scripting/client/functions/setsoundproperties.md)

- [setSoundSpeed](mta://scripting/client/functions/setsoundspeed.md)

- [setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)

- [stopSound](mta://scripting/client/functions/stopsound.md)
  

- **Shared**

- [playSoundFrontEnd](mta://scripting/shared/functions/playsoundfrontend.md)
