---
doc_id: "mta-wiki:13642"
title: "SvgSetUpdateCallback"
source_title: "SvgSetUpdateCallback"
source_url: "https://wiki.multitheftauto.com/wiki/SvgSetUpdateCallback"
revision_id: 81340
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:54.501609+00:00"
---

# SvgSetUpdateCallback

Sets the update callback of an [svg](mta://reference/misc/svg.md) element

## Syntax

```
bool svgSetUpdateCallback( svg svgElement, function / bool callback )
```

### Required Arguments

- **svgElement:** The [svg](mta://reference/misc/svg.md) you want to set the callback function of.

- **callback:** The callback function to store on the SVG. If **false** is provided, any existing callback function will be removed from the SVG.

### Returns

- Returns true if successful, false otherwise

## Example

For example of callback usage, see [svgSetSize](mta://scripting/client/functions/svgsetsize.md) or [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md).

## See Also

- [svgCreate](mta://scripting/client/functions/svgcreate.md)

- [svgGetDocumentXML](mta://scripting/client/functions/svggetdocumentxml.md)

- [svgGetSize](mta://scripting/client/functions/svggetsize.md)

- [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md)

- [svgSetSize](mta://scripting/client/functions/svgsetsize.md)

- svgSetUpdateCallback
