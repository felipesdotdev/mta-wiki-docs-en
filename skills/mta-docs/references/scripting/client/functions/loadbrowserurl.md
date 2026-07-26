---
doc_id: "mta-wiki:8015"
title: "LoadBrowserURL"
source_title: "LoadBrowserURL"
source_url: "https://wiki.multitheftauto.com/wiki/LoadBrowserURL"
revision_id: 68079
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
---

# LoadBrowserURL

This function loads the specified URL.

| [[{{{image}}}\|link=\|]] | Note: You should use requestBrowserDomains first to request permission to load the url on the client. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Calling loadBrowserURL right after createBrowser will not work normally due to the nature of the asynchronous browser interface. Refer to onClientBrowserCreated for more information. |
| --- | --- |
|  |  |

## Syntax

```
bool loadBrowserURL ( browser webBrowser, string url [, string postData = "", bool urlEncoded = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):loadURL(...)*

**Variable**: *.url*

**Counterpart**: *[getBrowserURL](mta://scripting/client/functions/getbrowserurl.md)*

### Required arguments

- **webBrowser:** The [browser](mta://reference/misc/element-browser.md) element which will load the URL

- **url:** The url you want to load. It can either contain a remote website ("http://" prefix) or a website stored within a local resource ("[http://mta/local/gui.html](http://mta/local/gui.html)" for example, see [Local Scheme Handler](mta://reference/misc/local-scheme-handler.md) for details).

### Optional Arguments

- **postData:** The post data passed to the website. Its content type can be any type (e.g. JSON) if urlEncoded is set to *false*

- **urlEncoded:** If set to *true*, it will be available f.e. in PHP's $_POST variable (the content type is: *application/x-www-form-urlencoded*)

### Returns

Returns *true* if the URL was successfully loaded.

## Example

```
-- In order to render the browser on the full screen, we need to know the dimensions.
local screenWidth, screenHeight = guiGetScreenSize()

-- Let's create a new browser in local mode. We will not be able to load an external URL.
local webBrowser = createBrowser(screenWidth, screenHeight, false, false)
	
-- This is the function to render the browser.
function webBrowserRender()
	-- Render the browser on the full size of the screen.
	dxDrawImage(0, 0, screenWidth, screenHeight, webBrowser, 0, 0, 0, tocolor(255,255,255,255), true)
end

-- The event onClientBrowserCreated will be triggered, after the browser has been initialized.
-- After this event has been triggered, we will be able to load our URL and start drawing.
addEventHandler("onClientBrowserCreated", webBrowser, 
	function()
		-- After the browser has been initialized, we can load our website.
		loadBrowserURL(webBrowser, "https://www.youtube.com/")

		-- Now we can start to render the browser.
		addEventHandler("onClientRender", root, webBrowserRender)
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

- [injectBrowserMouseUp](mta://scripting/client/functions/injectbrowsermouseup.md)

- [injectBrowserMouseWheel](mta://scripting/client/functions/injectbrowsermousewheel.md)

- [isBrowserDomainBlocked](mta://scripting/client/functions/isbrowserdomainblocked.md)

- [isBrowserFocused](mta://scripting/client/functions/isbrowserfocused.md)

- [isBrowserLoading](mta://scripting/client/functions/isbrowserloading.md)

- [isBrowserRenderingPaused](mta://scripting/client/functions/isbrowserrenderingpaused.md)

- loadBrowserURL

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
