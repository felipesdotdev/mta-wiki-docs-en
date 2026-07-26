---
doc_id: "mta-wiki:8125"
title: "OnClientBrowserCursorChange"
source_title: "OnClientBrowserCursorChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserCursorChange"
revision_id: 82083
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
---

# OnClientBrowserCursorChange

This event is triggered when the cursor changes within a browser window.

| [[{{{image}}}\|link=\|]] | Note: Cursor IDs: CT_POINTER 0 CT_CROSS 1 CT_HAND 2 CT_IBEAM 3 CT_WAIT 4 CT_HELP 5 CT_EASTRESIZE 6 CT_NORTHRESIZE 7 CT_NORTHEASTRESIZE 8 CT_NORTHWESTRESIZE 9 CT_SOUTHRESIZE 10 CT_SOUTHEASTRESIZE 11 CT_SOUTHWESTRESIZE 12 CT_WESTRESIZE 13 CT_NORTHSOUTHRESIZE 14 CT_EASTWESTRESIZE 15 CT_NORTHEASTSOUTHWESTRESIZE 16 CT_NORTHWESTSOUTHEASTRESIZE 17 CT_COLUMNRESIZE 18 CT_ROWRESIZE 19 CT_MIDDLEPANNING 20 CT_EASTPANNING 21 CT_NORTHPANNING 22 CT_NORTHEASTPANNING 23 CT_NORTHWESTPANNING 24 CT_SOUTHPANNING 25 CT_SOUTHEASTPANNING 26 CT_SOUTHWESTPANNING 27 CT_WESTPANNING 28 CT_MOVE 29 CT_VERTICALTEXT 30 CT_CELL 31 CT_CONTEXTMENU 32 CT_ALIAS 33 CT_PROGRESS 34 CT_NODROP 35 CT_COPY 36 CT_NONE 37 CT_NOTALLOWED 38 CT_ZOOMIN 39 CT_ZOOMOUT 40 CT_GRAB 41 CT_GRABBING 42 CT_CUSTOM 43 |
| --- | --- |
|  |  |

## Parameters

```
int cursorId
```

- **cursorId:** The new cursor ID.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the browser element the cursor change occured in.

## Example

```
TODO
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- onClientBrowserCursorChange

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
