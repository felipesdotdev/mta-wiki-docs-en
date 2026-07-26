---
doc_id: "mta-wiki:5418"
title: "OnClientSoundStream"
source_title: "OnClientSoundStream"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientSoundStream"
revision_id: 60834
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.411258+00:00"
---

# OnClientSoundStream

This event is triggered when a sound has just finished initial streaming. For file streams, this means the sound will now start playing, but isn't done downloading yet. For live streams, this just means the stream will start playing. This event will also trigger when, for some reason, the streaming failed.

## Parameters

```
bool success, int length, string streamName, string errorMessage
```

- **success**: A [boolean](mta://reference/misc/boolean.md) indicating whether the stream was a success or not

- **length**: The length of the stream in seconds. Always returns **0** for a live stream

- **streamName**: The name of the stream. Note that this isn't the filename. Also note that this isn't always provided

- **errorMessage**: A string containing the error message or an empty string if there was no error

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [sound](mta://reference/misc/sound.md) which either successfully streamed or failed to stream.

## Example

This example outputs to the chatbox (if it was a success) "thesoundname has finished in ... seconds.", if it was not a success then it would output "thesoundname failed to start".

```
addEventHandler("onClientSoundStream",root,function(suc,length,streamN)
	if not suc then outputChatBox("Sound: "..streamN.." failed to start.",100,0,0) return end
	outputChatBox("The sound: "..streamN.." has finished in "..length.."secs.")
end)
```

## See Also

### Client player events

- [onClientSoundBeat](mta://scripting/client/events/onclientsoundbeat.md)

- [onClientSoundChangedMeta](mta://scripting/client/events/onclientsoundchangedmeta.md)

- [onClientSoundFinishedDownload](mta://scripting/client/events/onclientsoundfinisheddownload.md)

- [onClientSoundStarted](mta://scripting/client/events/onclientsoundstarted.md)

- [onClientSoundStopped](mta://scripting/client/events/onclientsoundstopped.md)

- onClientSoundStream

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
