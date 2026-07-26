---
doc_id: "mta-wiki:9101"
title: "ResizeBrowser"
source_title: "ResizeBrowser"
source_url: "https://wiki.multitheftauto.com/wiki/ResizeBrowser"
revision_id: 65768
language: "en"
categories: ["Client_functions", "Changes_in_1.5.3"]
generated_at: "2026-07-26T16:16:34.514340+00:00"
---

# ResizeBrowser

Allows resizing of CEF browsers at runtime.

|  | Warning: Do not use this function with onClientRender as it re-creates the underlying texture internally (which is an expensive operation). |
| --- | --- |
|  |  |

## Syntax

```
bool resizeBrowser ( browser webBrowser, float width, float height )
```

### Required Arguments

- **webBrowser:** The browser you want to resize.

- **width:** The new width of the browser.

- **height:** The new height of the browser.

### Returns

Returns *true* if the browser is resized successfully, *false* if there's something wrong.

## Example

Example for resize browser by command.

```
screenWidth, screenHeight = guiGetScreenSize()
initBrowser = guiCreateBrowser(0, 0, screenWidth, screenHeight, true, true, false)
addCommandHandler("resize",
	function ( cmd, width, height )
		local browser = guiGetBrowser(initBrowser)
		local width, height = tonumber(width), tonumber(height)
		resizeBrowser( browser, width, height )
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

- [isBrowserFocused](mta://scripting/client/functions/isbrowserfocused.md)

- [isBrowserLoading](mta://scripting/client/functions/isbrowserloading.md)

- [isBrowserRenderingPaused](mta://scripting/client/functions/isbrowserrenderingpaused.md)

- [loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md)

- [navigateBrowserBack](mta://scripting/client/functions/navigatebrowserback.md)

- [navigateBrowserForward](mta://scripting/client/functions/navigatebrowserforward.md)

- [reloadBrowserPage](mta://scripting/client/functions/reloadbrowserpage.md)

- [requestBrowserDomains](mta://scripting/client/functions/requestbrowserdomains.md)

- resizeBrowser

- [setBrowserAjaxHandler](mta://scripting/client/functions/setbrowserajaxhandler.md)

- [setBrowserProperty](mta://scripting/client/functions/setbrowserproperty.md)

- [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md)

- [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
