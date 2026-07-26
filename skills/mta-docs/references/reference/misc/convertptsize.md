---
doc_id: "mta-wiki:9369"
title: "ConvertPTSize"
source_title: "ConvertPTSize"
source_url: "https://wiki.multitheftauto.com/wiki/ConvertPTSize"
revision_id: 79862
language: "en"
categories: ["Development"]
---

# ConvertPTSize

This C++ namespace function is a helper function for [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It converts size of PT stream to sizeof of N stream.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **SizePT:** To be defined.

## Returns

Returns an uint representing --.

## Code

```
uint ConvertPTSize ( uint SizePT )
{
    return SizePT * 12 / 20;
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
