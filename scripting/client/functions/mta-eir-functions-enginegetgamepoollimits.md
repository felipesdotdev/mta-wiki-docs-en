---
doc_id: "mta-wiki:7380"
title: "MTA:Eir/functions/engineGetGamePoolLimits"
source_title: "MTA:Eir/functions/engineGetGamePoolLimits"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetGamePoolLimits"
revision_id: 77719
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.405181+00:00"
---

# MTA:Eir/functions/engineGetGamePoolLimits

This function returns a table of game resource allocation limits. In GTA:SA resources are allocated on statically-sized pools. Pool information returned may look like this:

```
{
    { name = "Buildings", usedCount = 1132, maxCount = 13000 },
    { name = "Peds", usedCount = 2, maxCount = 110 },
    { name = "Objects", usedCount = 44, maxCount = 800 },
    { name = "Dummies", usedCount = 2199, maxCount = 8000 },
    { name = "Vehicles", usedCount = 2, maxCount = 110 },
    { name = "ColModels", usedCount = 2268, maxCount = 20000 },
    { name = "Tasks", usedCount = 7, maxCount = 9000 },
    { name = "Events", usedCount = 0, maxCount = 5000 },
    { name = "TaskAllocators", usedCount = 2, maxCount = 800 },
    { name = "PedIntelligence", usedCount = 2, maxCount = 110 },
    { name = "PedAttractors", usedCount = 0, maxCount = 400 },
    { name = "EntryInfoNodes", usedCount = 104, maxCount = 10000 },
    { name = "NodeRoutes", usedCount = 181, maxCount = 8000 },
    { name = "PatrolRoutes", usedCount = 23, maxCount = 6000 },
    { name = "PointRoutes", usedCount = 273, maxCount = 7000 },
    { name = "PointerNodeDoubleLinks", usedCount = 48, maxCount = 20000 },
    { name = "PointerNodeSingleLinks", usedCount = 3379, maxCount = 20000 },
    { name = "EnvMapMaterials", usedCount = 61, maxCount = 5000 },
    { name = "EnvMapAtomics", usedCount = 98, maxCount = 5000 },
    { name = "SpecMapMaterials", usedCount = 56, maxCount = 5000 },
    { name = "COLSectors", usedCount = 81, maxCount = 256 },
    { name = "IPLSectors", usedCount = 76, maxCount = 255 }
}
```

When certain limits (such as the "PointerNodeSingleLinks") are reached within the engine, the game will crash. Hence retrieving pool information during testing is important.

## Syntax

```
table engineGetGamePoolLimits ()
```

### Returns

Returns a **table** holding internal engine pool limit info.

### Useful Media

- [https://dl.dropboxusercontent.com/u/55896914/eir_resources/game_pools.zip](https://dl.dropboxusercontent.com/u/55896914/eir_resources/game_pools.zip) - resource to draw engine pool limits onto the screen

## Example

Click to collapse [-]
Client

This snippet prints out the engine pool information to the client console.

```
addCommandHandler( "debug_pools",
    function()
        local poolInfo = engineGetGamePoolLimits();

        outputConsole( "-- GAME POOL INFO --" );

        for m,n in ipairs( poolInfo ) do
            outputConsole( n.name .. ": " .. n.usedCount .. " / " .. n.maxCount );
        end
    end
);
```
