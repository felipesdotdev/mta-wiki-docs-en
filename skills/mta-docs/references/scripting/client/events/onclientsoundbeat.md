---
doc_id: "mta-wiki:6739"
title: "OnClientSoundBeat"
source_title: "OnClientSoundBeat"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientSoundBeat"
revision_id: 81142
language: "en"
categories: ["Client_events"]
---

# OnClientSoundBeat

This event is triggered when a **sound** beats.

| [[{{{image}}}\|link=\|]] | Note: This event does not work correctly pre 1.3.1-9-04627 |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: This event is triggered ahead of a sound beat the number passed is the play time at which the beat occurs |
| --- | --- |
|  |  |

## Parameters

```
double theTime
```

- **theTime**: the position in the song of the beat

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [sound's element](mta://reference/misc/element-sound.md).

## Example

Click to collapse [-]
Client

This code will change the vehicle color to a random value if the sound beats and the localPlayer is inside a vehicle

```
function playMySound()
    playSound("sound.mp3") -- play the sound used for onClientSoundBeat
    addEventHandler("onClientSoundBeat", getRootElement(), changeVehicleColorOnSoundBeat)
end
addEventHandler("onClientResourceStart", getRootElement(), playMySound)

function changeVehicleColorOnSoundBeat()
    if getPedOccupiedVehicle(localPlayer) then -- if the player is inside a vehicle
    setVehicleColor( getPedOccupiedVehicle(localPlayer), math.random(0,255), math.random(0,255), math.random(0,255) ) -- apply the color to the vehicle
    outputChatBox("The color of your vehicle was changed.") 
    else 
    outputChatBox("Could not change the vehicle color, the localPlayer is not inside a vehicle.") 
    return end;
end
```

## See Also

### Client sound events

- onClientSoundBeat

- [onClientSoundChangedMeta](mta://scripting/client/events/onclientsoundchangedmeta.md)

- [onClientSoundFinishedDownload](mta://scripting/client/events/onclientsoundfinisheddownload.md)

- [onClientSoundStarted](mta://scripting/client/events/onclientsoundstarted.md)

- [onClientSoundStopped](mta://scripting/client/events/onclientsoundstopped.md)

- [onClientSoundStream](mta://scripting/client/events/onclientsoundstream.md)

### Client event functions

- [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md)
  

- **Shared**

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- [triggerEvent](mta://scripting/shared/functions/triggerevent.md)

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
