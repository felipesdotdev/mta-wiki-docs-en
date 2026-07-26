---
doc_id: "mta-wiki:4432"
title: "SetRadioChannel"
source_title: "SetRadioChannel"
source_url: "https://wiki.multitheftauto.com/wiki/SetRadioChannel"
revision_id: 78437
language: "en"
categories: ["Client_functions", "Functions_and_events_with_issues"]
generated_at: "2026-07-26T16:16:44.262096+00:00"
---

# SetRadioChannel

This function sets the heard radio channel, even while not in a vehicle.

| [[{{{image}}}\|link=\|]] | Note: This function sometimes doesn't work when setting the radio channel to another different from the current one due to unknown reasons. If you experience this issue, simply add setRadioChannel(0) at the beginning of the script, outside any function. |
| --- | --- |
|  |  |

## Syntax

```
bool setRadioChannel ( int ID )
```

### Required Arguments

- **ID:** The ID of the radio station you want to play.

- **0:** Radio Off

- **1:** Playback FM

- **2:** K-Rose

- **3:** K-DST

- **4:** Bounce FM

- **5:** SF-UR

- **6:** Radio Los Santos

- **7:** Radio X

- **8:** CSR 103.9

- **9:** K-Jah West

- **10:** Master Sounds 98.3

- **11:** WCTR

- **12:** User Track Player

### Returns

Returns *true* if channel was set successfully, *false* otherwise.

## Example

This example adds a command *setradio* which can be used to change the current radio station by ID.

Click to collapse [-]
Client

```
addCommandHandler ( "setradio",
    function ( command, stationID )
        local result = setRadioChannel ( tonumber( stationID ) )
        if result then -- if we had a valid ID
            outputChatBox ( "Changed your radio station to " .. getRadioChannelName ( tonumber ( stationID ) ) .. "!" )
        else
            outputChatBox ( "Invalid radio station ID, valid ones are 0-12." )
        end
    end
)
```

## Issues

| Issue ID | Description |
| --- | --- |
| #423 | setRadioChannel doesn't work when outside a vehicle |

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

- [playSound](mta://scripting/client/functions/playsound.md)

- setRadioChannel

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
