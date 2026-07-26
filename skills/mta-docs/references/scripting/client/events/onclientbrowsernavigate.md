---
doc_id: "mta-wiki:8299"
title: "OnClientBrowserNavigate"
source_title: "OnClientBrowserNavigate"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserNavigate"
revision_id: 73894
language: "en"
categories: ["Client_events", "Changes_in_1.5", "Needs_Example"]
---

# OnClientBrowserNavigate

The event is executed when the browser loads a new page. Do not use [loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md) in the attached function.

## Parameters

```
string targetURL, bool isBlocked, bool isMainFrame
```

- **targetURL:** the page the browser loaded.

- **isBlocked:** if the [browser](https://wiki.multitheftauto.com/index.php?search=browser) was created with **isLocal** set to **true**, and the browser tried to load a remote page, this would be set to **true** (and vice-versa).

- **isMainFrame:** a [boolean](mta://reference/misc/boolean.md) representing whether the entire page (main frame) was loaded or an *<iframe>* inside the page was loaded.

## Source

The [browser](mta://reference/misc/element-browser.md) element.

## Example

|  | Script Example Missing Event OnClientBrowserNavigate needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

```
-- TODO
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- onClientBrowserNavigate

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
