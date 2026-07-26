---
doc_id: "mta-wiki:9377"
title: "MaybeUnsetAdditionalVertexStream"
source_title: "MaybeUnsetAdditionalVertexStream"
source_url: "https://wiki.multitheftauto.com/wiki/MaybeUnsetAdditionalVertexStream"
revision_id: 50995
language: "en"
categories: []
generated_at: "2026-07-26T16:16:10.971833+00:00"
---

# MaybeUnsetAdditionalVertexStream

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It maybe unsets additional vertex stream.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Code

```
void CAdditionalVertexStreamManager::MaybeUnsetAdditionalVertexStream ( void )
{
    HRESULT hr;
    if ( m_pOldVertexDeclaration )
    {
        // Set prev declaration
        hr = g_pProxyDevice->SetVertexDeclaration ( m_pOldVertexDeclaration );
        SAFE_RELEASE( m_pOldVertexDeclaration );

        // Unset additional stream
        hr = m_pDevice->SetStreamSource ( 2, NULL, 0, 0 );
    }
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
