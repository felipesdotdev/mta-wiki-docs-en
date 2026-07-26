---
doc_id: "mta-wiki:11762"
title: "Dgs-dxradiobutton"
source_title: "Dgs-dxradiobutton"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxradiobutton"
revision_id: 76175
language: "en"
categories: []
generated_at: "2026-07-26T16:11:23.135126+00:00"
---

# Dgs-dxradiobutton

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxradiobutton that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### alignment

Alignment of the text within the radiobutton.

The functions as follows are basic on this property.

[dgsRadioButtonSetHorizontalAlign](mta://scripting/client/functions/dgsradiobuttonsethorizontalalign.md)/[dgsRadioButtonGetHorizontalAlign](mta://scripting/client/functions/dgsradiobuttongethorizontalalign.md)

[dgsRadioButtonSetVerticalAlign](mta://scripting/client/functions/dgsradiobuttonsetverticalalign.md)/[dgsRadioButtonGetVerticalAlign](mta://scripting/client/functions/dgsradiobuttongetverticalalign.md)

```
dgsSetProperty(checkbx,"alignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the text within the radiobutton. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the text within the radiobutton. Can be "top", "center" or "bottom".

### buttonAlignment

This property determines alignment of the button of the radio button.

The functions as follows are basic on this property.

[dgsRadioButtonSetButtonAlign](mta://scripting/client/functions/dgsradiobuttonsetbuttonalign.md)/[dgsRadioButtonGetButtonAlign](mta://scripting/client/functions/dgsradiobuttongetbuttonalign.md)

```
dgsSetProperty(radiobutton,"buttonAlignment",buttonAlignment)
```

- **buttonAlignment** A string indicates the alignment of the button of radio button. Can be "left" or "right".

### buttonSide

This property determines side of the button of the radio button.

The functions as follows are basic on this property.

[dgsRadioButtonSetButtonSide](mta://scripting/client/functions/dgsradiobuttonsetbuttonside.md)/[dgsRadioButtonGetButtonSide](mta://scripting/client/functions/dgsradiobuttongetbuttonside.md)

```
dgsSetProperty(radiobutton,"buttonSide",buttonSide)
```

- **buttonSide** A string indicates the side of the button of radio button. Can be "left" or "right".

### buttonSize

This property determines the button size of the radio button.

```
dgsSetProperty(radiobutton,"buttonSize",{size,relative})
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
dgsSetProperty(radiobutton,"clip",clip)
```

- **clip:** If set to true, the parts of the text that don't fit within the bounding box will be cut off.

### colorUnchecked

This property determines the color of the icon under 3 conditions when the radio button is unchecked.

```
dgsSetProperty(radiobutton,"colorUnchecked",{ColorNormal,ColorHover,ColorClick})
```

- **ColorNormal:** An integer of the color of the icon under normal state. (unchecked)

- **ColorHover:** An integer of the color of the icon under hovering state. (unchecked)

- **ColorClick:** An integer of the color of the icon under clicked state. (unchecked)

### colorChecked

This property determines the color of the icon under 3 conditions when the radio button is checked.

```
dgsSetProperty(radiobutton,"colorChecked",{ColorNormal,ColorHover,ColorClick})
```

- **ColorNormal:** An integer of the color of the icon under normal state. (checked)

- **ColorHover:** An integer of the color of the icon under hovering state. (checked)

- **ColorClick:** An integer of the color of the icon under clicked state. (checked)

### colorCoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(radiobutton,"colorCoded",colorCoded)
```

- **colorCoded:** Set to true to enable embedded #FFFFFF color codes.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(radiobutton,"font",font)
```

- **font:** A string or a [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the radiobutton.

### imageUnchecked

This property determines the icon under 3 conditions when the radio button is unchecked.

```
dgsSetProperty(radiobutton,"imageUnchecked",{ImageNormal,ImageHover,ImageClick})
```

- **ImageNormal:** An image element of the icon under normal state. (unchecked)

- **ImageHover:** An image element of the icon under hovering state. (unchecked)

- **ImageClick:** An image element of the icon under clicked state. (unchecked)

### imageChecked

This property determines the icon under 3 conditions when the radio button is checked.

```
dgsSetProperty(radiobutton,"imageChecked",{ImageNormal,ImageHover,ImageClick})
```

- **ImageNormal:** An image element of the icon under normal state. (checked)

- **ImageHover:** An image element of the icon under hovering state. (checked)

- **ImageClick:** An image element of the icon under clicked state. (checked)

### shadow

The shadow text of the radiobutton.

```
dgsSetProperty(radiobutton,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the radiobutton.

- **offsetY:** A float of the 2D Y offset of the shadow text of the radiobutton.

- **color:** An integer of the color of the shadow text of the radiobutton.

- **outline:** A bool of the outline state of the shadow text.

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(radiobutton,"text",text)
```

- **text:** A string of the text of the radiobutton.

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the radiobutton.

```
dgsSetProperty(radiobutton,"textColor",textColor)
```

- **textColor:** An integer of the color of the text of the radiobutton.

### textOffset

The offset of the title text of radio button.

```
dgsSetProperty(radiobutton,"textOffset",{offsetX,offsetY,relative})
```

- **offsetX** : A float of the 2D X offset relative to the position of the text of radio button, depends on **relative**.

- **offsetY** : A float of the 2D Y offset relative to the position of the text of radio button, depends on **relative**.

- **relative** : A bool of whether the offset is relative or absolute.

### textPadding

This property determines the padding between the text and icon.

```
dgsSetProperty(radiobutton,"textPadding",textPadding)
```

- **textPadding:** A float of the distance from the icon to the text of the radio button.

### textSize

The scale of the text of the radiobutton. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(radiobutton,"textSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the radiobutton.

- **scaleY:** A float of the 2D Y scale of the text of the radiobutton.

### wordBreak

Whether the word-break is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(radiobutton,"wordBreak",wordBreak)
```

- **wordBreak:** If set to true, the text will wrap to a new line whenever it reaches the right side of the bounding box. If false, the text will always be completely on one line.

## Additional Property For Parent Element

### RadioButton

This property stores which radio button is selected.

```
dgsSetProperty(parent,"RadioButton",RadioButton)
```

- **RadioButton:** The radio button that is selected.

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

- dgs-dxradiobutton

- [dgs-dxscrollbar](mta://reference/misc/dgs-dxscrollbar.md)

- [dgs-dxscrollpane](mta://reference/misc/dgs-dxscrollpane.md)

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
