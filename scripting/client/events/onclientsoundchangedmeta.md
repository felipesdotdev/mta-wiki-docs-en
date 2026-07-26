---
doc_id: "mta-wiki:5421"
title: "OnClientSoundChangedMeta"
source_title: "OnClientSoundChangedMeta"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientSoundChangedMeta"
revision_id: 31167
language: "en"
categories: ["Client_events"]
generated_at: "2026-07-26T16:16:20.355052+00:00"
---

# OnClientSoundChangedMeta

This event is triggered when a sound's meta tags have been modified.

## Parameters

```
string streamTitle
```

- **streamTitle**: The title of a specific stream

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [sound](mta://reference/misc/sound.md) of which the meta tags have just been modified.

## Example

Click to collapse [-]
Client

This example will output the new stream title in the chatbox.

```
addEventHandler("onClientSoundChangedMeta", root, function(streamTitle)
    outputChatBox("* Now streaming: "..streamTitle, 255, 200, 0, false)
end)
```

## See Also

- [onClientSoundBeat](mta://scripting/client/events/onclientsoundbeat.md)

- onClientSoundChangedMeta

- [onClientSoundFinishedDownload](mta://scripting/client/events/onclientsoundfinisheddownload.md)

- [onClientSoundStarted](mta://scripting/client/events/onclientsoundstarted.md)

- [onClientSoundStopped](mta://scripting/client/events/onclientsoundstopped.md)

- [onClientSoundStream](mta://scripting/client/events/onclientsoundstream.md)
