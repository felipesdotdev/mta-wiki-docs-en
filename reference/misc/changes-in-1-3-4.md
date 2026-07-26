---
doc_id: "mta-wiki:7215"
title: "Changes in 1.3.4"
source_title: "Changes in 1.3.4"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.3.4"
revision_id: 58989
language: "en"
categories: ["Changes_in_1.3"]
generated_at: "2026-07-26T16:11:51.815988+00:00"
---

# Changes in 1.3.4

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

- Added "shared" export type in meta.xml

- Added Lua source encryption option

- Added the ability to cancel onClientKey

- Added escape to onClientKey (can't be cancelled twice in a row)

- Added SettingHUDMatchAspectRatio, SettingAspectRatio to dxGetStatus

### Client

#### New Functions

- Added [playSFX](mta://scripting/client/functions/playsfx.md)

- Added [playSFX3D](mta://scripting/client/functions/playsfx3d.md)

- Added [getSFXStatus](mta://scripting/client/functions/getsfxstatus.md)

- Added [setHeliBladeCollisionsEnabled](mta://scripting/client/functions/sethelibladecollisionsenabled.md)

- Added [getHeliBladeCollisionsEnabled](mta://scripting/client/functions/gethelibladecollisionsenabled.md)

- Added [getEventHandlers](mta://scripting/shared/functions/geteventhandlers.md)

#### New Events

#### Changes / Bug Fixes

- Fixed vehicle upgrades

- Fixed warpPedIntoVehicle causing desync when two players try to enter at the same time via vehicle_enter and warpPedIntoVehicle

- Fixed map editor crash

- Fixed debug filename for compiled scripts

- Fixed applying weapon mods may remove your weapon

- Fixed crash when streaming in tec-9 with a replaced weapon model

- Fixed console(F8) input focus begin lost sometimes

- Fixed building removal crashing after loading/unloading a model 16 times

- Fixed projectile-type weapons messing up ammo count

- Fixed guiCreateFont fails each second time resource is started

- Fixed client ammo desync when using giveWeapon sometimes

- Fixed guiLabelGetTextExtent not working with unicode

- Fixed onColShapeHit isn't triggered for towed vehicles server side

- Fixed GUI scrollpanes and scrollbars don't trigger onClientMouseEnter/Leave

- Fixed warpPedIntoVehicle after cancelEvent() of onVehicleStartEnter causes network trouble

- Fixed onPedWasted not triggered, when ped died because the vehicle he was in, exploded

- Fixed server createColPolygon

- Fixed a crash when destroying an object in onClientColShapeHit / onClientElementColShapeHit

- Fixed lightweight sync packet being misread on the client sometimes

- Fixed getLatentEventHandles sometimes returning false instead of an empty table

- Fixed setAccountData clips the digits after the decimal point

- Fixed peds/players being removed from vehicles that fall through the ground

### Server

#### New Functions

#### New Events

#### Changes / Bug Fixes

### Resources

- Added sfxbrowser resource

- Fixed instant reload exploits for the reload resource

- Fixed 'Use LODs' option in the map editor resource

- Fixed various things in admin, acpanel, freeroam, parachute and race resources

### Editor

## Extra information

*More detailed information available on [Bug tracker Changelog](https://bugs.multitheftauto.com/changelog_page.php) and Google Code repositories:*

- MTA:SA: from  [r5593](https://code.google.com/p/mtasa-blue/source/list?num=25&start=5609) to [r5800](https://code.google.com/p/mtasa-blue/source/list?num=25&start=5800)

- Resources: [from r938 to r955](https://code.google.com/p/mtasa-resources/source/list?num=25&start=955)

- [MTASA 1.3.4 released](https://forum.mtasa.com/viewtopic.php?f=31&t=64990)
