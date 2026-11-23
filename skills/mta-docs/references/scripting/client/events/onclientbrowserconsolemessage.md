---
doc_id: "mta-wiki:14689"
title: "OnClientBrowserConsoleMessage"
source_title: "OnClientBrowserConsoleMessage"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserConsoleMessage"
revision_id: 82895
language: "en"
categories: ["Client_events"]
---

# OnClientBrowserConsoleMessage

This event is triggered when a [browser](mta://reference/misc/element-browser.md) outputs a console message, such as a JavaScript error or a message written using console.log().

## Parameters

```lua
string message, string source, int line, int level
```

- **message**: the console message.

- **source**: the URL or source identifier where the message originated.

- **line**: the line number where the message originated.

- **level**: the severity level of the message:

- **0**: default

- **1**: verbose

- **2**: info

- **3**: warning

- **4**: error

- **5**: fatal

- **6**: disable

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [browser](mta://reference/misc/element-browser.md) element that generated the console message.

| [[{{{image}}}\|link=\|]] | Note: The source parameter is a string identifying the message's origin. It is separate from the event's source variable, which refers to the browser element. Use a different parameter name, such as messageSource , to access both. |
| --- | --- |
|  |  |

## Example

This example loads a local HTML page and prints its browser console messages to the debug output.

**Client-side Lua:**

```lua
local browser = createBrowser(25, 25, true, false)

local logLevels = {
    [0] = "default",
    [1] = "verbose",
    [2] = "info",
    [3] = "warning",
    [4] = "error",
    [5] = "fatal",
    [6] = "disable"
}

addEventHandler("onClientBrowserConsoleMessage", browser, function(message, messageSource, line, level)
    outputDebugString(("Browser console message: %s (line: %d, source: %s, level: %s)"):format(
        message, line, messageSource, logLevels[level] or tostring(level)
    ))
end)

addEventHandler("onClientBrowserCreated", browser, function()
    loadBrowserURL(browser, "http://mta/local/test.html")
end)
```

**test.html:**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Browser console example</title>
</head>
<body>
    <script>
        console.log("Hello from the browser!");
        console.warn("This is a warning.");
        console.error("This is an error.");
    </script>
</body>
</html>
```

Include the HTML file in your resource's **meta.xml**:

```xml
<file src="test.html" />
```

Use **/debugscript 3** to view the output.

## See also

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

ADDED/UPDATED IN VERSION 1.7.0 :

- onClientBrowserConsoleMessage
