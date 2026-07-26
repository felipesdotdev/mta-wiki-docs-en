---
doc_id: "mta-wiki:9374"
title: "MaybeSetAdditionalVertexStream"
source_title: "MaybeSetAdditionalVertexStream"
source_url: "https://wiki.multitheftauto.com/wiki/MaybeSetAdditionalVertexStream"
revision_id: 50994
language: "en"
categories: []
generated_at: "2026-07-26T16:16:10.968149+00:00"
---

# MaybeSetAdditionalVertexStream

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It maybe sets an additional vertex stream.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **PrimitiveType:** D3DPRIMITIVETYPE type --.

- **BaseVertexIndex:** INT value --.

- **MinVertexIndex:** UINT value.

- **NumVertices:** UINT value.

- **startIndex:** UINT value.

- **primCount:** UINT value.

## Returns

Returns a boolean representing whether an additional vertex stream was set or not.

## Code

```
bool CAdditionalVertexStreamManager::MaybeSetAdditionalVertexStream ( D3DPRIMITIVETYPE PrimitiveType,INT BaseVertexIndex,UINT MinVertexIndex,UINT NumVertices,UINT startIndex,UINT primCount )
{
    // Cache info
    SCurrentStateInfo state;

    // Save call arguments
    state.args.PrimitiveType = PrimitiveType;
    state.args.BaseVertexIndex = BaseVertexIndex;
    state.args.MinVertexIndex = MinVertexIndex;
    state.args.NumVertices = NumVertices;
    state.args.startIndex = startIndex;
    state.args.primCount = primCount;
  
    // Cache info about state streams etc
    UpdateCurrentStateInfo ( state );

    // For now, this only works if the original has 3 decl elements (0:D, 1:P, 1:T) and stream 1 has a stride of 20
    if ( !CheckCanDoThis ( state ) )
        return false;

    SetAdditionalVertexStream ( state );
    return true;
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
