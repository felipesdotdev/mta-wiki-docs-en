---
doc_id: "mta-wiki:9383"
title: "OnVertexBufferDestroy"
source_title: "OnVertexBufferDestroy"
source_url: "https://wiki.multitheftauto.com/wiki/OnVertexBufferDestroy"
revision_id: 51001
language: "en"
categories: []
---

# OnVertexBufferDestroy

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It serves as an event of when vertex buffer gets destroyed.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **pStreamData1:** Pointer to the IDirect3DVertexBuffer9 type.

## Code

```
void CAdditionalVertexStreamManager::OnVertexBufferDestroy ( IDirect3DVertexBuffer9* pStreamData1  )
{
    SAdditionalStreamInfo* pAdditionalInfo = GetAdditionalStreamInfo ( pStreamData1 );
    if ( pAdditionalInfo )
    {
        pAdditionalInfo->pStreamData->Release ();
        pAdditionalInfo->pVertexDeclaration->Release ();
        MapRemove ( m_AdditionalStreamInfoMap, pStreamData1 );
    }
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
