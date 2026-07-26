---
doc_id: "mta-wiki:11761"
title: "Dgs-dxcheckbox"
source_title: "Dgs-dxcheckbox"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxcheckbox"
revision_id: 76176
language: "en"
categories: []
generated_at: "2026-07-26T16:11:21.993760+00:00"
---

# Dgs-dxcheckbox

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxcheckbox that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the text within the checkbox.

The functions as follows are basic on this property.

[dgsCheckBoxSetHorizontalAlign](mta://scripting/client/functions/dgscheckboxsethorizontalalign.md)/[dgsCheckBoxGetHorizontalAlign](mta://scripting/client/functions/dgscheckboxgethorizontalalign.md)

[dgsCheckBoxSetVerticalAlign](mta://scripting/client/functions/dgscheckboxsetverticalalign.md)/[dgsCheckBoxGetVerticalAlign](mta://scripting/client/functions/dgscheckboxgetverticalalign.md)

```
dgsSetProperty(checkbx,"alignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the text within the checkbox. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the text within the checkbox. Can be "top", "center" or "bottom".

### buttonAlignment

This property determines alignment of the button of the check box.

The functions as follows are basic on this property.

[dgsCheckBoxSetButtonAlign](mta://scripting/client/functions/dgscheckboxsetbuttonalign.md)/[dgsCheckBoxGetButtonAlign](mta://scripting/client/functions/dgscheckboxgetbuttonalign.md)

```
dgsSetProperty(checkbox,"buttonAlignment",buttonAlignment)
```

- **buttonAlignment** A string indicates the alignment of the button of check box. Can be "left" or "right".

### buttonSide

This property determines side of the button of the check box.

The functions as follows are basic on this property.

[dgsCheckBoxSetButtonSide](mta://scripting/client/functions/dgscheckboxsetbuttonside.md)/[dgsCheckBoxGetButtonSide](mta://scripting/client/functions/dgscheckboxgetbuttonside.md)

```
dgsSetProperty(checkbox,"buttonSide",buttonSide)
```

- **buttonSide** A string indicates the side of the button of check box. Can be "left" or "right".

### buttonSize

This property determines the button size of the check box.

```
dgsSetProperty(checkbox,"buttonSize",{size,relative})
```

- **size:** A number of the size of the button on screen.

- **relative:** A bool indicates whether the size is relative or absolute.

```
dgsSetProperty(checkbox,"buttonSize",{width,height,relative})
```

- **width:** A number of the width of the button on screen.

- **height:** A number of the height of the button on screen.

- **relative:** A bool indicates whether the size is relative or absolute.

### clip

Whether the clip property is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(checkbox,"clip",clip)
```

- **clip:** If set to true, the parts of the text that don't fit within the bounding box will be cut off.

### colorIndeterminate

This property determines the color of the icon under 3 conditions when the check box is indeterminate.

```
dgsSetProperty(checkbox,"colorIndeterminate",{ColorNormal,ColorHover,ColorClick})
```

- **ColorNormal:** An integer of the color of the icon under normal state. (indeterminate)

- **ColorHover:** An integer of the color of the icon under hovering state. (indeterminate)

- **ColorClick:** An integer of the color of the icon under clicked state. (indeterminate)

### colorUnchecked

This property determines the color of the icon under 3 conditions when the check box is unchecked.

```
dgsSetProperty(checkbox,"colorUnchecked",{ColorNormal,ColorHover,ColorClick})
```

- **ColorNormal:** An integer of the color of the icon under normal state. (unchecked)

- **ColorHover:** An integer of the color of the icon under hovering state. (unchecked)

- **ColorClick:** An integer of the color of the icon under clicked state. (unchecked)

### colorChecked

This property determines the color of the icon under 3 conditions when the check box is checked.

```
dgsSetProperty(checkbox,"colorChecked",{ColorNormal,ColorHover,ColorClick})
```

- **ColorNormal:** An integer of the color of the icon under normal state. (checked)

- **ColorHover:** An integer of the color of the icon under hovering state. (checked)

- **ColorClick:** An integer of the color of the icon under clicked state. (checked)

### colorCoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(checkbox,"colorCoded",colorCoded)
```

- **colorCoded:** Set to true to enable embedded #FFFFFF color codes.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(checkbox,"font",font)
```

- **font:** A string or a [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the checkbox.

### imageUnchecked

This property determines the icon under 3 conditions when the check box is unchecked.

```
dgsSetProperty(checkbox,"imageUnchecked",{ImageNormal,ImageHover,ImageClick})
```

- **ImageNormal:** An image element of the icon under normal state. (unchecked)

- **ImageHover:** An image element of the icon under hovering state. (unchecked)

- **ImageClick:** An image element of the icon under clicked state. (unchecked)

### imageIndeterminate

This property determines the icon under 3 conditions when the check box is indeterminate.

```
dgsSetProperty(checkbox,"imageIndeterminate",{ImageNormal,ImageHover,ImageClick})
```

- **ImageNormal:** An image element of the icon under normal state. (indeterminate)

- **ImageHover:** An image element of the icon under hovering state. (indeterminate)

- **ImageClick:** An image element of the icon under clicked state. (indeterminate)

### imageChecked

This property determines the icon under 3 conditions when the check box is checked.

```
dgsSetProperty(checkbox,"imageChecked",{ImageNormal,ImageHover,ImageClick})
```

- **ImageNormal:** An image element of the icon under normal state. (checked)

- **ImageHover:** An image element of the icon under hovering state. (checked)

- **ImageClick:** An image element of the icon under clicked state. (checked)

### shadow

The shadow text of the checkbox.

```
dgsSetProperty(checkbox,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the checkbox.

- **offsetY:** A float of the 2D Y offset of the shadow text of the checkbox.

- **color:** An integer of the color of the shadow text of the checkbox.

- **outline:** A bool of the outline state of the shadow text.

### state

This property stores the state of the check box.

```
dgsSetProperty(checkbox,"state",state)
```

- **state:** A bool/nil of the state. Values can be as follows:

- **true:** Checked

- **false:** Unchecked

- **nil:** indeterminate

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(checkbox,"text",text)
```

- **text:** A string of the text of the checkbox.

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the checkbox.

```
dgsSetProperty(checkbox,"textColor",textColor)
```

- **textColor:** An integer of the color of the text of the checkbox.

### textOffset

The offset of the title text of check box.

```
dgsSetProperty(checkbox,"textOffset",{offsetX,offsetY,relative})
```

- **offsetX** : A float of the 2D X offset relative to the position of the text of check box, depends on **relative**.

- **offsetY** : A float of the 2D Y offset relative to the position of the text of check box, depends on **relative**.

- **relative** : A bool of whether the offset is relative or absolute.

### textPadding

This property determines the padding between the text and icon.

```
dgsSetProperty(checkbox,"textPadding",textPadding)
```

- **textPadding** A float of the distance from the icon to the text of the check box.

### textSize

The scale of the text of the checkbox. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(checkbox,"textSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the checkbox.

- **scaleY:** A float of the 2D Y scale of the text of the checkbox.

### wordBreak

Whether the word-break is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(checkbox,"wordBreak",wordBreak)
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

- dgs-dxcheckbox

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

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
