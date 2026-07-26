---
doc_id: "mta-wiki:1621"
title: "Element data"
source_title: "Element data"
source_url: "https://wiki.multitheftauto.com/wiki/Element_data"
revision_id: 82225
language: "en"
categories: ["Scripting_Concepts"]
---

# Element data

Each [element](mta://reference/misc/element.md) that is loaded is able to have element data values attached to it. These are values that can be accessed using a keyword string and directly correspond to the element's attributes in the map file, unless changed via scripting. Element data is a good (but expensive) way to store distributed information you want associated with an element, for example you could use it to associate a score with a player, or a team with a vehicle.

Element data is synchronized by default between the server and the client (you can disable it via fourth argument in [setElementData](mta://scripting/shared/functions/setelementdata.md). Setting data from any of the two sides will force an update in the other, triggering the corresponding element data change events. This is very useful, as it provides a simple way to keep element properties synced without having to set special events to do it manually.  This also means that excessive use of element data to store variables that are not required by both server and client becomes a waste of bandwidth.

Since not all data types can be packetized to be transferred, there are some restrictions. The types that cannot be stored as element data are *non-element userdata* (see [MTA Classes](mta://reference/misc/mta-classes.md)), *functions* and *threads*. Also, you may not send tables which contain one or more values of any of these types.

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22790](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22790))

Element data is not protected from client changes by default. You **SHOULD** enable [elementdata_whitelisted](mta://reference/misc/server-mtaserver-conf.md) in **mtaserver.conf** to protect your server simple cheats. Use the **clientChangesPolicy** parameter in [setElementData](mta://scripting/shared/functions/setelementdata.md) to allow some changes.

## Relevant functions

- [setElementData](mta://scripting/shared/functions/setelementdata.md): sets an element data value.

- [getElementData](mta://scripting/shared/functions/getelementdata.md): retrieves an element data value.

## Relevant events

- [onElementDataChange](mta://scripting/server/events/onelementdatachange.md): triggered on the server after element data is changed.

- [onPlayerChangesProtectedData](mta://scripting/server/events/onplayerchangesprotecteddata.md): triggered on the server after the client attempts to change protected element data.

- [onClientElementDataChange](mta://scripting/client/events/onclientelementdatachange.md): triggered on the client after element data is changed.
