---
doc_id: "mta-wiki:2296"
title: "Dimension"
source_title: "Dimension"
source_url: "https://wiki.multitheftauto.com/wiki/Dimension"
revision_id: 80720
language: "en"
categories: ["Scripting_Concepts"]
---

# Dimension

Dimensions are a way of separating parts of the game world from each other. Each dimension can contain elements of the types listed below. These are are only visible to players in the same dimension. You can, in theory, have up to 65535 dimensions.

The following [Element](mta://reference/misc/element.md) types can be used in the Dimension system:

- [Player](mta://reference/misc/element-player.md)

- [Ped](mta://reference/misc/element-ped.md)

- [Vehicle](mta://reference/misc/element-vehicle.md)

- [Object](mta://reference/misc/element-object.md)

- [Pickup](mta://reference/misc/element-pickup.md)

- [Marker](mta://reference/misc/element-marker.md)

- [Collision shape](mta://reference/misc/element-collision-shape.md)

- [Blip](mta://reference/misc/element-blip.md)

- [Radar area](mta://reference/misc/element-radar-area.md)

- [Team](mta://reference/misc/element-team.md)

- [Sound](mta://reference/misc/element-sound.md)

- [Weapon](mta://reference/misc/element-weapon.md)

- [Light](mta://reference/misc/element-light.md)

- [Water](mta://reference/misc/element-water.md)

- Custom dummy elements ([createElement](mta://scripting/shared/functions/createelement.md))

The camera's dimension is updated when:

- The local player joins the server (set to 0)

- [ResetMapInfo](mta://scripting/server/functions/resetmapinfo.md) is called (set to 0)

- The local player spawns (set to the player's dimension)

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) is called

## Uses

A useful use of this is for unique [interiors](mta://reference/misc/interior.md). For example, there is only one actual Pizza restaurant in San Andreas, with each warp point going to the same place. This works fine in single player games (as you aren't going to be in two places at once), but with multiplayer this can be confusing, as you could enter in one place and see all the players who entered in another. To avoid this, you can split the players into dimensions, so they will only see players who entered in the same place, duplicating the Pizza restaurant interior as many times as you want with different dimensions.

## Relevant scripting functions

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md)

- [getElementDimension](mta://scripting/shared/functions/getelementdimension.md)

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md)

## See Also

- [Interior](mta://reference/misc/interior.md)
