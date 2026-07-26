---
doc_id: "mta-wiki:1738"
title: "GetTypeIndexFromClothes"
source_title: "GetTypeIndexFromClothes"
source_url: "https://wiki.multitheftauto.com/wiki/GetTypeIndexFromClothes"
revision_id: 59283
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:26.590437+00:00"
---

# GetTypeIndexFromClothes

This function is used to get the clothes type and index from the texture and model.
(Scans through the list of clothes for the specific type).

## Syntax

```
int int getTypeIndexFromClothes ( string clothesTexture, string clothesModel )
```

### Required Arguments

- **clothesTexture**: A string determining the clothes texture that you wish to retrieve the type and index from. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

- **clothesModel**: A string determining the corresponding clothes model that you wish to retrieve the type and index from. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

## Returns

This function returns two integers, type and index respectively, *false* if invalid arguments were passed to the function.

## Example

This example gets the current clothes of a certain type on a player, then swaps with the previous in the clothes list.

```
function scriptPreviousClothes ( thePlayer, key, clothesType )
  local currentTexture, currentModel = getPedClothes ( thePlayer, clothesType ) -- get the current clothes on this slot
  local clothesIndex = 1
  if ( currentTexture ) then -- if he had clothes of that type
    local tempA, tempB = getTypeIndexFromClothes ( currentTexture, currentModel ) -- get the type and index for these clothes, so we can decrease and get the previous in the list
    if ( tempA and tempB ) then -- if we found them
      clothesType, clothesIndex = tempA, tempB
    end
  end
  clothesIndex = clothesIndex - 1
  local texture, model = getClothesByTypeIndex ( clothesType, clothesIndex ) -- get the new texture and model
  if ( texture == false ) then -- if we've reached the end of the list
    removePedClothes ( thePlayer, clothesType )
  else addPedClothes ( thePlayer, texture, model, clothesType )
  end
end
addCommandHandler ( "previousClothes", scriptPreviousClothes )
```

## See Also

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- getTypeIndexFromClothes

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)
