---
doc_id: "mta-wiki:9373"
title: "OnDeviceCreate"
source_title: "OnDeviceCreate"
source_url: "https://wiki.multitheftauto.com/wiki/OnDeviceCreate"
revision_id: 50989
language: "en"
categories: []
generated_at: "2026-07-26T16:16:20.826079+00:00"
---

# OnDeviceCreate

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It's used as an event when an IDirect3DDevice9 instance is created (?).

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **pDevice:** To be defined.

## Code

```
void CAdditionalVertexStreamManager::OnDeviceCreate ( IDirect3DDevice9* pDevice )
{
    m_pDevice = pDevice;
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
