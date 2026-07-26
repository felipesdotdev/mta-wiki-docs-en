---
doc_id: "mta-wiki:5486"
title: "EngineUnloadIFP"
source_title: "EngineUnloadIFP"
source_url: "https://wiki.multitheftauto.com/wiki/EngineUnloadIFP"
revision_id: 55373
language: "en"
categories: ["Client_functions", "Disabled_Functions_and_Events"]
generated_at: "2026-07-26T16:14:59.333368+00:00"
---

# EngineUnloadIFP

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: Function disabled. It doesn't exist anymore, use destroyElement to unload IFP. |  |

This function unloads an animation library loaded by [engineLoadIFP](mta://scripting/client/functions/engineloadifp.md).

## Syntax

```
bool engineLoadIFP ( element ifp )
```

### Required Arguments

- **ifp:** The IFP [element](mta://reference/misc/element.md) loaded by [engineLoadIFP](mta://scripting/client/functions/engineloadifp.md) to unload.

### Returns

Returns *true* if the IFP file has been unloaded succesfully, *false* otherwise.

## Example

Click to collapse [-]
animation.lua

```
local localPlayer = getLocalPlayer()
local ifp = nil

function setanimation()
  ifp = engineLoadIFP("data/ani.ifp")
  if ifp then
    setPedAnimation(localPlayer, "ANIMATIONBLOCK", "animation1")
  end
end

addCommandHandler("animation", setanimation)

function stopanimation()
  if ifp then
    engineUnloadIFP(ifp)
    setPedAnimation(localPlayer)
  end
end

addCommandHandler("stopanimation", stopanimation)
```

Click to collapse [-]
meta.xml

```
<meta>
  <info author="lukry" version="1.0" type="script" />
  <script src="animation.lua" type="client" />
  <file src="data/ani.ifp" />
</meta>
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
