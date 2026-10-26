---
doc_id: "mta-wiki:14690"
title: "OnAccountNameChange"
source_title: "OnAccountNameChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnAccountNameChange"
revision_id: 82917
language: "en"
categories: ["Server_Events"]
---

# OnAccountNameChange

ADDED/UPDATED IN VERSION 1.7.0 [r25351](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=25351):

This event is triggered before an [account](mta://reference/misc/account.md) name is changed using [setAccountName](mta://scripting/server/functions/setaccountname.md).

## Parameters

```lua
account theAccount, string previousName, string newName
```

- **theAccount:** The [account](mta://reference/misc/account.md) being renamed.

- **previousName:** The account's current name.

- **newName:** The proposed new account name.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root](https://wiki.multitheftauto.com/wiki/Root) element.

## Canceling

If this event is [canceled](mta://reference/misc/event-system.md), the account name will not change and [setAccountName](mta://scripting/server/functions/setaccountname.md) will return false.

## Example

This example prevents accounts from being renamed to names starting with "admin", regardless of capitalization.

```lua
addEventHandler("onAccountNameChange", root, function(theAccount, previousName, newName)
    if newName:lower():sub(1, 5) == "admin" then
        cancelEvent()
        outputServerLog("Blocked account rename from " .. previousName .. " to " .. newName)
    end
end)
```

## Note

The event runs before the name is changed, so [getAccountName](mta://scripting/server/functions/getaccountname.md) still returns the previous name inside the handler.

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
