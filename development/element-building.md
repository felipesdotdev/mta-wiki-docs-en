---
doc_id: "mta-wiki:14280"
title: "Element/Building"
source_title: "Element/Building"
source_url: "https://wiki.multitheftauto.com/wiki/Element/Building"
revision_id: 80971
language: "en"
categories: ["Changes_in_1.6.0", "Element_Types"]
generated_at: "2026-07-26T16:14:52.744469+00:00"
---

# Element/Building

The building class represents **static** 3D models in the GTA world.

The element type of this class is **"building"**.

## Important info about [Buildings](mta://development/building.md)

- There is a distinction in GTA: San Andreas between static and dynamic models (these use a separate streaming system). Examples of buildings include building models, roads, and terrain. Objects created as [Buildings](mta://development/building.md) can contain **glass** and **shadows**, unlike those created as [Objects](mta://reference/misc/object.md) (which are missing these features).

- Buildings can be created with dynamic object model IDs, but they won't have any physical interaction. For example, [object ID 1502 (Gen_doorINT04)](https://dev.prineside.com/en/gtasa_samp_model_id/model/1502-Gen_doorINT04/) is a door that can only be opened if created with [createObject](mta://scripting/shared/functions/createobject.md).

- Using buildings for mapping is more optimized than using objects. Gains in FPS can be noticed in areas where a lot of objects were replaced with buildings of this new system.

- Buildings can only be created inside regular GTA:SA Map Boundaries (X between -3000 and 3000; Y between -3000 and 3000). Use [createObject](mta://scripting/shared/functions/createobject.md) to spawn objects outside these normal limits. **This limitation is probably going to stop existing in the near future.**

- Created buildings can have **LOD models**. The procedure is as follows: spawn the LOD building using [createBuilding](mta://scripting/shared/functions/createbuilding.md), then use [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md) to associate it with the non-LOD building element you created beforehand. LOD model distance changed with [engineSetModelLODDistance](mta://scripting/client/functions/enginesetmodelloddistance.md) works for buildings.

- Buildings cannot appear in certain a [dimension](mta://reference/misc/dimension.md), and not show in others. Function [setElementDimension](mta://scripting/shared/functions/setelementdimension.md) returns false on any building. A building is created in a specific [interior world](mta://reference/misc/interior.md) (such as 0, the main world), like the default GTA:SA landscape objects. All **buildings appear in EVERY DIMENSION**.

## Object Models

[List of Object Model IDs](mta://reference/misc/object-ids.md)

## Related scripting functions

ADDED/UPDATED IN VERSION 1.6.0 [r22410](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22410):

- [createBuilding](mta://scripting/shared/functions/createbuilding.md)
