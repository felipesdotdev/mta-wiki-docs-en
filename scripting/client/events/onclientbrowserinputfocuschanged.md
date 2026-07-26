---
doc_id: "mta-wiki:8416"
title: "OnClientBrowserInputFocusChanged"
source_title: "OnClientBrowserInputFocusChanged"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserInputFocusChanged"
revision_id: 82062
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
generated_at: "2026-07-26T16:16:17.014043+00:00"
---

# OnClientBrowserInputFocusChanged

This event is triggered when the input focus inside a browser has changed.

## Parameters

```
bool gainedFocus
```

- **gainedFocus**: *true* if an input field has been focused, *false* if it has lost focus.

## Source

The [browser](mta://reference/misc/element-browser.md) element.

## Example

```
addEventHandler("onClientBrowserInputFocusChanged", root, function(gainedFocus)
  iprint(source, "gainedFocus:", gainedFocus)
end)
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- onClientBrowserInputFocusChanged

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
