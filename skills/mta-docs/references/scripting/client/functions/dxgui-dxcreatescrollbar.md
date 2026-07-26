---
doc_id: "mta-wiki:7102"
title: "DxGUI/dxCreateScrollBar"
source_title: "DxGUI/dxCreateScrollBar"
source_url: "https://wiki.multitheftauto.com/wiki/DxGUI/dxCreateScrollBar"
revision_id: 35581
language: "en"
categories: ["Client_functions"]
---

# DxGUI/dxCreateScrollBar

Example

```
dxTestWindow = exports.dxgui:dxCreateWindow(resourceRoot, 445, 150, 608, 335, "Main Window", tocolor(255,255,255,255), "default", "Lighter Black")
dxTestScrollBar = exports.dxgui:dxCreateScrollBar(resourceRoot, 25, 102, 242, 19, dxTestWindow, "Horizontal/Vertical", 0, 100, "Lighter Black")
```
