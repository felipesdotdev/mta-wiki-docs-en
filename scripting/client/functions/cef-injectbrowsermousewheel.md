---
doc_id: "mta-wiki:8202"
title: "InjectBrowserMouseWheel"
source_title: "Cef/injectBrowserMouseWheel"
source_url: "https://wiki.multitheftauto.com/wiki/Cef/injectBrowserMouseWheel"
revision_id: 65749
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
generated_at: "2026-07-26T16:12:06.175945+00:00"
---

# InjectBrowserMouseWheel

This function injects mouse wheel events.

## Syntax

```
bool injectBrowserMouseWheel ( browser webBrowser, int verticalScroll, int horizontalScroll )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):injectMouseWheel(...)*

**Counterpart**: *injectBrowserMouseWheel*

### Required arguments

- **webBrowser:** The web browser

- **verticalScroll**: Amount of units you want the browser to scroll along the Y-axe.

- **horizontalScroll**: Amount of units you want the browser to scroll along the X-axe.

### Returns

Returns *true* if the mouse action was successfully injected, *false* otherwise.

## Example

```
local webBrowser = createBrowser(1000, 1000, false, false)
showCursor(true)

function webBrowserRender()
        dxDrawImage(0, 0, 1000, 1000, webBrowser, 0, 0, 0, tocolor(255,255,255,255), true)
end

addEventHandler("onClientBrowserCreated", webBrowser,
        function()
              loadBrowserURL(webBrowser, "https://www.youtube.com/tv#/watch?mode=transport&v=jofNR_WkoCE")
              addEventHandler("onClientRender", root, webBrowserRender)
              addEventHandler("onClientKey", root, onKey)
	end
)

function onKey(button)
	if button == "mouse_wheel_down" then
		injectBrowserMouseWheel(webBrowser, -40, 0)
	elseif button == "mouse_wheel_up" then
		injectBrowserMouseWheel(webBrowser, 40, 0)
	end
end
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

- injectBrowserMouseWheel

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
