---
doc_id: "mta-wiki:1545"
title: "TriggerEvent"
source_title: "TriggerEvent"
source_url: "https://wiki.multitheftauto.com/wiki/TriggerEvent"
revision_id: 79034
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:17:00.974121+00:00"
---

# TriggerEvent

This function will trigger a named [event](mta://reference/misc/event.md) on a specific [element](mta://reference/misc/element.md) in the [element tree](mta://reference/misc/element-tree.md). See [event system](mta://reference/misc/event-system.md) for more information on how the event system works.

You can use the value returned from this function to determine if the event was cancelled by one of the event handlers. You should determine what your response (if any) to this should be based on the event's purpose. Generally, cancelling an event should prevent any further code being run that is dependent on whatever triggered that event. For example, if you have an *onFlagCapture* event, cancelling it would be expected to prevent the flag being able to be captured. Similarly, if you have *onPlayerKill* as an event you trigger, canceling it would either be expected to prevent the player being killed from dying or at least prevent the player from getting a score for it.

| [[{{{image}}}\|link=\|]] | Note: You should avoid triggering events on the root element unless you really need to. Doing this triggers the event on every element in the element tree, which is potentially very CPU intensive. Use as specific (i.e. low down the tree) element as you can. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: See Event Source Element for a descriptive visualization of the event system handling an event trigger. |
| --- | --- |
|  |  |

## Syntax

```
bool triggerEvent ( string eventName, element baseElement, [ var argument1, ... ] )
```

### Required Arguments

- **eventName:** The name of the event you wish to trigger

- **baseElement:** The element you wish to trigger the event on. See [event system](mta://reference/misc/event-system.md) for information on how this works.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **argument1:** The first argument that the event handler expects should be added after the *baseElement* variable.

- *NOTE:* This function can have more than one of these arguments specified, once for each argument the event handler is expecting.

### Returns

- Returns **nil** if the arguments are invalid or the event could not be found.

- Returns **true** if the event was triggered successfully, and *was not* cancelled using [cancelEvent](mta://scripting/shared/functions/cancelevent.md).

- Returns **false** if the event was triggered successfully, and *was* cancelled using [cancelEvent](mta://scripting/shared/functions/cancelevent.md).

## Example

If you define a new custom event as follows:

```
function onCustomEvent(chatMessage)
	outputChatBox(chatMessage)
end
addEvent("onCustomEvent", false) -- set to false, so this event won't be called from counter side - important security measure
addEventHandler("onCustomEvent", root, onCustomEvent)
```

You can then trigger this event later on using:

```
triggerEvent("onCustomEvent", resourceRoot, "Hello, world!")
```

## See Also

- [addEvent](mta://scripting/shared/functions/addevent.md)

- [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- [cancelEvent](mta://scripting/shared/functions/cancelevent.md)

- [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

- [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- [removeEventHandler](mta://scripting/shared/functions/removeeventhandler.md)

- triggerEvent

- [wasEventCancelled](mta://scripting/shared/functions/waseventcancelled.md)
