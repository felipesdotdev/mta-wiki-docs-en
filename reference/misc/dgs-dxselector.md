---
doc_id: "mta-wiki:13020"
title: "Dgs-dxselector"
source_title: "Dgs-dxselector"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxselector"
revision_id: 71993
language: "en"
categories: []
generated_at: "2026-07-26T16:11:23.395607+00:00"
---

# Dgs-dxselector

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxselector that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the text within the selector.

The functions as follows are based on this property.

[dgsSelectorSetHorizontalAlign](https://wiki.multitheftauto.com/index.php?title=DgsSelectorSetHorizontalAlign&action=edit&redlink=1)/[dgsSelectorGetHorizontalAlign](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetHorizontalAlign&action=edit&redlink=1)

[dgsSelectorSetVerticalAlign](https://wiki.multitheftauto.com/index.php?title=DgsSelectorSetVerticalAlign&action=edit&redlink=1)/[dgsSelectorGetVerticalAlign](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetVerticalAlign&action=edit&redlink=1)

```
dgsSetProperty(selector,"alignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the text within the selector. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the text within the selector. Can be "top", "center" or "bottom".

### clip

Whether the clip property is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(selector,"clip",clip)
```

- **clip:** If set to true, the parts of the text that don't fit within the bounding box will be cut off.

### colorcoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(selector,"colorcoded",colorcoded)
```

- **colorcoded:** Set to true to enable embedded #FFFFFF color codes.

### enableScroll

Enable/disable mouse wheel scroll items.

```
dgsSetProperty(selector,"enableScroll",enableScroll)
```

- **enableScroll:** A bool indicates whether to enable wheel scrolling on selector.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(selector,"font",font)
```

- **font:** A string or a [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the selector.

### isHorizontal

This proeprty determines whether the selector is horizontal or vertical.

```
dgsSetProperty(selector,"isHorizontal",isHorizontal)
```

- **isHorizontal:** A bool indicates whether the selector is horizontal or vertical.

### isReversed

This property determines whether the selector is reversed ( mirrorred ).

```
dgsSetProperty(selector,"isReversed",isReversed)
```

- **isReversed:** A bool indicates whether the selector is reversed ( mirrorred ).

### itemData

This property stores item data.

```
dgsSetProperty(selector,"itemData",itemData)
```

- **itemData:** A table stores all item data.

**Data Structure:**

```
{
	{text,alignment,color,colorcoded,sizex,sizey,font,translationTest,data,imageData},
	{text,alignment,color,colorcoded,sizex,sizey,font,translationTest,data,imageData},
	{text,alignment,color,colorcoded,sizex,sizey,font,translationTest,data,imageData},
}
```

### itemTextColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the item text of the selector.

```
dgsSetProperty(selector,"itemTextColor",itemTextColor)
```

- **itemTextColor:** An integer of the color of the text of the selector.

### itemTextSize

The scale of the item text of the selector. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(selector,"itemTextSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the item text of the selector.

- **scaleY:** A float of the 2D Y scale of the item text of the selector.

### placeHolder

This property determines what text will be when there's no items in selector

```
dgsSetProperty(selector,"placeHolder",placeHolder)
```

- **placeHolder:** A string of the text of the placeHolder of the selector.

### select

This property stores the selected item of the selector.

```
dgsSetProperty(selector,"select",select)
```

- **select:** A integer of the index of selected item .

### selectorSize

This property determines the size of selector button.

```
dgsSetProperty(selector,"selectorSize",{selectorSizeX,selectorSizeY,relative})
```

- **selectorSizeX:** A float of the 2D X size of selector button, set to *nil* to use **selectorSizeY**.

- **selectorSizeY:** A float of the 2D Y size of selector button, set to *nil* to use **selectorSizeX**.

- **relative:** A bool of whether the selectorSize is relative to the size of selector or absolute pixels.

### selectorText

The text of selector button of the selector.

```
dgsSetProperty(selector,"selectorText",{selectorTextLeft,selectorTextRight})
```

- **selectorTextLeft:** A string of the text of left selector button of the selector.

- **selectorTextRight:** A string of the text of right selector button of the selector.

### selectorTextColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of selector button of the selector.

```
dgsSetProperty(selector,"selectorTextColor",{normalColor,hoveringColor,clickedColor})
```

- **normalColor:** An integer of the color of the text of selector button of the selector ( neither hovering nor clicked by mouse ).

- **hoveringColor:** An integer of the color of the text of selector button of the selector which is hovering.

- **clickedColor:** An integer of the color of the text of selector button of the selector which is clicked.

### selectorTextSize

The scale of the text of the button of the selector. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(selector,"selectorTextSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the selector button of the selector.

- **scaleY:** A float of the 2D Y scale of the text of the selector button of the selector.

### shadow

The shadow text of the selector.

```
dgsSetProperty(selector,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the selector.

- **offsetY:** A float of the 2D Y offset of the shadow text of the selector.

- **color:** An integer of the color of the shadow text of the selector.

- **outline:** A bool of the outline state of the shadow text.

### subPixelPositioning

This property determines whether the **subPixelPositioning** is enabled or not, by default, it is disable. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

**subPixelPositioning** Will make positioning and resizing animation looks better, but you should know, it may blur your static text with unrounded position and size, or alignment.

If you are using dgs animation library, you'd better turn this on.

```
dgsSetProperty(selector,"subPixelPositioning",subPixelPositioning)
```

- **subPixelPositioning:** A bool indicates whether to enable subPixelPositioning or not.

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(selector,"text",text)
```

- **text:** A string of the text of the selector.

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the selector.

```
dgsSetProperty(selector,"textColor",textColor)
```

- **textColor:** An integer of the color of the text of the selector.

### textSize

The scale of the text of the selector. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(selector,"textSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the selector.

- **scaleY:** A float of the 2D Y scale of the text of the selector.

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

- [dgs-dxmemo](mta://reference/misc/dgs-dxmemo.md)

- [dgs-dxprogressbar](mta://reference/misc/dgs-dxprogressbar.md)

- [dgs-dxradiobutton](mta://reference/misc/dgs-dxradiobutton.md)

- [dgs-dxscrollbar](mta://reference/misc/dgs-dxscrollbar.md)

- [dgs-dxscrollpane](mta://reference/misc/dgs-dxscrollpane.md)

- dgs-dxselector

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
