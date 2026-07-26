---
doc_id: "mta-wiki:14543"
title: "AddClothingModel"
source_title: "AddClothingModel"
source_url: "https://wiki.multitheftauto.com/wiki/AddClothingModel"
revision_id: 81908
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# AddClothingModel

ADDED/UPDATED IN VERSION 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124):

This function adds a new wearable clothing item for CJ. 

## Syntax

```
bool addClothingModel ( string clothesTexture, string clothesModel, int clothesType )
```

### Required Arguments

- **clothesTexture:** A string determining the clothes texture that will be added.

- **clothesModel:** A string determining the clothes model that will be added.

- **clothesType:** A integer representing the clothes slot/type the clothes should be added to. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

### Returns

Returns *true* if the clothing was added, and *false* otherwise.

## Example

```
local dff = engineLoadDFF("shirt_model_1.dff")
local txd = engineLoadTXD("shirt_model_1.txd")

engineAddClothingModel(dff, "shirt_model_1.dff")
engineAddClothingTXD(txd, "shirt_model_1.txd")

addClothingModel("shirt_model_1", "shirt_model_1", 0)
```

## See Also

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- addClothingModel
