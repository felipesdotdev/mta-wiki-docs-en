---
doc_id: "mta-wiki:8207"
title: "GetBrowserURL"
source_title: "Cef/getBrowserURL"
source_url: "https://wiki.multitheftauto.com/wiki/Cef/getBrowserURL"
revision_id: 65741
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
generated_at: "2026-07-26T16:12:06.294656+00:00"
---

# GetBrowserURL

This function returns the URL of the specified [browser](mta://reference/misc/element-browser.md).

## Syntax

```
string getBrowserURL ( browser webBrowser )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):getURL(...)*

**Variable**: *.url*

**Counterpart**: *[loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md)*

### Required Arguments

- **webBrowser:** The browser

### Returns

Returns the web browser URL.

## Example

This example creates a command (/isyoutubeloaded) to check if the browser created have youtube loaded, if it isnt it loads youtube.

Click to collapse [-]
Client

```
-- In order to render the browser on a corner, we need to get the dimensions of the screen
local screenWidth, screenHeight = guiGetScreenSize( )

-- Let's create a new browser in remote mode
local window = guiCreateWindow( screenWidth/2, 0, screenWidth/2, screenHeight/2, "Web Browser", false )
local browser = guiCreateBrowser( 0, 28, screenWidth/2, screenHeight/2, false, false, false, window )
local theBrowser = guiGetBrowser( browser ) -- Get the browser element from gui-browser

-- Let's create a new command to check if youtube is loaded and load it if isnt
addCommandHandler ( "isyoutubeloaded",
    function ()
		if getBrowserURL(theBrowser) == "" then  -- If the browser didnt load anything yet, load youtube
			outputChatBox("Youtube isn't loaded yet, loading it now....")
			loadBrowserURL( theBrowser, "https://www.youtube.com/" )
		else -- If the browser loaded something
			outputChatBox("Youtube is loaded.")
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

- getBrowserURL

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
