---
doc_id: "mta-wiki:1737"
title: "GetClothesByTypeIndex"
source_title: "GetClothesByTypeIndex"
source_url: "https://wiki.multitheftauto.com/wiki/GetClothesByTypeIndex"
revision_id: 59275
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:08.560952+00:00"
---

# GetClothesByTypeIndex

This function is used to get the texture and model of clothes by the clothes type and index.
(Scans through the list of clothes for the specific type).

## Syntax

```
string string getClothesByTypeIndex ( int clothesType, int clothesIndex )
```

### Required Arguments

- **clothesType**: An integer representing the clothes slot/type to scan through.

Clothing Types

- **0:** SHIRT

- **1:** HEAD

- **2:** TROUSERS

- **3:** SHOES

- **4:** TATTOOS_LEFT_UPPER_ARM

- **5:** TATTOOS_LEFT_LOWER_ARM

- **6:** TATTOOS_RIGHT_UPPER_ARM

- **7:** TATTOOS_RIGHT_LOWER_ARM

- **8:** TATTOOS_BACK

- **9:** TATTOOS_LEFT_CHEST

- **10:** TATTOOS_RIGHT_CHEST

- **11:** TATTOOS_STOMACH

- **12:** TATTOOS_LOWER_BACK

- **13:** NECKLACE

- **14:** WATCH

- **15:** GLASSES

- **16:** HAT

- **17:** EXTRA

- **clothesIndex**: An integer representing the index (0 based) set of clothes in the list you wish to retrieve. Each type has a different number of valid indexes.

## Returns

This function returns 2 strings, a texture and model respectively, *false* if invalid arguments were passed to the function.

## Example

This example gets the current clothes of a certain type on a player, then swaps with the next in the clothes list.

```
function scriptNextClothes ( thePlayer, key, clothesType )
  local currentTexture, currentModel = getPedClothes ( thePlayer, clothesType ) -- get the current clothes on this slot
  local clothesIndex = -1
  if ( currentTexture ) then -- if he had clothes of that type
    local tempA, tempB = getTypeIndexFromClothes ( currentTexture, currentModel ) -- get the type and index for these clothes, so we can increase it to get the next set in the list
    if ( tempA and tempB ) then -- if we found them
      clothesType, clothesIndex = tempA, tempB
    end
  end
  clothesIndex = clothesIndex + 1
  local texture, model = getClothesByTypeIndex ( clothesType, clothesIndex ) -- get the new texture and model
  if ( texture == false ) then -- if we've reached the end of the list
    removePedClothes ( thePlayer, clothesType )
  else addPedClothes ( thePlayer, texture, model, clothesType )
  end
end
addCommandHandler ( "nextClothes", scriptNextClothes )
```

## See Also

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- getClothesByTypeIndex

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)
