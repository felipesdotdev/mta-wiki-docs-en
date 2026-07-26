---
doc_id: "mta-wiki:10741"
title: "Dgs-dxgridlist"
source_title: "Dgs-dxgridlist"
source_url: "https://wiki.multitheftauto.com/wiki/Dgs-dxgridlist"
revision_id: 82277
language: "en"
categories: []
generated_at: "2026-07-26T16:11:22.679707+00:00"
---

# Dgs-dxgridlist

[DGS](mta://reference/misc/dgs.md) Properties is always used to change the gui style and make it more fantastic.

This page shows the properties of dgs-dxgridlist that you could use.

## Main Functions

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

## Properties

### autoSort

This property determines whether auto sort is enabled. *See [dgsGridListSetAutoSortEnabled](mta://scripting/client/functions/dgsgridlistsetautosortenabled.md)/[dgsGridListGetAutoSortEnabled](mta://scripting/client/functions/dgsgridlistgetautosortenabled.md)*

```
dgsSetProperty(gridlist,"autoSort",autoSort)
```

- **autoSort:** A bool of auto sort state.

### backgroundOffset

This property determines the offset between the left border and row background.

```
dgsSetProperty(gridlist,"backgroundOffset",backgroundOffset)
```

- **backgroundOffset:** An integer of the offset between the left border and row background.

### bgColor

This property determines the background color of the grid list.

```
dgsSetProperty(gridlist,"bgColor",bgColor)
```

- **bgColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### bgImage

This property determines the background image of the grid list. To adjust the color of the image, use property **bgColor**

```
dgsSetProperty(gridlist,"bgImage",bgImage)
```

- **bgImage:** A material element that serves as the background image of the grid list (texture/shader/screen source/renderTarget).

### clip

Whether the clip property is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(gridlist,"clip",clip)
```

- **clip:** If set to true, the parts of the text that don't fit within the bounding box will be cut off.

### columnColor

This property determines the background color of the column of the grid list.

```
dgsSetProperty(gridlist,"columnColor",columnColor)
```

- **columnColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### columnData

This property stores column data.

```
dgsSetProperty(gridlist,"columnData",columnData)
```

- **columnData:** A table stores all column data.

**Data Structure**

```
{
	{ text, Width, AllWidthFront, Alignment, color, colorcoded, sizeX, sizeY, font },
	{ text, Width, AllWidthFront, Alignment, color, colorcoded, sizeX, sizeY, font },
	{ text, Width, AllWidthFront, Alignment, color, colorcoded, sizeX, sizeY, font },
	...
}
```

### columnHeight

This property determines the column height of the grid list.

```
dgsSetProperty(gridlist,"columnHeight",columnHeight)
```

- **columnHeight:** An integer of column height of the grid list.

### columnImage

This property determines the background image of the column of the grid list.

```
dgsSetProperty(gridlist,"columnImage",columnImage)
```

- **columnImage:** A material element that serves as the background image of the column of the grid list (texture/shader/screen source/renderTarget).

### columnMoveOffset

This property stores the move offset of column that is used to render.

```
dgsSetProperty(gridlist,"columnMoveOffset",columnMoveOffset)
```

- **columnMoveOffset:** A float stores the move offset of column that is used to render.

### columnOffset

This property determines the global offset between the left border and column text.

```
dgsSetProperty(gridlist,"columnOffset",columnOffset)
```

- **columnOffset:** An integer of offset of the column.

### columnRelative

This property determines whether the column length is relative or not. *See [dgsGridListSetColumnRelative](mta://scripting/client/functions/dgsgridlistsetcolumnrelative.md)/[dgsGridListGetColumnRelative](mta://scripting/client/functions/dgsgridlistgetcolumnrelative.md)*

```
dgsSetProperty(gridlist,"columnRelative",columnRelative)
```

- **columnRelative:** A bool of the relative state of the column length.

### columnShadow

The shadow text of the column.

```
dgsSetProperty(gridlist,"columnShadow",{offsetX,offsetY,color})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the column.

- **offsetY:** A float of the 2D Y offset of the shadow text of the column.

- **color:** An integer of the color of the shadow text of the column.

### columnTextColor

This property determines the color of the column text of the grid list.

```
dgsSetProperty(gridlist,"columnTextColor",columnTextColor)
```

- **columnTextColor:** An integer of the color that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md).

### columnTextPosOffset

This property adjusts the offset of the text of the column, which can solve text misplacing caused by font.

```
dgsSetProperty(gridlist,"columnTextPosOffset",{offsetX,offsetY})
```

- **offsetX:** A float of the 2D X offset of the text of the column.

- **offsetY:** A float of the 2D Y offset of the text of the column.

### columnTextSize

This property determines the scale of the column text of the grid list.

```
dgsSetProperty(gridlist,"columnTextSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the column.

- **scaleY:** A float of the 2D Y scale of the text of the column.

### columnWordBreak

This property determines whether word break property for column is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(gridlist,"columnWordBreak",columnWordBreak)
```

- **columnWordBreak:** A bool indicates whether the word break is enabled.

### colorCoded

Whether the color code is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(gridlist,"colorCoded",colorCoded)
```

- **colorCoded:** Set to true to enable embedded #FFFFFF color codes.

### defaultColumnOffset

This property determines offset of normal row column (is different from but works with columnOffset). *See [dgsGridListSetRowAsSection](mta://scripting/client/functions/dgsgridlistsetrowassection.md)*

```
dgsSetProperty(gridlist,"defaultColumnOffset",defaultColumnOffset)
```

- **defaultColumnOffset:** An integer of the offset of normal row column.

### defaultSortFunctions

This property determines the default sort function of grid list when clicking column.

```
dgsSetProperty(gridlist,"defaultSortFunctions",{lowerSortFunction,upperSortFunction})
```

- **lowerSortFunction:** A string of the lower sort function name.

- **upperSortFunction:** A string of the upper sort function name.

Here are three groups can be use:

- **greaterLower**/**greaterUpper**: Sorting directly with string.

- **numGreaterLowerNumFirst**/**numGreaterUpperNumFirst**: Sorting support number order with number first.

- **numGreaterLowerStrFirst**/**numGreaterUpperStrFirst**: Sorting support number order with string first.

- **longerLower**/**longerUpper**: Sorting according to the utf8 length of the string.

### defaultSortIcons

This property determines the icons of the default sort function.

```
dgsSetProperty(gridlist,"defaultSortIcons",{iconA,iconB})
```

- **iconA:** A string of the lower sort icon (**▲** By default).

- **iconB:** A string of the upper sort icon (**▼** By default).

### font

This is equivalent to [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)/[dgsGetFont](mta://scripting/client/functions/dgsgetfont.md). *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(gridlist,"font",font)
```

- **font:** A [dx font element](mta://reference/misc/element-dx-font.md) of the default text font of the gridlist.

### leading

This property determines the space between rows.

```
dgsSetProperty(gridlist,"leading",leading)
```

- **leading:** How many pixels between rows

### multiSelection

This property determines whether multi selection is enabled or not. *See [dgsGridListSetMultiSelectionEnabled](mta://scripting/client/functions/dgsgridlistsetmultiselectionenabled.md)/[dgsGridListGetMultiSelectionEnabled](mta://scripting/client/functions/dgsgridlistgetmultiselectionenabled.md)*

```
dgsSetProperty(gridlist,"multiSelection",multiSelection)
```

- **multiSelection:** A bool of the state of the multi selection.

### moveHardness

This property determines how hard will the grid list moves when scrolling.

```
dgsSetProperty(gridlist,"moveHardness",{scrollHardness,dragHardness})
```

- **scrollHardness:** A float determins how hard will the grid list moves when scrolling with wheel ( should be larger than 0, lower than 1 ).

- **dragHardness:** A float determins how hard will the grid list moves when dragging with mouse ( should be larger than 0, lower than 1 ).

### preSelect

This property stores the item id the cursor is hovering on.

```
dgsSetProperty(gridlist,"preSelect",{rowIndex,columnIndex})
```

- **rowIndex:** Row Index

- **columnIndex:** Column Index

### rowColor

This property determines the default 3 states' colors of row. *See [dgsGridListSetRowBackGroundColor](mta://scripting/client/functions/dgsgridlistsetrowbackgroundcolor.md)/[dgsGridListGetRowBackGroundColor](mta://scripting/client/functions/dgsgridlistgetrowbackgroundcolor.md)*. Note that this property does not affect rows that were created before the property was changed.

```
dgsSetProperty(gridlist,"rowColor",{colorDefault,colorHoving,colorSelected})
```

- **colorDefault:** An integer of the color of the row (Default State).

- **colorHoving:** An integer of the color of the row (Hoving State).

- **colorSelected:** An integer of the color of the row (Selected State).

### rowData

This property stores row data.

```
dgsSetProperty(gridlist,"rowData",rowData)
```

- **rowData:** A table stores all row data.

**Data Structure**

```
{

	[1] = {
		[-4] = columnOffset,				--column offset
		[-3] = {normal,hovering,selected},		--background image
		[-2] = true/false,				--selectable
		[-1] = true/false,				--clickable
		[0] = {normal,hovering,selected},		--background color
		[1] = {text,color,colorcoded,scalex,scaley,font,{image,color,imagex,imagey,imagew,imageh},unselectable,unclickable},	--Column 1
		[2] = {text,color,colorcoded,scalex,scaley,font,{image,color,imagex,imagey,imagew,imageh},unselectable,unclickable},	--Column 2
		...
	},		--Row 1
	[2] = {
		[-4] = columnOffset,				--column offset
		[-3] = {normal,hovering,selected},		--background image
		[-2] = true/false,				--selectable
		[-1] = true/false,				--clickable
		[0] = {normal,hovering,selected},		--background color
		[1] = {text,color,colorcoded,scalex,scaley,font,{image,color,imagex,imagey,imagew,imageh},unselectable,unclickable},	--Column 1
		[2] = {text,color,colorcoded,scalex,scaley,font,{image,color,imagex,imagey,imagew,imageh},unselectable,unclickable},	--Column 2
		...
	},		--Row 2
}
```

### rowHeight

This property determines the row height of the grid list.

```
dgsSetProperty(gridlist,"rowHeight",rowHeight)
```

- **rowHeight:** An integer of row height of the grid list.

### rowImage

This property determines the default 3 states' background image of row. *See [dgsGridListGetRowBackGroundImage](mta://scripting/client/functions/dgsgridlistgetrowbackgroundimage.md)/[dgsGridListSetRowBackGroundImage](mta://scripting/client/functions/dgsgridlistsetrowbackgroundimage.md)*. Note that this property does not affect rows that were created before the property was changed.

```
dgsSetProperty(gridlist,"rowImage",{normalImage,hoveringImage,selectedImage})
```

- **normalImage:** A texture of the image of the row (Normal State).

- **hoveringImage:** A texture of the image of the row (Hoving State).

- **selectedImage:** A texture of the image of the row (Selected State).

### rowImageStyle

This property determines the style of row background image.

```
dgsSetProperty(gridlist,"rowImageStyle",style)
```

- **style:** An integer of the style of row background image. Available values are as follows:

- **1:** Every item uses a complete background image.

- **2:** Every row uses a complete background image.

- **3:** Only the visible area of every row uses a complete background image.

### rowMoveOffset

This property stores the move offset of row that is used to render.

```
dgsSetProperty(gridlist,"rowMoveOffset",rowMoveOffset)
```

- **rowMoveOffset:** A float stores the move offset of row that is used to render.

### rowSelect

This property stores the selected rows.

```
dgsSetProperty(gridlist,"rowSelect",data)
```

- **data:** the data.

**Data Structure**

```
{
	[Column1] = {
		Row1,
		Row2,
		...
	},
	[Column2] = {
		Row1,
		Row2,
		...
	},
	...
}
```

### rowShadow

The shadow text of the row.

```
dgsSetProperty(gridlist,"rowShadow",{offsetX,offsetY,color})
```

- **offsetX:** A float of the 2D X offset of the shadow text of the row.

- **offsetY:** A float of the 2D Y offset of the shadow text of the row.

- **color:** An integer of the color of the shadow text of the row.

### rowShowUnclippedOnly

This property will force the grid list only show those unclipped row

```
dgsSetProperty(gridlist,"rowShowUnclippedOnly",rowShowUnclippedOnly)
```

- **rowShowUnclippedOnly:** A bool indicates if the only the unclipped rows will be shown in grid list.

### rowTextColor

This property determines the default color of the row text of the grid list.

```
dgsSetProperty(gridlist,"rowTextColor",rowTextColor)
```

- **rowTextColor:** An integer of the color of the row text that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md). Note that this property does not affect rows that were created before the property was changed.

```
dgsSetProperty(gridlist,"rowTextColor",{normalColor,hoveringColor,selectedColor})
```

- **normalColor:** A integer of the color of the row text that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md)(Normal State).

- **hoveringColor:** A integer of the color of the row text that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md)(Hoving State).

