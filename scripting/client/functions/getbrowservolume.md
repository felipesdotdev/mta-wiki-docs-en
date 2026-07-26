---
doc_id: "mta-wiki:8451"
title: "GetBrowserVolume"
source_title: "GetBrowserVolume"
source_url: "https://wiki.multitheftauto.com/wiki/GetBrowserVolume"
revision_id: 54153
language: "en"
categories: ["Client_functions", "Changes_in_1.5.1"]
generated_at: "2026-07-26T16:15:07.870840+00:00"
---

# GetBrowserVolume

This function returns a specific [browser](mta://reference/misc/element-browser.md)'s volume.

## Syntax

```
float getBrowserVolume ( browser webBrowser )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):getVolume(...)*

**Counterpart**: *[setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)*

### Required Arguments

- **webBrowser:** A browser element

### Returns

Returns a specific [browser](mta://reference/misc/element-browser.md)'s volume, or *false* if the browser element passed to the function is invalid.

## Example

Creates a browser in which the volume can be controlled by pressing the page-up & page-down keys

```
--In order to render the browser on the full screen, we need to know the dimensions.
local screenWidth, screenHeight = guiGetScreenSize()
 
--Let's create a new browser in remote mode.
local webBrowser = createBrowser(screenWidth, screenHeight, false, false)

-- How much we increase/decrease the volume by each time
local volumeStep = 0.1 

-- The min/max value for the browser volume. Change these if you like, but note that the minimum value is 0 and the maximum value is 1.
local MIN_VOLUME = 0
local MAX_VOLUME = 1
 
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

-- Now we create a function attached to an onClientKey event handler to catch user input.
-- Here we can utilize the getBrowserVolume function to lower or increase the volume of the browser based on the clients input
function handleVolumeKeys(button, press)
    if (press) then -- Is key pressed?
        if (button == "pgup") then
		local volume = getBrowserVolume(webBrowser) + volumeStep -- Get the current browser volume and add our volume step
		if (volume) > MAX_VOLUME then return end -- Check if the current volume is bigger than max value
		setBrowserVolume(webBrowser, volume) -- Set the browser volume			
	elseif (button == "pgdn") then -- Same as previous condition except we subtract the volume step and make sure the volume value doesn't fall below minimum.
		local volume = getBrowserVolume(webBrowser) - volumeStep
		if (volume) < MIN_VOLUME then return end
		setBrowserVolume(webBrowser, volume) 		
	end
    end
end
addEventHandler("onClientKey", root, handleVolumeKeys)
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

- [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
