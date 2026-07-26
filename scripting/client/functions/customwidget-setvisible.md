---
doc_id: "mta-wiki:10305"
title: "CustomWidget:setVisible"
source_title: "CustomWidget:setVisible"
source_url: "https://wiki.multitheftauto.com/wiki/CustomWidget%3AsetVisible"
revision_id: 57087
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:11:13.985819+00:00"
---

# CustomWidget:setVisible

This function set visibility of Custom Widget on screen.

## Syntax

```
bool CustomWidget:setVisible(bool Visibility)
```

### Required Arguments

- **Visibility** - Boolean value of visibility of widget on screen.

### Returns

Returns bool value - is changed widget visibility.

## Example

This example creating window with buttons, when click on them label changing visibility:

```
local Window = CustomWindow.create(5, 5, 120, 120, "Example", false)

local VisibleButton = CustomButton.create(10, 30, 100, 25, "Set Visible", false, Window)
local InvisibleButton = CustomButton.create(10, 65, 100, 25, "Set Invisible", false, Window)
local VLabel = CustomLabel.create(10, 100, 100, 15, "Example Label", false, Window)

VisibleButton:addEvent("onClientGUIClick", function()
	VLabel:setVisible(true)
end)

InvisibleButton:addEvent("onClientGUIClick", function()
	VLabel:setVisible(false)
end)
```

## See Also

