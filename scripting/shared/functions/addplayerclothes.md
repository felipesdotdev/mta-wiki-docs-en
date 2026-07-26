---
doc_id: "mta-wiki:1741"
title: "AddPlayerClothes"
source_title: "AddPlayerClothes"
source_url: "https://wiki.multitheftauto.com/wiki/AddPlayerClothes"
revision_id: 67705
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:10:20.717542+00:00"
---

# AddPlayerClothes

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use addPedClothes instead. |  |

This function is used to set the current clothes of a certain type on a [player](mta://reference/misc/player.md). It can only be used on players with the CJ skin (id 0).

## Syntax

```
bool addPlayerClothes ( player thePlayer, string clothesTexture, string clothesModel, int clothesType )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose clothes you want to change.

- **clothesTexture**: A string determining the clothes texture that will be added. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

- **clothesModel**: A string determining the clothes model that will be added. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

- **clothesType**: A integer representing the clothes slot/type the clothes should be added to. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

## Returns

This function returns 'true' if the clothes were successfully added to the player, 'false' otherwise.

## Example

This example adds a 'moto' helmet to a player when he gets on a nrg bike, and removes it when he gets off.

```
function onEnterVehicle ( theVehicle, seat, jacked )
  if ( getVehicleID ( theVehicle ) == 522 ) then      -- if it's an nrg
    addPlayerClothes ( source, "moto", "moto", 16 )   -- add the helmet
  end
end
addEventHandler ( "onPlayerVehicleEnter", root, onEnterVehicle )

function onExitVehicle ( theVehicle, seat, jacked )
  if ( getVehicleID ( theVehicle ) == 522 ) then      -- if it's an nrg
    removePlayerClothes ( source, 16 )                -- remove the helmet
  end
end
addEventHandler ( "onPlayerVehicleExit", root, onExitVehicle )
```

## See Also

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)
