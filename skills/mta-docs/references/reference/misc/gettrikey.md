---
doc_id: "mta-wiki:9370"
title: "GetTriKey"
source_title: "GetTriKey"
source_url: "https://wiki.multitheftauto.com/wiki/GetTriKey"
revision_id: 50986
language: "en"
categories: []
---

# GetTriKey

This C++ namespace function is a helper function for [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It gets 64 bit key for a triangle by using the ordered vertex indices.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **a:** To be defined.

- **b:** To be defined.

- **c:** To be defined.

## Returns

Returns a long long 64 bit key for a triangle.

## Code

```
long long getTriKey ( WORD a, WORD b, WORD c )
{
    WORD tmp;
    if ( b < a ) { tmp = b; b = a; a = tmp; }
    if ( c < b ) { tmp = c; c = b; b = tmp; }
    if ( b < a ) { tmp = b; b = a; a = tmp; }
    return ( ((long long)a) << 32 ) | ( ((long long)b) << 16 ) | ((long long)c);
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
