---
doc_id: "mta-wiki:11157"
title: "GetSoundBufferLength"
source_title: "GetSoundBufferLength"
source_url: "https://wiki.multitheftauto.com/wiki/GetSoundBufferLength"
revision_id: 80327
language: "en"
categories: ["Client_functions", "Changes_in_1.5.6"]
---

# GetSoundBufferLength

This function gets the buffer playback length of the specified [sound](https://wiki.multitheftauto.com/index.php?search=sound). Works only with streams.

## Syntax

```
float getSoundBufferLength ( element theSound )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[sound](https://wiki.multitheftauto.com/index.php?search=sound):getBufferLength(...)*

**Variable**: *.bufferLength*

### Required Arguments

- **theSound:** the [sound](https://wiki.multitheftauto.com/index.php?search=sound) element which buffer length you want to get.

### Returns

- A [float](mta://reference/misc/float.md) value indicating the buffer playback length of the [sound](https://wiki.multitheftauto.com/index.php?search=sound) in seconds.

- *false* if the sound is not a stream.

- *nil* if the sound is invalid.

## Example

This example draws a simple player that shows the length of the downloaded part of the song.

```
local screenSize = Vector2(guiGetScreenSize())
local BOX_SIZE = Vector2(300, 100)
local LINE_SIZE = Vector2(BOX_SIZE.x, 10)
local BOX_POSITION = screenSize / 2 - BOX_SIZE / 2
local TITLE_POSITION = BOX_POSITION + Vector2(8, 8)
local ARTIST_POSITION = BOX_POSITION + Vector2(8, 32)

local sound

addCommandHandler("playsound", function ()
    if isElement(sound) then
        destroyElement(sound)
    end
    sound = playSound("https://example.com/song.mp3")
end)

addCommandHandler("stopsound", function ()
    if isElement(sound) then
        destroyElement(sound)
    end
end)

addEventHandler("onClientRender", root, function ()
    if isElement(sound) then
        local soundLength = getSoundLength(sound)
        local soundPosition = getSoundPosition(sound)
        local soundBufferLength = getSoundBufferLength(sound)

        local meta = getSoundMetaTags(sound)

        dxDrawRectangle(BOX_POSITION, BOX_SIZE, tocolor(20, 20, 20, 255), false, false)

        if meta.title then
            dxDrawText(meta.title, TITLE_POSITION, 0, 0, tocolor(255, 255, 255, 255), 1.5, 1.5, "clear")
        end
        if meta.artist then
            dxDrawText(meta.artist, ARTIST_POSITION, 0, 0, tocolor(255, 255, 255, 255), 1.0, 1.0, "clear")
        end

        dxDrawText(("%d:%02d"):format(soundPosition / 60, soundPosition % 60), BOX_POSITION + Vector2(8, BOX_SIZE.y - 32), BOX_POSITION + BOX_SIZE - Vector2(8, 0), tocolor(255, 255, 255, 255), 1.0, 1.0, "clear", "left", "top")
        dxDrawText(("%d:%02d"):format(soundLength / 60, soundLength % 60), BOX_POSITION + Vector2(8, BOX_SIZE.y - 32), BOX_POSITION + BOX_SIZE - Vector2(8, 0), tocolor(255, 255, 255, 255), 1.0, 1.0, "clear", "right", "top")
        
        -- draw seek bar
        local linePosition = Vector2(BOX_POSITION.x, BOX_POSITION.y + BOX_SIZE.y - LINE_SIZE.y)
        dxDrawRectangle(linePosition, LINE_SIZE, tocolor(255, 255, 255, 128), false, false)

        -- draw buffer length
        if soundBufferLength then
            dxDrawRectangle(linePosition, Vector2(LINE_SIZE.x * (soundBufferLength / soundLength), LINE_SIZE.y), tocolor(255, 255, 255, 96), false, false)
        end
        -- draw current position
        dxDrawRectangle(linePosition, Vector2(LINE_SIZE.x * (soundPosition / soundLength), LINE_SIZE.y), tocolor(255, 255, 255, 255), false, false)
    end
end)
```

## See Also

- [getRadioChannel](mta://scripting/client/functions/getradiochannel.md)

- [getRadioChannelName](mta://scripting/client/functions/getradiochannelname.md)

- [getSFXStatus](mta://scripting/client/functions/getsfxstatus.md)

- [getSoundBPM](mta://scripting/client/functions/getsoundbpm.md)

- getSoundBufferLength

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
