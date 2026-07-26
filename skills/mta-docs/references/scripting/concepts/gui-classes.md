---
doc_id: "mta-wiki:4364"
title: "GUI Classes"
source_title: "GUI Classes"
source_url: "https://wiki.multitheftauto.com/wiki/GUI_Classes"
revision_id: 18487
language: "en"
categories: []
---

# GUI Classes

This page lists all the gui class objects. This will only work with: [http://community.mtasa.com/index.php?p=resources&s=details&id=241](http://community.mtasa.com/index.php?p=resources&s=details&id=241)

This system is created by the well known 50p!

GUI Classes made scripting gui objects easier!

## Installation

The installation is pretty simple. All you need to do is copy and paste folder **"gui_class/classes/"** into your resource which you want to use these classes in. Then just copy specified lines from **"gui_class/meta.xml"** into your meta.xml. As you know gui_class is not actually a resource that you can use exported functions of. It just includes all the classes that make scripting GUI cleaner, so that's why you have to copy the directory and include the files which are inside into meta.xml to tell the server/client which files you're using (that is, the classes you want to use).

You can also start gui_class resource and uncomment some examples which are located in **"test.lua"**

## Useful information

Once you create a GUI Object, it has a bunch of variables that you can access. One of them is **.gui** which represents the gui element that can be used with native GUI functions. Lets say, you want to use guiSetVisible() and you don't want to use object:Visible() then you can do so like this:

```
-- create our object
local button = Button:Create( 10, 200, 100, 18, "Woot!" );
-- now use native GUI function
guiSetVisible( button.gui, false );
```

## Classes

### Button class

- [Button:Create](mta://scripting/concepts/gui-classes-button-create.md)

- [Button:ColorOnHover](mta://scripting/concepts/gui-classes-button-coloronhover.md)

- [Button:AddOnTextChanged](mta://scripting/concepts/gui-classes-button-addontextchanged.md)

- [Button:RemoveOnTextChanged](mta://scripting/concepts/gui-classes-button-removeontextchanged.md)

### Check Box class

- [CheckBox:Create](mta://scripting/concepts/gui-classes-checkbox-create.md)

- [CheckBox:Selected](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/CheckBox:Selected&action=edit&redlink=1)

### Gridlist class

- [GridList:Create](https://wiki.multitheftauto.com/index.php?title=GridList:Create&action=edit&redlink=1)

- [GridList:AutoSizeColumn](https://wiki.multitheftauto.com/index.php?title=GridList:AutoSizeColumn&action=edit&redlink=1)

- [GridList:AddColumn](https://wiki.multitheftauto.com/index.php?title=GridList:AddColumn&action=edit&redlink=1)

- [GridList:AddRow](https://wiki.multitheftauto.com/index.php?title=GridList:AddRow&action=edit&redlink=1)

- [GridList:Clear](https://wiki.multitheftauto.com/index.php?title=GridList:Clear&action=edit&redlink=1)

- [GridList:ItemData](https://wiki.multitheftauto.com/index.php?title=GridList:ItemData&action=edit&redlink=1)

- [GridList:ItemText](https://wiki.multitheftauto.com/index.php?title=GridList:ItemText&action=edit&redlink=1)

- [GridList:SelectedItem](https://wiki.multitheftauto.com/index.php?title=GridList:SelectedItem&action=edit&redlink=1)

- [GridList:SortingEnabled](https://wiki.multitheftauto.com/index.php?title=GridList:SortingEnabled&action=edit&redlink=1)

- [GridList:RowCount](https://wiki.multitheftauto.com/index.php?title=GridList:RowCount&action=edit&redlink=1)

- [GridList:ColumnCount](https://wiki.multitheftauto.com/index.php?title=GridList:ColumnCount&action=edit&redlink=1)

- [GridList:InsertRowAfter](https://wiki.multitheftauto.com/index.php?title=GridList:InsertRowAfter&action=edit&redlink=1)

- [GridList:RemoveColumn](https://wiki.multitheftauto.com/index.php?title=GridList:RemoveColumn&action=edit&redlink=1)

- [GridList:RemoveRow](https://wiki.multitheftauto.com/index.php?title=GridList:RemoveRow&action=edit&redlink=1)

- [GridList:ScrollBars](https://wiki.multitheftauto.com/index.php?title=GridList:ScrollBars&action=edit&redlink=1)

- [GridList:SelectionMode](https://wiki.multitheftauto.com/index.php?title=GridList:SelectionMode&action=edit&redlink=1)

### Label class

- [Label:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Label:Create&action=edit&redlink=1)

- [Label:Color](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Label:Color&action=edit&redlink=1)

- [Label:VerticalAlign](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Label:VerticalAlign&action=edit&redlink=1)

- [Label:HorizontalAlign](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Label:HorizontalAlign&action=edit&redlink=1)

- [Label:GetTextExtent](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Label:GetTextExtent&action=edit&redlink=1)

- [Label:GetFontHeight](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Label:GetFontHeight&action=edit&redlink=1)

### Memo class

- [Memo:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Memo:Create&action=edit&redlink=1)

- [Memo:SetCaretIndex](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Memo:SetCaretIndex&action=edit&redlink=1)

- [Memo:ReadOnly](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Memo:ReadOnly&action=edit&redlink=1)

### Progress Bar class

Progress bar with this class is a little bit different from the native one. What's different is that I added a label on top, so that you can have a progress bar with some text on it.

- [ProgressBar:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ProgressBar:Create&action=edit&redlink=1)

- [ProgressBar:Font](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ProgressBar:Font&action=edit&redlink=1)

- [ProgressBar:LabelColor](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ProgressBar:LabelColor&action=edit&redlink=1)

- [ProgressBar:Progress](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ProgressBar:Progress&action=edit&redlink=1)

- [ProgressBar:Text](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ProgressBar:Text&action=edit&redlink=1)

- [ProgressBar:Size](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ProgressBar:Size&action=edit&redlink=1)

### Radio Button class

- [RadioButton:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/RadioButton:Create&action=edit&redlink=1)

- [RadioButton:Selected](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/RadioButton:Selected&action=edit&redlink=1)

### Scroll Bar class

- [ScrollBar:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ScrollBar:Create&action=edit&redlink=1)

- [ScrollBar:ScrollPosition](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/ScrollBar:ScrollPosition&action=edit&redlink=1)

### Static Image class

- [StaticImage:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/StaticImage:Create&action=edit&redlink=1)

- [StaticImage:LoadImage](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/StaticImage:LoadImage&action=edit&redlink=1)

### Tab class

- [Tab:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Tab:Create&action=edit&redlink=1)

### Tab panel class

- [TabPanel:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TabPanel:Create&action=edit&redlink=1)

- [TabPanel:AddTab](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TabPanel:AddTab&action=edit&redlink=1)

- [TabPanel:DeleteTab](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TabPanel:DeleteTab&action=edit&redlink=1)

- [TabPanel:GetTabs](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TabPanel:GetTabs&action=edit&redlink=1)

### Text Box class (formally known as Edit)

- [TextBox:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TextBox:Create&action=edit&redlink=1)

- [TextBox:SetCaratIndex](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TextBox:SetCaratIndex&action=edit&redlink=1)

- [TextBox:Masked](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TextBox:Masked&action=edit&redlink=1)

- [TextBox:MaxLength](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TextBox:MaxLength&action=edit&redlink=1)

- [TextBox:ReadOnly](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/TextBox:ReadOnly&action=edit&redlink=1)

### Window class

- [Window:Create](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Window:Create&action=edit&redlink=1)

- [Window:Movable](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Window:Movable&action=edit&redlink=1)

- [Window:Sizable](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/Window:Sizable&action=edit&redlink=1)

### Shared methods with all classes

- [GUISharedFuncs:Alpha](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Alpha&action=edit&redlink=1)

- [GUISharedFuncs:BringToFront](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:BringToFront&action=edit&redlink=1)

- [GUISharedFuncs:Dragable](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Dragable&action=edit&redlink=1)

- [GUISharedFuncs:Enabled](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Enabled&action=edit&redlink=1)

- [GUISharedFuncs:Font](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Font&action=edit&redlink=1)

- [GUISharedFuncs:MoveToBack](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:MoveToBack&action=edit&redlink=1)

- [GUISharedFuncs:Property](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Property&action=edit&redlink=1)

- [GUISharedFuncs:Text](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Text&action=edit&redlink=1)

- [GUISharedFuncs:Position](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Position&action=edit&redlink=1)

- [GUISharedFuncs:Size](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Size&action=edit&redlink=1)

- [GUISharedFuncs:Visible](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:Visible&action=edit&redlink=1)

- [GUISharedFuncs:AddOnClick](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:AddOnClick&action=edit&redlink=1)

- [GUISharedFuncs:RemoveOnClick](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:RemoveOnClick&action=edit&redlink=1)

- [GUISharedFuncs:AddOnMouseEnter](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:AddOnMouseEnter&action=edit&redlink=1)

- [GUISharedFuncs:RemoveOnMouseEnter](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:RemoveOnMouseEnter&action=edit&redlink=1)

- [GUISharedFuncs:AddOnMouseLeave](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:AddOnMouseLeave&action=edit&redlink=1)

- [GUISharedFuncs:RemoveOnMouseLeave](https://wiki.multitheftauto.com/index.php?title=GUI_Classes/GUISharedFuncs:RemoveOnMouseLeave&action=edit&redlink=1)
