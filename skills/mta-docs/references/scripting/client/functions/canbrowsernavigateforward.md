---
doc_id: "mta-wiki:9254"
title: "CanBrowserNavigateForward"
source_title: "CanBrowserNavigateForward"
source_url: "https://wiki.multitheftauto.com/wiki/CanBrowserNavigateForward"
revision_id: 69198
language: "en"
categories: ["Client_functions", "Changes_in_1.5.3"]
---

# CanBrowserNavigateForward

This function checks if the browser can go to the next page.

## Syntax

```
bool canBrowserNavigateForward( browser webBrowser )
```

### Required Arguments

- **webBrowser:** The browser you want check for a next page.

### Returns

Returns *true* if the browser can go to the next page, *false* otherwise.

## Example

Click to collapse [-]
Client

This example creates a browser that can return to the last and previous pages and can also be refreshed:

```
window = guiCreateWindow(126, 122, 848, 674, "browser", false)
guiWindowSetSizable(window, false)
navigateBackBtn = guiCreateButton(10, 19, 39, 36, "<", false, window)
navigateForwardBtn = guiCreateButton(98, 19, 39, 36, ">", false, window)
reloadBtn = guiCreateButton(49, 19, 49, 36, "reload", false, window)
addressBar =  guiCreateEdit(137, 19, 701, 36, "", false, window)
guiSetEnabled(addressBar,false)
webBrowser = guiCreateBrowser(10, 55, 828, 609, false, false, false, window)
local theBrowser = guiGetBrowser(webBrowser) 

-- Load our page on browser creation.
addEventHandler("onClientBrowserCreated", theBrowser, 
    function()
	showCursor(true)
        loadBrowserURL(source, "https://forum.mtasa.com/")
    end
)

addEventHandler( "onClientBrowserDocumentReady", theBrowser, function( url )
guiSetText( addressBar, getBrowserURL( theBrowser ) )
end )

-- This part handles the GUI navigation buttons for the browser.
addEventHandler( "onClientGUIClick", resourceRoot, function ( )
    if source == navigateBackBtn then
	if canBrowserNavigateBack(theBrowser) ~= true then return end -- This checks to see if the browser can navigate to the back
        navigateBrowserBack(theBrowser)
    elseif source == navigateForwardBtn then -- This checks to see if the browser can navigate to the forward
	if canBrowserNavigateForward(theBrowser) ~= true then return end
        navigateBrowserForward(theBrowser)
    elseif source == reloadBtn then
        reloadBrowserPage(theBrowser)
    end
end )
```

## See Also

- [canBrowserNavigateBack](mta://scripting/client/functions/canbrowsernavigateback.md)

- canBrowserNavigateForward

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
