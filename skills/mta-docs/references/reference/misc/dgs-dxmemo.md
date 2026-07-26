---
doc_id: "mta-wiki:9760"
title: "Dgs-dxmemo"
source_title: "Dgs-dxmemo"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxmemo"
revision_id: 82807
language: "en"
categories: []
---

# Dgs-dxmemo

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxmemo that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### allowCopy

This property determines whether the content of memo can be copy(ctrl+c)/cut(ctrl+x)

```
dgsSetProperty(memo,"allowCopy",allowCopy)
```

- **allowCopy:**  A boolean value of the state of whether this memo allows users to copy something from it.

### bgColor

This property determines the background color of the memo.

```
dgsSetProperty(memo,"bgColor",bgColor)
```

- **bgColor:**  An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgColorBlur

This property determines the background color of the memo when it is blurred.

```
dgsSetProperty(memo,"bgColorBlur",bgColorBlur)
```

- **bgColorBlur:**  An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md), leave to nil to use bgColor.

### bgImage

This property determines the background image of the memo.

```
dgsSetProperty(memo,"bgImage",bgImage)
```

- **bgImage:**  A material element that serves as the background image of the memo (texture/shader/screen source/renderTarget).

### bgImageBlur

This property determines the background image of the memo when it is blurred.

```
dgsSetProperty(memo,"bgImageBlur",bgImageBlur)
```

- **bgImageBlur:**  A material element that serves as the background image of the memo (texture/shader/screen source/renderTarget), leave to nil to use bgImage.

### caretColor

This property determines the color of the caret

```
dgsSetProperty(memo,"caretColor",caretColor)
```

- **caretColor:**  An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### caretHeight

The height of the caret of the memo (multiple of the font height).

```
dgsSetProperty(memo,"caretHeight",caretHeight)
```

- **caretHeight:** A float of the caret height.

### caretOffset

The offset of the caret of the memo.

```
dgsSetProperty(memo,"caretOffset",offsetY)
```

- **offsetY:**  A float of the 2D Y position offset of the caret of the memo.

### caretPos

The position in which the caret stays.

```
dgsSetProperty(memo,"caretPos",{index,line})
```

- **index:**  An integer of the index of the text in current line of the memo.

- **line:**  An integer of the line of the memo.

### caretStyle

