---
doc_id: "mta-wiki:13634"
title: "Dgs-dxline"
source_title: "Dgs-dxline"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxline"
revision_id: 74321
language: "en"
categories: []
generated_at: "2026-07-26T16:11:22.817932+00:00"
---

# Dgs-dxline

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxline that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the default color of the line. If the color of item is not specified, this color will be used.

```
dgsSetProperty(line,"color",color)
```

- **color:** An integer of the color of the line.

### lineData

A table stores the line data of line

```
dgsSetProperty(line,"lineData",lineData)
```

- **lineData:** A table stores all line data.

**Data Structure**

```
--- If StartXY don't exist, will use last endXY or 0,0
{
	{ startX, startY, endX, endY, width, color, relative },
	{ startX, startY, endX, endY, width, color, relative },
	...
}
```

### lineWidth

An float of the default width of line. If the width of item is not specified, this width will be used.

```
dgsSetProperty(line,"lineWidth",lineWidth)
```

- **lineWidth:** A float of the width.

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

- dgs-dxline

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
