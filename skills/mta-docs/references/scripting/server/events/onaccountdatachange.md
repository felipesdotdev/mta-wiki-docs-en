---
doc_id: "mta-wiki:5798"
title: "OnAccountDataChange"
source_title: "OnAccountDataChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnAccountDataChange"
revision_id: 59459
language: "en"
categories: ["Server_Events"]
---

# OnAccountDataChange

This event is triggered when an accounts data changes through [setAccountData](mta://scripting/server/functions/setaccountdata.md).

## Parameters

```
account theAccount, string theKey, string theValue
```

- **theAccount**: the [account](mta://reference/misc/account.md) that had data changed.

- **theKey**: the [string](mta://reference/misc/string.md) key that is being changed.

- **theValue**: the value it is changing to.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [root](https://wiki.multitheftauto.com/index.php?search=root) element.

## Example

This examples prevents the key of "level" being added or changed on every account.

```
function preventLevelChange(account, key, value)
    if (key == "level") then
        cancelEvent()
    end
end
addEventHandler("onAccountDataChange", root, preventLevelChange)
```

This examples logs every single account data change to server log.

```
function preventLevelChange(account, key, value)
    if (wasEventCancelled()) then return end -- If the data change was aborted don't log it.
    outputServerLog(getAccountName(account) .. " key: " .. key .. " changed to: " .. tostring(value))
end
addEventHandler("onAccountDataChange", root, preventLevelChange)
```

## See Also

### Account events

- onAccountDataChange

ADDED/UPDATED IN VERSION 1.6.0 [r22470](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22470):

- [onAccountCreate](mta://scripting/server/events/onaccountcreate.md)

- [onAccountRemove](mta://scripting/server/events/onaccountremove.md)

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
