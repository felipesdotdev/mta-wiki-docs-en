---
doc_id: "mta-wiki:10804"
title: "OnClientBrowserTooltip"
source_title: "OnClientBrowserTooltip"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserTooltip"
revision_id: 59201
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
---

# OnClientBrowserTooltip

The event is triggered when the user hovers a tooltip.

## Parameters

```
string text
```

- **text:** [string](mta://reference/misc/string.md) containing the tooltip text. Empty string if user is not longer hovering.

## Source

The [webbrowser](https://wiki.multitheftauto.com/index.php?search=webbrowser) element.

## Example

If the user hovers the Google search input field 'Tooltip-Text: Search' will be printed in the chatbox.

```
local browser = guiCreateBrowser(0, 0, 800, 600, false, false, false)
local theBrowser = guiGetBrowser(browser)
showCursor(true)

addEventHandler( "onClientBrowserCreated", theBrowser, function()
  loadBrowserURL(source, "https://www.google.com/?ncr&hl=en")
end)

addEventHandler("onClientBrowserTooltip", root, function(text)
  if (text ~= "") then
    outputChatBox("Tooltip-Text: "..text)
  else
    outputChatBox("You are not longer hovering a tooltip")
  end
end)
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

- onClientBrowserTooltip

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
