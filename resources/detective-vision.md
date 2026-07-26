---
doc_id: "mta-wiki:5875"
title: "Resource : Detective vision"
source_title: "Resource:Detective vision"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ADetective_vision"
revision_id: 27316
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:11.280342+00:00"
---

# Resource : Detective vision

This resource able players to see other ped/players below walls and check theys info.
You can download it [here](http://community.multitheftauto.com/index.php?p=resources&s=details&id=2074).

 

How its looks

## Exported Functions

### addWindowInfo

Click to collapse [-]
Client

By this function you can add custom values in info window.

## Syntax

```
bool [string] addWindowInfo ( { string valueName, string elementData, string/nil element, [ { table childValue1, table childValue2, ...} ] } )
```

## Required Arguments

- **valueName**:  Name of value what will shows in window

- **elementData**:  Name of element data from what it will get values

- **element**:  Type of element for what will shows this value, can be "player", "ped" or nil for both

## Returns

Returns true or false and error message if otherwise.

### removeWindowInfo

Click to collapse [-]
Client

By this function you can add remove values from info window.

## Syntax

```
bool [string] removeWindowInfo ( string valueName [, string elementData, string element ] )
```

## Required Arguments

- **valueName**:  Name of value what shows in window

## Optimal Arguments

- **elementData**:  Name of element data from what it get values

- **element**:  Type of element for what shows this value, can be "player" or "ped"

## Returns

Returns true or false if otherwise.

## See also

[MTA Forum topic](http://forum.mtasa.com/viewtopic.php?f=108&t=32886&p=345513#p345513)
