---
doc_id: "mta-wiki:9380"
title: "CheckCanDoThis"
source_title: "CheckCanDoThis"
source_url: "https://wiki.multitheftauto.com/wiki/CheckCanDoThis"
revision_id: 50998
language: "en"
categories: []
generated_at: "2026-07-26T16:12:16.424092+00:00"
---

# CheckCanDoThis

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It checks if --.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **state:** To be defined.

## Returns

Returns a boolean value representing whether this can be done or not.

## Code

```
bool CAdditionalVertexStreamManager::CheckCanDoThis ( const SCurrentStateInfo& state )
{
    if ( state.decl.numElements != 4 )
        return false;

    // Check vertex declaration requirements
    const D3DVERTEXELEMENT9* elements = state.decl.elements;
    if ( elements[0].Stream != 0 || elements[0].Type != D3DDECLTYPE_D3DCOLOR || elements[0].Usage != D3DDECLUSAGE_COLOR )
        return false;

    if ( elements[1].Stream != 1 || elements[1].Type != D3DDECLTYPE_FLOAT3 || elements[1].Usage != D3DDECLUSAGE_POSITION )
        return false;

    if ( elements[2].Stream != 1 || elements[2].Type != D3DDECLTYPE_FLOAT2 || elements[2].Usage != D3DDECLUSAGE_TEXCOORD )
        return false;

    if ( elements[3].Stream != 255 )
        return false;

    // Check vertex stream
    if ( !state.stream1.pStreamData )
        return false;

    if ( state.stream1.Stride != 20 )
        return false;

    if ( state.args.PrimitiveType != D3DPT_TRIANGLESTRIP && state.args.PrimitiveType != D3DPT_TRIANGLELIST )
        return false;

    return true;
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
