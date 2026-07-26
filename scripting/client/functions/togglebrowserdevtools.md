---
doc_id: "mta-wiki:8485"
title: "ToggleBrowserDevTools"
source_title: "ToggleBrowserDevTools"
source_url: "https://wiki.multitheftauto.com/wiki/ToggleBrowserDevTools"
revision_id: 65779
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
generated_at: "2026-07-26T16:16:58.676987+00:00"
---

# ToggleBrowserDevTools

This function toggles the visibility of the developer tools pane.

| [[{{{image}}}\|link=\|]] | Note: You should do a 'setDevelopmentMode(true, true)' before using this function. |
| --- | --- |
|  |  |

## Syntax

```
bool toggleBrowserDevTools ( browser webBrowser, bool visible )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/browser.md):toggleDevTools(...)*

**Variable**: *.devTools*

### Required Arguments

- **webBrowser:** The browser

- **visible:** *true* to show the tools, *false* to hide

### Returns

Returns *true* if the visibility was successfully toggled, *false* if an error occurred

## Example

This example will output browser console logs to debugscript.

```
local GUI_browser = guiCreateBrowser(100,100,640,480,false,false,false) -- Create Browser
local browser = guiGetBrowser(GUI_browser) -- Get browser from GUI element

setDevelopmentMode(true, true) -- Enable client dev mode

addEventHandler("onClientBrowserCreated", browser, function()
    toggleBrowserDevTools(browser, true) -- Toggle the CEF dev console
end)
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

- toggleBrowserDevTools

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
