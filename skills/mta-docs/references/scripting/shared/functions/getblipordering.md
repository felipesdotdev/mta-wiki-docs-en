---
doc_id: "mta-wiki:3612"
title: "GetBlipOrdering"
source_title: "GetBlipOrdering"
source_url: "https://wiki.multitheftauto.com/wiki/GetBlipOrdering"
revision_id: 63328
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetBlipOrdering

This function gets the Z ordering value of a blip. The Z ordering determines if a blip appears on top of or below other blips. Blips with a higher Z ordering value appear on top of blips with a lower value. The default value for all blips is 0.

## Syntax

```
int getBlipOrdering ( blip theBlip )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](https://wiki.multitheftauto.com/index.php?search=blip):getOrdering(...)*

**Variable**: *.ordering*

**Counterpart**: *[setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)*

### Required Arguments

- **theBlip:** the blip to retrieve the Z ordering value of.

### Returns

Returns the Z ordering value of the blip if successful, *false* otherwise.

## Example

```
function getMyBlip(theBlip)
    local ordering = getBlipOrdering ( theBlip )
    if (ordering) then
        outputChatBox("The following blip has a ordering of "..ordering)
    end
end
```

## See Also

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- getBlipOrdering

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- [setBlipOrdering](mta://scripting/shared/functions/setblipordering.md)

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)
