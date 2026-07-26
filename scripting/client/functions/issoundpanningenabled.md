---
doc_id: "mta-wiki:7062"
title: "IsSoundPanningEnabled"
source_title: "IsSoundPanningEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsSoundPanningEnabled"
revision_id: 81178
language: "en"
categories: ["Client_functions", "Changes_in_1.3.0", "Changes_in_1.4.0"]
generated_at: "2026-07-26T16:16:00.408272+00:00"
---

# IsSoundPanningEnabled

This function checks whether panning is enabled in a [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md) or not.

| [[{{{image}}}\|link=\|]] | Tip: Although this function works in no-3D sounds (those created by playSound ), it only makes sense to use it with 3D sounds (created by playSound3D ). Please refer to setSoundPanningEnabled for a explanation of what this property does. |
| --- | --- |
|  |  |

## Syntax

```
bool isSoundPanningEnabled ( element theSound )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](mta://reference/misc/sound.md):isPanningEnabled(...)*

**Variable**: *.panningEnabled*

**Counterpart**: *[setSoundPanningEnabled](mta://scripting/client/functions/setsoundpanningenabled.md)*

### Required Arguments

- **theSound :** A valid [sound](mta://reference/misc/sound.md) [element](mta://reference/misc/element.md).

### Returns

Returns *true* if the sound is valid and it has panning enabled, *false* if it does not or is not valid.

## Example

This example plays a *xy.mp3* file in the root folder of the resource which contains it at the center of the map, and proves that by default a sound enables panning by outputting the result of this function to the chatbox right after creating it. Then it disables the panning of the sound.

```
local function testPanning()
    -- Create the sound and output the panning property state
    local sound = playSound3D("xy.mp3", 0, 0, 0)
    outputChatBox("By default, the sound has its panning " .. (isSoundPanningEnabled(sound) and "enabled" or "disabled"))
    -- Disable the panning and ouput a fact
    setSoundPanningEnabled(sound, false)
    outputChatBox("The sound panning was disabled, so it won't annoy you when the camera it's in a side anymore!", 0, 255, 0)
end
addEventHandler("onClientResourceStart", resourceRoot, testPanning)
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

- isSoundPanningEnabled

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
