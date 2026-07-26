---
doc_id: "mta-wiki:8417"
title: "IsBrowserFocused"
source_title: "IsBrowserFocused"
source_url: "https://wiki.multitheftauto.com/wiki/IsBrowserFocused"
revision_id: 65753
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:53.464639+00:00"
---

# IsBrowserFocused

This function checks if a browser is focused.

## Syntax

```
bool isBrowserFocused ( browser webBrowser )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):isFocused(...)*

### Required arguments

- **webBrowser:** The browser

### Returns

Returns *true* if the browser is focused, *false* otherwise and *nil* if invalid arguments were passed.

## Example

This example creates a browser. If you press left control it will output to chatbox if the browser is focused or not.

Click to collapse [-]
Example

```
local theBrowser = guiCreateBrowser ( 150, 150, 1280, 720, true, false, false)
addEventHandler("onClientKey", localPlayer,
	function(button, state)  -- adds the event handler.
		if button == "lctrl" and state = "down" then -- if the pressed key is lctrl and the state is down then we will check is the browser focused or not. 
			if isBrowserFocused(theBrowser) then
				outputChatbox("the browser is focused.") -- if the browser is focused then we will write this to chatbox.
			else
				outputChatbox("the browser is not focused.")-- if the browser is not focused then we will write this to chatbox.
			end
 		end
	end
)
```

## See Also

- [canBrowserNavigateBack](mta://scripting/client/functions/canbrowsernavigateback.md)

- [canBrowserNavigateForward](mta://scripting/client/functions/canbrowsernavigateforward.md)

- [createBrowser](mta://scripting/client/functions/createbrowser.md)

- [executeBrowserJavascript](mta://scripting/client/functions/executebrowserjavascript.md)

- [focusBrowser](mta://scripting/client/functions/focusbrowser.md)

- [getBrowserProperty](mta://scripting/client/functions/getbrowserproperty.md)

- [getBrowserSettings](mta://scripting/client/functions/getbrowsersettings.md)

- [getBrowserSource](mta://scripting/client/functions/getbrowsersource.md)

- [getBrowserTitle](mta://scripting/client/functions/getbrowsertitle.md)

- [getBrowserURL](mta://scripting/client/functions/getbrowserurl.md)

- [injectBrowserMouseDown](mta://scripting/client/functions/injectbrowsermousedown.md)

- [injectBrowserMouseMove](mta://scripting/client/functions/injectbrowsermousemove.md)

- [injectBrowserMouseUp](mta://scripting/client/functions/injectbrowsermouseup.md)

- [injectBrowserMouseWheel](mta://scripting/client/functions/injectbrowsermousewheel.md)

- [isBrowserDomainBlocked](mta://scripting/client/functions/isbrowserdomainblocked.md)

- isBrowserFocused

- [isBrowserLoading](mta://scripting/client/functions/isbrowserloading.md)

- [isBrowserRenderingPaused](mta://scripting/client/functions/isbrowserrenderingpaused.md)

- [loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md)

- [navigateBrowserBack](mta://scripting/client/functions/navigatebrowserback.md)

- [navigateBrowserForward](mta://scripting/client/functions/navigatebrowserforward.md)

- [reloadBrowserPage](mta://scripting/client/functions/reloadbrowserpage.md)

- [requestBrowserDomains](mta://scripting/client/functions/requestbrowserdomains.md)

- [resizeBrowser](mta://scripting/client/functions/resizebrowser.md)

- [setBrowserAjaxHandler](mta://scripting/client/functions/setbrowserajaxhandler.md)

- [setBrowserProperty](mta://scripting/client/functions/setbrowserproperty.md)

- [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md)

- [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
