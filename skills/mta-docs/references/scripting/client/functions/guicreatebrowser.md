---
doc_id: "mta-wiki:8288"
title: "GuiCreateBrowser"
source_title: "GuiCreateBrowser"
source_url: "https://wiki.multitheftauto.com/wiki/GuiCreateBrowser"
revision_id: 78489
language: "en"
categories: ["Client_functions", "Changes_in_1.5.0", "Changes_in_1.6", "Utility_templates"]
---

# GuiCreateBrowser

ADDED/UPDATED IN VERSION 1.5.0 [r7172](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=7172):

This function creates a new CEGUI web [browser](mta://reference/misc/element-browser.md) element.
  
The difference between this and createBrowser is that this function handles inputs internally, and it can be attached to GUI windows. So the createBrowser function is more suitable for custom dx based interfaces, while this one is favorable for CEGUI all-in-all integration.
You can learn more about the differences [[here](https://forum.mtasa.com/topic/80422-dx-browser-vs-gui-browser/?do=findComment&comment=737334)].

## Syntax

```
gui-browser guiCreateBrowser ( float x, float y, float width, float height, bool isLocal, bool isTransparent, [ bool isRelative = false, gui-element parent = nil ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[GuiBrowser](https://wiki.multitheftauto.com/index.php?title=Element/gui-browser&action=edit&redlink=1)(...)*

### Required Arguments

- **x:** A float of the 2D x position of the browser on a player's screen.  This is affected by the *relative* argument.

- **y:** A float of the 2D y position of the browser on a player's screen. This is affected by the *relative* argument.

- **width:** The browser's native width. This should be greater than or equal to 1.

- **height:** The browser's native height. This should be greater than or equal to 1.

- **isLocal:** Sets whether the browser can only show local content or content from the internet (see examples over [here](mta://scripting/client/functions/createbrowser.md) for more information)

- **isTransparent:** *true* if you want the browser to support transparency, *false* otherwise

Providing a size of (0,0) will be a hard error.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **isRelative:** This is whether sizes and positioning are relative.  If this is *true*, then all x,y,width,height floats must be between 0 and 1, representing sizes/positions as a fraction of the screen size. If *false*, then the size and co-ordinates are based on client's resolution, accessible using [guiGetScreenSize](mta://scripting/client/functions/guigetscreensize.md).

- **parent:** This is the parent that the radio button is attached to. If the relative argument is true, sizes and positioning will be made relative to this parent. If the relative argument is false, positioning will be the number of offset pixels from the parent's origin. If no parent is passed, the parent will become the screen - causing positioning and sizing according to screen positioning.

### Returns

Returns a [gui-browser](https://wiki.multitheftauto.com/index.php?title=Gui-browser&action=edit&redlink=1) element if it was created successfully, *false* otherwise. Returns also *false*, if the user disabled remote pages and *isLocal* was set to *false*.

## Example

This examples simply creates a web browser and loads an URL

```
local browserGUI = guiCreateBrowser(100, 100, 300, 50, true, true, false)
local browser    = guiGetBrowser(browserGUI)

addEventHandler("onClientBrowserCreated", browser, function()
  loadBrowserURL(browser, "http://mta/local/html/index.html")
end)
```

This examples attaches a web browser to a CEGUI window.

```
-- In order to render the browser fullscreen, we need to get the dimensions of the screen
local screenWidth, screenHeight = guiGetScreenSize( )

-- Let's create a new browser in remote mode
local window = guiCreateWindow( 0, 0, screenWidth, screenHeight, "Web Browser", false )
local browser = guiCreateBrowser( 0, 28, screenWidth, screenHeight, false, false, false, window )
local theBrowser = guiGetBrowser( browser ) -- Get the browser element from gui-browser

-- The event onClientBrowserCreated will be triggered after the browser has been initialized
-- After this event has been triggered we will be able to load our URL
addEventHandler( "onClientBrowserCreated", theBrowser, 
	function( )
		-- After the browser has been initialized, we can load www.youtube.com
		loadBrowserURL( source, "https://www.youtube.com/" )
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
