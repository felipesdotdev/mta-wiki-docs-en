---
doc_id: "mta-wiki:11760"
title: "Dgs-dxscrollpane"
source_title: "Dgs-dxscrollpane"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxscrollpane"
revision_id: 78897
language: "en"
categories: []
---

# Dgs-dxscrollpane

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxscrollpane that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### basePointOffset

This property changes the offset of the base point where x=0, y=0. And by default, base point offset is 0, 0.

```
dgsSetProperty(scrollpane,"basePointOffset",{offsetX ,offsetY,relative})
```

- **offsetX :** A float of the 2D X offset relative to the position of the text of radio button, depends on relative.

- **offsetY:** A float of the 2D Y offset relative to the position of the text of radio button, depends on relative.

- **relative:** A bool of whether the offset is relative to the size of scroll pane or absolute pixels.

### bgColor

This property determines the background color of the scroll pane.

```
dgsSetProperty(scrollpane,"bgColor",bgColor)
```

- **bgColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgImage

This property determines the background image of the scroll pane. **Specify '[bgColor](mta://reference/misc/dgs-dxscrollpane.md)' before using bgImage**

```
dgsSetProperty(scrollpane,"bgImage",bgImage)
```

- **bgImage:** A material element that serves as the background image of the scroll pane (texture/shader/screen source/renderTarget).

### minViewSize

This property determines the minimal view size of scroll pane. By default, view size is determined by the content in the scroll pane.

```
dgsSetProperty(scrollpane,"minViewSize",{w,h,relative})
```

- **w:** A float if the minimal view size in width.

- **h:** A float if the minimal view size in height.

- **relative:** A bool of whether the minimal view size is relative to the size of scroll pane or absolute pixels.

### moveHardness

This property determines how hard will the scroll pane moves when scrolling.

```
dgsSetProperty(scrollpane,"moveHardness",{scrollHardness,dragHardness})
```

- **scrollHardness:** A float determins how hard will the scroll pane moves when scrolling with wheel ( should be larger than 0, lower than 1 ).

- **dragHardness:** A float determins how hard will the scroll pane moves when dragging with mouse ( should be larger than 0, lower than 1 ).

### padding

This property determines the content padding from 4 sides of element (left/top/right/bottom)

```
dgsSetProperty(scrollpane, "padding", {horizontal, vertical, relative})
```

- **horizontal:**  A float of the horizontal padding in pixels.

- **vertical:**  A float of the vertical padding in pixels.

### scrollBarThick

This property determines the thickness of scroll bar.

```
dgsSetProperty(scrollpane,"scrollBarThick",scrollBarThick)
```

- **scrollBarThick:** An integer of the thickness of scroll bar.

### scrollBarState

This property forces the visibility of scroll bar. *See [dgsScrollPaneSetScrollBarState](mta://scripting/client/functions/dgsscrollpanesetscrollbarstate.md)/[dgsScrollPaneGetScrollBarState](mta://scripting/client/functions/dgsscrollpanegetscrollbarstate.md)*

```
dgsSetProperty(scrollpane,"scrollBarState",{vertical,horizontal})
```

- **vertical:** A bool of the state of the vertical scroll bar.

- **horizontal:** A bool of the state of the horizontal scroll bar.

- **true:** Force to be visible

- **false:** Force to be invisible

- **nil:** Auto

### scrollBarLength

This property forces the length of the cursor of scroll bar to be static instead of being adjusted automatically.

```
dgsSetProperty(scrollpane,"scrollBarLength",{{VerticalLen,VerticalRelative},{HorizontalLen,HorizontalRelative}})
```

- **VerticalLen:** A float of the cursor length of the vertical scroll bar.

- **VerticalRelative:** A bool indicates whether the length is relative to the size of scroll bar or not.

- **HorizontalLen:** A float of the cursor length of the horizontal scroll bar.

- **HorizontalRelative:** A bool indicates whether the length is relative to the size of scroll bar or not.

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

- dgs-dxscrollpane

- [dgs-dxselector](mta://reference/misc/dgs-dxselector.md)

- [dgs-dxswitchbutton](mta://reference/misc/dgs-dxswitchbutton.md)

- [dgs-dxtabpanel](mta://reference/misc/dgs-dxtabpanel.md)

- [dgs-dxtab](mta://reference/misc/dgs-dxtab.md)

- [dgs-dxwindow](mta://reference/misc/dgs-dxwindow.md)

### Extra Properties For DGS Plugins
