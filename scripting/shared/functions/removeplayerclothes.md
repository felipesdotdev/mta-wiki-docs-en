---
doc_id: "mta-wiki:1742"
title: "RemovePlayerClothes"
source_title: "RemovePlayerClothes"
source_url: "https://wiki.multitheftauto.com/wiki/RemovePlayerClothes"
revision_id: 67713
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:32.514803+00:00"
---

# RemovePlayerClothes

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use removePedClothes instead. |  |

This function is used to remove the current clothes of a certain type on a [player](mta://reference/misc/player.md). It will remove them if the clothesTexture and clothesModel aren't specified, or if they match the current clothes on that slot.

## Syntax

```
bool removePlayerClothes ( player thePlayer, int clothesType, [ string clothesTexture, string clothesModel ] )
```

### Required Arguments

- **thePlayer**: The [player](mta://reference/misc/player.md) whose clothes you want to remove.

- **clothesType**: A integer representing the clothes slot/type to remove. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

### Optional Arguments

- **clothesTexture**: A string determining the clothes texture that will be removed. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

- **clothesModel**: A string determining the clothes model that will be removed. See the [clothes catalog](mta://reference/misc/cj-clothes.md).

## Returns

This function returns *true* if the clothes were successfully removed from the player, *false* otherwise.

## Example

This example adds a 'moto' helmet to a player when he gets on a nrg bike, and removes it when he gets off.

```
function addHelmetOnEnter ( vehicle, seat, jacked )
    if ( getVehicleID ( vehicle ) == 522 ) then            -- if its a nrg
        addPlayerClothes ( source, "moto", "moto", 16 )    -- add the helmet
    end
end
addEventHandler ( "onPlayerVehicleEnter", root, addHelmetOnEnter )

function addHelmetOnExit ( vehicle, seat, jacked )
    if ( getVehicleID ( vehicle ) == 522 ) then            -- if its a nrg
        removePlayerClothes ( source, 16, "moto", "moto" ) -- remove that helmet
    end
end
addEventHandler ( "onPlayerVehicleExit", root, addHelmetOnExit )
```

## See Also

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)
