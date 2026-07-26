---
doc_id: "mta-wiki:6119"
title: "OnClientSoundStopped"
source_title: "OnClientSoundStopped"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientSoundStopped"
revision_id: 64076
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.396556+00:00"
---

# OnClientSoundStopped

This event is triggered when a **sound** is stopped.

## Parameters

```
string reason
```

- **reason**: the reason the **sound** was stopped, can be "finished", "paused", "destroyed" or "disabled".

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [sound's element](mta://reference/misc/element-sound.md).

## Example

This example outputs the reason the sound stopped.

```
function onSoundStopped ( reason )
    if ( reason == "destroyed" ) then
        outputChatBox ( "sound destroyed" )
    elseif ( reason == "finished" ) then
        outputChatBox ( "end of sound" )
    elseif ( reason == "paused" ) then
        outputChatBox ( "sound paused" )
    end
end
addEventHandler ( "onClientSoundStopped", getRootElement(), onSoundStopped )
```

## See Also

### Client sound events

- [onClientSoundBeat](mta://scripting/client/events/onclientsoundbeat.md)

- [onClientSoundChangedMeta](mta://scripting/client/events/onclientsoundchangedmeta.md)

- [onClientSoundFinishedDownload](mta://scripting/client/events/onclientsoundfinisheddownload.md)

- [onClientSoundStarted](mta://scripting/client/events/onclientsoundstarted.md)

- onClientSoundStopped

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
