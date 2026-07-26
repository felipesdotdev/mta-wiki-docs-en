---
doc_id: "mta-wiki:3412"
title: "EngineReplaceModel"
source_title: "EngineReplaceModel"
source_url: "https://wiki.multitheftauto.com/wiki/EngineReplaceModel"
revision_id: 81976
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:57.389077+00:00"
---

# EngineReplaceModel

This function replaces the given model ID with the model contained in a DFF file loaded by [engineLoadDFF](mta://scripting/client/functions/engineloaddff.md). This function supports [vehicles](mta://reference/misc/vehicle.md), [objects](mta://reference/misc/object.md), [peds](mta://reference/misc/ped.md) and [players](mta://reference/misc/player.md).

Since version [r23124](https://buildinfo.multitheftauto.com/?Revision=23124&Branch=) and above replacing CJ clothing became possible - see: [Clothing Component IDs](mta://reference/misc/clothing-component-ids.md). Body parts replacements aren't supported at the moment.

To replace weapon models you must use their object IDs, not weapon IDs. There is a weapon model list available at [Weapons](mta://reference/misc/weapons.md).

| [[{{{image}}}\|link=\|]] | Note: Follow loading order ( COL -> TXD -> DFF ) which is used in the example - as other orders can cause collisions, textures or the DFF not to load due to technical limitations. Default GTA map objects behave inconsistently when using this function on them. If you want to replace models in the original GTA map, you need to call engineRestreamWorld after replacing models as well. A raw data DFF element can only be used once, because the underlying memory for the model is released after replacement. If the replacement model is broken and the original model is not loaded/streamed-in at the time of replacement, this function will succeed and you won't see any error message, neither when the model replacement fails once the original model starts to load/stream-in. |
| --- | --- |
|  |  |

## Syntax

```
bool engineReplaceModel ( dff theModel, int modelID [, bool alphaTransparency = false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[dff](mta://reference/misc/dff.md):replace(...)*

### Required Arguments

- **theModel:** The model to replace the given model ID with

- **modelID:** The model it to replace the model of

### Optional Arguments

- **alphaTransparency:** Set to true if model uses semi-transparent textures, e.g. windows. This will ensure other objects behind the semi-transparent textures are rendered correctly. (Can slightly impact performance, so only set when required)

### Returns

Returns *true* if the model was successfully replaced, *false* if it failed for some reason, ie. the DFF or the model ID is not valid.

## Example

Click to collapse [-]
Client

This example allows you to replace single or many models (with ability to toggle TXD filtering/DFF alpha transparency) - by using [table](mta://reference/misc/table.md). Do not forget to add those file paths to [meta.xml](mta://reference/misc/meta-xml.md)

```
function onClientResourceStartReplaceModels()
	local modelsToReplace = {
		{ -- replace object (all object IDs here: https://dev.prineside.com/en/gtasa_samp_model_id/)
			colFile = "object.col",
			txdFile = "object.txd",
			dffFile = "object.dff",
			modelID = 1337,
			alphaTransparency = false,
			filteringEnabled = true,
		},
		{ -- replace vehicle (all vehicle IDs here: https://wiki.multitheftauto.com/wiki/Vehicle_IDs)
			colFile = false, -- if file is not present set to false/nil
			txdFile = "vehicle.txd",
			dffFile = "vehicle.dff",
			modelID = 434,
			alphaTransparency = false,
			filteringEnabled = true,
		},
		{ -- replace skin (all ped IDs here: https://wiki.multitheftauto.com/wiki/Character_Skins)
			colFile = false, -- if file is not present set to false/nil
			txdFile = "ped.txd",
			dffFile = "ped.dff",
			modelID = 16,
			alphaTransparency = false,
			filteringEnabled = true,
		},
		{ -- replace weapon (all weapon IDs here: https://wiki.multitheftauto.com/wiki/Weapons)
			colFile = false, -- if file is not present set to false/nil
			txdFile = "m4.txd",
			dffFile = "m4.dff",
			modelID = 356,
			alphaTransparency = false,
			filteringEnabled = true,
		},
	}

	for assetID = 1, #modelsToReplace do
		local modelData = modelsToReplace[assetID]
		local modelCol = modelData.colFile
		local modelTxd = modelData.txdFile
		local modelDff = modelData.dffFile
		local modelID = modelData.modelID

		if (modelCol) then
			local colData = engineLoadCOL(modelCol)

			if (colData) then
				engineReplaceCOL(colData, modelID)
			end
		end

		if (modelTxd) then
			local filteringEnabled = modelData.filteringEnabled
			local txdData = engineLoadTXD(modelTxd, filteringEnabled)

			if (txdData) then
				engineImportTXD(txdData, modelID)
			end
		end

		if (modelDff) then
			local dffData = engineLoadDFF(modelDff)

			if (dffData) then
				local alphaTransparency = modelData.alphaTransparency
				
				engineReplaceModel(dffData, modelID, alphaTransparency)
			end
		end
	end
end
addEventHandler("onClientResourceStart", resourceRoot, onClientResourceStartReplaceModels)
```

## See Also

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

- engineReplaceModel

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

- [engineSetModelLODDistance](mta://scripting/client/functions/enginesetmodelloddistance.md)

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
