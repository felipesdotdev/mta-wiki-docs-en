---
doc_id: "mta-wiki:6504"
title: "Error/info-window"
source_title: "Error/info-window"
source_url: "https://wiki.multitheftauto.com/wiki/Error/info-window"
revision_id: 31285
language: "en"
categories: ["Utility_templates"]
generated_at: "2026-07-26T16:14:59.392457+00:00"
---

# Error/info-window

This resource provides a function that shows an dx-error- or infowindow. The window's size will fit the text that you put into it.

Example (error-window on top, info-window at the bottom):

In its settings, you can set for both the info- and error window these colors:

- Top-background (red, green, blue, alpha) (0-255)

- Top-text (red, green, blue) (0-255)

- Text-background (red, green, blue, alpha) (0-255)

- Text (red, green, blue) (0-255)

## Download

[http://community.multitheftauto.com/index.php?p=resources&s=details&id=4921](http://community.multitheftauto.com/index.php?p=resources&s=details&id=4921)

## Syntax

Click to collapse [-]
Server

```
exports.errorwindow: show ( player thePlayer, string windowtype, string text, [ int time = 0, string toptext = "Error" or "Info", bool disableByClick = true ] )
```

### Required Arguments

- **thePlayer:** Player to show the errorwindow to.

- **windowtype:** Windowtype, either **"error"** or **"info"**.

- **text:** Text to show in the errorwindow.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **time:** Time in milliseconds to show the window, before it disappears (if disableByClick is true and client clicks, timer is overridden).

- **toptext:** Text in the top of the window ("Scumbag customer" in example-image above).

- **disableByClick:** Close window when client clicks somewhere (**cursor must be enabled!**).

<section name="Client" class="client" show="true">

```
exports.errorwindow: show ( string windowtype, string text, [ int time = 0, string toptext = "Error" or "Info", bool disableByClick = true ] )
```

### Required Arguments

- **windowtype:** Windowtype, either **"error"** or **"info"**.

- **text:** Text to show in the errorwindow.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **time:** Time in milliseconds to show the window, before it disappears (if disableByClick is true and client clicks, timer is overridden).

- **toptext:** Text in the top of the window ("Scumbag customer" in example-image above).

- **disableByClick:** Close window when client clicks somewhere (**cursor must be enabled!**).
