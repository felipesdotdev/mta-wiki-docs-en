---
doc_id: "mta-wiki:8350"
title: "OnClientBrowserResourceBlocked"
source_title: "OnClientBrowserResourceBlocked"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserResourceBlocked"
revision_id: 82237
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
---

# OnClientBrowserResourceBlocked

This event is executed when a resource (images, sounds etc.) has been blocked.

## Parameters

```
string url, string domain, int reason
```

- **url**: the blocked URL.

- **domain**: the blocked domain (part of the URL).

- **reason**: the reason why the resource was blocked. Possibles values:

- **0**: not allowed yet

- **1**: blacklisted

- **2**: blocked protocol scheme

## Source

The [browser](mta://reference/misc/element-browser.md) element.

## Example

This example demonstrates how to open a browser window, load a test URL, and handle the onClientBrowserResourceBlocked event. If a resource is blocked, it outputs the details to chat and, if the reason is 0 (not allowed yet), requests the domain and reloads the page if accepted.

```
local screenWidth, screenHeight = guiGetScreenSize( )

local browser, theBrowser
local lastBrowser = nil
local testCases = {
    {name = "Google (HTTPS, should work)", url = "https://www.google.com/"},
    {name = "YouTube (HTTPS, should work)", url = "https://www.youtube.com/"},
    {name = "MTA Wiki (HTTPS, should work)", url = "https://wiki.multitheftauto.com/"}
}

addCommandHandler("openbrowser", function(_, case)
    if isElement(browser) then destroyElement(browser) end
    local sx, sy = guiGetScreenSize()
    local bw, bh = math.floor(sx * 0.6), math.floor(sy * 0.6)
    local bx, by = math.floor((sx - bw) / 2), math.floor((sy - bh) / 2)
    browser = guiCreateBrowser(bx, by, bw, bh, false, false, false)
    guiSetVisible(browser, true)
    guiBringToFront(browser)
    showCursor(true)
    theBrowser = guiGetBrowser(browser)

    local idx = tonumber(case) or 1
    if not testCases[idx] then idx = 1 end
    local test = testCases[idx]
    outputChatBox("[BrowserTest] Loading test case: "..test.name)

    addEventHandler("onClientBrowserCreated", theBrowser, function()
        loadBrowserURL(source, test.url)
    end)

    addEventHandler("onClientBrowserDocumentReady", theBrowser, function(url)
        outputChatBox("[BrowserTest] Browser loaded: " .. tostring(url))
    end)

    addEventHandler("onClientBrowserResourceBlocked", theBrowser, function(url, domain, reason)
        outputChatBox("[BrowserTest] Resource blocked! URL="..tostring(url).." DOMAIN="..tostring(domain).." REASON="..tostring(reason), 255, 0, 0)
        if (reason == 0) then
            lastBrowser = source
            requestBrowserDomains({domain}, false, function(accepted, newDomains)
                if (accepted == true) then
                    outputChatBox("[BrowserTest] Domain accepted, reloading page.")
                    reloadBrowserPage(lastBrowser)
                else
                    outputChatBox("[BrowserTest] Domain NOT accepted.")
                end
                lastBrowser = nil
            end)
        elseif (reason == 1) then
            outputChatBox("[BrowserTest] Domain is blacklisted.")
        elseif (reason == 2) then
            outputChatBox("[BrowserTest] Blocked protocol scheme.")
        end
    end)
end)
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- [onClientBrowserLoadingFailed](mta://scripting/client/events/onclientbrowserloadingfailed.md)

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- onClientBrowserResourceBlocked

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
