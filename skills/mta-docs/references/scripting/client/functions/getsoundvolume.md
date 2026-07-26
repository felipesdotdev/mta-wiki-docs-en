---
doc_id: "mta-wiki:4286"
title: "GetSoundVolume"
source_title: "GetSoundVolume"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundVolume"
revision_id: 72762
language: "en"
categories: ["Client_functions", "Changes_in_1.3.2"]
---

# GetSoundVolume

This function is used to return the volume level of the specified [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md).
If the element is a [player](https://wiki.multitheftauto.com/index.php?search=player), this function will use the players voice.

## Syntax

```
float getSoundVolume ( element theSound )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):getVolume(...)*

**Variable**: *.volume*

**Counterpart**: *[setSoundVolume](mta://scripting/client/functions/setsoundvolume.md)*

### Required Arguments

- **theSound:** the [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md) which volume you want to return.

### Returns

Returns a [float](mta://reference/misc/float.md) representing the volume level of the [sound](https://wiki.multitheftauto.com/index.php?search=sound) [element](mta://reference/misc/element.md), *false* if invalid arguments were passed.

## Example

This example creates a sound then outputs the volume for it.

```
function wasted (killer, weapon, bodypart) 
	local sound = playSound("sounds/wasted.mp3") --Play wasted.mp3 from the sounds folder
	outputChatBox("Wasted Sound volume: "..getSoundVolume(sound)) --outputs to the client the volume of the sound
end
addEventHandler("onClientPlayerWasted", localPlayer, wasted) --add the event handler
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.2 | Added player element to use a players voice |
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

- getSoundVolume

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

´
