---
doc_id: "mta-wiki:6360"
title: "OnClientWorldSound"
source_title: "OnClientWorldSound"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientWorldSound"
revision_id: 65698
language: "en"
categories: ["Client_events", "Changes_in_1.5.6"]
generated_at: "2026-07-26T16:16:20.754097+00:00"
---

# OnClientWorldSound

This event triggers whenever a GTA sound starts playing.

| [[{{{image}}}\|link=\|]] | Note: Use setWorldSoundEnabled if you want to disable certain sounds conditionless. For example, you should only cancel player emitted sounds in this event, because when you cancel certain vehicle sounds, the game will try to play the same sound on the next frame. |
| --- | --- |
|  |  |

## Parameters

```
int group, int index, float x, float y, float z
```

- **group:** An [integer](mta://reference/misc/int.md) representing the [world sound group](mta://reference/misc/world-sound-groups.md)

- **index:** An [integer](mta://reference/misc/int.md) representing an individual sound within the group

- **x:** a [floating](mta://reference/misc/float.md) point number representing the X coordinate on the map.

- **y:** a [floating](mta://reference/misc/float.md) point number representing the Y coordinate on the map.

- **z:** a [floating](mta://reference/misc/float.md) point number representing the Z coordinate on the map.

## Source

The source of this event is the element, which emitted the sound.

## Cancel effect

If this event is [canceled](mta://reference/misc/event-system.md), the sound won't play at all.

## Example

**Example 1:** This example will cancel every vehicle sound.

```
addEventHandler("onClientWorldSound", root, function()
    if getElementType(source) == "vehicle" then
        cancelEvent()
    end
end)
```

**Example 2:** This example lets you see how many times each sound that gets played has been played using '/seesoundlist'.

```
local sounds = {}

addEventHandler("onClientWorldSound", root, function(group, index)
	sounds[group.." | "..index] = (sounds[group.." | "..index] or 0) + 1
end)

function cmdSeeSoundList()
	-- Put the non iterated table into an interated table so we can sort them
	local tbl = {}
	for sound, count in pairs(sounds) do
		tbl[#tbl + 1] = {sound, count}
	end
	table.sort(tbl, function(a, b) return a[2] > b[2] end)
	-- Output the table to clipboard
	local str = "Group | Index: Times played\n"
	for i, dat in ipairs(tbl) do
		str = str..dat[1]..": "..dat[2].."\n"
	end
	setClipboard(str)
	outputChatBox("Use CTRL + V in notepad to view the table.")
end
addCommandHandler("seesoundlist", cmdSeeSoundList)
```

## See Also

### World sound functions

- [setWorldSoundEnabled](mta://scripting/client/functions/setworldsoundenabled.md)

- [isWorldSoundEnabled](mta://scripting/client/functions/isworldsoundenabled.md)

- [resetWorldSounds](mta://scripting/client/functions/resetworldsounds.md)

### Client other events

- [onClientChatMessage](mta://scripting/client/events/onclientchatmessage.md)

- [onClientConsole](mta://scripting/client/events/onclientconsole.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [onClientCoreCommand](mta://scripting/client/events/onclientcorecommand.md)

- [onClientDebugMessage](mta://scripting/client/events/onclientdebugmessage.md)

- [onClientExplosion](mta://scripting/client/events/onclientexplosion.md)

- [onClientFileDownloadComplete](mta://scripting/client/events/onclientfiledownloadcomplete.md)

- [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md)

- [onClientMinimize](mta://scripting/client/events/onclientminimize.md)

- [onClientMTAFocusChange](mta://scripting/client/events/onclientmtafocuschange.md)

- [onClientPedsProcessed](mta://scripting/client/events/onclientpedsprocessed.md)

- [onClientPlayerNetworkStatus](mta://scripting/client/events/onclientplayernetworkstatus.md)

- [onClientPreRender](mta://scripting/client/events/onclientprerender.md)

- [onClientRender](mta://scripting/client/events/onclientrender.md)

- [onClientRestore](mta://scripting/client/events/onclientrestore.md)

- [onClientTransferBoxProgressChange](mta://scripting/client/events/onclienttransferboxprogresschange.md)

- [onClientTransferBoxVisibilityChange](mta://scripting/client/events/onclienttransferboxvisibilitychange.md)

- onClientWorldSound

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
