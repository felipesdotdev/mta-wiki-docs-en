---
doc_id: "mta-wiki:9674"
title: "Dgs-dxlabel"
source_title: "Dgs-dxlabel"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxlabel"
revision_id: 75164
language: "en"
categories: []
generated_at: "2026-07-26T16:12:33.367273+00:00"
---

# Dgs-dxlabel

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxlabel that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the text within the label.

The functions as follows are based on this property.

[dgsLabelSetHorizontalAlign](mta://scripting/client/functions/dgslabelsethorizontalalign.md)/[dgsLabelGetHorizontalAlign](mta://scripting/client/functions/dgslabelgethorizontalalign.md)

[dgsLabelSetVerticalAlign](mta://scripting/client/functions/dgslabelsetverticalalign.md)/[dgsLabelGetVerticalAlign](mta://scripting/client/functions/dgslabelgetverticalalign.md)

```
dgsSetProperty(label,"alignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the text within the label. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the text within the label. Can be "top", "center" or "bottom".

### clip

Whether the clip property is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(label,"clip",clip)
```

- **clip:** If set to true, the parts of the text that don't fit within the bounding box will be cut off.

### colorCoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(label,"colorCoded",colorCoded)
```

- **colorCoded:** Set to true to enable embedded #FFFFFF color codes.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(label,"font",font)
```

- **font:** A string or a [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the label.

### shadow

The shadow text of the label.

```
dgsSetProperty(label,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the label.

- **offsetY:** A float of the 2D Y offset of the shadow text of the label.

- **color:** An integer of the color of the shadow text of the label.

- **outline:** An integer of the outline style of the shadow text.

### subPixelPositioning

This property determines whether the **subPixelPositioning** is enabled or not, by default, it is disable. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

**subPixelPositioning** Will make positioning and resizing animation looks better, but you should know, it may blur your static text with unrounded position and size, or alignment.

If you are using dgs animation library, you'd better turn this on.

```
dgsSetProperty(label,"subPixelPositioning",subPixelPositioning)
```

- **subPixelPositioning:** A bool indicates whether to enable subPixelPositioning or not.

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(label,"text",text)
```

- **text:** A string of the text of the label.

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the label.

```
dgsSetProperty(label,"textColor",textColor)
```

- **textColor:** An integer of the color of the text of the label.

### textOffset

The offset of the text on label.

```
dgsSetProperty(label,"textOffset",{offsetX,offsetY,relative})
```

- **offsetX** : A float of the 2D X offset relative to the position of the label, depends on **relative**.

- **offsetY** : A float of the 2D Y offset relative to the position of the label, depends on **relative**.

- **relative** : A bool of whether the offset is relative or absolute.

### textSize

The scale of the text of the label. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(label,"textSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the label.

- **scaleY:** A float of the 2D Y scale of the text of the label.

### wordBreak

Whether the word-break is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(label,"wordBreak",wordBreak)
```

- **wordBreak:** If set to true, the text will wrap to a new line whenever it reaches the right side of the bounding box. If false, the text will always be completely on one line.

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

- dgs-dxlabel

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
