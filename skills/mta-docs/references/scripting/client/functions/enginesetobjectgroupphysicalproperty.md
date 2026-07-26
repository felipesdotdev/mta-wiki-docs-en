---
doc_id: "mta-wiki:11892"
title: "EngineSetObjectGroupPhysicalProperty"
source_title: "EngineSetObjectGroupPhysicalProperty"
source_url: "https://wiki.multitheftauto.com/wiki/EngineSetObjectGroupPhysicalProperty"
revision_id: 81231
language: "en"
categories: ["Client_functions", "Changes_in_1.5.7"]
---

# EngineSetObjectGroupPhysicalProperty

This function sets physical property of given properties group.

## Syntax

```
bool engineSetObjectGroupPhysicalProperty ( int groupID, objectgroup-modifiable property, var newValue )
```

### Required Arguments

- **groupID**: the id of physical properties group which you wish to set a property of.

- **objectgroup-modifiable**: the property which you wish to set, as per table below.

- **newValue**: new value of the property, with proper type as specified in table below

### Returns

Returns **true** if everything went well, error is raised otherwise.

### Properties

### Physical properties

| Property | Type | Description |
| --- | --- | --- |
| mass | float | Mass of an object |
| turn_mass | float | Turn mass (kg m^3) of an object |
| air_resistance | float | Air resistance of an object |
| elasticity | float | Elasticity of an object |
| buoyancy | float | Buoyancy of an object |
| uproot_limit | float | How much force is needed to uproot the object |
| col_damage_multiplier | float | Force multiplier used when colliding with object |
| col_damage_effect | DamageEffect | Dictates which damage effect is applied to object on collision |
| special_col_response | CollisionResponse | Dictates how object responds to being collided with |
| avoid_camera | bool | Dictates whether camera passes throught the object |
| cause_explosion | bool | Dictates whether objects exploded upon collision |
| fx_type | FxType | Dictates when particles will be created when colliding with object |
| fx_offset | Vector3D | Offset from center of mass where particles will be created upon collision |
| fx_system | FxEffect(string) | Effect that will be used upon collision |
| smash_multiplier | float | Force multiplier when destroying object |
| break_velocity | Vector3D | Velocity and direction in which the object is destroyed |
| break_velocity_randomness | float | Randomness of velocity and direction in which the object is destroyed, 0 means that object uses break_velocity without any randomness |
| break_mode | BreakMode | Dictates how object can be damaged |
| sparks_on_impact | bool | Dictates whether object creates sparks upon impact |

### Damage effect

| Effect | Description |
| --- | --- |
| none | Object doesn't change at all once it's damaged |
| change_model | Some of the objects change model on collision, those use this |
| smash | Object is smashed |
| change_smash | First CHANGE_MODEL, afterwards smash on collision |
| breakable | Object is breakable normally |
| breakable_remove | object.dat says: '(ie. never regenerated after destroyed)' |

### Collision Response

| Response | Description |
| --- | --- |
| none | Object doesn't respond in any special way |
| lamppost | Objects acts like an lamp post |
| small_box | - |
| big_box | - |
| fence_part | - |
| grenade | - |
| swingdoor | - |
| lockdoor | - |
| hanging | - |
| poolball | - |

### Fx Type

| Type | Description |
| --- | --- |
| none | No particles effect played on collision |
| play_on_hit | Particles effect is played on collision, even if object isn't destroyed |
| play_on_destroyed | Particles effect is played only once object is destroyed |
| play_on_hitdestroyed | Particles effect is played both when hit and destroyed |

### Break Mode

| Mode | Description |
| --- | --- |
| not_by_gun | not breakable by gun |
| by_gun | - |
| smashable | - |

### Fx Effect

| effect | Description |
| --- | --- |
| wallbust | - |
| shootlight | - |
| puke | Puke effect |
| explosion_door | - |
| explosion_crate | Crate break |
| explosion_barrel | Barrel explosion |
| blood_heli | Heli cutting peds |
| tree_hit_palm | - |
| tree_hit_fir | - |
| water_swim | Water ripples |
| water_splsh_sml | - |
| water_splash_big | - |
| water_splash | - |
| water_hydrant | - |
| tank_fire | - |
| riot_smoke | - |
| gunsmoke | Gun smoke when firing |
| gunflash | Gun flash when firing |
| explosion_tiny | - |
| explosion_small | - |
| explosion_molotov | Molotov explosion |
| explosion_medium | - |
| explosion_large | - |
| explosion_fuel_car | - |
| exhale | - |
| camflash | Camera photo flash |
| prt_wake | Wake on water behind boats |

## Example

Click to collapse [-]
Client

```
function lamppostCollision()
engineSetObjectGroupPhysicalProperty(111, "cause_explosion", true)
end
addEventHandler("onClientResourceStart", resourceRoot, lamppostCollision)

--Every time you hit a lamppost, an explosion will be created
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

- engineSetObjectGroupPhysicalProperty

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
