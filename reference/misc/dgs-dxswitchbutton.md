---
doc_id: "mta-wiki:12153"
title: "Dgs-dxswitchbutton"
source_title: "Dgs-dxswitchbutton"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxswitchbutton"
revision_id: 76922
language: "en"
categories: []
generated_at: "2026-07-26T16:11:23.476797+00:00"
---

# Dgs-dxswitchbutton

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxswitchbutton that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### clip

Whether the clip property is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(switchButton,"clip",clip)
```

- **clip:** If set to true, the parts of the text that don't fit within the bounding box will be cut off.

### cursorMoveSpeed

This property determines the cursor moving speed when switch button changes state.

```
dgsSetProperty(switchButton,"cursorMoveSpeed",cursorMoveSpeed)
```

- **cursorMoveSpeed:** A float of the cursor moving speed when switch button changes state.

### cursorWidth

This property determines the cursor width of switch button.

```
dgsSetProperty(switchButton,"cursorWidth",cursorWidth)
```

- **cursorWidth:** A float of the cursor width of switch button.

### cursorLength

This property determines the cursor length of switch button.

```
dgsSetProperty(switchButton,"cursorLength",cursorLength)
```

- **cursorLength:** A float of the cursor length of switch button.

### colorcoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(switchButton,"colorcoded",colorcoded)
```

- **colorcoded:** Set to true to enable embedded #FFFFFF color codes.

### colorOn

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the background color when the switch button turns on.

```
dgsSetProperty(switchButton,"colorOn",{normalColor,hoverColor,clickColor})
```

- **normalColor:** A integer of background color of turned on switch button.

- **hoverColor:** A integer of background color of turned on switch button when the mouse is hovering on it.

- **clickColor:** A integer of background color of turned on switch button when the mouse is clicked on it.

### colorOff

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the background color when the switch button turns off.

```
dgsSetProperty(switchButton,"colorOff",{normalColor,hoverColor,clickColor})
```

- **normalColor:** A integer of background color of turned off switch button.

- **hoverColor:** A integer of background color of turned off switch button when the mouse is hovering on it.

- **clickColor:** A integer of background color of turned off switch button when the mouse is clicked on it.

### cursorColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the cursor color.

```
dgsSetProperty(switchButton,"cursorColor",{normalColor,hoverColor,clickColor})
```

- **normalColor:** A integer of cursor color of the switch button.

- **hoverColor:** A integer of cursor color of the switch button when the mouse is hovering on it.

- **clickColor:** A integer of cursor color of the switch button when the mouse is clicked on it.

### cursorImage

The cursor image of switch button.

```
dgsSetProperty(switchButton,"cursorImage",{normalColor,hoverColor,clickColor})
```

- **normalImage:** A material of cursor image of the switch button.

- **hoverImage:** A material of cursor image of the switch button when the mouse is hovering on it.

- **clickImage:** A material of cursor image of the switch button when the mouse is clicked on it.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(switchButton,"font",font)
```

- **font:** A string or a [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the switch button.

### imageOn

The background image of switch button when the state is on.

```
dgsSetProperty(switchButton,"imageOn",{normalImage,hoverImage,clickImage})
```

- **normalImage:** A material of background image of turned on switch button.

- **hoverImage:** A material of background image of turned on switch button when the mouse is hovering on it.

- **clickImage:** A material of background image of turned on switch button when the mouse is clicked on it.

### imageOff

The background image of switch button when the state is off.(

```
dgsSetProperty(switchButton,"imageOff",{normalImage,hoverImage,clickImage})
```

- **normalImage:** A material of background image of turned off switch button.

- **hoverImage:** A material of background image of turned off switch button when the mouse is hovering on it.

- **clickImage:** A material of background image of turned off switch button when the mouse is clicked on it.

### shadow

The shadow text of the switch button.

```
dgsSetProperty(switchButton,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the switch button.

- **offsetY:** A float of the 2D Y offset of the shadow text of the switch button.

- **color:** An integer of the color of the shadow text of the switch button.

- **outline:** A bool of the outline state of the shadow text.

### state

This property indicates the state of switch button.

```
dgsSetProperty(switchButton,"state",state)
```

- **state:** A bool indicates the state of switch button.

- **true:** Turns on

- **false:** Turns off

### stateAnim

This stores the progress of cursor animation, which is not recommend to modify.

```
dgsSetProperty(switchButton,"stateAnim",stateAnim)
```

- **stateAnim:** A float of the cursor animation progress.

### style

This property determines the state of switch button.

```
dgsSetProperty(switchButton,"style",style)
```

- **style:** Mixed, available values are as follows:

- **false:** Default, a switch button with fading color when changing state.

- **1:** Split background color for turned on and off ( also split images ).

- **2:** Split background color for turned on and off ( not split images ).

- **3:** Do not split background color. Just switch gradually.

- **4:** No cursor. Just switch gradually.

### textOn

This property stores the text to be shown when the switch button turns on.

```
dgsSetProperty(switchButton,"textOn",textOn)
```

- **textOn:** A string of the text of the switch button.

### textOff

This property stores the text to be shown when the switch button turns off.

```
dgsSetProperty(switchButton,"textOff",textOff)
```

- **textOff:** A string of the text of the switch button.

### textColorOn

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text when the switch button turns on.

```
dgsSetProperty(switchButton,"textColor_t",textColor_t)
```

- **textColor_t:** An integer of the color of the text when the switch button turns on.

### textColorOff

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text when the switch button turns off.(State=false)

```
dgsSetProperty(switchButton,"textColor_f",textColor_f)
```

- **textColor_f:** An integer of the color of the text when the switch button turns off.

### textSize

The scale of the text of the switch button. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(switchButton,"textSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the switch button.

- **scaleY:** A float of the 2D Y scale of the text of the switch button.

### troughWidth

This property determines trough length of switch button.

```
dgsSetProperty(switchButton,"troughWidth",troughWidth)
```

- **troughWidth:** A float of the trough length of switch button.

### wordBreak

Whether the word-break is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(switchButton,"wordBreak",wordBreak)
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

- [dgs-dxlabel](mta://reference/misc/dgs-dxlabel.md)

- [dgs-dxline](mta://reference/misc/dgs-dxline.md)

- [dgs-dxmemo](mta://reference/misc/dgs-dxmemo.md)

- [dgs-dxprogressbar](mta://reference/misc/dgs-dxprogressbar.md)

- [dgs-dxradiobutton](mta://reference/misc/dgs-dxradiobutton.md)

- [dgs-dxscrollbar](mta://reference/misc/dgs-dxscrollbar.md)

- [dgs-dxscrollpane](mta://reference/misc/dgs-dxscrollpane.md)

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- dgs-dxswitchbutton

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
