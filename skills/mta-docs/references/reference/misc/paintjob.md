---
doc_id: "mta-wiki:7639"
title: "Paintjob"
source_title: "Paintjob"
source_url: "https://wiki.multitheftauto.com/wiki/Paintjob"
revision_id: 73217
language: "en"
categories: []
---

# Paintjob

Paintjobs can be applied on a vehicle using [setVehiclePaintjob](mta://scripting/shared/functions/setvehiclepaintjob.md).

To remove a paintjob from a vehicle, apply paintjob number 3 to it.

## Supported vehicles

- Blade: 0,1,2

- Broadway: 0,1

- Camper: 0

- Elegy: 0,1,2

- Flash: 0,1,2

- Jester: 0,1,2

- Remington: 0,1,2

- Savanna: 0,1,2

- Slamvan: 0,1,2

- Sultan: 0,1,2

- Tornado: 0,1,2

- Uranus: 0,1,2

## Serialized table of supported vehicles

```
local supported_vehicles={
    [483]={0},        -- camper
    [534]={0,1,2},    -- remington
    [535]={0,1,2},    -- slamvan
    [536]={0,1,2},    -- blade
    [558]={0,1,2},    -- uranus
    [559]={0,1,2},    -- jester
    [560]={0,1,2},    -- sultan
    [561]={0,1,2},    -- stratum
    [562]={0,1,2},    -- elegy
    [565]={0,1,2},    -- flash
    [567]={0,1,2},    -- savanna
    [575]={0,1},      -- broadway
    [576]={0,1,2},    -- tornado
}
```

## See Also

- [ID Lists](https://wiki.multitheftauto.com/index.php?search=ID%20Lists)
