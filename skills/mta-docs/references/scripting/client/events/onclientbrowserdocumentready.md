---
doc_id: "mta-wiki:8298"
title: "OnClientBrowserDocumentReady"
source_title: "OnClientBrowserDocumentReady"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserDocumentReady"
revision_id: 50312
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
---

# OnClientBrowserDocumentReady

This event is executed after the web page has been loaded successfully.

## Parameters

```
string url
```

- **url:** the url of the web page loaded.

## Source

The [browser](mta://reference/misc/element-browser.md) element.

## Example

```
addEventHandler ( "onClientBrowserDocumentReady" , root , 
	function ( url ) 
		outputChatBox ( "The page '"  .. url ..  "' has been successfully loaded.") 
	end 
)
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- onClientBrowserDocumentReady

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
