---
doc_id: "mta-wiki:6503"
title: "Resource : Errorwindow"
source_title: "Resource:Errorwindow"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AErrorwindow"
revision_id: 69402
language: "en"
categories: ["Utility_templates", "Resource"]
generated_at: "2026-07-26T16:17:12.301474+00:00"
---

# Resource : Errorwindow

This resource provides a function that shows an dx-errorwindow. The window's size will fit the text that you put into it.

Example (top -> errorwindow, bottom -> infowindow):

In its settings, you can set the color of:

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
exports.errorwindow: show ( player thePlayer, string text, [ int time = 0, string toptext = "ERROR", bool disableByClick = true ] )
```

### Required Arguments

- **thePlayer:** Player to show the errorwindow to.

- **text:** Text to show in the errorwindow.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **time:** Time in milliseconds to show the window, before it disappears (if disableByClick is true and client clicks, timer is overridden).

- **toptext:** Text in the top of the window ("Scumbag customer" in example-image above).

- **disableByClick:** Close window when client clicks somewhere (**cursor must be enabled!**).

<section name="Client" class="client" show="true">

```
exports.errorwindow: show ( string text, [ int time = 0, string toptext = "ERROR", bool disableByClick = true ] )
```

### Required Arguments

- **text:** Text to show in the errorwindow.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **time:** Time in milliseconds to show the window, before it disappears (if disableByClick is true and client clicks, timer is overridden).

- **toptext:** Text in the top of the window ("Scumbag customer" in example-image above).

- **disableByClick:** Close window when client clicks somewhere (**cursor must be enabled!**).
