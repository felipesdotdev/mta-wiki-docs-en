---
doc_id: "mta-wiki:4573"
title: "EngineSetModelLODDistance"
source_title: "EngineSetModelLODDistance"
source_url: "https://wiki.multitheftauto.com/wiki/EngineSetModelLODDistance"
revision_id: 82273
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:14:58.433667+00:00"
---

# EngineSetModelLODDistance

This function sets a custom LOD distance for any object / model ID. This is the distance at which objects of that model ID are switched to their LOD model, or (if there is no LOD model) become invisible.

**Known Issues:**

- **This function only works with script-created objects**, just like objects created  with **CreateObject** or buildings created with **createBuilding**. It **DOES NOT** work with default map objects/buildings.

- **If the LOD distance**for a high LOD model**is set to more than 325, the fade out effect of the model will not trigger and the model will just pop in/pop out of existence.**

**Notes:**

- The actual draw distance used is modified by the draw distance slider in the settings 'Video' tab of the MTA client.

- When the 'Video' tab draw distance slider is 0%, the engineSetModelLODDistance setting approximately matches the draw distance used.

*e.g. engineSetModelLODDistance(1337,100) will mean model 1337 will be visible up to a distance of **100** units.*

- When the 'Video' tab draw distance slider is 100%, the engineSetModelLODDistance setting is approximately doubled before use.

*e.g. engineSetModelLODDistance(1337,100) will mean model 1337 will be visible up to a distance of **200** units.*

However, there is a general draw distance limit of 325 units. So engineSetModelLODDistance(1337,400) will mean model 1337 will be visible up to a distance of 325 units no matter what the 'Video' tab says.

Therefore, unless it's really important, engineSetModelLODDistance should not be set to anything greater than 170.  

170 will still give the maximum draw distance (of 325 units) on clients that have a 'Video' tab draw distance setting of 100%, and it will help reduce lag for players who chose a lower draw distance in their settings.

