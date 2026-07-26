---
doc_id: "mta-wiki:13375"
title: "SvgGetSize"
source_title: "SvgGetSize"
source_url: "https://wiki.multitheftauto.com/wiki/SvgGetSize"
revision_id: 81322
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:54.438452+00:00"
---

# SvgGetSize

Gets the underlying XML document from an SVG element.

## Syntax

```
int, int svgGetSize( svg svgElement )
```

### Required Arguments

- **svgElement:** The [svg](mta://reference/misc/svg.md) you want to get the size of.

### Returns

- Returns two [ints](mta://reference/misc/int.md), representing **width** and **height**

## Example

See the example for [svgSetSize](mta://scripting/client/functions/svgsetsize.md).

## See Also

- [svgCreate](mta://scripting/client/functions/svgcreate.md)

- [svgGetDocumentXML](mta://scripting/client/functions/svggetdocumentxml.md)

- svgGetSize

- [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md)

- [svgSetSize](mta://scripting/client/functions/svgsetsize.md)

- [svgSetUpdateCallback](mta://scripting/client/functions/svgsetupdatecallback.md)
