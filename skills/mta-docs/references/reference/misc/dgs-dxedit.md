---
doc_id: "mta-wiki:10184"
title: "Dgs-dxedit"
source_title: "Dgs-dxedit"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxedit"
revision_id: 77139
language: "en"
categories: []
---

# Dgs-dxedit

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxedit that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the text within the edit.

The functions as follows are basic on this property.

[dgsEditSetHorizontalAlign](mta://scripting/client/functions/dgseditsethorizontalalign.md)/[dgsEditGetHorizontalAlign](mta://scripting/client/functions/dgseditgethorizontalalign.md)

[dgsEditSetVerticalAlign](mta://scripting/client/functions/dgseditsetverticalalign.md)/[dgsEditGetVerticalAlign](mta://scripting/client/functions/dgseditgetverticalalign.md)

```
dgsSetProperty(edit,"alignment",{alignX,alignY})
```

- **alignX** : Horizontal alignment of the text within the edit. Can be "left", "center" or "right".

- **alignY** : Vertical alignment of the text within the edit. Can be "top", "center" or "bottom".

### allowCopy

This propertry determines whether the text can be copyed ( ctrl+c ) or cut ( ctrl+x )

```
dgsSetProperty(edit,"allowCopy",allowCopy)
```

- **allowCopy** : A bool indicates whether the text can be copyed ( ctrl+c ) or cut ( ctrl+x )

### autoComplete

This propertry allows auto complete for edit. *See* [dgsEditAddAutoComplete](mta://scripting/client/functions/dgseditaddautocomplete.md)\[dgsEditRemoveAutoComplete](mta://scripting/client/functions/dgseditremoveautocomplete.md)\[dgsEditSetAutoComplete](mta://scripting/client/functions/dgseditsetautocomplete.md)\[dgsEditGetAutoComplete](mta://scripting/client/functions/dgseditgetautocomplete.md)

```
dgsSetProperty(edit,"autoComplete",autoComplete)
```

- **autoComplete** : The auto complete table. Structure is as follows:

```
autoComplete = {
	name1 = isSensitive,
	name2 = isSensitive,
}
```

### autoCompleteSkip

This propertry allows skip auto complete detect.

```
dgsSetProperty(edit,"autoCompleteSkip",autoCompleteSkip)
```

- **autoCompleteSkip** : A bool if whether disabling auto complete check

### autoCompleteShow

This propertry stores current showing auto complete item.

```
dgsSetProperty(edit,"autoCompleteShow",autoCompleteShow)
```

- **autoCompleteShow** : A table stores the showing data. Structure is as follows:

```
autoCompleteShow = {matchedAutoCompletion,showingAutoCompletion}
```

**matchedAutoCompletion** may be different from **showingAutoCompletion** because of case sensitivity.

### bgColor

This property determines the background color of the edit.

```
dgsSetProperty(edit,"bgColor",bgColor)
```

- **bgColor** : An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgColorBlur

This property determines the background color of the edit when it is blurred.

```
dgsSetProperty(edit,"bgColorBlur",bgColorBlur)
```

- **bgColorBlur:**  An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md), leave to nil to use bgImage.

### bgImage

This property determines the background image of the edit.

```
dgsSetProperty(edit,"bgImage",bgImage)
```

- **bgImage** : A material element that serves as the background image of the edit (texture/shader/screen source/renderTarget).

### bgImageBlur

This property determines the background image of the edit when it is blurred.

```
dgsSetProperty(edit,"bgImageBlur",bgImageBlur)
```

- **bgImageBlur:**  A material element that serves as the background image of the edit(texture/shader/screen source/renderTarget), leave to nil to use bgImage.

### caretColor

This property determines the color of the caret

```
dgsSetProperty(edit,"caretColor",caretColor)
```

- **caretColor** : An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### caretHeight

This property determines what's the height of the caret.

```
dgsSetProperty(edit,"caretHeight",caretHeight)
```

- **caretHeight** : A float indicates what's the height of the caret.

### caretOffset

The offset of the caret of the edit.

```
dgsSetProperty(edit,"caretOffset",offset)
```

- **offset** : A float of the offset of the caret of the edit.

### caretPos

The position where the caret stays.

```
dgsSetProperty(edit,"caretPos",index)
```

- **index** : An integer of the index of the text that the caret stays.

### clearSelection

This property determines whether the text selection will be cleared when the edit blurs.

```
dgsSetProperty(edit,"clearSelection",clearSelection)
```

- **clearSelection** : A bool indicates whether the text selection will be cleared when the edit blurs.

### caretStyle

This is equivalent to [dgsEditSetCaretStyle](mta://scripting/client/functions/dgseditsetcaretstyle.md)/[dgsEditGetCaretStyle](mta://scripting/client/functions/dgseditgetcaretstyle.md).

This property allows us to change the style of caret of the edit. ( 0 is "|"; 1 is "_" )

Example(0):

This is Text|

Example(1):

This is Text_

```
dgsSetProperty(edit,"caretStyle",caretStyle)
```

- **caretStyle** : An integer of the caret style of the edit.

### caretThick

This property allows us to change the thickness of caret of the edit.

```
dgsSetProperty(edit,"caretThick",caretThick)
```

- **caretThick** : An integer of the thickness of the caret of the edit.

### caretWidth

This property allows us to change the caret width in caretStyle **"1"**.

```
dgsSetProperty(edit,"caretWidth",{caretWidth,caretDefaultWidth,relative})
```

- **caretWidth** : A float of the width of the caret of the edit. If **relative** is *true*, this will refer to font width of a character.

- **caretDefaultWidth** : A float of the width of the caret of the edit when there is no text to refer. If **relative** is **true**, this will refer to **textSize**.

- **relative** : A bool indicates whether caret width is relative or absolute.

### enableTabSwitch

This property determines whether we can use the key "tab" to switch to another edit.

```
dgsSetProperty(edit,"enableTabSwitch",enableTabSwitch)
```

- **enableTabSwitch** : A bool indicates whether we can use the key *tab* to switch to another edit.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(edit,"font",font)
```

- **font** : A [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the edit.

### masked

This is equivalent to [dgsEditSetMasked](mta://scripting/client/functions/dgseditsetmasked.md)/[dgsEditGetMasked](mta://scripting/client/functions/dgseditgetmasked.md)

```
dgsSetProperty(edit,"masked",masked)
```

- **masked** : A boolean value indicating whether masking is to be enabled or disabled.

### maskText

This property determines what the masked text will be, and the default is "*".

```
dgsSetProperty(edit,"maskText",maskText)
```

- **maskText** : A string that the masked text will be.

### maxLength

This is equivalent to [dgsEditGetMaxLength](mta://scripting/client/functions/dgseditgetmaxlength.md)/[dgsEditSetMaxLength](mta://scripting/client/functions/dgseditsetmaxlength.md)

```
dgsSetProperty(edit,"maxLength",maxLength)
```

- **maxLength** : An integer indicating the maximum number of characters that can be typed into the edit box.

### padding

This property determines the padding of the text.

```
dgsSetProperty(edit,"padding",{paddingX,paddingY})
```

- **paddingX** : An integer of 2D x padding value.

- **paddingY** : An integer of 2D y padding value.

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

### placeHolderTextSize

The scale of the place holder of the edit. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(edit,"textSize",{scaleX,scaleY})
```

- **scaleX** : A float of the 2D X scale of the place holder of the edit.

- **scaleY** : A float of the 2D Y scale of the place holder of the edit.

### readOnly

This is equivalent to [dgsEditSetReadOnly](mta://scripting/client/functions/dgseditsetreadonly.md)/[dgsEditGetReadOnly](mta://scripting/client/functions/dgseditgetreadonly.md).

```
dgsSetProperty(edit,"readOnly",readOnly)
```

- **readOnly** : A bool indicates whether the edit is only readable.

### readOnlyCaretShow

Whether the caret of edit will show/hide under read-only mode.

```
dgsSetProperty(edit,"readOnlyCaretShow",readOnlyCaretShow)
```

- **readOnlyCaretShow** : A bool indicates whether the caret is shown or hidden when the edit is read-only.

### renderTarget

This property stores a render target of the edit.

```
dgsSetProperty(edit,"renderTarget",renderTarget)
```

- **renderTarget** : A render target that is used to render the text.

### selectColorBlur

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the rectangle of text selection of the edit when blurred.

```
dgsSetProperty(edit,"selectColorBlur",selectColorBlur)
```

- **selectColorBlur** : An integer of the color of the rectangle of text selection of the edit when blurred.

### selectColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the rectangle of text selection of the edit.

```
dgsSetProperty(edit,"selectColor",selectColor)
```

- **selectColor** : An integer of the color of the rectangle of text selection of the edit.

### selectFrom

The position from which the text is selected.

```
dgsSetProperty(edit,"selectFrom",{index,line})
```

- **index** : An integer of the index of the text that selected from.

### shadow

The shadow text of the edit.

```
dgsSetProperty(edit,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the edit.

- **offsetY:** A float of the 2D Y offset of the shadow text of the edit.

- **color:** An integer of the color of the shadow text of the edit.

- **outline:** An integer of the outline style of the shadow text.

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(edit,"text",text)
```

- **text** : A *table* of the text of the edit.( Because of multi lines, I use table instead of string )

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the edit.

```
dgsSetProperty(edit,"textColor",textColor)
```

- **textColor** : An integer of the color of the text of the edit.

### textSize

The scale of the text of the edit. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(edit,"textSize",{scaleX,scaleY})
```

- **scaleX** : A float of the 2D X scale of the text of the edit.

- **scaleY** : A float of the 2D Y scale of the text of the edit.

### typingSound

Typing sound, nil for disabled. This is equivalent to [dgsEditSetTypingSound](mta://scripting/client/functions/dgseditsettypingsound.md)/[dgsEditGetTypingSound](mta://scripting/client/functions/dgseditgettypingsound.md)

```
dgsSetProperty(edit,"typingSound",typingSound)
```

- **typingSound:**  A string of the path/url of typing sound.

### typingSoundVolume

Typing sound, nil for disabled. This is equivalent to [dgsEditSetTypingSoundVolume](mta://scripting/client/functions/dgseditsettypingsoundvolume.md)/[dgsEditGetTypingSoundVolume](mta://scripting/client/functions/dgseditgettypingsoundvolume.md)

```
dgsSetProperty(edit,"typingSoundVolume",typingSoundVolume)
```

- **typingSoundVolume:**  A float of the volume of the typing sound. Range is from 0.0 to 1.0. This can go above 1.0 for amplification.

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

- dgs-dxedit

- [dgs-dxgridlist](mta://reference/misc/dgs-dxgridlist.md)

- [dgs-dximage](mta://reference/misc/dgs-dximage.md)

- [dgs-dxlabel](mta://reference/misc/dgs-dxlabel.md)

- [dgs-dxline](mta://reference/misc/dgs-dxline.md)

- [dgs-dxmemo](mta://reference/misc/dgs-dxmemo.md)

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
