---
doc_id: "mta-wiki:5420"
title: "OnClientSoundFinishedDownload"
source_title: "OnClientSoundFinishedDownload"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientSoundFinishedDownload"
revision_id: 31701
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.368700+00:00"
---

# OnClientSoundFinishedDownload

This event is triggered when a sound has just finished downloading. This means the complete sound file is now loaded in the player's RAM, and can be played completely from start to end. Unlike [onClientSoundStream](mta://scripting/client/events/onclientsoundstream.md), this event only triggers for file streams, not for live ones since live streams never actually end.

## Parameters

```
int length
```

- **length**: The length of the stream in milliseconds

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [sound](mta://reference/misc/sound.md) which just finished downloading.

## Example

This example would output to the chatbox after the sound is finish that the sound has finished downloading in ... milliseconds.

```
addEventHandler("onClientSoundFinishedDownload",root,function(length)
	local meta = getSoundMetaTags(source)
	outputChatBox("The sound: "..(meta.title).." has finished in :"..length.."ms.")
end)
```

## See Also

### Client player events

- [onClientSoundBeat](mta://scripting/client/events/onclientsoundbeat.md)

- [onClientSoundChangedMeta](mta://scripting/client/events/onclientsoundchangedmeta.md)

- onClientSoundFinishedDownload

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
