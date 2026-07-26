---
doc_id: "mta-wiki:14649"
title: "Astrath:createTabPanel"
source_title: "Astrath:createTabPanel"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateTabPanel"
revision_id: 82567
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:10:24.359120+00:00"
---

# Astrath:createTabPanel

DxTabPanel:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new tab panel DX element. A tab panel can hold multiple tabs and manage their selection and hover states. Automatically adjusts child tab positions and sizes.

**Parameters:**

- posX, posY (float) – Position of the tab panel on screen.

- width, height (float) – Dimensions of the tab panel.

- parent (element) – Parent DX element to attach this panel to (optional).

- relative (boolean) – Position relative to parent (optional).

- color (table / tocolor) – Main background color of the panel (optional, default: dark grey).

- tabColor (table / tocolor) – Default color for tabs (optional).

- activeColor (table / tocolor) – Color for the active tab (optional).

- hoverColor (table / tocolor) – Hover color for tabs (optional).

- font (string) – Font used for tab text (optional, default: "default-bold").

- fontsize (float) – Font size for tab text (optional, default: 1).

- style (string) – DX style used for the panel (optional).

- tabStyle (string) – DX style used for tabs (optional).

**Returns:**

Returns the newly created DxTabPanel element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the tab panel and all child tabs and elements. |
| Ath:setVisible(boolean) | Shows or hides the tab panel. |
| Ath:setEnabled(boolean) | Enables or disables the tab panel for interaction. |
| Ath:addTab(text) | Adds a new tab with the given text to the panel. |
| Ath:getSelected() | Returns the currently selected tab element. |
| Ath:setSelected(tabElement) | Sets a specific tab as selected. |
| Ath:setHoverable(boolean) | Enables or disables hover effect for tabs. |
| Ath:setColor(r, g, b, a, type) | Sets colors for the panel or tabs. Type can be 'mainColor', 'hoverColor', 'tabColor', 'activeColor'. |

**Example:**

```
local tabPanel = DxTabPanel:new(100, 100, 400, 300)
tabPanel:setVisible(true)
tabPanel:addTab("Tab 1")
tabPanel:addTab("Tab 2")
tabPanel:draw()
```

**See also:**

- [DxTab:new](https://wiki.multitheftauto.com/index.php?title=DxTab:new&action=edit&redlink=1) – Page for individual tab elements

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – For window parent reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event to render DX elements
