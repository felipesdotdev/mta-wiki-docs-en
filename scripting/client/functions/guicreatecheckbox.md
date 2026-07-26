---
doc_id: "mta-wiki:2680"
title: "GuiCreateCheckBox"
source_title: "GuiCreateCheckBox"
source_url: "https://wiki.multitheftauto.com/wiki/GuiCreateCheckBox"
revision_id: 78477
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:15:32.767125+00:00"
---

# GuiCreateCheckBox

This function creates a [checkbox](mta://scripting/concepts/element-gui-checkbox.md).

## Syntax

```
element guiCreateCheckBox ( float x, float y, float width, float height, string text, bool selected, [ bool relative = false, gui-element parent = nil] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[GuiCheckBox](mta://scripting/concepts/element-gui-checkbox.md)(...)*

### Required Arguments

 

Test Checkbox

- **x:** A float of the 2D x position of the checkbox on a player's screen. This is affected by the *relative* argument.

- **y:** A float of the 2D y position of the checkbox on a player's screen. This is affected by the *relative* argument.

- **width:** A float of the width of the text field next to the checkbox. This is affected by the *relative* argument.

- **height:** A float of the height of the text field next to the checkbox. This is affected by the *relative* argument.

- **text:** The text to be displayed next to the checkbox.

- **selected:** A boolean representing whether the checkbox created should be selected by default.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **relative:** This is whether sizes and positioning are relative. If this is *true*, then all x,y,width,height floats must be between 0 and 1, representing measures relative to the parent.

- **parent:** This is the parent that the checkbox is attached to. If the *relative* argument is true, sizes and positioning will be made relative to this parent. If the *relative* argument is false, positioning will be the number of offset pixels from the parent's origin. If no parent is passed, the parent will become the screen - causing positioning and sizing according to screen positioning.

### Returns

Returns [element](mta://reference/misc/element.md) of the checkbox if it was created succesfully, *false* otherwise.

## Example

This example creates a GUI window with a checked and an unchecked checkbox and adds a command to toggle their visibility

```
function drawGUI()
	local guiWindow = guiCreateWindow(100,100,200,100,"Checkbox test area",false,false) -- create the container window
	local checkedBox = guiCreateCheckBox(20,30,150,20,"Checked checkbox",true,false,guiWindow) -- note the parameter after header, it will make the checkbox be checked
	local uncheckedBox = guiCreateCheckBox(20,60,150,20,"Unchecked checkbox",false,false,guiWindow) -- not here though
	guiSetVisible(guiWindow,false) -- set it invisible just in case
	return guiWindow -- we return the guiWindow
end
function cmdGUI(cmd)
	if not checkBoxWindow then -- if it hasn't been declared yet
		checkBoxWindow = drawGUI() -- we draw the gui window
		guiSetVisible(checkBoxWindow,true) -- we set it visible again. Strictly speaking it's not necessary, could have omitted both this and the upper guiSetVisible, but this is needed if you want to cache a window without actually showing it
	else -- if we actually have run this function before and declared checkBoxWindow
		guiSetVisible(checkBoxWindow, not guiGetVisible(checkBoxWindow)) -- we just toggle the visibility. If it was visible, not visible returns false and thus sets it's visibility false, effectivly hiding it	
	end
	showCursor(not isCursorShowing()) -- similar to above visibility
end
addCommandHandler("guiwindow",cmdGUI) -- trigger cmdGUI function with this command
```

## See Also

### General functions

- [guiBringToFront](mta://scripting/client/functions/guibringtofront.md)

- [getChatboxLayout](mta://scripting/client/functions/getchatboxlayout.md)

- [getChatboxCharacterLimit](mta://scripting/client/functions/getchatboxcharacterlimit.md)

- [guiCreateFont](mta://scripting/client/functions/guicreatefont.md)

- [guiBlur](mta://scripting/client/functions/guiblur.md)

- [guiFocus](mta://scripting/client/functions/guifocus.md)

- [guiGetAlpha](mta://scripting/client/functions/guigetalpha.md)

- [guiGetCursorType](mta://scripting/client/functions/guigetcursortype.md)

- [guiGetEnabled](mta://scripting/client/functions/guigetenabled.md)

- [guiGetFont](mta://scripting/client/functions/guigetfont.md)

- [guiGetInputEnabled](mta://scripting/client/functions/guigetinputenabled.md)

- [guiGetInputMode](mta://scripting/client/functions/guigetinputmode.md)

- [guiGetPosition](mta://scripting/client/functions/guigetposition.md)

- [guiGetProperties](mta://scripting/client/functions/guigetproperties.md)

- [guiGetProperty](mta://scripting/client/functions/guigetproperty.md)

- [guiGetScreenSize](mta://scripting/client/functions/guigetscreensize.md)

- [guiGetSize](mta://scripting/client/functions/guigetsize.md)

- [guiGetText](mta://scripting/client/functions/guigettext.md)

- [guiGetVisible](mta://scripting/client/functions/guigetvisible.md)

- [guiMoveToBack](mta://scripting/client/functions/guimovetoback.md)

- [guiSetAlpha](mta://scripting/client/functions/guisetalpha.md)

- [guiSetEnabled](mta://scripting/client/functions/guisetenabled.md)

- [guiSetFont](mta://scripting/client/functions/guisetfont.md)

- [guiSetInputEnabled](mta://scripting/client/functions/guisetinputenabled.md)

- [guiSetInputMode](mta://scripting/client/functions/guisetinputmode.md)

- [guiSetPosition](mta://scripting/client/functions/guisetposition.md)

- [guiSetProperty](mta://scripting/client/functions/guisetproperty.md)

- [guiSetSize](mta://scripting/client/functions/guisetsize.md)

- [guiSetText](mta://scripting/client/functions/guisettext.md)

- [guiSetVisible](mta://scripting/client/functions/guisetvisible.md)

- [isChatBoxInputActive](mta://scripting/client/functions/ischatboxinputactive.md)

- [isConsoleActive](mta://scripting/client/functions/isconsoleactive.md)

- [isDebugViewActive](mta://scripting/client/functions/isdebugviewactive.md)

- [isMainMenuActive](mta://scripting/client/functions/ismainmenuactive.md)

- [isMTAWindowActive](mta://scripting/client/functions/ismtawindowactive.md)

- [isTransferBoxActive](mta://scripting/client/functions/istransferboxactive.md)

- [setChatboxCharacterLimit](mta://scripting/client/functions/setchatboxcharacterlimit.md)

- [setDebugViewActive](mta://scripting/client/functions/setdebugviewactive.md)

### Browsers

- [guiCreateBrowser](mta://scripting/client/functions/guicreatebrowser.md)

- [guiGetBrowser](mta://scripting/client/functions/guigetbrowser.md)

### Buttons

- [guiCreateButton](mta://scripting/client/functions/guicreatebutton.md)

### Checkboxes

- [guiCheckBoxGetSelected](mta://scripting/client/functions/guicheckboxgetselected.md)

- [guiCheckBoxSetSelected](mta://scripting/client/functions/guicheckboxsetselected.md)

- guiCreateCheckBox

### Comboboxes

- [guiCreateComboBox](mta://scripting/client/functions/guicreatecombobox.md)

- [guiComboBoxAddItem](mta://scripting/client/functions/guicomboboxadditem.md)

- [guiComboBoxClear](mta://scripting/client/functions/guicomboboxclear.md)

- [guiComboBoxGetItemCount](mta://scripting/client/functions/guicomboboxgetitemcount.md)

- [guiComboBoxGetItemText](mta://scripting/client/functions/guicomboboxgetitemtext.md)

- [guiComboBoxGetSelected](mta://scripting/client/functions/guicomboboxgetselected.md)

- [guiComboBoxIsOpen](mta://scripting/client/functions/guicomboboxisopen.md)

- [guiComboBoxRemoveItem](mta://scripting/client/functions/guicomboboxremoveitem.md)

- [guiComboBoxSetItemText](mta://scripting/client/functions/guicomboboxsetitemtext.md)

- [guiComboBoxSetOpen](mta://scripting/client/functions/guicomboboxsetopen.md)

- [guiComboBoxSetSelected](mta://scripting/client/functions/guicomboboxsetselected.md)

### Edit Boxes

- [guiCreateEdit](mta://scripting/client/functions/guicreateedit.md)

- [guiEditGetCaretIndex](mta://scripting/client/functions/guieditgetcaretindex.md)

- [guiEditGetMaxLength](mta://scripting/client/functions/guieditgetmaxlength.md)

- [guiEditIsMasked](mta://scripting/client/functions/guieditismasked.md)

- [guiEditIsReadOnly](mta://scripting/client/functions/guieditisreadonly.md)

- [guiEditSetCaretIndex](mta://scripting/client/functions/guieditsetcaretindex.md)

- [guiEditSetMasked](mta://scripting/client/functions/guieditsetmasked.md)

- [guiEditSetMaxLength](mta://scripting/client/functions/guieditsetmaxlength.md)

- [guiEditSetReadOnly](mta://scripting/client/functions/guieditsetreadonly.md)

### Gridlists

- [guiCreateGridList](mta://scripting/client/functions/guicreategridlist.md)

- [guiGridListAddColumn](mta://scripting/client/functions/guigridlistaddcolumn.md)

- [guiGridListAddRow](mta://scripting/client/functions/guigridlistaddrow.md)

- [guiGridListAutoSizeColumn](mta://scripting/client/functions/guigridlistautosizecolumn.md)

- [guiGridListClear](mta://scripting/client/functions/guigridlistclear.md)

- [guiGridListGetColumnCount](mta://scripting/client/functions/guigridlistgetcolumncount.md)

- [guiGridListGetColumnTitle](mta://scripting/client/functions/guigridlistgetcolumntitle.md)

- [guiGridListGetColumnWidth](mta://scripting/client/functions/guigridlistgetcolumnwidth.md)

- [guiGridListGetHorizontalScrollPosition](mta://scripting/client/functions/guigridlistgethorizontalscrollposition.md)

- [guiGridListGetItemColor](mta://scripting/client/functions/guigridlistgetitemcolor.md)

- [guiGridListGetItemData](mta://scripting/client/functions/guigridlistgetitemdata.md)

- [guiGridListGetItemText](mta://scripting/client/functions/guigridlistgetitemtext.md)

- [guiGridListGetRowCount](mta://scripting/client/functions/guigridlistgetrowcount.md)

- [guiGridListGetSelectedCount](mta://scripting/client/functions/guigridlistgetselectedcount.md)

- [guiGridListGetSelectedItem](mta://scripting/client/functions/guigridlistgetselecteditem.md)

- [guiGridListGetSelectedItems](mta://scripting/client/functions/guigridlistgetselecteditems.md)

- [guiGridListGetSelectionMode](mta://scripting/client/functions/guigridlistgetselectionmode.md)

- [guiGridListIsSortingEnabled](mta://scripting/client/functions/guigridlistissortingenabled.md)

- [guiGridListGetVerticalScrollPosition](mta://scripting/client/functions/guigridlistgetverticalscrollposition.md)

- [guiGridListInsertRowAfter](mta://scripting/client/functions/guigridlistinsertrowafter.md)

- [guiGridListRemoveColumn](mta://scripting/client/functions/guigridlistremovecolumn.md)

- [guiGridListRemoveRow](mta://scripting/client/functions/guigridlistremoverow.md)

- [guiGridListSetColumnTitle](mta://scripting/client/functions/guigridlistsetcolumntitle.md)

- [guiGridListSetColumnWidth](mta://scripting/client/functions/guigridlistsetcolumnwidth.md)

- [guiGridListSetHorizontalScrollPosition](mta://scripting/client/functions/guigridlistsethorizontalscrollposition.md)

- [guiGridListSetItemColor](mta://scripting/client/functions/guigridlistsetitemcolor.md)

- [guiGridListSetItemData](mta://scripting/client/functions/guigridlistsetitemdata.md)

- [guiGridListSetItemText](mta://scripting/client/functions/guigridlistsetitemtext.md)

- [guiGridListSetScrollBars](mta://scripting/client/functions/guigridlistsetscrollbars.md)

- [guiGridListSetSelectedItem](mta://scripting/client/functions/guigridlistsetselecteditem.md)

- [guiGridListSetSelectionMode](mta://scripting/client/functions/guigridlistsetselectionmode.md)

- [guiGridListSetSortingEnabled](mta://scripting/client/functions/guigridlistsetsortingenabled.md)

- [guiGridListSetVerticalScrollPosition](mta://scripting/client/functions/guigridlistsetverticalscrollposition.md)

### Memos

- [guiCreateMemo](mta://scripting/client/functions/guicreatememo.md)

- [guiMemoGetCaretIndex](mta://scripting/client/functions/guimemogetcaretindex.md)

- [guiMemoGetVerticalScrollPosition](mta://scripting/client/functions/guimemogetverticalscrollposition.md)

- [guiMemoSetVerticalScrollPosition](mta://scripting/client/functions/guimemosetverticalscrollposition.md)

- [guiMemoIsReadOnly](mta://scripting/client/functions/guimemoisreadonly.md)

- [guiMemoSetCaretIndex](mta://scripting/client/functions/guimemosetcaretindex.md)

- [guiMemoSetReadOnly](mta://scripting/client/functions/guimemosetreadonly.md)

### Progressbars

- [guiCreateProgressBar](mta://scripting/client/functions/guicreateprogressbar.md)

- [guiProgressBarGetProgress](mta://scripting/client/functions/guiprogressbargetprogress.md)

- [guiProgressBarSetProgress](mta://scripting/client/functions/guiprogressbarsetprogress.md)

### Radio Buttons

- [guiCreateRadioButton](mta://scripting/client/functions/guicreateradiobutton.md)

- [guiRadioButtonGetSelected](mta://scripting/client/functions/guiradiobuttongetselected.md)

- [guiRadioButtonSetSelected](mta://scripting/client/functions/guiradiobuttonsetselected.md)

### Scrollbars

- [guiCreateScrollBar](mta://scripting/client/functions/guicreatescrollbar.md)

- [guiScrollBarGetScrollPosition](mta://scripting/client/functions/guiscrollbargetscrollposition.md)

- [guiScrollBarSetScrollPosition](mta://scripting/client/functions/guiscrollbarsetscrollposition.md)

### Scrollpanes

- [guiCreateScrollPane](mta://scripting/client/functions/guicreatescrollpane.md)

- [guiScrollPaneGetHorizontalScrollPosition](mta://scripting/client/functions/guiscrollpanegethorizontalscrollposition.md)

- [guiScrollPaneGetVerticalScrollPosition](mta://scripting/client/functions/guiscrollpanegetverticalscrollposition.md)

- [guiScrollPaneSetHorizontalScrollPosition](mta://scripting/client/functions/guiscrollpanesethorizontalscrollposition.md)

- [guiScrollPaneSetScrollBars](mta://scripting/client/functions/guiscrollpanesetscrollbars.md)

- [guiScrollPaneSetVerticalScrollPosition](mta://scripting/client/functions/guiscrollpanesetverticalscrollposition.md)

### Static Images

- [guiCreateStaticImage](mta://scripting/client/functions/guicreatestaticimage.md)

- [guiStaticImageGetNativeSize](mta://scripting/client/functions/guistaticimagegetnativesize.md)

- [guiStaticImageLoadImage](mta://scripting/client/functions/guistaticimageloadimage.md)

### Tab Panels

- [guiCreateTabPanel](mta://scripting/client/functions/guicreatetabpanel.md)

- [guiGetSelectedTab](mta://scripting/client/functions/guigetselectedtab.md)

- [guiSetSelectedTab](mta://scripting/client/functions/guisetselectedtab.md)

### Tabs

- [guiCreateTab](mta://scripting/client/functions/guicreatetab.md)

- [guiDeleteTab](mta://scripting/client/functions/guideletetab.md)

### Text Labels

- [guiCreateLabel](mta://scripting/client/functions/guicreatelabel.md)

- [guiLabelGetColor](mta://scripting/client/functions/guilabelgetcolor.md)

- [guiLabelGetFontHeight](mta://scripting/client/functions/guilabelgetfontheight.md)

- [guiLabelGetTextExtent](mta://scripting/client/functions/guilabelgettextextent.md)

- [guiLabelSetColor](mta://scripting/client/functions/guilabelsetcolor.md)

- [guiLabelSetHorizontalAlign](mta://scripting/client/functions/guilabelsethorizontalalign.md)

- [guiLabelSetVerticalAlign](mta://scripting/client/functions/guilabelsetverticalalign.md)

### Windows

- [guiCreateWindow](mta://scripting/client/functions/guicreatewindow.md)

- [guiWindowIsMovable](mta://scripting/client/functions/guiwindowismovable.md)

- [guiWindowIsSizable](mta://scripting/client/functions/guiwindowissizable.md)

- [guiWindowSetMovable](mta://scripting/client/functions/guiwindowsetmovable.md)

- [guiWindowSetSizable](mta://scripting/client/functions/guiwindowsetsizable.md)

### Input

- [onClientCharacter](mta://scripting/client/events/onclientcharacter.md)

- [onClientClick](mta://scripting/client/events/onclientclick.md)

- [onClientCursorMove](mta://scripting/client/events/onclientcursormove.md)

- [onClientDoubleClick](mta://scripting/client/events/onclientdoubleclick.md)

- [onClientKey](mta://scripting/client/events/onclientkey.md)

- [onClientPaste](mta://scripting/client/events/onclientpaste.md)

### GUI

- [onClientGUIAccepted](mta://scripting/client/events/onclientguiaccepted.md)

- [onClientGUIBlur](mta://scripting/client/events/onclientguiblur.md)

- [onClientGUIChanged](mta://scripting/client/events/onclientguichanged.md)

- [onClientGUIClick](mta://scripting/client/events/onclientguiclick.md)

- [onClientGUIComboBoxAccepted](mta://scripting/client/events/onclientguicomboboxaccepted.md)

- [onClientGUIDoubleClick](mta://scripting/client/events/onclientguidoubleclick.md)

- [onClientGUIFocus](mta://scripting/client/events/onclientguifocus.md)

- [onClientGUIMouseDown](mta://scripting/client/events/onclientguimousedown.md)

- [onClientGUIMouseUp](mta://scripting/client/events/onclientguimouseup.md)

- [onClientGUIMove](mta://scripting/client/events/onclientguimove.md)

- [onClientGUIScroll](mta://scripting/client/events/onclientguiscroll.md)

- [onClientGUISize](mta://scripting/client/events/onclientguisize.md)

- [onClientGUITabSwitched](mta://scripting/client/events/onclientguitabswitched.md)

- [onClientMouseEnter](mta://scripting/client/events/onclientmouseenter.md)

- [onClientMouseLeave](mta://scripting/client/events/onclientmouseleave.md)

- [onClientMouseMove](mta://scripting/client/events/onclientmousemove.md)

- [onClientMouseWheel](mta://scripting/client/events/onclientmousewheel.md)