This is equivalent to [dgsMemoSetCaretStyle](mta://scripting/client/functions/dgsmemosetcaretstyle.md)/[dgsMemoGetCaretStyle](mta://scripting/client/functions/dgsmemogetcaretstyle.md).

This property allows us to change the style of caret of the memo. ( 0 is "|"; 1 is "_" )

Example(0):

This is Text|

Example(1):

This is Text_

```
dgsSetProperty(memo,"caretStyle",caretStyle)
```

- **caretStyle:**  An integer of the caret style of the memo.

### caretThick

This property allows us to change the thickness of caret of the memo.

```
dgsSetProperty(memo,"caretThick",caretThick)
```

- **caretThick:**  An integer of the thickness of the caret of the memo.

### colorCoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(memo,"colorCoded",colorCoded)
```

- **colorCoded:** Set to true to enable embedded #FFFFFF color codes.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(memo,"font",font)
```

- **font:**  A [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the memo.

### padding

This property determines the content padding from 4 sides of element (left/top/right/bottom)

```
dgsSetProperty(memo,"padding", {horizontal, vertical})
```

- **horizontal:**  A float of the horizontal padding in pixels.

- **vertical:**  A float of the vertical padding in pixels.

### placeHolder

This is equivalent to [dgsEditSetPlaceHolder](mta://scripting/client/functions/dgseditsetplaceholder.md)//[dgsEditGetPlaceHolder](mta://scripting/client/functions/dgseditgetplaceholder.md)

```
dgsSetProperty(edit,"placeHolder",placeHolder)
```

- **placeHolder** : A string of the place holder text of dgs edit ( This text will show when there is no text in a blurred dgs edit ).

### placeHolderColor

This property determines the color of the place holder text. The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md).

```
dgsSetProperty(edit,"placeHolderColor",placeHolderColor)
```

- **placeHolderColor** : An integer of the color of the place holder text of the edit.

### placeHolderColorcoded

This property determines whether the place holder supports color code.

```
dgsSetProperty(edit,"placeHolderColorcoded",placeHolderColorcoded)
```

- **placeHolderColorcoded** : A bool indicates whether the place holder supports color code.

### placeHolderFont

This property changes the font of place holder.

```
dgsSetProperty(edit,"placeHolderFont",placeHolderFont)
```

- **placeHolderFont** : A string/dx-font element of the font of the place holder.

### placeHolderIgnoreRenderTarget

This property determines whether the place holder isn't restricted by render target.

```
dgsSetProperty(edit,"placeHolderIgnoreRenderTarget",placeHolderIgnoreRenderTarget)
```

- **placeHolderIgnoreRenderTarget** : A bool indicates whether the place holder isn't restricted by render target.

### placeHolderOffset

This property allows place holder has offsets relative to its original position.

```
dgsSetProperty(edit,"placeHolderOffset",{ xOffset, yOffset })
```

- **xOffset** : An integer of 2D x offset.

- **yOffset** : An integer of 2D y offset.

### placeHolderVisibleWhenFocus

This property allows place holder to be visible even when edit is focused.

```
dgsSetProperty(edit,"placeHolderVisibleWhenFocus",placeHolderVisibleWhenFocus)
```

- **placeHolderVisibleWhenFocus** : A bool indicates whether the place holder when the edit is focused.

### readOnly

This is equivalent to [dgsMemoSetReadOnly](mta://scripting/client/functions/dgsmemosetreadonly.md)/[dgsMemoGetReadOnly](mta://scripting/client/functions/dgsmemogetreadonly.md).

```
dgsSetProperty(memo,"readOnly",readOnly)
```

- **readOnly:**  A bool indicates whether the memo is only readable.

### readOnlyCaretShow

Whether the caret of memo will show/hide under read-only mode.

```
dgsSetProperty(memo,"readOnlyCaretShow",readOnlyCaretShow)
```

- **readOnlyCaretShow:**  A bool indicates whether the caret is shown or hidden when the memo is read-only.

### renderTarget

This property stores a render target of the memo.

```
dgsSetProperty(memo,"renderTarget",renderTarget)
```

- **renderTarget:**  A render target that is used to render the text.

### scrollbars

This property stores two scroll bars which can be got by [dgsMemoGetScrollBar](mta://scripting/client/functions/dgsmemogetscrollbar.md) of the memo.

```
dgsSetProperty(memo,"scrollbars",{Vertical,Horizontal})
```

- **Vertical:**  A vertical scroll bar of the memo.

- **Horizontal:**  A horizontal scroll bar of the memo.

### scrollBarThick

This property allows us to change the thickness of scroll bars of the memo.

```
dgsSetProperty(memo,"scrollBarThick",scrollBarThick)
```

- **scrollBarThick:**  An integer of the thickness of scroll bars of the memo.

### scrollSize

This property determines how many lines will get scrolled out of the rendering area once when you are scrolling your mouse wheel.

```
dgsSetProperty(memo,"scrollSize",scrollSize)
```

- **scrollSize:**  Lines to be scrolled.

### selectColorBlur

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the rectangle of text selection of the memo when blurred.

```
dgsSetProperty(memo,"selectColorBlur",selectColorBlur)
```

- **selectColorBlur:**  An integer of the color of the rectangle of text selection of the memo when blurred.

### selectColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the rectangle of text selection of the memo.

```
dgsSetProperty(memo,"selectColor",selectColor)
```

- **selectColor:**  An integer of the color of the rectangle of text selection of the memo.

### selectFrom

The position from which the text is selected.

```
dgsSetProperty(memo,"selectFrom",{index,line})
```

- **index:**  An integer of the index of the text in the line where the text is selected from of the memo.

- **line:**  An integer of the line where the text is selected from of the memo.

### shadow

The shadow text of the memo.

```
dgsSetProperty(memo,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the memo.

- **offsetY:** A float of the 2D Y offset of the shadow text of the memo.

- **color:** An integer of the color of the shadow text of the memo.

- **outline:** An integer of the outline style of the shadow text.

### showLine

This property stores the value of how many lines does the text move to top.

```
dgsSetProperty(memo,"showLine",line)
```

- **line:**  An integer indicates how many lines does the text move to top.

### showPos

This property stores the value of how many pixels of the text are moved to left.

```
dgsSetProperty(memo,"showPos",posX)
```

- **posX:**  An integer indicates how many pixels of the text are moved to left.

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(memo,"text",text)
```

- **text:**  A *table* of the text of the memo.( Because of multi lines, I use table instead of string )

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the memo.

```
dgsSetProperty(memo,"textColor",textColor)
```

- **textColor:**  An integer of the color of the text of the memo.

### textLength

This is for scroll bar detection. You had better not touch it.

```
dgsSetProperty(memo,"textLength",textlen)
```

- **textlen:**  A table stores the length of text in every line.

### textSize

The scale of the text of the memo. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(memo,"textSize",{scaleX,scaleY})
```

- **scaleX:**  A float of the 2D X scale of the text of the memo.

- **scaleY:**  A float of the 2D Y scale of the text of the memo.

### typingSound

Typing sound, nil for disabled. This is equivalent to [dgsMemoSetTypingSound](mta://scripting/client/functions/dgsmemosettypingsound.md)/[dgsMemoGetTypingSound](mta://scripting/client/functions/dgsmemogettypingsound.md)

```
dgsSetProperty(memo,"typingSound",typingSound)
```

- **typingSound:**  A string of the path/url of typing sound.

### typingSoundVolume

Typing sound, nil for disabled. This is equivalent to [dgsMemoSetTypingSoundVolume](mta://scripting/client/functions/dgsmemosettypingsoundvolume.md)/[dgsMemoGetTypingSoundVolume](mta://scripting/client/functions/dgsmemogettypingsoundvolume.md)

```
dgsSetProperty(memo,"typingSoundVolume",typingSoundVolume)
```

- **typingSoundVolume:**  A float of the volume of the typing sound. Range is from 0.0 to 1.0. This can go above 1.0 for amplification.

### wordWrap

This property determines the word wrap state of dgs memo. This is equivalent to [dgsMemoSetWordWrapState](mta://scripting/client/functions/dgsmemosetwordwrapstate.md)/[dgsMemoGetWordWrapState](mta://scripting/client/functions/dgsmemogetwordwrapstate.md)

```
dgsSetProperty(memo,"wordWrap",wordWrap)
```

- **wordWarp:**  An integer or a bool of word wrap state, vaild state are as follows:

- **false:** Non-wordwrap

- **1:** Split via single character ( This will break a word into 2 parts )

- **2:** Split via word

## See Also

### General Properties

- [DGS General Basic Properties](mta://reference/misc/dgs-general-basic-properties.md)

### Unique Properties For DGS Core Elements

- [dgs-dx3dinterface](mta://reference/misc/dgs-dx3dinterface.md)

- [dgs-dx3dimage](mta://reference/misc/dgs-dx3dimage.md)

- [dgs-dx3dtext](mta://reference/misc/dgs-dx3dtext.md)

- [dgs-dx3dline](mta://reference/misc/dgs-dx3dline.md)

- [dgs-dxbutton](mta://reference/misc/dgs-dxbutton.md)

- [dgs-dxcheckbox](mta://reference/misc/dgs-dxcheckbox.md)

- [dgs-dxcombobox](mta://reference/misc/dgs-dxcombobox.md)

- [dgs-dxdetectarea](mta://reference/misc/dgs-dxdetectarea.md)

- [dgs-dxedit](mta://reference/misc/dgs-dxedit.md)

- [dgs-dxgridlist](mta://reference/misc/dgs-dxgridlist.md)

- [dgs-dximage](mta://reference/misc/dgs-dximage.md)

- [dgs-dxlabel](mta://reference/misc/dgs-dxlabel.md)

- [dgs-dxline](mta://reference/misc/dgs-dxline.md)

- dgs-dxmemo

- [dgs-dxprogressbar](mta://reference/misc/dgs-dxprogressbar.md)

- [dgs-dxradiobutton](mta://reference/misc/dgs-dxradiobutton.md)

- [dgs-dxscrollbar](mta://reference/misc/dgs-dxscrollbar.md)

- [dgs-dxscrollpane](mta://reference/misc/dgs-dxscrollpane.md)

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
