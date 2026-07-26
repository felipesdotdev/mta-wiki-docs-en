---
doc_id: "mta-wiki:14302"
title: "OnAccountRemove"
source_title: "OnAccountRemove"
source_url: "https://wiki.multitheftauto.com/wiki/OnAccountRemove"
revision_id: 79413
language: "en"
categories: ["Server_Events"]
---

# OnAccountRemove

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470))

This event is triggered every time an [account](mta://reference/misc/account.md) is removed

## Parameters

```
account theAccount
```

- **theAccount:** An [account](mta://reference/misc/account.md) element that was removed

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root](https://wiki.multitheftauto.com/index.php?search=root) element.

## Canceling

This event cannot be [canceled](mta://reference/misc/event-system.md).

## Example

This example prints a message every time new account is created.

```
addEventHandler('onAccountRemove', root, function(acc)
    local accName = getAccountName(acc)
    local accType = getAccountType(acc) or 'Unknown'
    iprint('An account has been removed! Type: '..accType..', name: '..accName)
end)
```

## See Also

### Server events

- [onBan](mta://scripting/server/events/onban.md)

- [onChatMessage](mta://scripting/server/events/onchatmessage.md)

- [onDebugMessage](mta://scripting/server/events/ondebugmessage.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21914](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21914))

- [onExplosion](mta://scripting/server/events/onexplosion.md)

- [onSettingChange](mta://scripting/server/events/onsettingchange.md)

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
