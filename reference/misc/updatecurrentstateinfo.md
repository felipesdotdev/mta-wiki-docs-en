---
doc_id: "mta-wiki:9379"
title: "UpdateCurrentStateInfo"
source_title: "UpdateCurrentStateInfo"
source_url: "https://wiki.multitheftauto.com/wiki/UpdateCurrentStateInfo"
revision_id: 50997
language: "en"
categories: []
generated_at: "2026-07-26T16:16:50.814800+00:00"
---

# UpdateCurrentStateInfo

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It updates current state info.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **state:** To be defined.

## Returns

Returns a boolean value whether current state info was updated or not.

## Code

```
bool CAdditionalVertexStreamManager::UpdateCurrentStateInfo ( SCurrentStateInfo& state )
{
    // Get vertex declaration
    if ( FAILED( m_pDevice->GetVertexDeclaration ( &state.decl.pVertexDeclaration ) ) )
        return false;

    // Get vertex declaration desc
    if ( state.decl.pVertexDeclaration )
    {
        if ( FAILED( state.decl.pVertexDeclaration->GetDeclaration ( state.decl.elements, &state.decl.numElements ) ) )
            return false;
    }

    // Get vertex stream
    if ( FAILED( m_pDevice->GetStreamSource ( 1, &state.stream1.pStreamData, &state.stream1.OffsetInBytes, &state.stream1.Stride ) ) )
        return NULL;

    // Get vertex stream desc
    if ( state.stream1.pStreamData )
    {
        if ( FAILED( state.stream1.pStreamData->GetDesc ( &state.decl.VertexBufferDesc1 ) ) )
            return false;
    }

    return true;
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
