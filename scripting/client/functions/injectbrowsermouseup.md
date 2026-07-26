---
doc_id: "mta-wiki:8019"
title: "InjectBrowserMouseUp"
source_title: "InjectBrowserMouseUp"
source_url: "https://wiki.multitheftauto.com/wiki/InjectBrowserMouseUp"
revision_id: 65747
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
generated_at: "2026-07-26T16:15:52.909235+00:00"
---

# InjectBrowserMouseUp

This function injects a mouse click (state: up).

## Syntax

```
bool injectBrowserMouseUp ( browser webBrowser, string mouseButton )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):injectMouseUp(...)*

### Required arguments

- **webBrowser:** The web browser

- **mouseButton:** The mouse button (Possible values: *left*, *middle*, *right*)

### Returns

Returns *true* if the click was successfully injected, *false* otherwise.

## Example

```
addEventHandler("onClientClick", root,
	function(button, state)
		if state == "down" then
			injectBrowserMouseDown(browser, button)
		else
			injectBrowserMouseUp(browser, button)
		end
	end
)
```

## See also

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

- injectBrowserMouseUp

- [injectBrowserMouseWheel](mta://scripting/client/functions/injectbrowsermousewheel.md)

- [isBrowserDomainBlocked](mta://scripting/client/functions/isbrowserdomainblocked.md)

- [isBrowserFocused](mta://scripting/client/functions/isbrowserfocused.md)

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
