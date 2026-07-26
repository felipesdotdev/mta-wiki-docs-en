---
doc_id: "mta-wiki:14650"
title: "Astrath:createTab"
source_title: "Astrath:createTab"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateTab"
revision_id: 82569
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:24.328772+00:00"
---

# Astrath:createTab

DxTab:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new tab element inside a `DxTabPanel`. Tabs are linked to a panel and their positions are automatically managed according to the panel layout. Only usable with a valid `DxTabPanel` parent.

**Parameters:**

- parent (element) – A `DxTabPanel` element where this tab will be attached (required).

- text (string) – The text to display on the tab (optional, default: 'tab').

- color (table / tocolor) – The main color of the tab (optional, defaults to parent's color).

- hoverColor (table / tocolor) – Color when hovering (optional, defaults to parent's hoverColor).

- activeColor (table / tocolor) – Color when tab is active (optional, defaults to parent's activeColor).

- tabColor (table / tocolor) – Base color for inactive tabs (optional, defaults to parent's tabColor).

**Returns:**

Returns the newly created `DxTab` element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the tab and removes it from the parent panel. |
| Ath:setVisible(boolean) | Shows or hides the tab and triggers reordering in the panel. |
| Ath:setEnabled(boolean) | Enables or disables the tab. |
| Ath:setHoverable(boolean) | Enables or disables hover effects for this tab. |
| Ath:setColor(r, g, b, a, type) | Sets the tab's color. Type can be 'mainColor', 'hoverColor', 'tabColor', 'activeColor'. |

**Example:**

```
-- Crear un tab panel
local tabPanel = DxTabPanel:new(100, 100, 400, 300)
tabPanel:setVisible(true)

-- Agregar tabs
local tab1 = DxTab:new(tabPanel, "Tab 1")
local tab2 = DxTab:new(tabPanel, "Tab 2", tocolor(200,0,0,255))

-- Establecer tab seleccionado
tabPanel:setSelected(tab1)
```

**See also:**

- [DxTabPanel:new](https://wiki.multitheftauto.com/index.php?title=DxTabPanel:new&action=edit&redlink=1) – The panel container required for tabs

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to draw DX elements each frame

- [adjustAlpha](https://wiki.multitheftauto.com/index.php?title=AdjustAlpha&action=edit&redlink=1) – Function used internally to adjust tab opacity
