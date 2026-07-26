---
doc_id: "mta-wiki:8262"
title: "CEF Tutorial"
source_title: "CEF Tutorial"
source_url: "https://wiki.multitheftauto.com/wiki/CEF_Tutorial"
revision_id: 71138
language: "en"
categories: ["Tutorials"]
---

# CEF Tutorial

This page gives you a brief introduction to CEF.

# What is CEF?

CEF stands for **C**hromium **E**mbedded **F**ramework and is a framework for embedding Chromium-based browsers in other applications - in our case MTA. CEF is based on Google's Chromium project so it is also a fast, secure and stable web engine.

You can find more information about CEF on CEF's GoogleCode project page: [https://bitbucket.org/chromiumembedded/cef](https://bitbucket.org/chromiumembedded/cef)

# The basics

Creating a new browser is really simple. Let's open YouTube for example:

```
-- Create a new remote browser (size is 800*600px) with transparency enabled
local browser = createBrowser(800, 600, true, true)

-- "Wait" for the browser (this is necessary because CEF runs in a secondary thread and hence requires the 'asynchronous' event mechanism)
addEventHandler("onClientBrowserCreated", browser,
    function()
        -- We're ready to load the URL now (the source of this event is the browser that has been created)
        loadBrowserURL(source, "https://youtube.com/")
    end
)
```

This example does not require any domain requests as YouTube is whitelisted by default. More about domain requests below.

# Domain request system

In order to prevent people from abusing the possibilities CEF offers, we decided to introduce a request system.
This means the domain you want to load has to meet at least one of the following requirements:

- it is whitelisted globally by the MTA team (you can create a post in [this topic] to suggest a new domain to be whitelisted) - ****TODO: Add forum URL here****

- the domain was requested via requestBrowserDomains/Browser.requestDomains and accepted by the player **before**

- the domain is on the user's whitelist (MTA settings => Tab: Browser => Whitelist)

Apart from these options, a domain might be blacklisted due to malicious content. Such domains cannot be requested.

# Local vs remote mode

There are two modes CEF can run in:

Characteristics of local mode:

