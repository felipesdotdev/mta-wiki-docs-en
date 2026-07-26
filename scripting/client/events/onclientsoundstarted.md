---
doc_id: "mta-wiki:6118"
title: "OnClientSoundStarted"
source_title: "OnClientSoundStarted"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientSoundStarted"
revision_id: 64075
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.383485+00:00"
---

# OnClientSoundStarted

This event is triggered when a **sound** is started.

## Parameters

```
string reason
```

- **reason**: the reason the **sound** was started, can be "play", "resumed" or "enabled".

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [sound's element](mta://reference/misc/element-sound.md).

## Example

This example outputs the reason the sound started .

```
function onSoundStarted ( reason )
    if ( reason == "play" ) then
        outputChatBox ( "sound started" )
    elseif ( reason == "resumed" ) then
        outputChatBox ( "sound resumed" )
    end
end
addEventHandler ( "onClientSoundStarted", getRootElement(), onSoundStarted )
```

## See Also

### Client sound events

- [onClientSoundBeat](mta://scripting/client/events/onclientsoundbeat.md)

- [onClientSoundChangedMeta](mta://scripting/client/events/onclientsoundchangedmeta.md)

- [onClientSoundFinishedDownload](mta://scripting/client/events/onclientsoundfinisheddownload.md)

- onClientSoundStarted

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
