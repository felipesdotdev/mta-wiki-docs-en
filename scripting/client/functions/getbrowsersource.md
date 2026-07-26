---
doc_id: "mta-wiki:8420"
title: "GetBrowserSource"
source_title: "GetBrowserSource"
source_url: "https://wiki.multitheftauto.com/wiki/GetBrowserSource"
revision_id: 65737
language: "en"
categories: ["Client_functions", "Changes_in_1.5.1"]
generated_at: "2026-07-26T16:15:07.806857+00:00"
---

# GetBrowserSource

This function can be used to retrieve the source code of a website (asynchronously). The size of the source code is limited to 2 MiB (remaining bytes are cut).

## Syntax

```
bool getBrowserSource ( browser webBrowser, function callback )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):getSource(...)*

### Required arguments

- **webBrowser:** The browser element you want to get the source of

- **callback:** a callback function with syntax as described below

#### Callback syntax

```
function ( string code )
```

## Returns

Returns *true* if valid arguments have been passed, *false* otherwise.

## Example

```
local browser = createBrowser(1024,1024,false,false)      --Create Browser

addEventHandler("onClientBrowserCreated",browser,function()
    loadBrowserURL(browser,"http://www.youtube.com")    --Load URL
end)

addEventHandler("onClientBrowserDocumentReady",browser,function(url)
    local rnt = getBrowserSource(browser,function(code)     --Get Browser Source and Call Function
        outputChatBox(code)                             --Output Code
    end)
    if rnt then
        outputChatBox("Browser Source Got",0,255,0)
    else
        outputChatBox("Failed To Get Browser Source",255,0,0)
    end
end)
```

## See Also

- [canBrowserNavigateBack](mta://scripting/client/functions/canbrowsernavigateback.md)

- [canBrowserNavigateForward](mta://scripting/client/functions/canbrowsernavigateforward.md)

- [createBrowser](mta://scripting/client/functions/createbrowser.md)

- [executeBrowserJavascript](mta://scripting/client/functions/executebrowserjavascript.md)

- [focusBrowser](mta://scripting/client/functions/focusbrowser.md)

- [getBrowserProperty](mta://scripting/client/functions/getbrowserproperty.md)

- [getBrowserSettings](mta://scripting/client/functions/getbrowsersettings.md)

- getBrowserSource

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
