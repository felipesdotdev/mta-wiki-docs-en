---
doc_id: "mta-wiki:4385"
title: "GUI Classes/CheckBox:Create"
source_title: "GUI Classes/CheckBox:Create"
source_url: "https://wiki.multitheftauto.com/wiki/GUI_Classes/CheckBox%3ACreate"
revision_id: 18489
language: "en"
categories: ["Utility_templates"]
---

# GUI Classes/CheckBox:Create

This function creates a [CheckBox](mta://scripting/concepts/element-gui-checkbox.md) object.

## Syntax

```
checkboxObject CheckBox:Create ( float x, float y, float width, float height, string text, bool selected, [ bool relative = false, element parent = nil] )
```

### Required Arguments

- **x:** A float of the 2D x position of the checkbox on a player's screen. This is affected by the *relative* argument.

- **y:** A float of the 2D y position of the checkbox on a player's screen. This is affected by the *relative* argument.

- **width:** A float of the width of the text field next to the checkbox. This is affected by the *relative* argument.

- **height:** A float of the height of the text field next to the checkbox. This is affected by the *relative* argument.

- **text:** The text to be displayed next to the checkbox.

- **selected:** A boolean representing whether the checkbox created should be selected by default.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **relative:** This is whether sizes and positioning are relative. If this is *true*, then all x,y,width,height floats must be between 0 and 1, representing measures relative to the parent. Default value is **false**

- **parent:** This is the parent that the checkbox is attached to. If the *relative* argument is true, sizes and positioning will be made relative to this parent. If the *relative* argument is false, positioning will be the number of offset pixels from the parent's origin. If no parent is passed, the parent will become the screen - causing positioning and sizing according to screen positioning.

### Returns

- **checkboxObject** if it was created succesfully

- **false** otherwise.

## Example

This example does...

```

```

## See Also

[Back to GUI Classes page](mta://scripting/concepts/gui-classes.md)

### Button class

- [Button:Create](mta://scripting/concepts/gui-classes-button-create.md)

- [Button:ColorOnHover](mta://scripting/concepts/gui-classes-button-coloronhover.md)

- [Button:AddOnTextChanged](mta://scripting/concepts/gui-classes-button-addontextchanged.md)

- [Button:RemoveOnTextChanged](mta://scripting/concepts/gui-classes-button-removeontextchanged.md)

### Check Box class

- CheckBox:Create

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
