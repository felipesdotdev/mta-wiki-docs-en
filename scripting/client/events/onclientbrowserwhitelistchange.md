---
doc_id: "mta-wiki:8415"
title: "OnClientBrowserWhitelistChange"
source_title: "OnClientBrowserWhitelistChange"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserWhitelistChange"
revision_id: 59199
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
generated_at: "2026-07-26T16:16:17.101813+00:00"
---

# OnClientBrowserWhitelistChange

The event is triggered when the whitelist has changed. Note that this event is only triggered if the request window was confirmed by accepting.

| [[{{{image}}}\|link=\|]] | Note: Attaching the event to a webbrowser won't work. Attach it to the root element instead. |
| --- | --- |
|  |  |

## Parameters

```
table changedDomains
```

- **changedDomains:** a [table](mta://reference/misc/table.md) of changed domains.

## Source

The [root](mta://reference/misc/element-tree.md) element.

## Example

```
requestBrowserDomains({ "mtasa.com" }) -- request browser domain
showCursor(true) -- show cursor
addEventHandler("onClientBrowserWhitelistChange", root,
   function(newDomains)
     if newDomains[1] == "mtasa.com" then
       local browser = createBrowser(1280, 720, false, false) -- create browser
       loadBrowserURL(browser, "http://mtasa.com/") -- load browser url
   end
end
)
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- onClientBrowserWhitelistChange
