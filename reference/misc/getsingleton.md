---
doc_id: "mta-wiki:9372"
title: "GetSingleton"
source_title: "GetSingleton"
source_url: "https://wiki.multitheftauto.com/wiki/GetSingleton"
revision_id: 50988
language: "en"
categories: []
generated_at: "2026-07-26T16:15:24.884603+00:00"
---

# GetSingleton

This C++ function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It returns an instance of CAdditionalVertexStreamManager.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Returns

Returns an instance of CAdditionalVertexStreamManager.

## Code

```
CAdditionalVertexStreamManager* CAdditionalVertexStreamManager::GetSingleton ( void )
{
    if ( !ms_Singleton )
        ms_Singleton = new CAdditionalVertexStreamManager ();
    return ms_Singleton;
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
