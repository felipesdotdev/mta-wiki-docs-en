---
doc_id: "mta-wiki:1739"
title: "GetClothesTypeName"
source_title: "GetClothesTypeName"
source_url: "https://wiki.multitheftauto.com/wiki/GetClothesTypeName"
revision_id: 64782
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetClothesTypeName

This function is used to get the name of a certain clothes type.

## Syntax

```
string getClothesTypeName ( int clothesType )
```

### Required Arguments

- **clothesType**: An integer determining the type of clothes you want to get the clothes of.

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

## Returns

This function returns a string (the name of the clothes type) if found, *false* otherwise.

## Example

This example is used to output in the chatbox what clothes type the player who uses the 'clothes' command is wearing.

```
function getClothes ( thePlayer, key, clothesType )
  local texture, model = getPedClothes ( source, clothesType )
  if ( texture and model ) then
    outputChatBox ( getPlayerName ( thePlayer ) .. " is wearing " .. texture .. " " .. model .. " on his " .. getClothesTypeName ( clothesType ) )
  end
end
addCommandHandler ( "clothes", getClothes )
```

## See Also

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- getClothesTypeName

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)