Resource Wiki with *content* located here: [Resource:CustomWidgets](mta://resources/customwidgets.md)

### **Custom Widgets**

This methods working for all elements except *CustomDialogs* and *CustomTooltips*

#### Set Functions

- [CustomWidget:setPosition](mta://scripting/client/functions/customwidget-setposition.md)

- [CustomWidget:setSize](mta://scripting/client/functions/customwidget-setsize.md)

- CustomWidget:setVisible

- [CustomWidget:setEnabled](mta://scripting/client/functions/customwidget-setenabled.md)

- [CustomWidget:setColorScheme](mta://scripting/client/functions/customwidget-setcolorscheme.md)

- [CustomWidget:setFont](mta://scripting/client/functions/customwidget-setfont.md)

- [CustomWidget:setFontSize](mta://scripting/client/functions/customwidget-setfontsize.md)

- [CustomWidget:setSystemFont](mta://scripting/client/functions/customwidget-setsystemfont.md)

#### Get Functions

- [CustomWidget:getPosition](mta://scripting/client/functions/customwidget-getposition.md)

- [CustomWidget:getSize](mta://scripting/client/functions/customwidget-getsize.md)

- [CustomWidget:getRealSize](mta://scripting/client/functions/customwidget-getrealsize.md)

- [CustomWidget:getVisible](mta://scripting/client/functions/customwidget-getvisible.md)

- [CustomWidget:getEnabled](mta://scripting/client/functions/customwidget-getenabled.md)

- [CustomWidget:getColorScheme](mta://scripting/client/functions/customwidget-getcolorscheme.md)

- [CustomWidget:getFont](mta://scripting/client/functions/customwidget-getfont.md)

- [CustomWidget:getFontSize](mta://scripting/client/functions/customwidget-getfontsize.md)

- [getCWType](https://wiki.multitheftauto.com/index.php?title=GetCWType&action=edit&redlink=1)

#### Event Functions

- [CustomWidget:bringToFront](mta://scripting/client/functions/customwidget-bringtofront.md)

- [CustomWidget:moveToBack](mta://scripting/client/functions/customwidget-movetoback.md)

- [CustomWidget:addEvent](mta://scripting/client/functions/customwidget-addevent.md)

- [CustomWidget:removeEvent](mta://scripting/client/functions/customwidget-removeevent.md)

- [CustomWidget:destroy](mta://scripting/client/functions/customwidget-destroy.md)

- [proceedColor](mta://scripting/client/functions/proceedcolor.md)

### **Custom Windows**

#### Create Function

- [CustomWindow.create](mta://scripting/client/functions/customwindow-create.md)

#### Set Functions

- [CustomWindow:setTitle](mta://scripting/client/functions/customwindow-settitle.md)

- [CustomWindow:setText](mta://scripting/client/functions/customwindow-settext.md)

- [CustomWindow:setMovable](mta://scripting/client/functions/customwindow-setmovable.md)

- [CustomWindow:setSizable](mta://scripting/client/functions/customwindow-setsizable.md)

- [CustomWindow:setCloseEnabled](mta://scripting/client/functions/customwindow-setcloseenabled.md)

- [CustomWindow:setSideBarLength](mta://scripting/client/functions/customwindow-setsidebarlength.md)

- [CustomWindow:setSideBarPosition](mta://scripting/client/functions/customwindow-setsidebarposition.md)

- [CustomWindow:setMinimalWidth](https://wiki.multitheftauto.com/index.php?title=CustomWindow:setMinimalWidth&action=edit&redlink=1)

- [CustomWindow:setMinimalHeight](https://wiki.multitheftauto.com/index.php?title=CustomWindow:setMinimalHeight&action=edit&redlink=1)

- [CustomWindow:setMinimalSize](https://wiki.multitheftauto.com/index.php?title=CustomWindow:setMinimalSize&action=edit&redlink=1)

- [CustomWindow:setMaximalWidth](https://wiki.multitheftauto.com/index.php?title=CustomWindow:setMaximalWidth&action=edit&redlink=1)

- [CustomWindow:setMaximalHeight](https://wiki.multitheftauto.com/index.php?title=CustomWindow:setMaximalHeight&action=edit&redlink=1)

- [CustomWindow:setMaximalSize](https://wiki.multitheftauto.com/index.php?title=CustomWindow:setMaximalSize&action=edit&redlink=1)

#### Get Functions

- [CustomWindow:getTitle](mta://scripting/client/functions/customwindow-gettitle.md)

- [CustomWindow:getText](mta://scripting/client/functions/customwindow-gettext.md)

- [CustomWindow:getMovable](mta://scripting/client/functions/customwindow-getmovable.md)

- [CustomWindow:getSizable](mta://scripting/client/functions/customwindow-getsizable.md)

- [CustomWindow:getCloseEnabled](mta://scripting/client/functions/customwindow-getcloseenabled.md)

- [CustomWindow:getSideBarLength](mta://scripting/client/functions/customwindow-getsidebarlength.md)

- [CustomWindow:getSideBarPosition](mta://scripting/client/functions/customwindow-getsidebarposition.md)

- [CustomWindow:getMinimalWidth](https://wiki.multitheftauto.com/index.php?title=CustomWindow:getMinimalWidth&action=edit&redlink=1)

- [CustomWindow:getMinimalHeight](https://wiki.multitheftauto.com/index.php?title=CustomWindow:getMinimalHeight&action=edit&redlink=1)

- [CustomWindow:getMinimalSize](https://wiki.multitheftauto.com/index.php?title=CustomWindow:getMinimalSize&action=edit&redlink=1)

- [CustomWindow:getMaximalWidth](https://wiki.multitheftauto.com/index.php?title=CustomWindow:getMaximalWidth&action=edit&redlink=1)

- [CustomWindow:getMaximalHeight](https://wiki.multitheftauto.com/index.php?title=CustomWindow:getMaximalHeight&action=edit&redlink=1)

- [CustomWindow:getMaximalSize](https://wiki.multitheftauto.com/index.php?title=CustomWindow:getMaximalSize&action=edit&redlink=1)

#### Event Functions

- [CustomWindow:open](mta://scripting/client/functions/customwindow-open.md)

- [CustomWindow:close](mta://scripting/client/functions/customwindow-close.md)

- [CustomWindow:addElement](mta://scripting/client/functions/customwindow-addelement.md)

- [CustomWindow:addElements](mta://scripting/client/functions/customwindow-addelements.md)

- [CustomWindow:showDialog](mta://scripting/client/functions/customwindow-showdialog.md)

- [CustomWindow:showBar](mta://scripting/client/functions/customwindow-showbar.md)

- [CustomWindow:getMainElement](mta://scripting/client/functions/customwindow-getmainelement.md)

- [CustomWindow:getHeader](mta://scripting/client/functions/customwindow-getheader.md)

- [CustomWindow:getDialog](mta://scripting/client/functions/customwindow-getdialog.md)

### **Custom Buttons**

#### Create Function

- [CustomButton.create](mta://scripting/client/functions/custombutton-create.md)

#### Set Functions

- [CustomButton:setText](mta://scripting/client/functions/custombutton-settext.md)

- [CustomButton:setImage](mta://scripting/client/functions/custombutton-setimage.md)

#### Get Functions

- [CustomButton:getText](mta://scripting/client/functions/custombutton-gettext.md)

- [CustomButton:getImage](mta://scripting/client/functions/custombutton-getimage.md)

#### Event Functions

- [CustomButton:getMainElement](mta://scripting/client/functions/custombutton-getmainelement.md)

### **Custom Progress Bars**

#### Create Function

- [CustomProgressBar.create](mta://scripting/client/functions/customprogressbar-create.md)

#### Set Functions

- [CustomProgressBar:setProgress](mta://scripting/client/functions/customprogressbar-setprogress.md)

#### Get Functions

- [CustomProgressBar:getProgress](mta://scripting/client/functions/customprogressbar-getprogress.md)

#### Event Functions

- [CustomProgressBar:getMainElement](mta://scripting/client/functions/customprogressbar-getmainelement.md)

### **Custom Scroll Bars**

#### Create Function

- [CustomScrollBar.create](mta://scripting/client/functions/customscrollbar-create.md)

#### Set Functions

- [CustomScrollBar:setScrollPosition](mta://scripting/client/functions/customscrollbar-setscrollposition.md)

- [CustomScrollBar:setScrollLength](mta://scripting/client/functions/customscrollbar-setscrolllength.md)

- [CustomScrollBar:setScrollSpeed](mta://scripting/client/functions/customscrollbar-setscrollspeed.md)

#### Get Functions

- [CustomScrollBar:getScrollPosition](mta://scripting/client/functions/customscrollbar-getscrollposition.md)

- [CustomScrollBar:getScrollLength](mta://scripting/client/functions/customscrollbar-getscrolllength.md)

- [CustomScrollBar:getScrollSpeed](mta://scripting/client/functions/customscrollbar-getscrollspeed.md)

### **Custom Edit Boxes**

All functions, what has mark *CustomEditBox* available for *CustomEdit*, *CustomMemo* and *CustomSpinner*.

#### Create Functions

- [CustomEdit.create](mta://scripting/client/functions/customedit-create.md)

- [CustomMemo.create](mta://scripting/client/functions/custommemo-create.md)

- [CustomSpinner.create](mta://scripting/client/functions/customspinner-create.md)

#### Set Functions

- [CustomEditBox:setReadOnly](mta://scripting/client/functions/customeditbox-setreadonly.md)

- [CustomEditBox:setText](mta://scripting/client/functions/customeditbox-settext.md)

- [CustomEditBox:setCaretIndex](mta://scripting/client/functions/customeditbox-setcaretindex.md)

- [CustomEditBox:setSidesColor](mta://scripting/client/functions/customeditbox-setsidescolor.md)

- [CustomEdit:setMasked](mta://scripting/client/functions/customedit-setmasked.md)

- [CustomEdit:setMaxLength](mta://scripting/client/functions/customedit-setmaxlength.md)

- [CustomSpinner:setMinimal](mta://scripting/client/functions/customspinner-setminimal.md)

- [CustomSpinner:setMaximal](mta://scripting/client/functions/customspinner-setmaximal.md)

- [CustomSpinner:setStepSize](mta://scripting/client/functions/customspinner-setstepsize.md)

#### Get Functions

- [CustomEditBox:getReadOnly](mta://scripting/client/functions/customeditbox-getreadonly.md)

- [CustomEditBox:getText](mta://scripting/client/functions/customeditbox-gettext.md)

- [CustomEditBox:getCaretIndex](mta://scripting/client/functions/customeditbox-getcaretindex.md)

- [CustomEditBox:isOnSide](mta://scripting/client/functions/customeditbox-isonside.md)

- [CustomEditBox:getSidesColor](mta://scripting/client/functions/customeditbox-getsidescolor.md)

- [CustomEdit:getMasked](mta://scripting/client/functions/customedit-getmasked.md)

- [CustomEdit:getMaxLength](mta://scripting/client/functions/customedit-getmaxlength.md)

- [CustomSpinner:getMinimal](mta://scripting/client/functions/customspinner-getminimal.md)

- [CustomSpinner:getMaximal](mta://scripting/client/functions/customspinner-getmaximal.md)

- [CustomSpinner:getStepSize](mta://scripting/client/functions/customspinner-getstepsize.md)

#### Event Functions

- [CustomEditBox:putOnSide](mta://scripting/client/functions/customeditbox-putonside.md)

### **Custom Check Boxes**

#### Create Function

- [CustomCheckBox.create](mta://scripting/client/functions/customcheckbox-create.md)

#### Set Functions

- [CustomCheckBox:setText](mta://scripting/client/functions/customcheckbox-settext.md)

- [CustomCheckBox:setChecked](mta://scripting/client/functions/customcheckbox-setchecked.md)

#### Get Functions

- [CustomCheckBox:getText](mta://scripting/client/functions/customcheckbox-gettext.md)

- [CustomCheckBox:getChecked](mta://scripting/client/functions/customcheckbox-getchecked.md)

#### Event Functions

- [CustomCheckBox:getMainElement](mta://scripting/client/functions/customcheckbox-getmainelement.md)

### **Custom Combo Boxes**

#### Create Function

- [CustomComboBox.create](mta://scripting/client/functions/customcombobox-create.md)

#### Set Functions

- [CustomComboBox:setSelectedItem](mta://scripting/client/functions/customcombobox-setselecteditem.md)

- [CustomComboBox:setItemText](mta://scripting/client/functions/customcombobox-setitemtext.md)

- [CustomComboBox:setMaxHeight](mta://scripting/client/functions/customcombobox-setmaxheight.md)

#### Get Functions

- [CustomComboBox:getSelectedItem](mta://scripting/client/functions/customcombobox-getselecteditem.md)

- [CustomComboBox:getItemText](mta://scripting/client/functions/customcombobox-getitemtext.md)

- [CustomComboBox:getMaxHeight](mta://scripting/client/functions/customcombobox-getmaxheight.md)

- [CustomComboBox:getItemsCount](mta://scripting/client/functions/customcombobox-getitemscount.md)

- [CustomComboBox:getItems](mta://scripting/client/functions/customcombobox-getitems.md)

#### Event Functions

- [CustomComboBox:addItem](mta://scripting/client/functions/customcombobox-additem.md)

- [CustomComboBox:removeItem](mta://scripting/client/functions/customcombobox-removeitem.md)

- [CustomComboBox:clear](mta://scripting/client/functions/customcombobox-clear.md)

- [CustomComboBox:getMainElement](mta://scripting/client/functions/customcombobox-getmainelement.md)

### **Custom Tabbed Panels**

#### Create Function

- [CustomTabPanel.create](mta://scripting/client/functions/customtabpanel-create.md)

#### Set Functions

- [CustomTabPanel:setTabVisible](mta://scripting/client/functions/customtabpanel-settabvisible.md)

- [CustomTabPanel:setTabEnabled](mta://scripting/client/functions/customtabpanel-settabenabled.md)

- [CustomTabPanel:setTabText](mta://scripting/client/functions/customtabpanel-settabtext.md)

- [CustomTabPanel:setSelectedTab](mta://scripting/client/functions/customtabpanel-setselectedtab.md)

- [CustomTabPanel:setTabsMinLength](mta://scripting/client/functions/customtabpanel-settabsminlength.md)

#### Get Functions

- [CustomTabPanel:getTabVisible](mta://scripting/client/functions/customtabpanel-gettabvisible.md)

- [CustomTabPanel:getTabEnabled](mta://scripting/client/functions/customtabpanel-gettabenabled.md)

- [CustomTabPanel:getTabText](mta://scripting/client/functions/customtabpanel-gettabtext.md)

- [CustomTabPanel:getTabFromText](mta://scripting/client/functions/customtabpanel-gettabfromtext.md)

- [CustomTabPanel:getSelectedTab](mta://scripting/client/functions/customtabpanel-getselectedtab.md)

- [CustomTabPanel:getTabsMinLength](mta://scripting/client/functions/customtabpanel-gettabsminlength.md)

- [CustomTabPanel:getTabHeader](mta://scripting/client/functions/customtabpanel-gettabheader.md)

#### Event Functions

- [CustomTabPanel:addTab](mta://scripting/client/functions/customtabpanel-addtab.md)

- [CustomTabPanel:removeTab](mta://scripting/client/functions/customtabpanel-removetab.md)

- [CustomTabPanel:clearTabs](mta://scripting/client/functions/customtabpanel-cleartabs.md)

- [CustomTabPanel:getMainElement](mta://scripting/client/functions/customtabpanel-getmainelement.md)

### **Custom Labels**

#### Create Function

- [CustomLabel.create](mta://scripting/client/functions/customlabel-create.md)

#### Set Functions

- [CustomLabel:setText](mta://scripting/client/functions/customlabel-settext.md)

- [CustomLabel:setColor](mta://scripting/client/functions/customlabel-setcolor.md)

- [CustomLabel:setSchematicalColor](mta://scripting/client/functions/customlabel-setschematicalcolor.md)

- [CustomLabel:setHoverable](mta://scripting/client/functions/customlabel-sethoverable.md)

- [CustomLabel:setVerticalAlign](mta://scripting/client/functions/customlabel-setverticalalign.md)

- [CustomLabel:setHorizontalAlign](mta://scripting/client/functions/customlabel-sethorizontalalign.md)

- [CustomLabel:setAlign](mta://scripting/client/functions/customlabel-setalign.md)

#### Get Functions

- [CustomLabel:getText](mta://scripting/client/functions/customlabel-gettext.md)

- [CustomLabel:getColor](mta://scripting/client/functions/customlabel-getcolor.md)

- [CustomLabel:getVerticalAlign](mta://scripting/client/functions/customlabel-getverticalalign.md)

- [CustomLabel:getHorizontalAlign](mta://scripting/client/functions/customlabel-gethorizontalalign.md)

- [CustomLabel:isSchematicalColor](mta://scripting/client/functions/customlabel-isschematicalcolor.md)

- [CustomLabel:isHoverable](mta://scripting/client/functions/customlabel-ishoverable.md)

#### Event Functions

- [CustomLabel:getMainElement](mta://scripting/client/functions/customlabel-getmainelement.md)

- [CustomLabel:addElement](mta://scripting/client/functions/customlabel-addelement.md)

- [CustomLabel:removeElement](mta://scripting/client/functions/customlabel-removeelement.md)

### **Custom Dialogs**

#### Create Function

- [CustomDialog.create](mta://scripting/client/functions/customdialog-create.md)

#### Event Functions

- [CustomDialog:open](mta://scripting/client/functions/customdialog-open.md)

- [CustomDialog:close](mta://scripting/client/functions/customdialog-close.md)

### **Custom Tool Tips**

#### Create Function

- [CustomTooltip.create](mta://scripting/client/functions/customtooltip-create.md)

#### Set Function

- [CustomTooltip:setShowTime](https://wiki.multitheftauto.com/index.php?title=CustomTooltip:setShowTime&action=edit&redlink=1)

- [CustomTooltip:setText](https://wiki.multitheftauto.com/index.php?title=CustomTooltip:setText&action=edit&redlink=1)

#### Get Function

- [CustomTooltip:getShowTime](https://wiki.multitheftauto.com/index.php?title=CustomTooltip:getShowTime&action=edit&redlink=1)

- [CustomTooltip:getText](https://wiki.multitheftauto.com/index.php?title=CustomTooltip:getText&action=edit&redlink=1)

### **Custom Loadings**

#### Create Function

- [CustomLoading.create](mta://scripting/client/functions/customloading-create.md)

#### Set Functions

- [CustomLoading:setProgress](mta://scripting/client/functions/customloading-setprogress.md)

- [CustomLoading:setAnimated](mta://scripting/client/functions/customloading-setanimated.md)

#### Get Functions

- [CustomLoading:getProgress](mta://scripting/client/functions/customloading-getprogress.md)

- [CustomLoading:getAnimated](mta://scripting/client/functions/customloading-getanimated.md)

### **Custom Scroll Panes**

#### Create Function

- [CustomScrollPane.create](mta://scripting/client/functions/customscrollpane-create.md)

#### Set Functions

- [CustomScrollPane:setScrollSpeed](mta://scripting/client/functions/customscrollpane-setscrollspeed.md)

- [CustomScrollPane:setVerticalScrollPosition](mta://scripting/client/functions/customscrollpane-setverticalscrollposition.md)

- [CustomScrollPane:setHorizontalScrollPosition](mta://scripting/client/functions/customscrollpane-sethorizontalscrollposition.md)

- [CustomScrollPane:setVerticalScrollInversed](mta://scripting/client/functions/customscrollpane-setverticalscrollinversed.md)

- [CustomScrollPane:setHorizontalScrollInversed](mta://scripting/client/functions/customscrollpane-sethorizontalscrollinversed.md)

- [CustomScrollPane:setHorizontalScrolling](mta://scripting/client/functions/customscrollpane-sethorizontalscrolling.md)

- [CustomScrollPane:setScrollingWithCursor](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:setScrollingWithCursor&action=edit&redlink=1)

- [CustomScrollPane:setScrollingWithWheel](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:setScrollingWithWheel&action=edit&redlink=1)

- [CustomScrollPane:addVerticalPixelScrollPosition](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:addVerticalPixelScrollPosition&action=edit&redlink=1)

- [CustomScrollPane:addHorizontalPixelScrollPosition](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:addHorizontalPixelScrollPosition&action=edit&redlink=1)

#### Get Functions

- [CustomScrollPane:getScrollSpeed](mta://scripting/client/functions/customscrollpane-getscrollspeed.md)

- [CustomScrollPane:getVerticalScrollPosition](mta://scripting/client/functions/customscrollpane-getverticalscrollposition.md)

- [CustomScrollPane:getHorizontalScrollPosition](mta://scripting/client/functions/customscrollpane-gethorizontalscrollposition.md)

- [CustomScrollPane:isVerticalScrollInversed](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:isVerticalScrollInversed&action=edit&redlink=1)

- [CustomScrollPane:isHorizontalScrollInversed](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:isHorizontalScrollInversed&action=edit&redlink=1)

- [CustomScrollPane:isHorizontalScrolling](mta://scripting/client/functions/customscrollpane-ishorizontalscrolling.md)

- [CustomScrollPane:getScrollingWithCursor](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:getScrollingWithCursor&action=edit&redlink=1)

- [CustomScrollPane:getScrollingWithWheel](https://wiki.multitheftauto.com/index.php?title=CustomScrollPane:getScrollingWithWheel&action=edit&redlink=1)

#### Event Functions

- [CustomScrollPane:getMainElement](mta://scripting/client/functions/customscrollpane-getmainelement.md)

- [CustomScrollPane:addElement](mta://scripting/client/functions/customscrollpane-addelement.md)

- [CustomScrollPane:removeElement](mta://scripting/client/functions/customscrollpane-removeelement.md)

- [CustomScrollPane:update](mta://scripting/client/functions/customscrollpane-update.md)

### **Custom Table Views**

#### Create Function

- [CustomTableView.create](mta://scripting/client/functions/customtableview-create.md)

#### Set Functions

- [CustomTableView:setSelectedLine](mta://scripting/client/functions/customtableview-setselectedline.md)

- [CustomTableView:setIndentation](mta://scripting/client/functions/customtableview-setindentation.md)

- [CustomTableView:setTitleBarVisible](mta://scripting/client/functions/customtableview-settitlebarvisible.md)

- [CustomTableView:setLineHeight](mta://scripting/client/functions/customtableview-setlineheight.md)

- [CustomTableView:setColumnWidth](mta://scripting/client/functions/customtableview-setcolumnwidth.md)

- [CustomTableView:setColumnTitle](mta://scripting/client/functions/customtableview-setcolumntitle.md)

- [CustomTableView:setCellText](mta://scripting/client/functions/customtableview-setcelltext.md)

- [CustomTableView:setShadowsEnabled](https://wiki.multitheftauto.com/index.php?title=CustomTableView:setShadowsEnabled&action=edit&redlink=1)

#### Get Functions

- [CustomTableView:getSelectedLine](mta://scripting/client/functions/customtableview-getselectedline.md)

- [CustomTableView:getIndentation](mta://scripting/client/functions/customtableview-getindentation.md)

- [CustomTableView:getTitleBarVisible](mta://scripting/client/functions/customtableview-gettitlebarvisible.md)

- [CustomTableView:getLineHeight](mta://scripting/client/functions/customtableview-getlineheight.md)

- [CustomTableView:getColumnWidth](mta://scripting/client/functions/customtableview-getcolumnwidth.md)

- [CustomTableView:getColumnTitle](mta://scripting/client/functions/customtableview-getcolumntitle.md)

- [CustomTableView:getCellText](mta://scripting/client/functions/customtableview-getcelltext.md)

- [CustomTableView:getCell](mta://scripting/client/functions/customtableview-getcell.md)

- [CustomTableView:getLinesCount](mta://scripting/client/functions/customtableview-getlinescount.md)

- [CustomTableView:getColumnsCount](mta://scripting/client/functions/customtableview-getcolumnscount.md)

- [CustomTableView:getShadowsEnabled](https://wiki.multitheftauto.com/index.php?title=CustomTableView:getShadowsEnabled&action=edit&redlink=1)

#### Event Functions

- [CustomTableView:addLine](mta://scripting/client/functions/customtableview-addline.md)

- [CustomTableView:removeLine](mta://scripting/client/functions/customtableview-removeline.md)

- [CustomTableView:clearLines](mta://scripting/client/functions/customtableview-clearlines.md)

- [CustomTableView:addColumn](mta://scripting/client/functions/customtableview-addcolumn.md)

- [CustomTableView:removeColumn](mta://scripting/client/functions/customtableview-removecolumn.md)

- [CustomTableView:update](mta://scripting/client/functions/customtableview-update.md)

### **Custom Static Images**

#### Create Function

- [CustomStaticImage.create](mta://scripting/client/functions/customstaticimage-create.md)

#### Set Function

- [CustomStaticImage:setColor](https://wiki.multitheftauto.com/index.php?title=CustomStaticImage:setColor&action=edit&redlink=1)

- [CustomStaticImage:setImage](https://wiki.multitheftauto.com/index.php?title=CustomStaticImage:setImage&action=edit&redlink=1)

- [CustomStaticImage:setSchematicalColor](https://wiki.multitheftauto.com/index.php?title=CustomStaticImage:setSchematicalColor&action=edit&redlink=1)

#### Get Function

- [CustomStaticImage:getColor](https://wiki.multitheftauto.com/index.php?title=CustomStaticImage:getColor&action=edit&redlink=1)

- [CustomStaticImage:getImage](https://wiki.multitheftauto.com/index.php?title=CustomStaticImage:getImage&action=edit&redlink=1)

- [CustomStaticImage:getNativeSize](https://wiki.multitheftauto.com/index.php?title=CustomStaticImage:getNativeSize&action=edit&redlink=1)

- [CustomStaticImage:isSchematicalColor](https://wiki.multitheftauto.com/index.php?title=CustomStaticImage:isSchematicalColor&action=edit&redlink=1)

#### Event Functions

- [CustomStaticImage:getMainElement](mta://scripting/client/functions/customstaticimage-getmainelement.md)

- [CustomStaticImage:addElement](mta://scripting/client/functions/customstaticimage-addelement.md)

### **Custom Text Boxes**

#### Create Function

- [CustomTextBox.create](mta://scripting/client/functions/customtextbox-create.md)

- [CustomMemoBox.create](mta://scripting/client/functions/custommemobox-create.md)

#### Set Function

- [CustomTextBox:setText](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:setText&action=edit&redlink=1)

- [CustomTextBox:setColor](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:setColor&action=edit&redlink=1)

- [CustomTextBox:setCaretIndex](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:setCaretIndex&action=edit&redlink=1)

- [CustomTextBox:setReadOnly](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:setReadOnly&action=edit&redlink=1)

- [CustomTextBox:setMasked](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:setMasked&action=edit&redlink=1)

- [CustomTextBox:setBordersEnabled](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:setBordersEnabled&action=edit&redlink=1)

- [CustomTextBox:setBackgroundEnabled](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:setBackgroundEnabled&action=edit&redlink=1)

#### Get Function

- [CustomTextBox:getText](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:getText&action=edit&redlink=1)

- [CustomTextBox:getColor](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:getColor&action=edit&redlink=1)

- [CustomTextBox:getCaretIndex](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:getCaretIndex&action=edit&redlink=1)

- [CustomTextBox:getCaretSelectionStart](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:getCaretSelectionStart&action=edit&redlink=1)

- [CustomTextBox:getCaretSelectionEnd](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:getCaretSelectionEnd&action=edit&redlink=1)

- [CustomTextBox:getCaretSelectionLength](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:getCaretSelectionLength&action=edit&redlink=1)

- [CustomTextBox:isReadOnly](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:isReadOnly&action=edit&redlink=1)

- [CustomTextBox:isMasked](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:isMasked&action=edit&redlink=1)

- [CustomTextBox:isBordersEnabled](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:isBordersEnabled&action=edit&redlink=1)

- [CustomTextBox:isBackgroundEnabled](https://wiki.multitheftauto.com/index.php?title=CustomTextBox:isBackgroundEnabled&action=edit&redlink=1)

### **Custom Events**

- [onCustomScrollPaneScrolled](https://wiki.multitheftauto.com/index.php?title=OnCustomScrollPaneScrolled&action=edit&redlink=1)

- [onCustomScrollBarScrolled](https://wiki.multitheftauto.com/index.php?title=OnCustomScrollBarScrolled&action=edit&redlink=1)

- [onCustomDialogClick](https://wiki.multitheftauto.com/index.php?title=OnCustomDialogClick&action=edit&redlink=1)

- [onCustomWindowClose](https://wiki.multitheftauto.com/index.php?title=OnCustomWindowClose&action=edit&redlink=1)

- [onCustomCheckBoxChecked](https://wiki.multitheftauto.com/index.php?title=OnCustomCheckBoxChecked&action=edit&redlink=1)

- [onCustomComboBoxSelectItem](https://wiki.multitheftauto.com/index.php?title=OnCustomComboBoxSelectItem&action=edit&redlink=1)

- [onCustomTabPanelChangeTab](https://wiki.multitheftauto.com/index.php?title=OnCustomTabPanelChangeTab&action=edit&redlink=1)

### **Other about Custom Widgets**

- [CustomWidgets.Variables](mta://reference/misc/customwidgets-variables.md)

- [CustomWidgets.Examples](mta://reference/misc/customwidgets-examples.md)

- [CustomWidgets.DemoWidgets](https://wiki.multitheftauto.com/index.php?title=CustomWidgets.DemoWidgets&action=edit&redlink=1)
