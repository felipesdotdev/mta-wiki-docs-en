---
doc_id: "mta-wiki:8472"
title: "GetSearchLightEndRadius"
source_title: "GetSearchLightEndRadius"
source_url: "https://wiki.multitheftauto.com/wiki/GetSearchLightEndRadius"
revision_id: 62379
language: "en"
categories: ["Client_functions", "Needs_Example"]
generated_at: "2026-07-26T16:15:24.413896+00:00"
---

# GetSearchLightEndRadius

|  | Script Example Missing Function GetSearchLightEndRadius needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

This function gets the end radius of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```
float getSearchLightEndRadius ( searchlight theSearchLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[searchLight](mta://reference/misc/element-searchlight.md):getEndRadius(...)*

**Variable**: *.endRadius*

**Counterpart**: *[setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)*

### Required Arguments

- **theSearchLight**: the searchlight to get the radius of the searchlight's light cone in its end.

### Returns

If the specified searchlight element is valid, this function will return one *float*, which is the searchlight's end radius. If not, it will return *false* plus an error message.

## Example

```
-- TODO
```

## See also

- [createSearchLight](mta://scripting/client/functions/createsearchlight.md)

- [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)

- getSearchLightEndRadius

- [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)

- [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
