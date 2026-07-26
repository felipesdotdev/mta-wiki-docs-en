---
doc_id: "mta-wiki:8414"
title: "GetBrowserSettings"
source_title: "GetBrowserSettings"
source_url: "https://wiki.multitheftauto.com/wiki/GetBrowserSettings"
revision_id: 66850
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
generated_at: "2026-07-26T16:15:07.786652+00:00"
---

# GetBrowserSettings

This function returns a table containing the browser settings.

## Syntax

```
table getBrowserSettings ()
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Browser](mta://reference/misc/element-browser.md).getSettings(...)*

## Returns

A table having the following keys:

- **RemoteEnabled**: *true* if remote websites are enabled, *false* otherwise

- **RemoteJavascript**: *true* if Javascript is enabled on remote websites, *false* otherwise

- **PluginsEnabled**: *true* if plugins such as Flash, Silverlight (but not Java) are enabled, *false* otherwise. This setting is *false* by default.

## Example

Click to collapse [-]
Example

This creates a browser and get the browser settings when the browser has been created

```
window = guiCreateWindow(377, 156, 671, 454, "", false)
guiWindowSetSizable(window, true)

webBrowser = guiCreateBrowser(9, 26, 652, 418, false, false, false, window)

local theBrowser = guiGetBrowser(webBrowser)

addEventHandler("onClientBrowserCreated", theBrowser, function()
showCursor(true)
loadBrowserURL(source, "http://google.com\\")
for k,v in pairs(getBrowserSettings(theBrowser)) do
outputChatBox("['"..tostring(k).."'] = "..tostring(v))
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

- getBrowserSettings

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
