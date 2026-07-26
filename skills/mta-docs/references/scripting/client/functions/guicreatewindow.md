---
doc_id: "mta-wiki:2400"
title: "GuiCreateWindow"
source_title: "GuiCreateWindow"
source_url: "https://wiki.multitheftauto.com/wiki/GuiCreateWindow"
revision_id: 78460
language: "en"
categories: ["Client_functions", "Utility_templates"]
---

# GuiCreateWindow

This function is for creating a new GUI window.  This provides a base for other gui elements to be created within.  However, windows do not have a parent and cannot be created in any GUI elements.

## Syntax

```
element guiCreateWindow ( float x, float y, float width, float height, string titleBarText, [ bool relative = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[GuiWindow](mta://scripting/concepts/element-gui-window.md)(...)*

### Required Arguments

 
Example Window.

- **x:** A float of the 2D x position of the GUI window on a player's screen.  This is affected by the *relative* argument.

- **y:** A float of the 2D y position of the GUI window on a player's screen. This is affected by the *relative* argument.

- **width:** A float of the width of the GUI window. This is affected by the *relative* argument.

- **height:** A float of the height of the GUI window. This is affected by the *relative* argument.

- **titleBarText:** A string of the text that will be displayed in the title bar of the window.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **relative:** This is whether sizes and positioning are relative.  If this is *true*, then all x,y,width,height floats must be between 0 and 1, representing sizes/positions as a fraction of the screen size. If *false*, then the size and co-ordinates are based on client's resolution, accessible using [guiGetScreenSize](mta://scripting/client/functions/guigetscreensize.md).

### Returns

Returns a gui window element if it was created successfully, false otherwise.

## Example

**Example 1:** This example creates a information window and adds two tabs to a "tabPanel" tabpanel, and adds some other gui elements to it.

```
local myWindow = guiCreateWindow ( 0, 0, 0.5, 0.4, "Information", true )  -- create a window which has "Information" in the title bar.
local tabPanel = guiCreateTabPanel ( 0, 0.1, 1, 1, true, myWindow )       -- create a tab panel which fills the whole window
local tabMap = guiCreateTab( "Map Information", tabPanel )                -- create a tab named "Map Information" on 'tabPanel'
local tabHelp = guiCreateTab( "Help", tabPanel )                          -- create another tab named "Help" on 'tabPanel'

-- adds a label (text) to each tab
guiCreateLabel(0.02, 0.04, 0.94, 0.2, "This is information about the current map", true, tabMap)
guiCreateLabel(0.02, 0.04, 0.94, 0.92, "This is help text.", true, tabHelp)
```

**Example 2:** This example creates a weapon selection screen, complete with a window, gridlist and a button. Users can select a shotgun or a machine gun. The window is not movable or sizable.

```
--Setup some tables

shotguns = {
      "chrome",
      "sawn-off",
      "combat"
}

machineGun = {
      "m4",
      "ak-47"
}

function setupWeaponSelection ( theResource )
      -- getResourceRootElement(getThisResource()) at the bottom means it will only create the gui on this resource start
      -- Create a window for our spawnscreen, with the title "Select your weapons".
      spawnScreenMenu = guiCreateWindow ( 0.15, 0.33, 0.7, 0.34, "Select your weapons", true )
      -- create an OK button to allow the user to confirm their selections, and attach it to the confirmSelection function
      spawnScreenOKButton = guiCreateButton ( 0.4, 0.85, 0.20, 0.15, "OK", true, spawnScreenMenu )
      -- ensure the user can't move or resize our spawnscreen.
      guiWindowSetMovable ( spawnScreenMenu, false )
      guiWindowSetSizable ( spawnScreenMenu, false )
      -- create our gridlist, which fills up most of the window.
      spawnScreenGridList = guiCreateGridList ( 0, 0.1, 1, 0.9, true, spawnScreenMenu )
      guiGridListSetSelectionMode ( spawnScreenGridList, 2 ) -- ensure the selection mode is one per column
      -- Since we have 2 sets of weapons, create a column for shotguns and one for machine guns
      guiGridListAddColumn ( spawnScreenGridList, "Shotguns", 0.3 )
      guiGridListAddColumn ( spawnScreenGridList, "Machine guns", 0.3 )
      -- next, we loop through our handguns table to add handgun items to the gridlist
      for key,weaponName in pairs(shotguns) do
            -- add a new row to our gridlist each time
            local row = guiGridListAddRow ( spawnScreenGridList )
            -- next, we set that row's text to the weapon name. Column is 1 since the "Shotguns" column was created first.
            guiGridListSetItemText ( spawnScreenGridList, row, 1, weaponName, false, false )
      end
      -- we repeat the process for other weapon list, changing the column number
      row = 0
      for key,weaponName in pairs(machineGun) do
            -- we don't need to create new rows as that was done in the previous loop
            -- we just set the row's text to the weapon name. Column is 2 since the "Machine guns" column was created second.
            guiGridListSetItemText ( spawnScreenGridList, row, 2, weaponName, false, false )
            row = row + 1 -- increase the row number
      end
end
addEventHandler ( "onClientResourceStart", getResourceRootElement(getThisResource()), setupWeaponSelection )
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

- [guiCreateCheckBox](mta://scripting/client/functions/guicreatecheckbox.md)

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

- guiCreateWindow

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
