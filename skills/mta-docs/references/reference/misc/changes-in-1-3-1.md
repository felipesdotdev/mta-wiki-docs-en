---
doc_id: "mta-wiki:6212"
title: "Changes in 1.3.1"
source_title: "Changes in 1.3.1"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.3.1"
revision_id: 42218
language: "en"
categories: ["Changes_in_1.3"]
---

# Changes in 1.3.1

| MTA:SA Releases | Changelog Pages |
| --- | --- |
| 1.0 | 1.0.0 • 1.0.1 • 1.0.2 • 1.0.3 • 1.0.4 |
| 1.1 | 1.1.0 • 1.1.1 |
| 1.2 | 1.2.0 |
| 1.3 | 1.3.0 • 1.3.1 • 1.3.2 • 1.3.3 • 1.3.4 • 1.3.5 |
| 1.4 | 1.4.0 • 1.4.1 |
| 1.5 | 1.5.0 • 1.5.1 • 1.5.2 • 1.5.3 • 1.5.4 • 1.5.5 • 1.5.6 • 1.5.7 • 1.5.8 • 1.5.9 |
| 1.6 | 1.6.0 |
| 1.7 | 1.7.0 |

## Main Additions / Changes

- Added Custom Vehicle Sirens

- Fixed map files are downloading very slow issue

- Fixed timeouts on map change

- Fixed various issues, crashes and freezes

- Updated max players to 4096

- Added BASS Effects

- Added Analog Controls States

- Added bullet sync

- Fixed several custom model replacing issues

- Windows 8 support (both 32-bits and 64-bits)

- Added ability to create pedless weapons via weapon creation

- Improved Map Editor stability and added new features

- Installers for regular builds and nightlies are now digitally signed

## Client

### New Functions

