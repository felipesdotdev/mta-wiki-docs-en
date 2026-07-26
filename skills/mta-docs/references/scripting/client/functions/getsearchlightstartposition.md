---
doc_id: "mta-wiki:8469"
title: "GetSearchLightStartPosition"
source_title: "GetSearchLightStartPosition"
source_url: "https://wiki.multitheftauto.com/wiki/GetSearchLightStartPosition"
revision_id: 62378
language: "en"
categories: ["Client_functions", "Needs_Example"]
---

# GetSearchLightStartPosition

|  | Script Example Missing Function GetSearchLightStartPosition needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

This function gets the start position of a [searchlight](mta://reference/misc/element-searchlight.md) element.

## Syntax

```
float, float, float getSearchLightStartPosition ( searchlight theSearchLight )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[searchLight](mta://reference/misc/element-searchlight.md):getStartPosition(...)*

**Variable**: *.startPosition*

**Counterpart**: *[setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)*

### Required Arguments

- **theSearchLight**: the searchlight to get the position where the searchlight's light cone starts.

### Returns

If the specified searchlight element is valid, this function will return three *float*, which are the three coordinates of searchlight's start position. If not, it will return *false* plus an error message.

## Example

```
-- TODO
```

## See also

- [createSearchLight](mta://scripting/client/functions/createsearchlight.md)

- [getSearchLightEndPosition](mta://scripting/client/functions/getsearchlightendposition.md)

- [getSearchLightEndRadius](mta://scripting/client/functions/getsearchlightendradius.md)

- getSearchLightStartPosition

- [getSearchLightStartRadius](mta://scripting/client/functions/getsearchlightstartradius.md)

- [setSearchLightEndPosition](mta://scripting/client/functions/setsearchlightendposition.md)

- [setSearchLightEndRadius](mta://scripting/client/functions/setsearchlightendradius.md)

- [setSearchLightStartPosition](mta://scripting/client/functions/setsearchlightstartposition.md)

- [setSearchLightStartRadius](mta://scripting/client/functions/setsearchlightstartradius.md)
