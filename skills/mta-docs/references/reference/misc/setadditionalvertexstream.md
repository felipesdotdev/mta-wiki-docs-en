---
doc_id: "mta-wiki:9376"
title: "SetAdditionalVertexStream"
source_title: "SetAdditionalVertexStream"
source_url: "https://wiki.multitheftauto.com/wiki/SetAdditionalVertexStream"
revision_id: 50993
language: "en"
categories: []
---

# SetAdditionalVertexStream

This C++ Function is found inside of [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md).

It sets an additional vertex stream.

It can be found in **Client/Client Core/Sources/CAdditionalVertexStreamManager.cpp** in Visual Studio.

## Required Arguments

- **state:** To be defined.

## Code

```
void CAdditionalVertexStreamManager::SetAdditionalVertexStream ( SCurrentStateInfo& state )
{
    HRESULT hr;

    // Get matching custom N vbuffer for std PT vbuffer
    SAdditionalStreamInfo* pAdditionalInfo = GetAdditionalStreamInfo ( state.stream1.pStreamData );
    if ( !pAdditionalInfo )
        pAdditionalInfo = CreateAdditionalStreamInfo ( state );

    uint StridePT = 20;
    uint StrideN = 12;

    // Calc area we are going to use
    uint viMinBased = state.args.MinVertexIndex + state.args.BaseVertexIndex;
    uint viMaxBased = state.args.MinVertexIndex + state.args.NumVertices + state.args.BaseVertexIndex;

    uint ReadOffsetStart = viMinBased * StridePT + state.stream1.OffsetInBytes;
    uint ReadOffsetSize = ( viMaxBased - viMinBased ) * StridePT;

    uint OffsetInBytesN = ConvertPTSize ( state.stream1.OffsetInBytes );
    uint WriteOffsetStart = viMinBased * StrideN + OffsetInBytesN;
    uint WriteOffsetSize = ( viMaxBased - viMinBased ) * StrideN;

    assert ( WriteOffsetStart == ConvertPTSize ( ReadOffsetStart ) );
    assert ( WriteOffsetSize == ConvertPTSize ( ReadOffsetSize ) );

    // See if area VB area needs updating
    if ( !pAdditionalInfo->ConvertedRanges.IsRangeSet ( WriteOffsetStart, WriteOffsetSize ) )
    {
        // Update VB area
        UpdateAdditionalStreamContent ( state, pAdditionalInfo, ReadOffsetStart, ReadOffsetSize, WriteOffsetStart, WriteOffsetSize );
        pAdditionalInfo->ConvertedRanges.SetRange ( WriteOffsetStart, WriteOffsetSize );
    }

    // Save old declaration
    hr = m_pDevice->GetVertexDeclaration ( &m_pOldVertexDeclaration );

    // Set declaration
    hr = g_pProxyDevice->SetVertexDeclaration ( pAdditionalInfo->pVertexDeclaration );

    // Set additional stream
    uint OffsetInBytes = ConvertPTSize ( state.stream1.OffsetInBytes );
    hr = m_pDevice->SetStreamSource ( 2, pAdditionalInfo->pStreamData, OffsetInBytes, pAdditionalInfo->Stride );
}
```

## See Also

- [CAdditionalVertexStreamManager](mta://reference/misc/cadditionalvertexstreammanager.md)
