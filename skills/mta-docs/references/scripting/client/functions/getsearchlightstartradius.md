---
doc_id: "mta-wiki:8471"
title: "GetSearchLightStartRadius"
source_title: "GetSearchLightStartRadius"
source_url: "https://wiki.multitheftauto.com/wiki/GetSearchLightStartRadius"
revision_id: 62380
language: "en"
categories: ["Client_functions", "Needs_Example"]
---

# GetSearchLightStartRadius

|  | Script Example Missing Function GetSearchLightStartRadius needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

This function gets the start radius of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```
float getSearchLightStartRadius ( searchlight theSearchLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[searchLight](mta://reference/misc/element-searchlight.md):getStartRadius(...)*

**Variable**: *.startRadius*

**Counterpart**: *[setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)*

### Required Arguments

- **theSearchLight**: the searchlight to get the radius of the searchlight's light cone in its beginning.

### Returns

If the specified searchlight element is valid, this function will return one *float*, which is the searchlight's start radius. If not, it will return *false* plus an error message.

## Example

```
-- TODO
```

## See also

- [createSearchLight](mta://scripting/client/functions/createsearchlight.md)

- [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)

- [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md)

- [getSearchLightStartPosition](mta://scripting/client/functions/getsearchlightstartposition.md)

- getSearchLightStartRadius

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