- Added [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- Added [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- Added [dxSetBlendMode](mta://scripting/client/functions/dxsetblendmode.md)

- Added [dxGetBlendMode](mta://scripting/client/functions/dxgetblendmode.md)

- Added [dxDrawMaterialLine3D](mta://scripting/client/functions/dxdrawmaterialline3d.md)

- Added [dxDrawMaterialSectionLine3D](mta://scripting/client/functions/dxdrawmaterialsectionline3d.md)

- Added [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- Added [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- Added [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- Added [triggerLatentServerEvent](mta://scripting/client/functions/triggerlatentserverevent.md)

- Added [getVehicleSirenParams](mta://scripting/shared/functions/getvehiclesirenparams.md)

- Added [getVehicleSirens](mta://scripting/shared/functions/getvehiclesirens.md)

- Added [setVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- Added [getSoundProperties](mta://scripting/client/functions/getsoundproperties.md)

- Added [setSoundProperties](mta://scripting/client/functions/setsoundproperties.md)

- Added [getSoundFFTData](mta://scripting/client/functions/getsoundfftdata.md)

- Added [setSoundPanningEnabled](mta://scripting/client/functions/setsoundpanningenabled.md)

- Added [isSoundPanningEnabled](mta://scripting/client/functions/issoundpanningenabled.md)

- Added [setWorldSoundEnabled](mta://scripting/client/functions/setworldsoundenabled.md)

- Added [isWorldSoundEnabled](mta://scripting/client/functions/isworldsoundenabled.md)

- Added [resetWorldSounds](mta://scripting/client/functions/resetworldsounds.md)

- Added [getSoundBPM](mta://scripting/client/functions/getsoundbpm.md)

- Added [getSoundLevelData](mta://scripting/client/functions/getsoundleveldata.md)

- Added [getSoundWaveData](mta://scripting/client/functions/getsoundwavedata.md)

- Added [setPedAnalogControlState](mta://scripting/client/functions/setpedanalogcontrolstate.md)

- Added [getPedAnalogControlState](mta://scripting/client/functions/getpedanalogcontrolstate.md)

- Added [setAnalogControlState](mta://scripting/client/functions/setanalogcontrolstate.md)

- Added [getAnalogControlState](mta://scripting/client/functions/getanalogcontrolstate.md)

- Added [setPedTargetingMarkerEnabled](mta://scripting/client/functions/setpedtargetingmarkerenabled.md)

- Added [isPedTargetingMarkerEnabled](mta://scripting/client/functions/ispedtargetingmarkerenabled.md)

- Added [setElementMatrix](mta://scripting/shared/functions/setelementmatrix.md)

- Added [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)

- Added [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md)

- Added [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)

- Added [createWeapon](mta://scripting/client/functions/createweapon.md)

- Added [fireWeapon](mta://scripting/client/functions/fireweapon.md)

- Added [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)

- Added [setWeaponState](mta://scripting/client/functions/setweaponstate.md)

- Added [setWeaponTarget](mta://scripting/client/functions/setweapontarget.md)

- Added [getWeaponOwner](mta://scripting/client/functions/getweaponowner.md)

- Added [setWeaponOwner](mta://scripting/client/functions/setweaponowner.md)

- Added [setWeaponFlags](mta://scripting/client/functions/setweaponflags.md)

- Added [getWeaponFlags](mta://scripting/client/functions/getweaponflags.md)

- Added [setWeaponFiringRate](mta://scripting/client/functions/setweaponfiringrate.md)

- Added [getWeaponFiringRate](mta://scripting/client/functions/getweaponfiringrate.md)

- Added [resetWeaponFiringRate](mta://scripting/client/functions/resetweaponfiringrate.md)

- Added [getWeaponClipAmmo](mta://scripting/client/functions/getweaponclipammo.md)

- Added [setWeaponClipAmmo](mta://scripting/client/functions/setweaponclipammo.md)

- Added [getWeaponAmmo](mta://scripting/client/functions/getweaponammo.md)

- Added [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- Added [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- Added [setWaterDrawnLast](mta://scripting/client/functions/setwaterdrawnlast.md)

- Added [isWaterDrawnLast](mta://scripting/client/functions/iswaterdrawnlast.md)

- Added [guiLabelGetColor](mta://scripting/client/functions/guilabelgetcolor.md)

### New Events

- Added [onClientPedHeliKilled](mta://scripting/client/events/onclientpedhelikilled.md)

- Added [onClientPlayerHeliKilled](mta://scripting/client/events/onclientplayerhelikilled.md)

- Added [onClientPlayerHitByWaterCannon](mta://scripting/client/events/onclientplayerhitbywatercannon.md)

- Added [onClientPedHitByWaterCannon](mta://scripting/client/events/onclientpedhitbywatercannon.md)

- Added [onClientPlayerPickupHit](mta://scripting/client/events/onclientplayerpickuphit.md)

- Added [onClientPlayerPickupLeave](mta://scripting/client/events/onclientplayerpickupleave.md)

- Added [onClientSoundBeat](mta://scripting/client/events/onclientsoundbeat.md)

- Added [onClientWeaponFire](mta://scripting/client/events/onclientweaponfire.md)

### Changes / Bug Fixes

- Fixed 'not being able to enter vehicles' bug

- Added order priority to [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- Fixed 'engineless' NRG-500 Variant

- Added option to skip Dual Monitor Resolution Select

- Made [playSound3D](mta://scripting/client/functions/playsound3d.md) use the camera position instead of the player position when determining the distance

- Added color coding and sub-pixel positioning options to [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)

- Added ability to create and modify cubemaps and volume textures - Details: [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md)

- Added model cache system to reduce loading delays

- Added CJ clothes cache to help reduce game freezes

- Sped up event handling system for server and client

- Added element option to [engineApplyShaderToWorldTexture](mta://scripting/client/functions/engineapplyshadertoworldtexture.md)

- Added optional bool to [getElementMatrix](mta://scripting/shared/functions/getelementmatrix.md) ( element, bool )

- Added unrar for smoother update procedure

- Fixed custom model replacement errors sometimes with weapons & weapon pickups.

- Fixed vehicle upgrade custom models not showing immediately

- Fixed accuracy of hit point in [onClientPlayerWeaponFire](mta://scripting/client/events/onclientplayerweaponfire.md) and added shot origin parameter

- Fixed [setPedAimTarget](mta://scripting/client/functions/setpedaimtarget.md) direction being all wrong

- Fixed issue when peds' bullets origin from wrong position

- Fixed custom models not rendering correctly sometimes parameter

- Fixed custom model LOD distance is not reseting after quiting

- Added size limit for clientscript.log file

- Added ability to shoot with any weapon with jetpack

- Made timers less crashy

- Fixed some animation crashes

- Fixed [getPedMoveState](mta://scripting/client/functions/getpedmovestate.md) returns false when moving in crouch state

- Fixed a bug when a resource that replace an object model (dff) and texture (txd) is stopped the object texture get white

- Added ped pixel shaders

- Added ability to layer multiple shaders on a world texture

- Fixed Windows 8 missing dll error

- Fixed [setElementPosition](mta://scripting/shared/functions/setelementposition.md) for vehicles on a non streamed in position will make the vehicle spin very quickly

- Added check for GTA file loading failures

- Fixed map editor crash

- Fixed floating vehicles when using [setVehicleIdleRespawnDelay](mta://scripting/server/functions/setvehicleidlerespawndelay.md)

- Fixed [showhud](mta://reference/misc/client-commands.md) not fully working before the player has spawned

- Fixed connect problem when using a domain name that starts with a number

- Fixed missing font error message

- Fixed [getSoundLength](mta://scripting/client/functions/getsoundlength.md) returns 0 for sound streams (not radio streams)

- Fixed a crash when taking a screenshot and minimizing then restoring

- Fixed setElementFrozen killing players from falls

- Fixed textures disappearing and flickering at certain camera angles

## Server

### New Functions

- Added [fetchRemote](mta://scripting/shared/functions/fetchremote.md)

- Added [reloadBans](mta://scripting/server/functions/reloadbans.md)

- Added [getAllAccountData](mta://scripting/server/functions/getallaccountdata.md)

- Added [getLatentEventHandles](mta://scripting/shared/functions/getlatenteventhandles.md)

- Added [getLatentEventStatus](mta://scripting/shared/functions/getlatenteventstatus.md)

- Added [cancelLatentEvent](mta://scripting/shared/functions/cancellatentevent.md)

- Added [removeVehicleSirens](mta://scripting/shared/functions/removevehiclesirens.md)

- Added [getVehicleSirenParams](mta://scripting/shared/functions/getvehiclesirenparams.md)

- Added [getVehicleSirens](mta://scripting/shared/functions/getvehiclesirens.md)

- Added [setVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- Added [addVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md)

- Added [setJetpackWeaponEnabled](mta://scripting/server/functions/setjetpackweaponenabled.md)

- Added [getJetpackWeaponEnabled](mta://scripting/server/functions/getjetpackweaponenabled.md)

- Added [fileCopy](mta://scripting/shared/functions/filecopy.md)

### New Events

- None yet

### Changes / Bug Fixes

- Fixed map files are downloading very slow issue

- Fixed timeouts on map change

- Tweaks and fixes for vehicle sync

- Added order priority to [addEventHandler](mta://scripting/shared/functions/addeventhandler.md)

- Improved performance when the server has a large number of IP bans

- Added debug info to timers

- Added adjustable sync rates to [setServerConfigSetting](mta://scripting/server/functions/setserverconfigsetting.md) and the server config - Details: [Sync_interval_settings](mta://reference/misc/sync-interval-settings.md)

- Fixed lightsync vehicles ghost streaming in when locally they are miles away

- Fixed server sometimes not appearing in the browser

- Added server setting to reduce CPU usage

- Sped up event handling system for server and client

- Tweaked server networking

- Improved Lua errors for server element functions

- Reduced CPU usage more

- Made timers less crashy

- Added vehicle extrapolation - Details: [mtaserver.conf -> vehext_](https://wiki.multitheftauto.com/index.php?search=mtaserver.conf%20-%3E%20vehext_)

- Fixed server crash when towing a clientside vehicle

- Added option to suppress certain MySQL error messages

- Sped up [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md)

- Made [setVehicleIdleRespawnDelay](mta://scripting/server/functions/setvehicleidlerespawndelay.md) work for non-streamed in vehicles

- Added logging for [callRemote](mta://scripting/server/functions/callremote.md)

- Large amount of other crashfixes, improvements and tweaks

## Resources

- Updated parachute to fix high CPU usage on clients

- Added Visualiser resource

- Added GUI Siren Editor

- Fixed a reload exploit where you could jump and then reload for an instant reload

- Made reload with jetpack work again

- Fixed freeroam bookmarks

- Fixed some errors and warnings

## Editor

- Fixed Map editor not saving locations of objects on Linux machines

- Added cancel option when starting map editor from menu

- Added ability to change object and vehicle alpha

- Changed vehicle color selection to use the new RGB color system

- Fixed server settings tab in options not showing up when using Map Editor from main menu

- Added ability to place peds

- Added object scale option

- Added object collisions option
