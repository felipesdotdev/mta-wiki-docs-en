---
doc_id: "mta-wiki:8204"
title: "ExecuteBrowserJavascript"
source_title: "Cef/executeBrowserJavascript"
source_url: "https://wiki.multitheftauto.com/wiki/Cef/executeBrowserJavascript"
revision_id: 79774
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
generated_at: "2026-07-26T16:12:06.225273+00:00"
---

# ExecuteBrowserJavascript

This function executes a Javascript string to the specified [browser](mta://reference/misc/element-browser.md). Works only with local browsers.

## Syntax

```
bool executeBrowserJavascript ( browser webBrowser, string jsCode )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):executeJavascript(...)*

### Required Arguments

- **webBrowser:** The web browser which will execute the Javascript code

- **jsCode:** The Javascript code string

### Returns

Returns *true* if executing Javascript is allowed in the current context, *false* otherwise.

## Example

This example shows how to display the name (nick) of the local player on the webpage.

```
local browser = guiGetBrowser(guiCreateBrowser(200, 200, 400, 200, true, false, false))

addEventHandler("onClientBrowserCreated", browser,
    function ()
        loadBrowserURL(source, "http://mta/local/example.html") --Containing <span id="nick"></span> somewhere in the file
    end)

--The page has to load first
addEventHandler("onClientBrowserDocumentReady", browser,
    function ()
        executeBrowserJavascript(source, string.format("document.getElementById('nick').innerText = %q;", getPlayerName(localPlayer)))
    end)
```

## See Also

- [canBrowserNavigateBack](mta://scripting/client/functions/canbrowsernavigateback.md)

- [canBrowserNavigateForward](mta://scripting/client/functions/canbrowsernavigateforward.md)

- [createBrowser](mta://scripting/client/functions/createbrowser.md)

- executeBrowserJavascript

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
