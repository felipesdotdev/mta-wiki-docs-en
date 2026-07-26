---
doc_id: "mta-wiki:10783"
title: "DGS OOP Class"
source_title: "DGS OOP Class"
source_url: "https://wiki.multitheftauto.com/wiki/DGS_OOP_Class"
revision_id: 78901
language: "en"
categories: []
generated_at: "2026-07-26T16:11:19.746263+00:00"
---

# DGS OOP Class

DGS provides not only POP ( Procedure Oriented Programming ) but also [OOP](mta://tutorials/oop.md) ( Object Oriented Programming ). This page introduces [OOP](mta://tutorials/oop.md) of dgs.

## Structure

When using DGS [OOP](mta://tutorials/oop.md), DGS objects to be operated are no longer elements, instead, they will be tables ( table is the only type whose call methods can be defined in lua ) .
Here is the structure of DGS OOP Object:

```
DGSObject = {
	DGSElement = DGSElement -- The actual dgs element
	function1,
	function2,
	...
}
```

- **The built-in functions are non-modifiable**

- **Any variable of the table are get/set via [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)/[dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md) ( Exclude DGSElement )**

- **After importing DGS OOP Class, there is a table called : *DGSClass***

## Get Started

Instead of using

```
label = exports.dgs:dgsCreateLabel(0, 0, 0.5, 0.1, "text", true)
```

```
DGS = exports.dgs
 label = DGS:dgsCreateLabel(0,0,0.5,0.1,"text",true)
```

```
loadstring(exports.dgs:dgsImportFunction())()-- load functions
 label = dgsCreateLabel(0,0,0.5,0.1,"text",true) --create a label
```

We provides Object Oriented Programming

```
loadstring(exports.dgs:dgsImportOOPClass())()-- load OOP class
 window = dgsWindow(0,0,0.5,0.1,"test",true) --create a window with oop
 label = window:dgsLabel(0,0,1,1,"label",true) --create a label inside the window
 label.text = "DGS OOP Test" --set text
```

**Notice:** When you are going to create a child element, there is no need to pass **parent** as an argument into the function, because the parent dgs element is the function caller.

This is the **Wrong** Usage:

```
loadstring(exports.dgs:dgsImportOOPClass())()-- load OOP class
 window = dgsWindow(0,0,0.5,0.1,"test",true) --create a window with oop
 label = dgsLabel(0,0,1,1,"label",true,window) --create a label inside the window ( Wrong )
 label.text = "DGS OOP Test" --set text
```

This is the **Correct** Usage:

```
loadstring(exports.dgs:dgsImportOOPClass())()-- load OOP class
 window = dgsWindow(0,0,0.5,0.1,"test",true) --create a window with oop
 label = window:dgsLabel(0,0,1,1,"label",true) --create a label inside the window ( Correct )
 label.text = "DGS OOP Test" --set text
```

## Special

For Position and Size, we have a more convenient method to do.

```
loadstring(exports.dgs:dgsImportOOPClass())()-- load OOP class
 window = dgsWindow(0,0,0.5,0.1,"test",true) --create a window with oop
 window.position.x = 0.2 -- For relative position
 window.position.relative = false -- Change to absolute position
 window.position.x = 10 -- For absolute position
 window.size.relative = false
 window.size.w = 400
```

## Functions

### Creation Functions

| OOP Functions | POP Functions |
| --- | --- |
| dgs3DInterface | dgsCreate3DInterface |
| dgs3DText | dgsCreate3DText |
| dgsBrowser | dgsCreateBrowser |
| dgsButton | dgsCreateButton |
| dgsCheckBox | dgsCreateCheckBox |
| dgsComboBox | dgsCreateComboBox |
| dgsDetectArea | dgsCreateDetectArea |
| dgsEdit | dgsCreateEdit |
| dgsGridList | dgsCreateGridList |
| dgsImage | dgsCreateImage |
| dgsLabel | dgsCreateLabel |
| dgsMemo | dgsCreateMemo |
| dgsProgressBar | dgsCreateProgressBar |
| dgsRadioButton | dgsCreateRadioButton |
| dgsScrollBar | dgsCreateScrollBar |
| dgsScrollPane | dgsCreateScrollPane |
| dgsSwitchButton | dgsCreateSwitchButton |
| dgsTabPanel | dgsCreateTabPanel |
| dgsWindow | dgsCreateWindow |

### Non Object Functions

| OOP Functions | POP Functions |
| --- | --- |
| isStyleAvailable | dgsIsStyleAvailable |
| getLoadedStyleList | dgsGetLoadedStyleList |
| setCurrentStyle | dgsSetCurrentStyle |
| getCurrentStyle | dgsGetCurrentStyle |
| getScreenSize | guiGetScreenSize |
| setInputEnabled | guiSetInputEnabled |
| getInputEnabled | guiGetInputEnabled |
| setRenderSetting | dgsSetRenderSetting |
| getRenderSetting | dgsGetRenderSetting |
| getLayerElements | dgsGetLayerElements |
| addEasingFunction | dgsAddEasingFunction |
| easingFunctionExists | dgsEasingFunctionExists |
| removeEasingFunction | dgsRemoveEasingFunction |
| getSystemFont | dgsGetSystemFont |
| setSystemFont | dgsSetSystemFont |
| translationTableExists | dgsTranslationTableExists |
| setTranslationTable | dgsSetTranslationTable |
| setAttachTranslation | dgsSetAttachTranslation |

### General Functions

| OOP Functions | POP Functions |
| --- | --- |
| getPosition | dgsGetPosition |
| setPosition | dgsSetPosition |
| getParent | dgsGetParent |
| setParent | dgsSetParent |
| getChild | dgsGetChild |
| getChildren | dgsGetChildren |
| getSize | dgsGetSize |
| setSize | dgsSetSize |
| getType | dgsGetType |
| setLayer | dgsSetLayer |
| getLayer | dgsSetLayer |
| setCurrentLayerIndex | dgsSetCurrentLayerIndex |
| getCurrentLayerIndex | dgsGetCurrentLayerIndex |
| getProperty | dgsGetProperty |
| setProperty | dgsSetProperty |
| getProperties | dgsGetProperties |
| setProperties | dgsSetProperties |
| getVisible | dgsGetVisible |
| setVisible | dgsGetVisible |
| getEnabled | dgsGetEnabled |
| setEnabled | dgsSetEnabled |
| getSide | dgsGetSide |
| setSide | dgsSetSide |
| getAlpha | dgsGetAlpha |
| setAlpha | dgsSetAlpha |
| getFont | dgsGetFont |
| setFont | dgsSetFont |
| getText | dgsGetText |
| setText | dgsSetText |
| bringToFront | dgsBringToFront |
| moveToBack | dgsMoveToBack |
| focus | dgsFocus |
| blur | dgsBlur |
| simulateClick | dgsSimulateClick |
| animTo | dgsAnimTo |
| isAniming | dgsIsAniming |
| stopAniming | dgsStopAniming |
| moveTo | dgsMoveTo |
| isMoving | dgsIsMoving |
| stopMoving | dgsStopMoving |
| sizeTo | dgsSizeTo |
| isSizing | dgsIsSizing |
| stopSizing | dgsStopSizing |
| alphaTo | dgsAlphaTo |
| isAlphaing | dgsIsAlphaing |
| stopAlphaing | dgsStopAlphaing |
| getPostGUI | dgsGetPostGUI |
| setPostGUI | dgsSetPostGUI |
| destroy | destroyElement |
| isElement | isElement |
| getElement | self.dgsElement |
| addMoveHandler | dgsAddMoveHandler |
| removeMoveHandler | dgsRemoveMoveHandler |
| isMoveHandled | dgsIsMoveHandled |
| addSizeHandler | dgsAddSizeHandler |
| removeSizeHandler | dgsRemoveSizeHandler |
| isSizeHandled | dgsIsSizeHandled |
| attachToTranslation | dgsAttachToTranslation |
| detachFromTranslation | dgsDetachFromTranslation |
| getTranslationName | dgsGetTranslationName |
| on | addEventHandler (Handled By DGS) |
| removeOn | removeEventHandler (Handled By DGS) |

### Window

| OOP Functions | POP Functions |
| --- | --- |
| setSizable | dgsWindowSetSizable |
| setMovable | dgsWindowSetMovable |
| close | dgsCloseWindow |
| setCloseButtonEnabled | dgsWindowSetCloseButtonEnabled |
| getCloseButtonEnabled | dgsWindowGetCloseButtonEnabled |
| getCloseButton | dgsWindowGetCloseButton |

### 3D Interface

| OOP Functions | POP Functions |
| --- | --- |
| getBlendMode | dgs3DInterfaceGetBlendMode |
| setBlendMode | dgs3DInterfaceSetBlendMode |
| getPosition | dgs3DInterfaceGetPosition |
| setPosition | dgs3DInterfaceSetPosition |
| getSize | dgs3DInterfaceGetSize |
| setSize | dgs3DInterfaceSetSize |
| getResolution | dgs3DInterfaceGetResolution |
| setFaceTo | dgs3DInterfaceSetFaceTo |
| getFaceTo | dgs3DInterfaceGetFaceTo |
| setResolution | dgs3DInterfaceSetResolution |
| attachToElement | dgs3DInterfaceAttachToElement |
| isAttached | dgs3DInterfaceIsAttached |
| detachFromElement | dgs3DInterfaceDetachFromElement |
| setAttachedOffsets | dgs3DInterfaceSetAttachedOffsets |
| getAttachedOffsets | dgs3DInterfaceGetAttachedOffsets |
| setRotation | dgs3DInterfaceSetRotation |
| getRotation | dgs3DInterfaceGetRotation |

### 3D Text

| OOP Functions | POP Functions |
| --- | --- |
| getDimension | dgs3DTextGetDimension |
| setDimension | dgs3DTextSetDimension |
| getInterior | dgs3DTextGetInterior |
| setInterior | dgs3DTextSetInterior |
| attachToElement | dgs3DTextAttachToElement |
| detachFromElement | dgs3DTextDetachFromElement |
| isAttached | dgs3DTextIsAttached |
| setAttachedOffsets | dgs3DTextSetAttachedOffsets |
| getAttachedOffsets | dgs3DTextGetAttachedOffsets |
| getPosition | dgs3DTextGetPosition |
| setPosition | dgs3DTextSetPosition |

### Check Box

| OOP Functions | POP Functions |
| --- | --- |
| getSelected | dgsCheckBoxGetSelected |
| setSelected | dgsCheckBoxSetSelected |

### Combo Box

| OOP Functions | POP Functions |
| --- | --- |
| addItem | dgsComboBoxAddItem |
| removeItem | dgsComboBoxRemoveItem |
| setItemText | dgsComboBoxSetItemText |
| getItemText | dgsComboBoxGetItemText |
| getItemCount | dgsComboBoxGetItemCount |
| getText | dgsComboBoxGetText |
| clear | dgsComboBoxClear |
| setSelectedItem | dgsComboBoxSetSelectedItem |
| getSelectedItem | dgsComboBoxGetSelectedItem |
| setItemColor | dgsComboBoxSetItemColor |
| getItemColor | dgsComboBoxGetItemColor |
| getState | dgsComboBoxGetState |
| setState | dgsComboBoxSetState |
| getBoxHeight | dgsComboBoxGetBoxHeight |
| setBoxHeight | dgsComboBoxSetBoxHeight |
| getScrollBar | dgsComboBoxGetScrollBar |
| setScrollPosition | dgsComboBoxSetScrollPosition |
| getScrollPosition | dgsComboBoxGetScrollPosition |
| setCaptionText | dgsComboBoxSetCaptionText |
| getCaptionText | dgsComboBoxGetCaptionText |
| setEditEnabled | dgsComboBoxSetEditEnabled |
| getEditEnabled | dgsComboBoxGetEditEnabled |

### Custom Renderer

| OOP Functions | POP Functions |
| --- | --- |
| setFunction | dgsCustomRendererSetFunction |

### Detect Area

| OOP Functions | POP Functions |
| --- | --- |
| setFunction | dgsDetectAreaSetFunction |

### Edit

| OOP Functions | POP Functions |
| --- | --- |
| moveCaret | dgsEditMoveCaret |
| getCaretPosition | dgsEditGetCaretPosition |
| setCaretPosition | dgsEditSetCaretPosition |
| setCaretStyle | dgsEditSetCaretStyle |
| getCaretStyle | dgsEditGetCaretStyle |
| setWhiteList | dgsEditSetWhiteList |
| getMaxLength | dgsEditGetMaxLength |
| setMaxLength | dgsEditSetMaxLength |
| setReadOnly | dgsEditSetReadOnly |
| getReadOnly | dgsEditGetReadOnly |
| setMasked | dgsEditSetMasked |
| getMasked | dgsEditGetMasked |
| setUnderlined | dgsEditSetUnderlined |
| getUnderlined | dgsEditGetUnderlined |
| setHorizontalAlign | dgsEditSetHorizontalAlign |
| getHorizontalAlign | dgsEditGetHorizontalAlign |
| setVerticalAlign | dgsEditSetVerticalAlign |
| getVerticalAlign | dgsEditGetVerticalAlign |
| setAlignment | dgsEditSetAlignment |
| getAlignment | dgsEditGetAlignment |
| insertText | dgsEditInsertText |
| deleteText | dgsEditDeleteText |
| getPartOfText | dgsEditGetPartOfText |
| clearText | dgsEditClearText |
| replaceText | dgsEditReplaceText |
| setTypingSound | dgsEditSetTypingSound |
| getTypingSound | dgsEditGetTypingSound |
| setPlaceHolder | dgsEditSetPlaceHolder |
| getPlaceHolder | dgsEditGetPlaceHolder |

### Grid List

| OOP Functions | POP Functions |
| --- | --- |
| getScrollBar | dgsGridListGetScrollBar |
| setScrollPosition | dgsGridListSetScrollPosition |
| getScrollPosition | dgsGridListGetScrollPosition |
| resetScrollBarPosition | dgsGridListResetScrollBarPosition |
| setColumnRelative | dgsGridListSetColumnRelative |
| getColumnRelative | dgsGridListGetColumnRelative |
| addColumn | dgsGridListAddColumn |
| getColumnCount | dgsGridListGetColumnCount |
| removeColumn | dgsGridListRemoveColumn |
| getColumnAllWidth | dgsGridListGetColumnAllWidth |
| getColumnWidth | dgsGridListGetColumnWidth |
| setColumnWidth | dgsGridListSetColumnWidth |
| getColumnTitle | dgsGridListGetColumnTitle |
| setColumnTitle | dgsGridListSetColumnTitle |
| getColumnFont | dgsGridListGetColumnFont |
| setColumnFont | dgsGridListSetColumnFont |
| addRow | dgsGridListAddRow |
| removeRow | dgsGridListRemoveRow |
| clearRow | dgsGridListClearRow |
| clearColumn | dgsGridListClearColumn |
| clear | dgsGridListClear |
| getRowCount | dgsGridListGetRowCount |
| setItemText | dgsGridListSetItemText |
| getItemText | dgsGridListGetItemText |
| getSelectedItem | dgsGridListGetSelectedItem |
| setSelectedItem | dgsGridListSetSelectedItem |
| setItemColor | dgsGridListSetItemColor |
| getItemColor | dgsGridListGetItemColor |
| setItemData | dgsGridListSetItemData |
| getItemData | dgsGridListGetItemData |
| setItemImage | dgsGridListSetItemImage |
| getItemImage | dgsGridListGetItemImage |
| removeItemImage | dgsGridListRemoveItemImage |
| getRowBackGroundImage | dgsGridListGetRowBackGroundImage |
| setRowBackGroundImage | dgsGridListSetRowBackGroundImage |
| setRowBackGroundColor | dgsGridListSetRowBackGroundColor |
| getRowBackGroundColor | dgsGridListGetRowBackGroundColor |
| setRowAsSection | dgsGridListSetRowAsSection |
| selectItem | dgsGridListSelectItem |
| itemIsSelected | dgsGridListItemIsSelected |
| setMultiSelectionEnabled | dgsGridListSetMultiSelectionEnabled |
| getMultiSelectionEnabled | dgsGridListGetMultiSelectionEnabled |
| setSelectionMode | dgsGridListSetSelectionMode |
| getSelectionMode | dgsGridListGetSelectionMode |
| getSelectedItems | dgsGridListGetSelectedItems |
| setSelectedItems | dgsGridListSetSelectedItems |
| getSelectedCount | dgsGridListGetSelectedCount |
| setSortFunction | dgsGridListSetSortFunction |
| setAutoSortEnabled | dgsGridListSetAutoSortEnabled |
| getAutoSortEnabled | dgsGridListGetAutoSortEnabled |
| setSortEnabled | dgsGridListSetSortEnabled |
| getSortEnabled | dgsGridListGetSortEnabled |
| setSortColumn | dgsGridListSetSortColumn |
| getSortColumn | dgsGridListGetSortColumn |
| getEnterColumn | dgsGridListGetEnterColumn |
| sort | dgsGridListSort |
| setNavigationEnabled | dgsGridListSetNavigationEnabled |
| getNavigationEnabled | dgsGridListGetNavigationEnabled |

### Image

| OOP Functions | POP Functions |
| --- | --- |
| setImage | dgsImageSetImage |
| getImage | dgsImageGetImage |
| setUVSize | dgsImageSetUVSize |
| getUVSize | dgsImageGetUVSize |
| setUVPosition | dgsImageSetUVPosition |
| getUVPosition | dgsImageGetUVPosition |

### Label

| OOP Functions | POP Functions |
| --- | --- |
| setColor | dgsLabelSetColor |
| getColor | dgsLabelGetColor |
| setHorizontalAlign | dgsLabelSetHorizontalAlign |
| getHorizontalAlign | dgsLabelGetHorizontalAlign |
| setVerticalAlign | dgsLabelSetVerticalAlign |
| getVerticalAlign | dgsLabelGetVerticalAlign |
| getTextExtent | dgsLabelGetTextExtent |
| getFontHeight | dgsLabelGetFontHeight |

### Memo

| OOP Functions | POP Functions |
| --- | --- |
| moveCaret | dgsMemoMoveCaret |
| seekPosition | dgsMemoSeekPosition |
| getScrollBar | dgsMemoGetScrollBar |
| setScrollPosition | dgsMemoSetScrollPosition |
| getScrollPosition | dgsMemoGetScrollPosition |
| setCaretPosition | dgsMemoSetCaretPosition |
| getCaretPosition | dgsMemoGetCaretPosition |
| setCaretStyle | dgsMemoSetCaretStyle |
| getCaretStyle | dgsMemoGetCaretStyle |
| setReadOnly | dgsMemoSetReadOnly |
| getReadOnly | dgsMemoGetReadOnly |
| getPartOfText | dgsMemoGetPartOfText |
| deleteText | dgsMemoDeleteText |
| insertText | dgsMemoInsertText |
| clearText | dgsMemoClearText |
| clearText | dgsMemoClearText |
| setScrollBarState | dgsMemoSetScrollBarState |
| getScrollBarState | dgsMemoGetScrollBarState |
| setTypingSound | dgsMemoSetTypingSound |
| getLineCount | dgsMemoGetLineCount |
| setWordWrapState | dgsMemoSetWordWrapState |
| getWordWrapState | dgsMemoGetWordWrapState |

### Progress Bar

| OOP Functions | POP Functions |
| --- | --- |
| getProgress | dgsProgressBarGetProgress |
| setProgress | dgsProgressBarSetProgress |
| getMode | dgsProgressBarGetMode |
| setMode | dgsProgressBarSetMode |
| getVerticalSide | dgsProgressBarGetVerticalSide |
| setVerticalSide | dgsProgressBarSetVerticalSide |
| getHorizontalSide | dgsProgressBarGetHorizontalSide |
| setHorizontalSide | dgsProgressBarSetHorizontalSide |

### Radio Button

| OOP Functions | POP Functions |
| --- | --- |
| getSelected | dgsRadioButtonGetSelected |
| setSelected | dgsRadioButtonSetSelected |

### Scroll Bar

| OOP Functions | POP Functions |
| --- | --- |
| setScrollPosition | dgsScrollBarSetScrollPosition |
| getScrollPosition | dgsScrollBarGetScrollPosition |
| setScrollSize | dgsScrollBarSetScrollSize |
| getScrollSize | dgsScrollBarGetScrollSize |
| setLocked | dgsScrollBarSetLocked |
| getLocked | dgsScrollBarGetLocked |

### Switch Button

| OOP Functions | POP Functions |
| --- | --- |
| getState | dgsSwitchButtonGetState |
| setState | dgsSwitchButtonSetState |
| setText | dgsSwitchButtonSetText |
| getText | dgsSwitchButtonGetText |

### Scroll Pane

| OOP Functions | POP Functions |
| --- | --- |
| getScrollBar | dgsScrollPaneGetScrollBar |
| setScrollPosition | dgsScrollPaneSetScrollPosition |
| getScrollPosition | dgsScrollPaneGetScrollPosition |
| setScrollBarState | dgsScrollPaneSetScrollBarState |
| getScrollBarState | dgsScrollPaneGetScrollBarState |

### Tab Panel

| OOP Functions | POP Functions |
| --- | --- |
| getSelectedTab | dgsGetSelectedTab |
| setSelectedTab | dgsSetSelectedTab |
| getTabFromID | dgsTabPanelGetTabFromID |
| moveTab | dgsTabPanelMoveTab |
| getTabID | dgsTabPanelGetTabID |
| dgsTab | dgsCreateTab |

### Tab

| OOP Functions | POP Functions |
| --- | --- |
| deleteTab | dgsDeleteTab |

## Events

| OOP Events | POP Events |
| --- | --- |
| dgsMouseLeave | onDgsMouseLeave |
| dgsMouseEnter | onDgsMouseEnter |
| dgsMouseClick | onDgsMouseClick |
| dgsMouseWheel | onDgsMouseWheel |
| dgsMouseDoubleClick | onDgsMouseDoubleClick |
| dgsWindowClose | onDgsWindowClose |
| dgsPositionChange | onDgsPositionChange |
| dgsSizeChange | onDgsSizeChange |
| dgsTextChange | onDgsTextChange |
| dgsScrollBarScrollPositionChange | onDgsScrollBarScrollPositionChange |
| dgsScrollPaneScroll | onDgsScrollPaneScroll |
| dgsDestroy | onDgsDestroy |
| dgsSwitchButtonStateChange | onDgsSwitchButtonStateChange |
| dgsGridListSelect | onDgsGridListSelect |
| dgsGridListItemDoubleClick | onDgsGridListItemDoubleClick |
| dgsProgressBarChange | onDgsProgressBarChange |
| dgsCreate | onDgsCreate |
| dgsPreRender | onDgsPreRender |
| dgsRender | onDgsRender |
| dgsElementRender | onDgsElementRender |
| dgsFocus | onDgsFocus |
| dgsBlur | onDgsBlur |
| dgsCursorMove | onDgsCursorMove |
| dgsTabSelect | onDgsTabSelect |
| dgsTabPanelTabSelect | onDgsTabPanelTabSelect |
| dgsRadioButtonChange | onDgsRadioButtonChange |
| dgsCheckBoxChange | onDgsCheckBoxChange |
| dgsComboBoxSelect | onDgsComboBoxSelect |
| dgsComboBoxStateChange | onDgsComboBoxStateChange |
| dgsEditPreSwitch | onDgsEditPreSwitch |
| dgsEditSwitched | onDgsEditSwitched |
| dgsEditAccepted | onDgsEditAccepted |
| dgsComboBoxAccepted | onDgsComboBoxAccepted |
| dgsStopMoving | onDgsStopMoving |
| dgsStopSizing | onDgsStopSizing |
| dgsStopAlphaing | onDgsStopAlphaing |
| dgsStopAniming | onDgsStopAniming |
| dgsCursorDrag | onDgsCursorDrag |
