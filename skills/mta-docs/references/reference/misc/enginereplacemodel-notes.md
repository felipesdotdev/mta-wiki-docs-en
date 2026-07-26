---
doc_id: "mta-wiki:7701"
title: "EngineReplaceModel notes"
source_title: "EngineReplaceModel notes"
source_url: "https://wiki.multitheftauto.com/wiki/EngineReplaceModel_notes"
revision_id: 80960
language: "en"
categories: ["MTA_Wiki:Delete"]
---

# EngineReplaceModel notes

Replacing models in the original GTA map

There are two ways to replace models in the original GTA map:

## Method 1: Move camera away during replace process

Click to collapse [-]
Client

```
local modelId = 12853

    setCameraMatrix( 10000, 0, 0 ) -- Move camera far away

    col = engineLoadCOL( "garage.col" )
    txd = engineLoadTXD( "garage.txd" )
    dff = engineLoadDFF( "garage.dff", 0 )
     
    engineReplaceCOL( col, modelId )
    engineImportTXD( txd, modelId )
    engineReplaceModel( dff, modelId )

    setTimer( function()
        setCameraTarget( localPlayer ) -- Move camera back after a delay
    end, 50, 1 )
```

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Template not needed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

## Method 2: Create custom object and hide original

Click to collapse [-]
Client

```
local modelId = 12853
    local x,y,z = 661, -561, 17

    obj = createObject( modelId, x,y,z )
    removeWorldModel( modelId, 100, x,y,z ) -- Hide original

    col = engineLoadCOL( "garage.col" )
    txd = engineLoadTXD( "garage.txd" )
    dff = engineLoadDFF( "garage.dff", 0 )
     
    engineReplaceCOL( col, modelId )
    engineImportTXD( txd, modelId )
    engineReplaceModel( dff, modelId )
```

# Additonal Note

**Sometimes you need to replace the model far away from where the model/texture change is being made**
so if you are in the game and you are trying to replace a model then get away from the model till it is gone from your draw distance for making sure that this problem won't happen
