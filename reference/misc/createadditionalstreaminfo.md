---
doc_id: "mta-wiki:9382"
title: "CreateAdditionalStreamInfo"
source_title: "CreateAdditionalStreamInfo"
source_url: "https://wiki.multitheftauto.com/wiki/CreateAdditionalStreamInfo"
revision_id: 51000
language: "en"
categories: []
generated_at: "2026-07-26T16:12:16.450434+00:00"
---

# CreateAdditionalStreamInfo

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It creates additional stream info.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **state:** To be defined.

## Returns

Returns --to be defined.

## Code

```
SAdditionalStreamInfo* CAdditionalVertexStreamManager::CreateAdditionalStreamInfo ( const SCurrentStateInfo& state )
{
    SAdditionalStreamInfo* pAdditionalInfo = MapFind ( m_AdditionalStreamInfoMap, state.stream1.pStreamData );
    if ( !pAdditionalInfo )
    {
        // Create it
        SAdditionalStreamInfo info;

        // Create new decleration
        D3DVERTEXELEMENT9 elements[MAXD3DDECLLENGTH];
        assert ( state.decl.numElements > 3 && state.decl.numElements < 5 );
        memcpy ( elements, state.decl.elements, state.decl.numElements * sizeof ( D3DVERTEXELEMENT9 ) );

        D3DVERTEXELEMENT9* declNew = &elements[ state.decl.numElements - 1 ];
        elements[ state.decl.numElements ] = *declNew;

        declNew->Stream = 2;
        declNew->Offset = 0;
        declNew->Type = D3DDECLTYPE_FLOAT3;
        declNew->Method = D3DDECLMETHOD_DEFAULT;
        declNew->Usage = D3DDECLUSAGE_NORMAL;
        declNew->UsageIndex = 0;
        if ( FAILED( m_pDevice->CreateVertexDeclaration ( elements, &info.pVertexDeclaration ) ) )
            return false;

        // Create new stream
        info.Stride = sizeof ( float ) * 3;
        UINT Size2 = ConvertPTSize ( state.decl.VertexBufferDesc1.Size );
        if ( FAILED( m_pDevice->CreateVertexBuffer( Size2, D3DUSAGE_WRITEONLY, 0, D3DPOOL_MANAGED, &info.pStreamData, NULL ) ) )
            return false;

        // Save info
        MapSet ( m_AdditionalStreamInfoMap, state.stream1.pStreamData, info );
        pAdditionalInfo = MapFind ( m_AdditionalStreamInfoMap, state.stream1.pStreamData );
    }

    return pAdditionalInfo;
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
