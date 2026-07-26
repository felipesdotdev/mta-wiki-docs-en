---
doc_id: "mta-wiki:8273"
title: "GetBrowserProperty"
source_title: "GetBrowserProperty"
source_url: "https://wiki.multitheftauto.com/wiki/GetBrowserProperty"
revision_id: 66844
language: "en"
categories: ["Client_functions", "Changes_in_1.5"]
---

# GetBrowserProperty

This function gets a given property of a specified browser.

## Syntax

```
bool getBrowserProperty ( browser theBrowser, string key )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[browser](mta://reference/misc/element-browser.md):getProperty(...)*

**Counterpart**: *[setBrowserProperty](mta://scripting/client/functions/setbrowserproperty.md)*

### Required arguments

- **theBrowser:** browser element to get the property value of

- **key:** The browser property key. It can be:

- **mobile:** Surfing the web as mobile

### Returns

Returns the value if the property was successfully found, *false* otherwise.

## Example

Click to collapse [-]
Example

This example creates a browser that displays (youtube.com), adds a button to get the browser property, and displays the web page as a web page or a phone page:

```
--[[ Example By MrKAREEM --]]

gui = guiCreateWindow(422, 177, 535, 365, "youtube", false)
guiWindowSetSizable(gui, false)
propertyState = guiCreateButton(10, 332, 515, 23, "getBrowserProperty", false, gui) -- Create button to get your browser property
webBrowser = guiCreateBrowser(9, 22, 516, 299, false, false, false, gui) -- Create a web browser, only works with local pages!

local theBrowser = guiGetBrowser(webBrowser) -- Get the web browser

-- Load our page on browser creation.
addEventHandler("onClientBrowserCreated", theBrowser, function()
showCursor(true)
loadBrowserURL(source, "http://m.youtube.com\\")
end
)

addEventHandler( "onClientGUIClick", resourceRoot, function ( )
if source == propertyState then
if isBrowserLoading(theBrowser) then return outputChatBox('Please wait until the browser load!',255,0,0) end -- To avoid mistakes
local getType = getBrowserProperty(theBrowser,'mobile') -- Getting the value of the browser property for the "mobile" key
if getType == '0' then -- This checks whether or not the browser appears as a mobile page
setBrowserProperty(theBrowser, "mobile", '1') -- Show the browser as a mobile page
reloadBrowserPage(theBrowser) -- Reload the browser page
guiSetText( gui, 'mobile_page' )
outputChatBox('You are viewing the browser as a mobile page')
elseif getType == '1' then
setBrowserProperty(theBrowser, "mobile", '0') -- Show the browser as a normal page
reloadBrowserPage(theBrowser) -- Reload the browser page
guiSetText( gui, 'web_page' )
outputChatBox('You are viewing the browser as a web page')
end
end
end )
```

## See also

- [canBrowserNavigateBack](mta://scripting/client/functions/canbrowsernavigateback.md)

- [canBrowserNavigateForward](mta://scripting/client/functions/canbrowsernavigateforward.md)

- [createBrowser](mta://scripting/client/functions/createbrowser.md)

- [executeBrowserJavascript](mta://scripting/client/functions/executebrowserjavascript.md)

- [focusBrowser](mta://scripting/client/functions/focusbrowser.md)

- getBrowserProperty

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
