---
doc_id: "mta-wiki:12082"
title: "Dgs-dxtab"
source_title: "Dgs-dxtab"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxtab"
revision_id: 74516
language: "en"
categories: []
generated_at: "2026-07-26T16:11:23.532958+00:00"
---

# Dgs-dxtab

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxtab that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### bgColor

This property determines the background color in the tab panel when current tab is selected, if this is not set, [bgColor of tab panel](mta://reference/misc/dgs-dxtabpanel.md) will be used. [[. Different from **tabColor**

```
dgsSetProperty(tab,"bgColor",bgColor)
```

- **bgColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgImage

This property determines the background image in the tab panel when current tab is selected, if this is not set, [bgImage of tab panel](mta://reference/misc/dgs-dxtabpanel.md) will be used. Different from **tabImage**

```
dgsSetProperty(tab,"bgImage",bgImage)
```

- **bgImage:** A material element that serves as the background image of the tab. ( Passing a nil value can disable this option )

### font

This property determines the default font of tabs. This is equivalent to dgsSetFont/dgsGetFont. Learn More dxDrawText

```
dgsSetProperty(tab,"font",font)
```

- **font:** A dx font element of the default text font of the tab panel.

### id

Tis property stores the id of the tab.

```
dgsSetProperty(tab,"id",id)
```

- **id** : The id of the tab.

### parent

This property stores the parent tab panel of tab.

```
dgsSetProperty(tab,"parent",parent)
```

- **parent:** The tab panel parent

### shadow

The shadow text of the tab. If not specified, **shadow** of tabpanel will be used.

```
dgsSetProperty(tab,"shadow",{offsetX,offsetY,color})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the tab.

- **offsetY:** A float of the 2D Y offset of the shadow text of the tab.

- **color:** An integer of the color of the shadow text of the tab.

### tabColor

This property determines the color of the tab button, if this is not set, [tabColor of tab panel](mta://reference/misc/dgs-dxtab.md) will be used. Different from **bgColor**

```
dgsSetProperty(tab,"tabColor",{defaultColor,hoveringColor,selectedColor})
```

- **defaultColor:** An integer of the color of the normal tab button.

- **hoveringColor:** An integer of the color of the tab button which is hovered on.

- **selectedColor:** An integer of the color of the tab button which is selected.

### tabImage

This property determines the image of the tab button, if this is not set, [tabImage of tab panel](mta://reference/misc/dgs-dxtab.md) . Different from **bgImage**

```
dgsSetProperty(tab,"tabImage",{defaultImage,hoveringImage,selectedImage})
```

- **defaultImage:** A material element of the normal tab button. ( Passing a nil value can disable this option )

- **hoveringImage:** A material element of the tab button which is hovered on. ( Passing a nil value can disable this option )

- **selectedImage:** A material element of the tab button which is selected. ( Passing a nil value can disable this option )

### text

This is equivalent to [dgsSetText](mta://scripting/client/functions/dgssettext.md)/[dgsGetText](mta://scripting/client/functions/dgsgettext.md).

```
dgsSetProperty(tab,"text",text)
```

- **text** : A string of the text of the tab button.

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the text of the tab button.

*Usage 1:*

```
dgsSetProperty(tab,"textColor",textColor)
```

- **textColor:** An integer of the color of the text of the tab button.

*Usage 2:*

```
dgsSetProperty(tab,"textColor",{ColorNormal,ColorHover,ColorClick})
```

- **ColorNormal:** An integer of the color of the text under normal state.

- **ColorHover:** An integer of the color of the text under hovering state.

- **ColorClick:** An integer of the color of the text under clicked state.

### textSize

The scale of the text of the tab button. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(tab,"textSize",{scaleX,scaleY})
```

- **scaleX** : A float of the 2D X scale of the text of the tab button.

- **scaleY** : A float of the 2D Y scale of the text of the tab button.

### width

This property stores the width of the tab (exclude tab gap).

```
dgsSetProperty(tab,"width",width)
```

- **width:** An integer indicates the width of the tab in pixels

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

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- dgs-dxtab

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
