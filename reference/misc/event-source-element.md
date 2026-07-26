---
doc_id: "mta-wiki:8306"
title: "Event Source Element"
source_title: "Event Source Element"
source_url: "https://wiki.multitheftauto.com/wiki/Event_Source_Element"
revision_id: 45083
language: "en"
categories: []
generated_at: "2026-07-26T16:14:59.755076+00:00"
---

# Event Source Element

How it works

Triggering an [event](mta://reference/misc/event.md) on an [element](mta://reference/misc/element.md), also triggers the event on its parents (up the [element tree](mta://reference/misc/element-tree.md)) and its children (down the [element tree](mta://reference/misc/element-tree.md))

| Example |  | Handlers which will get triggered |
| --- | --- | --- |
| triggerEvent( "eventName", root) |  | addEventHandler( "eventName", root ) addEventHandler( "eventName", resourceRoot ) *In any resource* addEventHandler( "eventName", anyPlayerElement ) addEventHandler( "eventName", anyVehicleElement ) source is root |
| triggerEvent( "eventName", myPlayerElement ) |  | addEventHandler( "eventName", root ) addEventHandler( "eventName", myPlayerElement ) source is myPlayerElement |
| triggerEvent( "eventName", resourceRoot) |  | addEventHandler( "eventName", root ) addEventHandler( "eventName", resourceRoot ) *Only in same resource* addEventHandler( "eventName", aVehicleElement ) source is resourceRoot of the calling resource |
| triggerEvent( "eventName", myVehicleElement) |  | addEventHandler( "eventName", root ) addEventHandler( "eventName", resourceRoot ) *Only in resource vehicle was created in* addEventHandler( "eventName", myVehicleElement ) source is myVehicleElement |