- you **can** execute Javascript code without any restriction (See: [executeBrowserJavascript](mta://scripting/client/functions/executebrowserjavascript.md))

- you **can** only load websites stored in the resource folder

- you **cannot** load remote content

Characteristics of remote mode:

- you **cannot** execute Javascript code

- you **can** only load remote content

- keep in mind that either loading remote websites or Javascript on remote websites can be disabled in the MTA settings

Changing the mode after the browser was created is not possible due to technical reasons.

# Resource management

## How to load local HTML files

Loading local HTML files works similar to loading images.

Add your HTML files to your meta.xml through the file tag:

```
<file src="html/myAwesomeUI.html"/>
```

## How to load local resources in local HTML files

Imagine you want to load an image or play a video from your MTA resource. This is possible via a custom URI scheme named ***"[http://mta/](http://mta/)"***

### Example

This examples shows how to play a video. Note that you have to enable OOP.

#### Lua

```
-- Create a browser (local mode is also required to access local data)
local webView = Browser(640, 480, true, true)

addEventHandler("onClientBrowserCreated", webView,
     function()
    
          -- Load HTML UI
          webView:loadURL("http://mta/local/html/myVideo.html")

     end
)
```

#### meta.xml

```
<file src="html/myVideo.html"/>
<file src="media/myVideo.webm"/>
```

#### HTML

This is the most interesting part:

```
<!DOCTYPE HTML>
<html>
<head></head>
<body>
    <video width="640" height="480" controls>
         <source src="http://mta/local/myVideo.webm" type="video/webm"/>
    </video>
</body>
</html>
```

# Lua <==> Javascript communication

First of all, communication between Lua and Javascript is only available in local mode due to security reasons.

## Lua to Javascript

Lua to javascript is pretty easy as you can execute Javascript code from Lua using [executeBrowserJavascript](mta://scripting/client/functions/executebrowserjavascript.md).

So, a bit Lua code around it and you have got the first direction:

- [https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/src/WebWindow.lua#L180-189](https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/src/WebWindow.lua#L180-189)

- [https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/src/mtaevents.js#L9-L15](https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/src/mtaevents.js#L9-L15)

## Javascript to Lua

You are able to trigger a client event via the Javascript method *triggerEvent* which is part of the static class/namespace *mta*.
The syntax is as follows:

```
mta.triggerEvent(string event, var parameter1, var parameter2, var parameter3, ...)
```

The source of this event is always the browser element that triggered the event.

An example is available here:

- [https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/examples/html/ui2.html#L66](https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/examples/html/ui2.html#L66)

- [https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/examples/Main.lua#L35-L40](https://github.com/Jusonex/mtasa_cef_tools/blob/master/webui/examples/Main.lua#L35-L40)

# Debugging

The *web development mode* can be enabled as follows (type it in the client's F8 console):

```
start runcode
crun setDevelopmentMode(true, true)
debugscript 3
```

Now, you should be able to see web errors and blocked domains/URLs in the debug window at the bottom.

# Things you should keep in mind while working with CEF

You should always keep in mind that some modern browser features are not available on some computers.
This is for example true for **WebGL**.

Another problematic feature is **Adobe Flash**. Adobe Flash is enabled by default, but you should avoid using it due to the fact that plugins can be disabled in the settings on the one hand (Java is disabled completely by the way) and Flash is very restrictive on the other hand. Restrictive means it runs in a separate process uses a very old interface and offers therefore just a few ways to control it.
As a consequence, you cannot control the volume of flash objects. Fortunately, HTML5 is an even better replacement and provides very good audio and video interface ([http://www.w3schools.com/tags/ref_av_dom.asp](http://www.w3schools.com/tags/ref_av_dom.asp)) which even supports 3D sound (@all bored people among us: Feel free to write a 3D sound 'wrapper' that maps the GTA onto HTML5 coordinates :P).

# Advanced usage

Since our CEF implementation does not do z-ordering by default, you have to provide your own z-ordering mechanism.
You can find a basic implementation of such a mechanism here: [https://github.com/Jusonex/mtasa_cef_tools](https://github.com/Jusonex/mtasa_cef_tools)
There are also a few utility functions that allow you to integrate these classes easily into your own object-oriented UI system.
I'll provide some code to use CEF along with CEGUI soon too.

# Performance

Creating lots of browsers does not influence MTA directly (except the fact MTA has to copy the texture data in the main/GTA thread due to technical restrictions), because one part of CEF runs in another process and the other part in a secondary thread.
So if you do not want to show the browser, it is definitely the best to destroy the browser. If you cannot destroy the browser (imagine you have to save the website's state for some reason), you can save a lot of resources by disabling rendering via [setBrowserRenderingPaused](mta://scripting/client/functions/setbrowserrenderingpaused.md). This will stop CEF from rendering new frames/processing input and MTA from copying the texture data.

# Troubleshooting

### google.com doesn't work (even though I requested google.com)

Google redirects to a country-specific website by default. If you want to prevent Google from doing this, load the following URL: [https://www.google.com/ncr](https://www.google.com/ncr)

# 3-rd party

## Typescript

Typescript declaration for mta functions:

```
declare var mta: {
    triggerEvent(event: string): void;
    triggerEvent(event: string, ...any): void;
};
```

## React

Example how to call react function from mta:
1. Create a hook:

```
const useMta = () => {
  const dispatch = yourDispatcherHere();
  const w = window as any;
  w.MtaPrefixSomeName = () => dispatch(dispatchFunction());
}
export default useMta;
```

2. Add this hook to main App component.

3. Call from lua:

```
function callReactFunction(name, arg)
    local name = string.format(name, "[^a-zA-Z0-9]", "");
    local code;
    if(arg~= nil)then
        code = string.format("MtaPrefix%s(%q)",name, arg)
    else
        code = string.format("MtaPrefix%s()",name)
    end
    return executeBrowserJavascript(theBrowser, code)
end
```

Use of prefix let you call only mta specific functions with bare minimum of validation required.
option `%q` puts quotes around a string argument's value. Read more at [https://www.gammon.com.au/scripts/doc.php?lua=string.format](https://www.gammon.com.au/scripts/doc.php?lua=string.format)

# Scripting functions

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

# Scripting events

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
