---
doc_id: "mta-wiki:3594"
title: "SetBlipOrdering"
source_title: "SetBlipOrdering"
source_url: "https://wiki.multitheftauto.com/wiki/SetBlipOrdering"
revision_id: 63360
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:38.273947+00:00"
---

# SetBlipOrdering

This function sets the Z ordering of a blip. It allows you to make a blip appear on top of or below other blips.

## Syntax

```
bool setBlipOrdering ( blip theBlip, int ordering )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[blip](mta://reference/misc/blip.md):setOrdering(...)*

**Variable**: *.ordering*

**Counterpart**: *[getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)*

### Required Arguments

- **theBlip:** the blip whose Z ordering to change.

- **ordering:** the new Z ordering value. Blips with higher values will appear on top of blips with lower values. Possible range: -32767 to 32767. Default: 0.

### Returns

Returns *true* if the blip ordering was changed successfully, *false* otherwise.

## Example

This example will create a blip and make your blip on top of all other blip's.

Click to collapse [-]
Server

```
function makeBlipHigher(thePlayer)
    local setmeup = createBlipAttachedTo ( thePlayer, 3, 3, 255, 0,0,255,0,99999.0, root)
    setBlipOrdering(setmeup, getBlipOrdering(setmeup) + 1)
    outputChatBox("*INFO: #ffff00Your blip is now on top of others!", thePlayer, 255,0,0,true)
    for i,v in ipairs(getElementsByType"player") do
          if v ~= thePlayer then
                  outputChatBox("*INFO: #ffff00" .. getPlayerName(thePlayer) .. "'s blip is now on top of your blip!",v,255,0,0,true)
          end
    end
end
addCommandHandler("incrementBlip", makeBlipHigher, false, false)
```

## See Also

- [createBlip](mta://scripting/shared/functions/createblip.md)

- [createBlipAttachedTo](mta://scripting/shared/functions/createblipattachedto.md)

- [getBlipColor](mta://scripting/shared/functions/getblipcolor.md)

- [getBlipIcon](mta://scripting/shared/functions/getblipicon.md)

- [getBlipOrdering](mta://scripting/shared/functions/getblipordering.md)

- [getBlipSize](mta://scripting/shared/functions/getblipsize.md)

- [getBlipVisibleDistance](mta://scripting/shared/functions/getblipvisibledistance.md)

- [setBlipColor](mta://scripting/shared/functions/setblipcolor.md)

- [setBlipIcon](mta://scripting/shared/functions/setblipicon.md)

- setBlipOrdering

- [setBlipSize](mta://scripting/shared/functions/setblipsize.md)

- [setBlipVisibleDistance](mta://scripting/shared/functions/setblipvisibledistance.md)
