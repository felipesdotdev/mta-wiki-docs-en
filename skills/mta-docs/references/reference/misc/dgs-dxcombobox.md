---
doc_id: "mta-wiki:12352"
title: "Dgs-dxcombobox"
source_title: "Dgs-dxcombobox"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxcombobox"
revision_id: 77497
language: "en"
categories: []
---

# Dgs-dxcombobox

[DGS](https://wiki.multitheftauto.com/index.php?search=DGS) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxcombobox that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### arrow

This property determines the arrow material of the combo box.

```
dgsSetProperty(combobox,"arrow",arrow)
```

- **arrow:** A material element (texture/shader/screen).

### arrowSize

This property determines the size of the arrow of the combo box.

```
dgsSetProperty(combobox,"arrowSize",{arrowSizeX,arrowSizeY,relative})
```

- **arrowSizeX** : A number of the 2D X scale to the size of the arrow .

- **arrowSizeY** : A number of the 2D Y scale to the size of the arrow .

- **relative** : A bool of whether the size of the arrow is relative to its button size or absolute pixels.

### alignment

Alignment of the caption text within the combo box.

```
dgsSetProperty(combobox,"alignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the caption text within the combo box. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the caption text within the combo box. Can be "top", "center" or "bottom".

### autoHideAfterSelected

This property determines whether the drop down will be hide automatically after selected.

```
dgsSetProperty(combobox,"autoHideAfterSelected",autoHideAfterSelected)
```

- **autoHideAfterSelected:** A bool indicates whether the drop down will be hide automatically after selected.

### autoSort

This property determines whether auto sort is enabled. *See [dgsComboBoxSetAutoSortEnabled](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxSetAutoSortEnabled&action=edit&redlink=1)/[dgsComboBoxGetAutoSortEnabled](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxGetAutoSortEnabled&action=edit&redlink=1)*

```
dgsSetProperty(combobox,"autoSort",autoSort)
```

- **autoSort:** A bool of auto sort state.

### bgColor

This property determines the background color of the combo box (behind items).

```
dgsSetProperty(combobox,"bgColor",bgColor)
```

- **bgColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgImage

This property determines the background image of the combo box (behind items).

```
dgsSetProperty(combobox,"bgImage",bgImage)
```

- **bgImage:** A material element that serves as the background image of the combo box (texture/shader/screen source/renderTarget).

### buttonLen

This property stores the width of the arrow button.

```
dgsSetProperty(combobox,"buttonLen",{buttonLen,relative})
```

- **buttonLen:** A float of the width of arrow button, which is affected by **relative**.

- **relative:** If set to *true*, **buttonLen** will range from 0 to 1 relative to combo box's height, otherwise the **buttonLen** will be absolute pixels.

### captionEdit

This property stores the caption edit when the caption is editable with [dgsComboBoxSetEditEnabled](mta://scripting/client/functions/dgscomboboxseteditenabled.md).

```
dgsSetProperty(combobox,"captionEdit",captionEdit)
```

- **captionEdit:** A dgs-dxedit element.

### caption

This property stores the caption text of combo box.

```
dgsSetProperty(combobox,"caption",caption)
```

- **caption:** A string of the caption text of the combo box.

### clip

Whether the clip property is enabled (include caption text and item text). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(combobox,"clip",clip)
```

- **clip:** If set to true, the parts of the text that don't fit within the bounding box will be cut off.

### color

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the background of the combobox (behind arrow).

```
dgsSetProperty(combobox,"color",{normalColor,hoveringColor,clickedColor})
```

- **normalColor:** An integer of the color of the combobox ( neither selected nor clicked by mouse ).

- **hoveringColor:** An integer of the color of the combobox which is selected.

- **clickedColor:** An integer of the color of the comboox which is clicked.

### colorcoded

Whether the color code is enabled (include caption text and item text). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(combobox,"colorcoded",colorcoded)
```

- **colorcoded:** Set to true to enable embedded #FFFFFF color codes.

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(combobox,"font",font)
```

- **font:** A string or a [dx font element](mta://reference/misc/element-dx-font.md) of the text font of the combo box.

### scrollBarThick

This property determines the thickness of scroll bar.

```
dgsSetProperty(combobox,"scrollBarThick",scrollBarThick)
```

- **scrollBarThick:** An integer of the thickness of scroll bar.

### shadow

The shadow of the text of the combo box.

```
dgsSetProperty(combobox,"shadow",{offsetX,offsetY,color,outline})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the combo box.

- **offsetY:** A float of the 2D Y offset of the shadow text of the combo box.

- **color:** An integer of the color of the shadow text of the combo box.

- **outline:** A bool of the outline state of the shadow text.

### myBox

Combo box is composed by dgs-dxcombobox and dgs-dxcombobox-Box. This property stores the dgs-combobox-Box of dgs-dxcombobox.

```
dgsSetProperty(combobox,"myBox",myBox)
```

- **myBox:** A dgs-dxcombobox-box element.

### image

The image of combo box ( under arrow ).

```
dgsSetProperty(combobox,"image",{normalImage,hoveringImage,clickedImage})
```

- **normalImage:** A texture element of the background of the combobox ( no mouse enter and no mouse click ).

- **hoveringImage:** A texture element of the background of the combobox which is selected.

- **clickedImage:** A texture element of the background of the combobox which is clicked.

### itemAlignment

Alignment of the item text within the combo box.

```
dgsSetProperty(combobox,"itemAlignment",{alignX,alignY})
```

- **alignX:** Horizontal alignment of the item text within the combo box. Can be "left", "center" or "right".

- **alignY:** Vertical alignment of the item text within the combo box. Can be "top", "center" or "bottom".

### itemTextPadding

This property determines the item text padding of combo box.

```
dgsSetProperty(combobox,"itemTextPadding",{paddingX,paddingY})
```

- **paddingX** : An integer of 2D x padding value.

- **paddingY** : An integer of 2D y padding value.

### itemColor

This property determines the 3 states' back ground colors of item.

```
dgsSetProperty(combobox,"itemColor",{colorNormal,colorHoving,colorSelected})
```

- **colorNormal:** An integer of the color of the item (Normal State).

- **colorHoving:** An integer of the color of the item (Hoving State).

- **colorSelected:** An integer of the color of the item (Selected State).

### itemData

This property stores item data.

```
dgsSetProperty(gridlist,"itemData",itemData)
```

- **columnData:** A table stores all item data.

**Item Structure**

```
{
	 textColor	BackGround Image			BackGround Color			Text	
	{[-2]=color,	[-1]={normal,hovering,selected},	[0]={normal,hovering,selected},		text	},
	{[-2]=color,	[-1]={normal,hovering,selected},	[0]={normal,hovering,selected},		text	},
	{[-2]=color,	[-1]={normal,hovering,selected},	[0]={normal,hovering,selected},		text	},
	{	...												},
}
]]
```

### itemImage

This property determines the 3 states' background image of item.

```
dgsSetProperty(combobox,"itemImage",{imageNormal,imageHoving,imageSelected})
```

- **imageNormal:** A texture of the image of the row (Normal State).

- **imageHoving:** A texture of the image of the row (Hoving State).

- **imageSelected:** A texture of the image of the row (Selected State).

### itemMoveOffset

This property stores the move offset of item that is used to render.

```
dgsSetProperty(combobox,"itemMoveOffset",itemMoveOffset)
```

- **itemMoveOffset:** A float stores the move offset of item that is used to render.

### itemTextColor

This property determines the color of the item text of the combo box.

```
dgsSetProperty(combobox,"itemTextColor",itemTextColor)
```

- **itemTextColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### itemTextSize

This property determines the scale of the item text of the combo box.

```
dgsSetProperty(combobox,"itemTextSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the item.

- **scaleY:** A float of the 2D Y scale of the text of the item.

### listState

This property stores the state of combo box which determines whether the combo box is opened(1) or closed(-1).
See: [dgsComboBoxGetState](mta://scripting/client/functions/dgscomboboxgetstate.md)/[dgsComboBoxSetState](mta://scripting/client/functions/dgscomboboxsetstate.md)

```
dgsSetProperty(combobox,"listState",listState)
```

- **listState:** An integer of the state of combo box.

### moveHardness

This property determines how hard will the combo box moves when scrolling.

```
dgsSetProperty(combobox,"moveHardness",moveHardness)
```

- **moveHardness:** A float determins how hard will the combo box moves when scrolling ( should be larger than 0, lower than 1 ).

### scrollbar

This property stores the scroll bar of combo box.

```
dgsSetProperty(combobox,"scrollbar",scrollbar)
```

- **scrollbar:** a dgs-dxscrollbar element.

### select

This property stores the selected item of combo box.

```
dgsSetProperty(combobox,"select",select)
```

- **select:** A integer of the index of selected item .

### textColor

The color which can be translated by [tocolor](mta://scripting/shared/functions/tocolor.md) of the caption text of the combo box.

```
dgsSetProperty(combobox,"textColor",textColor)
```

- **textColor:** An integer of the color of the text of the combo box.

### textPadding

This property determines the caption text padding of combo box.

```
dgsSetProperty(combobox,"textPadding",{paddingX,paddingY})
```

- **paddingX** : An integer of 2D x padding value.

- **paddingY** : An integer of 2D y padding value.

### textSize

The scale of the capiton text of the combo box. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(combobox,"textSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the combo box.

- **scaleY:** A float of the 2D Y scale of the text of the combo box.

### textBox

This property determines whether the **caption** of combo box is enabled or not.

```
dgsSetProperty(combobox,"textBox",textBox)
```

- **textBox:** A bool indicates whether the **caption** of combo box is enabled or not.

### wordBreak

Whether the word-break of capiton text is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(capiton ,"wordBreak",wordbreak)
```

- **wordBreak:** If set to true, the text will wrap to a new line whenever it reaches the right side of the bounding box. If false, the text will always be completely on one line.

## Property of dgs-dxcombobox-Box

### myCombo

Combo box is composed by dgs-dxcombobox and dgs-dxcombobox-Box. This property stores the dgs-combobox of dgs-dxcombobox-Box.

```
dgsSetProperty(myCombo,"myCombo",myCombo)
```

- **myComboyBox:** A dgs-dxcombobox element.

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

- dgs-dxcombobox

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
