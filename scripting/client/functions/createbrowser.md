---
doc_id: "mta-wiki:8012"
title: "CreateBrowser"
source_title: "CreateBrowser"
source_url: "https://wiki.multitheftauto.com/wiki/CreateBrowser"
revision_id: 82133
language: "en"
categories: ["Client_functions", "Changes_in_1.5", "Changes_in_1.6"]
generated_at: "2026-07-26T16:12:03.484872+00:00"
---

# CreateBrowser

This function creates a new web [browser](mta://reference/misc/element-browser.md) element.

| [[{{{image}}}\|link=\|]] | Note: You can also enable CEF development tools using toggleBrowserDevTools |
| --- | --- |
|  |  |

## Syntax

```
element createBrowser ( int width, int height, bool isLocal [, bool transparent = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Browser](mta://reference/misc/element-browser.md)(...)*

### Required Arguments

- **width:** The browser's native width. This should be greater than or equal to 1.

- **height:** The browser's native height. This should be greater than or equal to 1.

- **isLocal:**  Sets whether the browser can only show local content or content from the internet (see examples for more information)

Invalid sizes will be a hard error.

### Optional Arguments

- **transparent:** *true* if you want the browser transparent, *false* for opaque.

### Returns

Returns a [texture](mta://reference/misc/texture.md) of the [browser](mta://reference/misc/browser.md) if it was created successfully, *false* otherwise. Returns also *false*, if the user disabled remote pages and *isLocal* was set to *false*.

## Examples

|  | Warning: The scheme for local files has changed. Please read Local Scheme Handler for details. |
| --- | --- |
|  |  |

**Local Example**: This example shows you how to create a fullscreen web browser (showing a local html file) without input-handling.

```
--In order to render the browser on the full screen, we need to know the dimensions.
local screenWidth, screenHeight = guiGetScreenSize()

--Let's create a new browser in local mode. We will not be able to load an external URL.
local webBrowser = createBrowser(screenWidth, screenHeight, true, false)
	
--This is the function to render the browser.
function webBrowserRender()
	--Render the browser on the full size of the screen.
	dxDrawImage(0, 0, screenWidth, screenHeight, webBrowser, 0, 0, 0, tocolor(255,255,255,255), true)
end

--The event onClientBrowserCreated will be triggered, after the browser has been initialized.
--After this event has been triggered, we will be able to load our URL and start drawing.
addEventHandler("onClientBrowserCreated", webBrowser, 
	function()
		--After the browser has been initialized, we can load our file.
		loadBrowserURL(webBrowser, "http://mta/local/html/site.html")
		--Now we can start to render the browser.
		addEventHandler("onClientRender", root, webBrowserRender)
	end
)
```

**Remote Example**: This example shows you how to create a fullscreen web browser (showing youtube.com) without input-handling.  

Remember, that youtube.com is on the global whitelist. If you want to load a domain/page that is not on the global whitelist, you have to request it with [requestBrowserDomains](mta://scripting/client/functions/requestbrowserdomains.md).

```
--In order to render the browser on the full screen, we need to know the dimensions.
local screenWidth, screenHeight = guiGetScreenSize()

--Let's create a new browser in remote mode.
local webBrowser = createBrowser(screenWidth, screenHeight, false, false)
	
--Function to render the browser.
function webBrowserRender()
	--Render the browser on the full size of the screen.
	dxDrawImage(0, 0, screenWidth, screenHeight, webBrowser, 0, 0, 0, tocolor(255,255,255,255), true)
end

--The event onClientBrowserCreated will be triggered, after the browser has been initialized.
--After this event has been triggered, we will be able to load our URL and start drawing.
addEventHandler("onClientBrowserCreated", webBrowser, 
	function()
		--After the browser has been initialized, we can load www.youtube.com
		loadBrowserURL(webBrowser, "http://www.youtube.com")
		--Now we can start to render the browser.
		addEventHandler("onClientRender", root, webBrowserRender)
	end
)
```

## See Also

- [canBrowserNavigateBack](mta://scripting/client/functions/canbrowsernavigateback.md)

- [canBrowserNavigateForward](mta://scripting/client/functions/canbrowsernavigateforward.md)

- createBrowser

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

- [resizeBrowser](mta://scripting/client/functions/resizebrowser.md)

- [setBrowserAjaxHandler](mta://scripting/client/functions/setbrowserajaxhandler.md)

- [setBrowserProperty](mta://scripting/client/functions/setbrowserproperty.md)

- [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md)

- [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
