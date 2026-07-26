---
doc_id: "mta-wiki:12638"
title: "IsSoundLooped"
source_title: "IsSoundLooped"
source_url: "https://wiki.multitheftauto.com/wiki/IsSoundLooped"
revision_id: 81277
language: "en"
categories: ["Client_functions"]
---

# IsSoundLooped

This function is used to return the current loop state of the [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md).

## Syntax

```
bool isSoundLooped ( element theSound )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):isLooped(...)*

**Counterpart**: *[setSoundLooped](mta://scripting/client/functions/setsoundlooped.md)*

### Required Arguments

- **theSound:** The [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) which you want to get the loop state.

### Returns

Returns *true* if the [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) is looped, *false* otherwise.

## Example

This will create a [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) and change its state to looped, with a command to switch the loop state and output its state:

```
local mySound

addEventHandler ("onClientResourceStart", resourceRoot, function ()
    mySound = playSound ("sound.mp3")
    setSoundLooped (mySound, true)
end)

addCommandHandler ("loop", function ()
    if isElement (mySound) then
        local newState = not isSoundLooped (mySound)
        setSoundLooped (mySound, newState)

        if newState then
            outputChatBox ("The sound will loop!")
        else
            outputChatBox ("The sound will not loop anymore!")
        end
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

- isSoundLooped

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
