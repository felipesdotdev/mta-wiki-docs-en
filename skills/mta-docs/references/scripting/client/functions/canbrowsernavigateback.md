---
doc_id: "mta-wiki:9253"
title: "CanBrowserNavigateBack"
source_title: "CanBrowserNavigateBack"
source_url: "https://wiki.multitheftauto.com/wiki/CanBrowserNavigateBack"
revision_id: 69194
language: "en"
categories: ["Client_functions", "Changes_in_1.5.3"]
---

# CanBrowserNavigateBack

This function checks if the browser can return to the previous page.

## Syntax

```
bool canBrowserNavigateBack( browser webBrowser )
```

### Required Arguments

- **webBrowser:** The browser you want to check for a previous page.

### Returns

Returns *true* if the browser can navigate back, *false* otherwise.

## Example

Click to collapse [-]
Example

This example creates a browser that can return to the last and previous pages and can also be refreshed:

```
window = guiCreateWindow(126, 122, 848, 674, "Firechrome", false)
guiWindowSetSizable(window, false)

navigateBackBtn = guiCreateButton(10, 19, 39, 36, "<", false, window)
navigateForwardBtn = guiCreateButton(98, 19, 39, 36, ">", false, window)
addressBar =  guiCreateEdit(137, 19, 701, 36, "", false, window)
guiSetEnabled( addressBar, false )
reloadBtn = guiCreateButton(49, 19, 49, 36, "reload", false, window)
browser = guiCreateBrowser(10, 55, 828, 609, false, false, false, window)

-- Load our page on browser creation.
local theBrowser = guiGetBrowser(browser) 
addEventHandler("onClientBrowserCreated", theBrowser, 
    function()
        loadBrowserURL(source, "https://forum.mtasa.com/")
    end
)

-- This checks to see if the browser can navigate in any direction and enables the back or forward buttons
addEventHandler( "onClientBrowserDocumentReady", theBrowser, function( )
    navigateForwardBtn.enabled = (canBrowserNavigateForward(theBrowser))
    navigateBackBtn.enabled = (canBrowserNavigateBack(theBrowser))
    guiSetText( addressBar, getBrowserURL( theBrowser ) )
end )

-- This part handles the GUI navigation buttons for the browser.
addEventHandler( "onClientGUIClick", resourceRoot, function ( )
    if source == navigateBackBtn then
        navigateBrowserBack(theBrowser)
    elseif source == navigateForwardBtn then
        navigateBrowserForward(theBrowser)
    elseif source == reloadBtn then
        reloadBrowserPage(theBrowser)
    end
end )
```

## See Also

- canBrowserNavigateBack

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