**Note for low LOD [objects](mta://reference/misc/object.md)**:

- The limit is 325 units, but the actual draw distance used is 5 times the setting value. Also, they ignore the 'Video' tab draw distance slider. So a setting of 200 will mean a low LOD element will always have a draw distance of **1000** units.

**Note for low LOD [buildings](mta://development/building.md)**:

- The distance must be set greater than 300 for a low LOD building in order to work correctly. Otherwise, the low LOD will always be visible. The actual draw distance is NOT 5 times the setting value.

## Syntax

```
bool engineSetModelLODDistance ( int model, float distance [, bool extendedLod = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *Engine.setModelLODDistance(...)*

### Required Arguments

- **model:** The model / object ID number you want to change the LOD distance of.

- **distance:** New LOD distance value in San Andreas units.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

ADDED/UPDATED IN VERSION 1.6.0 [r22676](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22676):

- **extendedLod:** Allows to set a greater distance than the current 325 units.

### Returns

Returns *true* if the function executed succesfully, *false* otherwise.

## Example

This example will set the LOD distance of all script-created objects.

```
-- Client-side
-- WARNING: Can cause significant lag.

-- Adjusts LOD for all objects.
function setAllObjectsLOD()

    -- Get all current objects.
    local objects = getElementsByType("object", root, false)

    for _, theObject in ipairs(objects) do

        local modelID = getElementModel(theObject)
        local lodLevel = 325 -- Distance value

        -- Set LOD for this model ID.
        -- The 'true' enables extended range.
        engineSetModelLODDistance(modelID, lodLevel, true)

    end
end

-- Command to run the function.
addCommandHandler("setAllObjectsLOD", setAllObjectsLOD)
```

This example will, besides replacing with custom map objects, also set the LOD distance accordingly, a necessary step (otherwise the object could seem to fail loading and only show up 1 feet away).

```
function replaceObjects()

	local col1 = engineLoadCOL("map1.col")
	local col2 = engineLoadCOL("map2.col")

	local txd = engineLoadTXD("map.txd")
	engineImportTXD(txd, 2357)
	engineImportTXD(txd, 2290)

	local dff1 = engineLoadDFF("map1.dff")
	local dff2 = engineLoadDFF("map2.dff")

	engineReplaceCOL(col1, 2357)
	engineReplaceCOL(col2, 2290)
	engineReplaceModel(dff1, 2357)
	engineReplaceModel(dff2, 2290)

	engineSetModelLODDistance(2357, 325)
	engineSetModelLODDistance(2290, 325)
end
```

This example shows how to use LOD's with buildings.

```
function createMyPyramid()
    local pos = Vector3(0, 0, 3)
    local rot = Vector3(0, 0, 0)
    
    local modelHi = 8395  -- This model has a lot of polygons
    local modelLow = 8701 -- This model is optimized for drawing at a long distance

    -- Always call this function if you don't like default draw distance
    -- or you allocated the model with using engineRequestModel
    engineSetModelLODDistance(modelHi, 100, true)
    engineSetModelLODDistance(modelLow, 500, true)

    local lod = createBuilding(modelLow, pos, rot)
    local building = createBuilding(modelHi, pos, rot)

    setLowLODElement(building,lod)
end
```

## Changelog

| Version | Description |
| --- | --- |

| 1.6.0-9.22676 | Added extendedLod argument |
| --- | --- |

## See Also

- [getVehiclesLODDistance](mta://scripting/client/functions/getvehiclesloddistance.md)

- [resetVehiclesLODDistance](mta://scripting/client/functions/resetvehiclesloddistance.md)

- [setVehiclesLODDistance](mta://scripting/client/functions/setvehiclesloddistance.md)

- [engineAddImage](mta://scripting/client/functions/engineaddimage.md)

- [engineApplyShaderToWorldTexture](mta://scripting/client/functions/engineapplyshadertoworldtexture.md)

- [engineFreeModel](mta://scripting/client/functions/enginefreemodel.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22190](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22190))

- [engineFreeTXD](mta://scripting/client/functions/enginefreetxd.md)

- [engineGetModelFlags](mta://scripting/client/functions/enginegetmodelflags.md)

- [engineGetModelIDFromName](mta://scripting/client/functions/enginegetmodelidfromname.md)

- [engineGetModelLODDistance](mta://scripting/client/functions/enginegetmodelloddistance.md)

- [engineGetModelNameFromID](mta://scripting/client/functions/enginegetmodelnamefromid.md)

- [engineGetModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginegetmodelphysicalpropertiesgroup.md)

- [engineGetModelTextureNames](mta://scripting/client/functions/enginegetmodeltexturenames.md)

- [engineGetModelTextures](mta://scripting/client/functions/enginegetmodeltextures.md)

- [engineGetModelTXDID](mta://scripting/client/functions/enginegetmodeltxdid.md)

- [engineGetModelVisibleTime](mta://scripting/client/functions/enginegetmodelvisibletime.md)

- [engineGetObjectGroupPhysicalProperty](mta://scripting/client/functions/enginegetobjectgroupphysicalproperty.md)

- [engineGetSurfaceProperties](mta://scripting/client/functions/enginegetsurfaceproperties.md)

- [engineGetVisibleTextureNames](mta://scripting/client/functions/enginegetvisibletexturenames.md)

- [engineImageGetFilesCount](mta://scripting/client/functions/engineimagegetfilescount.md)

- [engineImageGetFiles](mta://scripting/client/functions/engineimagegetfiles.md)

- [engineImageGetFile](mta://scripting/client/functions/engineimagegetfile.md)

- [engineImageLinkDFF](mta://scripting/client/functions/engineimagelinkdff.md)

- [engineImageLinkTXD](mta://scripting/client/functions/engineimagelinktxd.md)

- [engineImportTXD](mta://scripting/client/functions/engineimporttxd.md)

- [engineLoadCOL](mta://scripting/client/functions/engineloadcol.md)

- [engineLoadDFF](mta://scripting/client/functions/engineloaddff.md)

- [engineLoadIMG](mta://scripting/client/functions/engineloadimg.md)

- [engineLoadIFP](mta://scripting/client/functions/engineloadifp.md)

- [engineLoadTXD](mta://scripting/client/functions/engineloadtxd.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22678](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22678):

- [enginePreloadWorldArea](mta://scripting/client/functions/enginepreloadworldarea.md)

- [engineRemoveImage](mta://scripting/client/functions/engineremoveimage.md)

- [engineRemoveShaderFromWorldTexture](mta://scripting/client/functions/engineremoveshaderfromworldtexture.md)

- [engineReplaceAnimation](mta://scripting/client/functions/enginereplaceanimation.md)

- [engineReplaceCOL](mta://scripting/client/functions/enginereplacecol.md)

- [engineReplaceModel](mta://scripting/client/functions/enginereplacemodel.md)

- [engineRequestModel](mta://scripting/client/functions/enginerequestmodel.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22190](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22190))

- [engineRequestTXD](mta://scripting/client/functions/enginerequesttxd.md)

- [engineResetModelFlags](mta://scripting/client/functions/engineresetmodelflags.md)

- [engineResetModelLODDistance](mta://scripting/client/functions/engineresetmodelloddistance.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22190](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22190))

- [engineResetModelTXDID](mta://scripting/client/functions/engineresetmodeltxdid.md)

- [engineResetSurfaceProperties](mta://scripting/client/functions/engineresetsurfaceproperties.md)

- [engineRestoreAnimation](mta://scripting/client/functions/enginerestoreanimation.md)

- [engineRestoreCOL](mta://scripting/client/functions/enginerestorecol.md)

- [engineRestoreDFFImage](mta://scripting/client/functions/enginerestoredffimage.md)

- [engineRestoreModel](mta://scripting/client/functions/enginerestoremodel.md)

- [engineRestoreModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginerestoremodelphysicalpropertiesgroup.md)

- [engineRestoreObjectGroupPhysicalProperties](mta://scripting/client/functions/enginerestoreobjectgroupphysicalproperties.md)

- [engineRestoreTXDImage](mta://scripting/client/functions/enginerestoretxdimage.md)

- [engineRestreamWorld](mta://scripting/client/functions/enginerestreamworld.md)

- [engineSetAsynchronousLoading](mta://scripting/client/functions/enginesetasynchronousloading.md)

- [engineSetModelFlag](mta://scripting/client/functions/enginesetmodelflag.md)

- [engineSetModelFlags](mta://scripting/client/functions/enginesetmodelflags.md)

- engineSetModelLODDistance

- [engineSetModelPhysicalPropertiesGroup](mta://scripting/client/functions/enginesetmodelphysicalpropertiesgroup.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22190](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22190))

- [engineSetModelTXDID](mta://scripting/client/functions/enginesetmodeltxdid.md)

- [engineSetModelVisibleTime](mta://scripting/client/functions/enginesetmodelvisibletime.md)

- [engineSetObjectGroupPhysicalProperty](mta://scripting/client/functions/enginesetobjectgroupphysicalproperty.md)

- [engineSetSurfaceProperties](mta://scripting/client/functions/enginesetsurfaceproperties.md)

- [engineStreamingFreeUpMemory](mta://scripting/client/functions/enginestreamingfreeupmemory.md)

- [engineStreamingGetUsedMemory](mta://scripting/client/functions/enginestreaminggetusedmemory.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21874](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21874))

- [engineStreamingSetMemorySize](mta://scripting/client/functions/enginestreamingsetmemorysize.md)

- [engineStreamingGetMemorySize](mta://scripting/client/functions/enginestreaminggetmemorysize.md)

- [engineStreamingRestoreMemorySize](mta://scripting/client/functions/enginestreamingrestorememorysize.md)

- [engineStreamingSetBufferSize](mta://scripting/client/functions/enginestreamingsetbuffersize.md)

- [engineStreamingGetBufferSize](mta://scripting/client/functions/enginestreaminggetbuffersize.md)

- [engineStreamingRestoreBufferSize](mta://scripting/client/functions/enginestreamingrestorebuffersize.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r21947](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21947))

- [engineStreamingSetModelCacheLimits](mta://scripting/client/functions/enginestreamingsetmodelcachelimits.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22471](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22471))

- [engineGetPoolCapacity](mta://scripting/client/functions/enginegetpoolcapacity.md)

- [engineSetPoolCapacity](mta://scripting/client/functions/enginesetpoolcapacity.md)

- [engineGetPoolDefaultCapacity](mta://scripting/client/functions/enginegetpooldefaultcapacity.md)

- [engineGetPoolUsedCapacity](mta://scripting/client/functions/enginegetpoolusedcapacity.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r22676](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22676))

- [engineStreamingRequestModel](mta://scripting/client/functions/enginestreamingrequestmodel.md)

- [engineStreamingReleaseModel](mta://scripting/client/functions/enginestreamingreleasemodel.md)

- [engineStreamingGetModelLoadState](mta://scripting/client/functions/enginestreaminggetmodelloadstate.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [engineAddClothingTXD](mta://scripting/client/functions/engineaddclothingtxd.md)

- [engineAddClothingModel](mta://scripting/client/functions/engineaddclothingmodel.md)
