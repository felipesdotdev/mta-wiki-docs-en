---
doc_id: "mta-wiki:2281"
title: "OnVehicleExplode"
source_title: "OnVehicleExplode"
source_url: "https://wiki.multitheftauto.com/wiki/OnVehicleExplode"
revision_id: 82228
language: "en"
categories: ["Server_Events", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:26.531022+00:00"
---

# OnVehicleExplode

This event is triggered when a vehicle explodes.

## Parameters

```
bool withExplosion, player player
```

- **withExplosion:** Determines whether the vehicle was blown with or without an explosion.

ADDED/UPDATED IN VERSION 1.6.0 [r22680](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22680):

- **player:** The player who sent the explosion packet.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [vehicle](mta://reference/misc/vehicle.md) that exploded.

## Cancel effect

ADDED/UPDATED IN VERSION 1.6.0 [r23281](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23281):

If this event is cancelled, the vehicle won't explode. 

## Example

**Example 1**

```
local vagosVehicle = nil

-- This will get called when the vagos vehicle explodes
function onVagosVehicleExplode ()
	outputChatBox ( "VAGOS VEHICLE DESTROYED!" )
end

-- This is called when THIS resource starts
function onThisResourceStart ()

	-- Create the vagos vehicle. A van.
	vagosVehicle = createVehicle ( 522, 0, 0, 5 )

	-- Add its explode handler. When this car explodes, onVagosVehicleExplode is called
	addEventHandler ( "onVehicleExplode", vagosVehicle, onVagosVehicleExplode )
end

--Add the resource start event
addEventHandler ( "onResourceStart", resourceRoot, onThisResourceStart )
```

**Example 2:** This will show the name of any vehicle that blew up:

```
function notifyAboutExplosion()
    -- source is the element that triggered the event and can be used in other events as well
    outputChatBox(getVehicleName(source) .. " just blew up")
end

-- by using root, it will work for any vehicle (even if it wasn't created via this resource)
addEventHandler("onVehicleExplode", root, notifyAboutExplosion)
```

## See Also

### Vehicle events

- [onTrailerAttach](mta://scripting/server/events/ontrailerattach.md)

- [onTrailerDetach](mta://scripting/server/events/ontrailerdetach.md)

- [onVehicleDamage](mta://scripting/server/events/onvehicledamage.md)

- [onVehicleEnter](mta://scripting/server/events/onvehicleenter.md)

- [onVehicleExit](mta://scripting/server/events/onvehicleexit.md)

- onVehicleExplode

- [onVehicleRespawn](mta://scripting/server/events/onvehiclerespawn.md)

- [onVehicleStartEnter](mta://scripting/server/events/onvehiclestartenter.md)

- [onVehicleStartExit](mta://scripting/server/events/onvehiclestartexit.md)

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
