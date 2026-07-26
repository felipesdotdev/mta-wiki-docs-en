---
doc_id: "mta-wiki:10805"
title: "OnClientBrowserLoadingStart"
source_title: "OnClientBrowserLoadingStart"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserLoadingStart"
revision_id: 82035
language: "en"
categories: ["Client_events", "Changes_in_1.5", "Changes_in_1.6"]
---

# OnClientBrowserLoadingStart

The event is triggered when a [webbrowser](https://wiki.multitheftauto.com/index.php?search=webbrowser) starts loading a page.

## Parameters

```
string URL, boolean isMainFrame
```

- **URL:** [string](mta://reference/misc/string.md) containing the URL that will be loaded.

- **isMainFrame:** a [boolean](mta://reference/misc/boolean.md) representing whether the entire page (main frame) was loaded or an *<iframe>* inside the page was loaded. **true**: If the URL is loaded in the main frame. **false**: If the URL is loaded in a *<iframe>*.

## Source

The [webbrowser](https://wiki.multitheftauto.com/index.php?search=webbrowser) element.

## Example

```
local browser = guiCreateBrowser(0, 0, 800, 600, false, false, false)
local theBrowser = guiGetBrowser(browser)
showCursor(true)

addEventHandler("onClientBrowserLoadingStart", theBrowser, function(url, isMainFrame)
  if (isMainFrame) then
    outputChatBox("Loading "..url.." in the main frame...")
  else
    outputChatBox("Loading "..url.." in a iframe...")
  end
end)

addEventHandler("onClientBrowserCreated", theBrowser, function()
  loadBrowserURL(source, "https://www.w3schools.com/html/html_iframe.asp")
end)
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- onClientBrowserLoadingStart

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
