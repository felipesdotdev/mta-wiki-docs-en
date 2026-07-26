---
doc_id: "mta-wiki:14646"
title: "Astrath:createMemo"
source_title: "Astrath:createMemo"
source_url: "https://wiki.multitheftauto.com/wiki/Astrath%3AcreateMemo"
revision_id: 82564
language: "en"
categories: ["Client_functions"]
---

# Astrath:createMemo

DxMemo:new

[Template:FuncDef](https://wiki.multitheftauto.com/index.php?title=Template:FuncDef&action=edit&redlink=1)

**Description:**
Creates a new DX-based memo element. Memos are multi-line text boxes that support scrolling, cursor positioning, text input, custom fonts, colors, and read-only mode. Each memo instance is automatically registered in the DX library.

**Parameters:**

- text (string) – Initial text content for the memo (optional).

- posX, posY (float) – Position on screen.

- width, height (float) – Size of the memo.

- parent (element) – Parent DX element to attach this memo to (optional).

- relative (boolean) – Position relative to parent (optional).

- font (string) – Font used for the text (optional, default: "default-bold").

- fontsize (float) – Font size multiplier (optional, default: 1).

**Returns:**

Returns the newly created DxMemo element.

**Methods:**

| Method | Description |
| --- | --- |
| Ath:destroy() | Destroys the memo element and all its child elements. |
| Ath:setVisible(boolean) | Shows or hides the memo. |
| Ath:setEnabled(boolean) | Enables or disables the memo for interaction. |
| Ath:setText(string) | Sets the memo text. |
| Ath:getText() | Returns the current memo text. |
| Ath:clear() | Clears all text and resets the cursor. |
| Ath:setReadOnly(boolean) | Enables or disables read-only mode. |
| Ath:getReadOnly() | Returns whether the memo is read-only. |
| Ath:setHoverable(boolean) | Enables or disables hover effect. |
| Ath:setColor(r, g, b, a, type) | Sets the main or hover background color. |

**Example:**

```
local myMemo = DxMemo:new("Hello World", 100, 100, 300, 200)

myMemo:setVisible(true)
myMemo:setReadOnly(false)
myMemo:setHoverable(true)
myMemo:setColor(255, 255, 255, 255, "mainColor")
myMemo:setText("Welcome to MTA DX Memo")
myMemo:draw()
```

**See also:**

- [Astrath](mta://reference/misc/astrath.md) – Main library page

- [DxWindow:new](https://wiki.multitheftauto.com/index.php?title=DxWindow:new&action=edit&redlink=1) – Page for window element reference

- [DxLabel:new](https://wiki.multitheftauto.com/index.php?title=DxLabel:new&action=edit&redlink=1) – Page for label element reference

- [onClientRender](mta://scripting/client/events/onclientrender.md) – Event used to render DX elements
