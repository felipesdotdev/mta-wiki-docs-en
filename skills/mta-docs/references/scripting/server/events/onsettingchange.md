---
doc_id: "mta-wiki:5475"
title: "OnSettingChange"
source_title: "OnSettingChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnSettingChange"
revision_id: 72996
language: "en"
categories: ["Server_Events"]
---

# OnSettingChange

This event is triggered when resource setting has been changed. For instance, this event would trigger if you would edit the settings of the Race resource through the Admin panel.

## Parameters

```
string setting, string oldValue, string newValue
```

- **setting**: The setting which was changed. For instance: "*race.ghostmode"

- **oldValue**: The previous value. Please note that this value is in [JSON](mta://reference/misc/json.md). To get a normal Lua value, use [fromJSON](mta://scripting/shared/functions/fromjson.md)

- **newValue**: The new value. Also in [JSON](mta://reference/misc/json.md)

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root element](https://wiki.multitheftauto.com/index.php?search=root%20element).

## Example

```
function makeSettingsChangesVisible(setting, oldValue, newValue)
    local whatItWas = fromJSON(oldValue)
    local whatItsNow = fromJSON(newValue)
    outputDebugString("The setting "..setting.." was "..whatItWas.." and has been changed to "..whatItsNow..".") -- Making the setting change visible in debug (use /debugscript [number] to see it)
end
addEventHandler("onSettingChange", root, makeSettingsChangesVisible)
```

## See Also

### Server events

- [onBan](mta://scripting/server/events/onban.md)

- [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- [onDebugMessage](mta://scripting/server/events/ondebugmessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21914](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21914))

- [onExplosion](mta://scripting/server/events/onexplosion.md)

- onSettingChange

- [onUnban](mta://scripting/server/events/onunban.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22837](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22837):

- [onShutdown](mta://scripting/server/events/onshutdown.md)

### Event functions

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
