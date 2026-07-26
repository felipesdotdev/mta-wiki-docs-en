---
doc_id: "mta-wiki:12665"
title: "IsBrowserRenderingPaused"
source_title: "IsBrowserRenderingPaused"
source_url: "https://wiki.multitheftauto.com/wiki/IsBrowserRenderingPaused"
revision_id: 81282
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:53.512540+00:00"
---

# IsBrowserRenderingPaused

This function gets the rendering state of a [browser](mta://reference/misc/browser.md) [element](mta://reference/misc/element.md).

## Syntax

```
bool isBrowserRenderingPaused ( browser webBrowser )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/browser.md):isRenderingPaused(...)*

**Variable**: *.renderingPaused*

**Counterpart**: *[setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md)*

### Required Arguments

- **webBrowser:** The [browser](mta://reference/misc/browser.md) [element](mta://reference/misc/element.md) to get the rendering state of.

### Returns

Returns *true* if the browser rendering is paused, *false* otherwise.

## Example

This will create a [browser](mta://reference/misc/browser.md) [element](mta://reference/misc/element.md) and a command to pause the browser rendering:

```
-- In order to render the browser on the full screen, we need to know the dimensions.
local screenWidth, screenHeight = guiGetScreenSize ()
 
-- Let's create a new browser in remote mode.
local window = guiCreateWindow (0, 0, screenWidth, screenHeight, "Webbrowser", false)
local browser = guiCreateBrowser (0, 0, 800, 600, false, false, false, window)
 
-- The event onClientBrowserCreated will be triggered, after the browser has been initialized.
-- After this event has been triggered, we will be able to load our URL
local theBrowser = guiGetBrowser (browser) -- Get the browser element from gui-browser
addEventHandler ("onClientBrowserCreated", theBrowser, 
    function ()
		-- After the browser has been initialized, we can load www.youtube.com
		loadBrowserURL (source, "http://www.youtube.com")
	end
)

addCommandHandler ("pause", -- Add a command named 'pause'
  function (player, commandName)
      if isBrowserRenderingPaused (theBrowser) then
          setBrowserRenderingPaused (theBrowser, false)
      else
          setBrowserRenderingPaused (theBrowser, true)
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

- isBrowserRenderingPaused

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
