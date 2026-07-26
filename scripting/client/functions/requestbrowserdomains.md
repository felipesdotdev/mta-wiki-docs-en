---
doc_id: "mta-wiki:8013"
title: "RequestBrowserDomains"
source_title: "RequestBrowserDomains"
source_url: "https://wiki.multitheftauto.com/wiki/RequestBrowserDomains"
revision_id: 65766
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
generated_at: "2026-07-26T16:16:32.967341+00:00"
---

# RequestBrowserDomains

This function opens a request window in order to accept the requested remote URLs.

| [[{{{image}}}\|link=\|]] | Note: You must use this function prior to calling loadBrowserURL because every domain, with exceptions in the whitelist here and there , is blocked by default. |
| --- | --- |
|  |  |

## Syntax

```
bool requestBrowserDomains ( table pages [, bool parseAsURL = false, function callback ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Browser](mta://reference/misc/element-browser.md).requestDomains(...)*

### Required Arguments

- **pages:** A table containing all domains

### Optional Arguments

- **parseAsURL:** *true* if the passed addresses should be converted from URLs, *false* otherwise.

- **callback:** A callback function that is called as soon as the result is available

Syntax:

```
function(bool wasAccepted, table new_domains)
```

### Returns

Returns **true**, if the string was successfully read, **false** otherwise.

## Example

```
requestBrowserDomains({ "mtasa.com" }) -- request browser domain
showCursor(true) -- show cursor
addEventHandler("onClientBrowserWhitelistChange", root,
   function(newDomains)
     if newDomains[1] == "mtasa.com" then
       local browser = createBrowser(1280, 720, false, false) -- create browser
       loadBrowserURL(browser, "http://mtasa.com/") -- load browser url
   end
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

- [loadBrowserURL](mta://scripting/client/functions/loadbrowserurl.md)

- [navigateBrowserBack](mta://scripting/client/functions/navigatebrowserback.md)

- [navigateBrowserForward](mta://scripting/client/functions/navigatebrowserforward.md)

- [reloadBrowserPage](mta://scripting/client/functions/reloadbrowserpage.md)

- requestBrowserDomains

- [resizeBrowser](mta://scripting/client/functions/resizebrowser.md)

- [setBrowserAjaxHandler](mta://scripting/client/functions/setbrowserajaxhandler.md)

- [setBrowserProperty](mta://scripting/client/functions/setbrowserproperty.md)

- [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md)

- [setBrowserVolume](mta://scripting/client/functions/setbrowservolume.md)

- [toggleBrowserDevTools](mta://scripting/client/functions/togglebrowserdevtools.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22789](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22789):

- [isBrowserGPUEnabled](mta://scripting/client/functions/isbrowsergpuenabled.md)
