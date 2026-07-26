---
doc_id: "mta-wiki:8402"
title: "SetBrowserAjaxHandler"
source_title: "SetBrowserAjaxHandler"
source_url: "https://wiki.multitheftauto.com/wiki/SetBrowserAjaxHandler"
revision_id: 65771
language: "en"
categories: ["Client_functions", "Changes_in_1.5.1"]
---

# SetBrowserAjaxHandler

This function provides a requestable ajax resource for Lua/Javascript communication for a [browser](mta://reference/misc/element-browser.md).

## Syntax

```
bool setBrowserAjaxHandler ( browser webBrowser, string url [, function handler] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):setAjaxHandler(...)*

### Required Arguments

- **webBrowser:** The web browser which will execute the Javascript code

- **url:** The URL endpoint to handle

| [[\|link=\|]] | Warning: Do not use the same path as an existing file as url parameter. Ajax handlers have a higher priority than regular files, which will lead to inaccesibility of the original file if an ajax handler is attached to the same path. |
| --- | --- |
|  |  |

### Optional Arguments

- **handler:** The function to call if the webBrowser attempts to open the ajax endpoint. If this parameter is nil or omitted, the ajax handler for the url will be deleted.

### Additional Information

The handling function (if given), will be called with two tables, representing GET and POST parameters. The handling function may return a string which will be provided to the browser as file content.

## Example

This example will output all GET Parameters as well the number of requests made to the ajax endpoint.

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

local counter = 0
setBrowserAjaxHandler(webBrowser, "ajax.html",
	function(get, post)
		counter = counter+1
		local output = string.format("<pre>You have requested this page %d times.\n", counter)
		-- List Parameters
		local getParameters = "Get Parameters: \n"
		for k, v in pairs(get) do 
			getParameters = getParameters..string.format("[%s] = %s\n", k, v)
		end 
		
		output = output..getParameters.."</pre>"
		return output
	end
);
 
--The event onClientBrowserCreated will be triggered, after the browser has been initialized.
--After this event has been triggered, we will be able to load our URL and start drawing.
addEventHandler("onClientBrowserCreated", webBrowser, 
	function()
		--After the browser has been initialized, we can load our file.
		loadBrowserURL(webBrowser, "http://mta/local/ajax.html?hello=world")
		--Now we can start to render the browser.
		addEventHandler("onClientRender", root, webBrowserRender)
	end
)
```

### Returns

Returns *true* if the ajax handler could be created/removed.

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

- [resizeBrowser](mta://scripting/client/functions/resizebrowser.md)

- setBrowserAjaxHandler

- [setBrowserProperty](mta://scripting/client/functions/setbrowserproperty.md)

- [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md)

- [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
