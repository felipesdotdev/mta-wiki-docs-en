---
doc_id: "mta-wiki:8345"
title: "OnClientBrowserCreated"
source_title: "OnClientBrowserCreated"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserCreated"
revision_id: 67013
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
generated_at: "2026-07-26T16:16:16.981964+00:00"
---

# OnClientBrowserCreated

This event is triggered when the CEF browser instance has been created. If you want to load a specific website right after creating the browser (using [createBrowser](mta://scripting/client/functions/createbrowser.md) or [guiCreateBrowser](mta://scripting/client/functions/guicreatebrowser.md)), this event will be the convenient place.

| [[{{{image}}}\|link=\|]] | Note: Calling loadBrowserURL right after createBrowser will not work normally due to the nature of the asynchronous browser interface. |
| --- | --- |
|  |  |

## Parameters

No parameters.

## Source

The [browser](mta://reference/misc/element-browser.md) element.

## Example

```
addEventHandler("onClientBrowserCreated", resourceRoot,
function ()
    -- when the browser is loaded
    loadBrowserURL(source, "http://mtasa.com") -- load MTA:SA site
end)
```

## See Also

- onClientBrowserCreated

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
