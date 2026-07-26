---
doc_id: "mta-wiki:9384"
title: "OnVertexBufferRangeInvalidated"
source_title: "OnVertexBufferRangeInvalidated"
source_url: "https://wiki.multitheftauto.com/wiki/OnVertexBufferRangeInvalidated"
revision_id: 51002
language: "en"
categories: []
generated_at: "2026-07-26T16:16:26.986944+00:00"
---

# OnVertexBufferRangeInvalidated

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It serves as an event when vertex buffer rage is invalidated.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **pStreamData1:** Pointer to the IDirect3DVertexBuffer9 type.

- **Offset:** uint --.

- **Size:** uint --.

## Code

```
void CAdditionalVertexStreamManager::OnVertexBufferRangeInvalidated ( IDirect3DVertexBuffer9* pStreamData1, uint Offset, uint Size )
{
    SAdditionalStreamInfo* pAdditionalInfo = GetAdditionalStreamInfo ( pStreamData1 );
    if ( pAdditionalInfo )
    {
        pAdditionalInfo->ConvertedRanges.UnsetRange ( Offset, Size );
    }
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
