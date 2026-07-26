---
doc_id: "mta-wiki:12081"
title: "Dgs-dxtabpanel"
source_title: "Dgs-dxtabpanel"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxtabpanel"
revision_id: 74517
language: "en"
categories: []
---

# Dgs-dxtabpanel

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxtabpanel that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### bgColor

This property determines the default background color of the tab panel.

```
dgsSetProperty(tabpanel,"bgColor",bgColor)
```

- **bgColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgImage

This property determines the default background image of the tab panel.

```
dgsSetProperty(tabpanel,"bgImage",bgImage)
```

- **bgImage:** A material element that serves as the background image of the tab panel (texture/shader/screen source/renderTarget).

### font

This property determines the default font of tabs. This is equivalent to dgsSetFont/dgsGetFont. Learn More dxDrawText

```
dgsSetProperty(tabpanel,"font",font)
```

- **font:** A dx font element of the default text font of the tab panel.

### tabAlignment

This property determines the alignment of all tabs.

```
dgsSetProperty(tabpanel,"tabAlignment",tabAlignment)
```

- **tabAlignment:** A string determines the alignment of all tabs (NOT The Text Alignment). Available values are as follows:

- **"left"**:

- **"center"**:

- **"right"**:

### tabColor

This property determines the color of all tab buttons if not specified by [tabColor of tab](mta://reference/misc/dgs-dxtab.md). Different from **bgColor**

```
dgsSetProperty(tabpanel,"tabColor",{defaultColor,hoveringColor,selectedColor})
```

- **defaultColor:** An integer of the color of the normal tab button.

- **hoveringColor:** An integer of the color of the tab button which is hovered on.

- **selectedColor:** An integer of the color of the tab button which is selected.

### tabHeight

This property determines the height of tab.

```
dgsSetProperty(tabpanel,"tabHeight",{tabHeight,relative})
```

- **tabHeight:** A number of the height of the tab.

- **relative:** A bool of the relative state of the tab height.

### tabImage

This property determines the image of all tab buttons if not specified by [tabImage of tab](mta://reference/misc/dgs-dxtab.md). Different from **bgImage**

```
dgsSetProperty(tabpanel,"tabImage",{defaultImage,hoveringImage,selectedImage})
```

- **defaultImage:** A material element of the normal tab button. ( Passing a nil value can disable this option )

- **hoveringImage:** A material element of the tab button which is hovered on. ( Passing a nil value can disable this option )

- **selectedImage:** A material element of the tab button which is selected. ( Passing a nil value can disable this option )

### tabOffset

This property determines the offset of all tabs.

```
dgsSetProperty(tabpanel,"tabOffset",{tabOffset,relative})
```

- **tabOffset:** An number of the offset of all tabs.

- **relative:** A bool of the relative state of all tabs' offset.

### tabPadding

This property determines the distance between the horizontal border of tabs to its text's bounding box.

```
dgsSetProperty(tabpanel,"tabPadding",{tabPadding,relative})
```

- **tabPadding:** An number of the padding of the tab.

- **relative:** A bool of the relative state of the tab padding.

### tabGapSize

This property determines the distance between two tabs.

```
dgsSetProperty(tabpanel,"tabGapSize",{tabGapSize,relative})
```

- **tabGapSize:** An number of distance between two tabs.

- **relative:** A bool of the relative state of the tab gap size.

### tabLengthAll

This property stores the length of all tabs (You may crash tab panel if you modify this property).

```
dgsSetProperty(tabpanel,"tabLengthAll",tabLengthAll)
```

- **tabLengthAll:** A integer of the length of all tabs in pixels.

### showPos

This property stores the value of how many pixels does the tabs scroll to left.

```
dgsSetProperty(tabpanel,"showPos",showPos)
```

- **showPos:** A integer of how many pixels does the tabs scroll to left.

### scrollSpeed

If you created a lot of tabs in tab panel, you can scroll your wheel on the tabs to view the tabs that are out of range.

This property determines the scroll speed.

```
dgsSetProperty(tabpanel,"scrollSpeed",{scrollSpeed,relative})
```

- **scrollSpeed:** A number of scroll speed depends on **relative**.

- **relative:** A bool of the relative state of the **scrollSpeed**.[false: pixels/scroll,true: ratio/scroll]

### tabMaxWidth

This property restricts the maximum width of the tab.

```
dgsSetProperty(tabpanel,"tabMaxWidth",{tabMaxWidth,relative})
```

- **tabMaxWidth:** A number of the maximum width of the tab.

- **relative:** A bool of the relative state of the **tabMaxWidth**.

### tabMinWidth

This property restricts the minimum width of the tab.

```
dgsSetProperty(tabpanel,"tabMinWidth",{tabMinWidth,relative})
```

- **tabMinWidth:** A number of the minimum width of the tab.

- **relative:** A bool of the relative state of the **tabMinWidth**.

### selected

This property stores the index of selected tab.

```
dgsSetProperty(tabpanel,"selected",selected)
```

- **selected:** A number of the index of selected tab.

### shadow

The shadow text of the tab if not specified by tab.

```
dgsSetProperty(tabpanel,"shadow",{offsetX,offsetY,color})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the tab.

- **offsetY:** A float of the 2D Y offset of the shadow text of the tab.

- **color:** An integer of the color of the shadow text of the tab.

### renderTarget

This property stores the render target that is used to render the tab button.

```
dgsSetProperty(tabpanel,"renderTarget",renderTarget)
```

- **renderTarget:** A render target.

### preSelect

This property stores the index of the tab which your mouse is hovering on.

```
dgsSetProperty(tabpanel,"preSelect",preSelect)
```

- **preSelect:** A number of the index of the tab which your mouse is hovering on.

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

- dgs-dxtabpanel

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
