---
doc_id: "mta-wiki:7216"
title: "SetChatAlpha"
source_title: "SetChatAlpha"
source_url: "https://wiki.multitheftauto.com/wiki/SetChatAlpha"
revision_id: 73905
language: "en"
categories: ["Disabled_Functions_and_Events", "Client_functions"]
generated_at: "2026-07-26T16:16:38.695263+00:00"
---

# SetChatAlpha

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: This function doesn't exists. See issue 7698 on bugtracker. |  |

This function sets the global alpha value of the in-game chat. The alpha value applies to text output, input line and background colors.

## Syntax

```
bool setChatAlpha ( float alpha )
```

### Required Arguments

- **alpha:** the new global alpha value for the in-game chat (0-255)

### Returns

Returns *true* if alpha is a number and resides in a valid range (0-255), *false* if alpha is not a number or resides in an invalid range (like 9001).

## Example

This example makes everybodies chatbox flash in 1 second intervals.

```
local startTime = getTickCount()
local interval = 1000 -- time in milliseconds
local baseAlpha = 200 -- the alpha value the chat will at least have
                      -- valid: 0 - 255

addEventHandler( "onClientRender", root,
    function()
        local elapsedTime = getTickCount() - startTime
        local modAlpha = ( 255 - baseAlpha ) / 2
        local alpha = math.sin( elapsedTime / interval * math.pi * 2 ) * modAlpha
                      + baseAlpha + modAlpha
                      
        setChatAlpha( alpha )
    end
)
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

- [guiCreateWindow](mta://scripting/client/functions/guicreatewindow.md)

- [guiWindowIsMovable](mta://scripting/client/functions/guiwindowismovable.md)

- [guiWindowIsSizable](mta://scripting/client/functions/guiwindowissizable.md)

- [guiWindowSetMovable](mta://scripting/client/functions/guiwindowsetmovable.md)

- [guiWindowSetSizable](mta://scripting/client/functions/guiwindowsetsizable.md)
