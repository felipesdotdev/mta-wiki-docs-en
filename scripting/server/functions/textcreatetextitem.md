---
doc_id: "mta-wiki:1288"
title: "TextCreateTextItem"
source_title: "TextCreateTextItem"
source_url: "https://wiki.multitheftauto.com/wiki/TextCreateTextItem"
revision_id: 31244
language: "en"
categories: ["Server_functions", "Utility_templates"]
generated_at: "2026-07-26T16:16:57.814253+00:00"
---

# TextCreateTextItem

This function creates a text item. A text item represents a single area of text, much like a label does in standard GUI programming. A text item can only be seen by players if it is added to a [textdisplay](mta://reference/misc/textdisplay.md) using [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md). Each text item can be added to multiple displays, if need be.

## Syntax

```
textitem textCreateTextItem ( string text, float x, float y, [string priority, int red = 255, int green = 255, int blue = 255, int alpha = 255, float scale = 1, string alignX = "left", string alignY = "top", int shadowAlpha = 0] )
```

### Required Arguments

- **text**: A string of text you want to display

- **x**: A floating point number between 0.0 and 1.0 indicating how far across the screen the text should be shown, as a percentage of the width, from the left hand side.

- **y**: A floating point number between 0.0 and 1.0 indicating how far down the screen the text should be shown, as a percentage of the height, from the top.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **priority**: How important it is that this text should be up to date on client's screens. Valid values are: "low", "medium", "high" which are aliases for 0, 1 and 2 respectively.

- **red**: A value between 0 and 255 indicating how red the text should be.

- **green**: A value between 0 and 255 indicating how green the text should be.

- **blue**: A value between 0 and 255 indicating how blue the text should be.

- **alpha**: A value between 0 and 255 indicating how transparent the text should be, with 0 being fully transparent, and 255 being opaque.

- **scale**: A floating point value indicating the scale of the text. The default is 1.0, which is around 12pt.

- **alignX**: A string representing the X-alignment of the text. ("left", "center", "right")

- **alignY**: A string representing the Y-alignment of the text. ("top", "center", "bottom")

- **shadowAlpha**: A value between 0 and 255 indicating how dark the drop shadow should be.

### Returns

Returns a [textitem](mta://reference/misc/textitem.md) object.

## Example

```
myDisplay = textCreateDisplay ()                              -- create a display
textDisplayAddObserver ( myDisplay, myPlayer )                -- make it visible to a player
myTextItem = textCreateTextItem ( "Hello world!", 0.5, 0.5 )  -- create text item for the display
textDisplayAddText ( myDisplay, myTextItem )                  -- add created item to text display so it is displayed
```

## See Also

- [textCreateDisplay](mta://scripting/server/functions/textcreatedisplay.md)

- textCreateTextItem

- [textDestroyDisplay](mta://scripting/server/functions/textdestroydisplay.md)

- [textDestroyTextItem](mta://scripting/server/functions/textdestroytextitem.md)

- [textDisplayAddObserver](mta://scripting/server/functions/textdisplayaddobserver.md)

- [textDisplayAddText](mta://scripting/server/functions/textdisplayaddtext.md)

- [textDisplayGetObservers](mta://scripting/server/functions/textdisplaygetobservers.md)

- [textDisplayIsObserver](mta://scripting/server/functions/textdisplayisobserver.md)

- [textDisplayRemoveObserver](mta://scripting/server/functions/textdisplayremoveobserver.md)

- [textDisplayRemoveText](mta://scripting/server/functions/textdisplayremovetext.md)

- [textItemGetColor](mta://scripting/server/functions/textitemgetcolor.md)

- [textItemGetPosition](mta://scripting/server/functions/textitemgetposition.md)

- [textItemGetPriority](mta://scripting/server/functions/textitemgetpriority.md)

- [textItemGetScale](mta://scripting/server/functions/textitemgetscale.md)

- [textItemGetText](mta://scripting/server/functions/textitemgettext.md)

- [textItemSetColor](mta://scripting/server/functions/textitemsetcolor.md)

- [textItemSetPosition](mta://scripting/server/functions/textitemsetposition.md)

- [textItemSetPriority](mta://scripting/server/functions/textitemsetpriority.md)

- [textItemSetScale](mta://scripting/server/functions/textitemsetscale.md)

- [textItemSetText](mta://scripting/server/functions/textitemsettext.md)
