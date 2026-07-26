---
doc_id: "mta-wiki:2297"
title: "Interior"
source_title: "Interior"
source_url: "https://wiki.multitheftauto.com/wiki/Interior"
revision_id: 66263
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:15:53.055234+00:00"
---

# Interior

An *interior* in GTA is an area that isn't 'outside'. For example, inside houses, casinos, restaurants, shops etc. Players can not, by default, access these. You can use various scripting functions to move elements into these interiors. When you change the interior a player is in, they can only see the non-player elements in that interior. Players can see each other in whatever interior they are in.

You can have up to 255 interiors, interior 0 being the first one and referring to the normal GTA world.

The camera's interior is updated when:

- The local player joins the server (set to 0)

- [ResetMapInfo](mta://scripting/server/functions/resetmapinfo.md) is called (set to 0)

- The local player spawns (set to the player's interior)

- [setElementInterior](mta://scripting/shared/functions/setelementinterior.md) is called

## Uses

To allow a player to enter an interior, you should use the [setElementInterior](mta://scripting/shared/functions/setelementinterior.md) function on the player you wish to move. You can also use this function on other elements, for example to make a vehicle or object appear in the interior.

## Dimensions

The original GTA interiors are reused in a number of places throughout the game - e.g. each fast food restaurant interior is used many times. [Dimensions](mta://reference/misc/dimension.md) are a feature that was added to MTA to solve this problem. You can allocate each instance of the interior a separate dimension which will mean that the players in each dimension won't be able to see each other or interact with each other. This will mean that the interiors appear to be entirely separate, despite physically being in the same place.

## Relevant scripting functions

- [getElementInterior](mta://scripting/shared/functions/getelementinterior.md)

- [setElementInterior](mta://scripting/shared/functions/setelementinterior.md)

- [spawnPlayer](mta://scripting/server/functions/spawnplayer.md)

## See Also

- [List of interior IDs](mta://reference/misc/interior-ids.md)

- [Dimension](mta://reference/misc/dimension.md)
