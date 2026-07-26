---
doc_id: "mta-wiki:9381"
title: "GetAdditionalStreamInfo"
source_title: "GetAdditionalStreamInfo"
source_url: "https://wiki.multitheftauto.com/wiki/GetAdditionalStreamInfo"
revision_id: 50999
language: "en"
categories: []
generated_at: "2026-07-26T16:15:06.394711+00:00"
---

# GetAdditionalStreamInfo

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It gets and returns additional stream info.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **pStreamData1:** Pointer to the IDirect3DVertexBuffer9 type.

## Returns

Returns additional stream info in form of --.

## Code

```
SAdditionalStreamInfo* CAdditionalVertexStreamManager::GetAdditionalStreamInfo ( IDirect3DVertexBuffer9* pStreamData1 )
{
    return MapFind ( m_AdditionalStreamInfoMap, pStreamData1 );
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
