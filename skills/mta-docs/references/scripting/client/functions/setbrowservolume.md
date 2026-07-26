---
doc_id: "mta-wiki:8042"
title: "SetBrowserVolume"
source_title: "SetBrowserVolume"
source_url: "https://wiki.multitheftauto.com/wiki/SetBrowserVolume"
revision_id: 65777
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
---

# SetBrowserVolume

This function sets either a specific [browser](mta://reference/misc/element-browser.md)'s volume, or the overall volume for browsers.

## Syntax

```
bool setBrowserVolume ( [browser webBrowser], float volume )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):setVolume(...)*

**Variable**: *.volume*

**Counterpart**: *[getBrowserVolume](mta://scripting/client/functions/getbrowservolume.md)*

### Required Arguments

- **volume:** A [floating](mta://reference/misc/float.md) point number representing the desired volume level. Range is from **0.0** to **1.0**

### Optional Arguments

- **webBrowser:** A browser element

## Example

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

addCommandHandler ("volume", -- Add command named 'volume'
  function (command, value)
    if tonumber (value) then -- checking if the value is a number
      setBrowserVolume (webBrowser, value) -- setting the volume value
    else -- if there is no value
      outputChatBox ("You must enter a value.")
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

- setBrowserVolume

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