- **selectedColor:** A integer of the color of the row text that can be converted by [tocolor](mta://scripting/shared/functions/tocolor.md)(Selected State).

### rowTextPosOffset

This property adjusts the offset of the text of the row, which can solve text misplacing caused by font.

```
dgsSetProperty(gridlist,"rowTextPosOffset",{offsetX,offsetY})
```

- **offsetX:** A float of the 2D X offset of the text of the row.

- **offsetY:** A float of the 2D Y offset of the text of the row.

### rowTextSize

This property determines the default scale of the row text of the grid list. Note that this property does not affect rows that were created before the property was changed.

```
dgsSetProperty(gridlist,"rowTextSize",{scaleX,scaleY})
```

- **scaleX:** A float of the 2D X scale of the text of the row.

- **scaleY:** A float of the 2D Y scale of the text of the row.

### rowWordBreak

This property determines whether word break property for row is enabled or not. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(gridlist,"rowWordBreak",rowWordBreak)
```

- **rowWordBreak:** A bool indicates whether the word break is enabled.

### scrollBarAlignment

This property sets the alignment of the scroll bars in the grid list.

```
dgsSetProperty(gridlist, "scrollBarAlignment",{vertical})
```

- **vertical:** Specifies the alignment of the vertical scroll bar, which can be set to:

- **left:** Aligns the vertical scroll bar to the left of the grid list.

- **right:** Aligns the vertical scroll bar to the right of the grid list.

### scrollBarState

This property forces the visibility of scroll bar. *See [dgsGridListSetScrollBarState](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetScrollBarState&action=edit&redlink=1)/[dgsGridListGetScrollBarState](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetScrollBarState&action=edit&redlink=1)*

```
dgsSetProperty(gridlist,"scrollBarState",{vertical,horizontal})
```

- **vertical:** A bool of the state of the vertical scroll bar.

- **horizontal:** A bool of the state of the horizontal scroll bar.

- **true:** Force to be visible

- **false:** Force to be invisible

- **nil:** Auto

### scrollBarThick

This property determines the thickness of scroll bar.

```
dgsSetProperty(gridlist,"scrollBarThick",scrollBarThick)
```

- **scrollBarThick:** An integer of the thickness of scroll bar.

### sectionColumnOffset

This property determines offset of section row column (is different from but works with columnOffset). *See [dgsGridListSetRowAsSection](mta://scripting/client/functions/dgsgridlistsetrowassection.md)*

```
dgsSetProperty(gridlist,"sectionColumnOffset",sectionColumnOffset)
```

- **sectionColumnOffset:** An integer of the offset of section row column.

### sectionFont

This property determines the font of the text of which row is in section mode. *Learn More [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)*

```
dgsSetProperty(gridlist,"sectionFont",sectionFont)
```

- **sectionFont:** A [dx font element](mta://reference/misc/element-dx-font.md) of the text of which row is in section mode.

### selectionMode

This property stores current selection mode of grid list. *See [dgsGridListSetSelectionMode](mta://scripting/client/functions/dgsgridlistsetselectionmode.md)/[dgsGridListGetSelectionMode](mta://scripting/client/functions/dgsgridlistgetselectionmode.md)*

```
dgsSetProperty(gridlist,"selectionMode",selectionMode)
```

- **selectionMode:** The mode of the selection.  Can be the following values:

- **1:** row selection

- **2:** column selection

- **3:** cell selection

### selectedColumn

This property stores the index of which column the cursor is hovering. *See [dgsGridListGetEnterColumn](mta://scripting/client/functions/dgsgridlistgetentercolumn.md)*

```
dgsSetProperty(gridlist,"selectedColumn",selectedColumn)
```

- **columnHeight:** Column Index.

### sortColumn

This property determines target sort column. *See [dgsGridListSetSortColumn](mta://scripting/client/functions/dgsgridlistsetsortcolumn.md)*

```
dgsSetProperty(gridlist,"sortColumn",sortColumn)
```

- **sortColumn:** An integer of the specific column to be sorted by.

### sortEnabled

This property determines whether sort is enabled. *See [dgsGridListSetSortEnabled](mta://scripting/client/functions/dgsgridlistsetsortenabled.md)/[dgsGridListGetSortEnabled](mta://scripting/client/functions/dgsgridlistgetsortenabled.md)*

```
dgsSetProperty(gridlist,"sortEnabled",sortEnabled)
```

- **sortEnabled:** A bool of sort state.

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

- dgs-dxgridlist

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
