---
doc_id: "mta-wiki:6582"
title: "Changes in 1.3"
source_title: "Changes in 1.3.0"
source_url: "https://wiki.multitheftauto.com/wiki/Changes_in_1.3.0"
revision_id: 69205
language: "en"
categories: ["Changelog", "Changes_in_1.3"]
generated_at: "2026-07-26T16:11:39.732464+00:00"
---

# Changes in 1.3

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

## Main Additions

- Added functions to remove and re-add parts of the San Andreas world

## Client

### New Functions

- Added [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md) (Available in 1.2.0-3591)

- Added [restoreWorldModel](mta://scripting/shared/functions/restoreworldmodel.md) (Available in 1.2.0-3591)

- Added [restoreAllWorldModels](mta://scripting/shared/functions/restoreallworldmodels.md) (Available in 1.2.0-3591)

- Added [getBirdsEnabled](mta://scripting/client/functions/getbirdsenabled.md)

- Added [setBirdsEnabled](mta://scripting/client/functions/setbirdsenabled.md)

- Added [setOcclusionsEnabled](mta://scripting/shared/functions/setocclusionsenabled.md)

### New Events

- Added [onClientVehicleCollision](mta://scripting/client/functions/onclientvehiclecollision.md)

### Changes

- Online players in the bottom right of the server browser

- New "Lighter Black" skin for CEGUI from Aibo

### Bug Fixes

- Fixed custom vehicle collisions not loading

- Fixed custom model textures not loading sometimes

- onVehicleExplode triggers for RC Vehicles now

- Projectiles fire at a normal rate

- Fixed spider CJ

- Speed up in entity collision detection client side

- Fixed the glitchy GTASA animation when you block+sprint (where hands are repeatedly raised and lowered)

- Fixed Objects scaled with setObjectScale aren't rendered when the unscaled bounding box goes off-screen

- Fixed Always falling off bikes and motorbikes

- Fixed Some vehicles become indestructible when a certain door is open

- Possible fix for client freezing/crashing after playing a long while

- Markers in interiors not appearing

- Chineese/Japanese/Korean input fixed

## Server

### New Functions

- Added [takePlayerScreenShot](mta://scripting/server/functions/takeplayerscreenshot.md)

- Added [setOcclusionsEnabled](mta://scripting/shared/functions/setocclusionsenabled.md)

- Added [removeWorldModel](mta://scripting/shared/functions/removeworldmodel.md) (Available in 1.2.0-3624)

- Added [restoreWorldModel](mta://scripting/shared/functions/restoreworldmodel.md) (Available in 1.2.0-3624)

- Added [restoreAllWorldModels](mta://scripting/shared/functions/restoreallworldmodels.md) (Available in 1.2.0-3624)

### New Events

- Added [onPlayerScreenShot](mta://scripting/server/events/onplayerscreenshot.md)

### Changes

- None yet

### Bug Fixes

- Fixed Map download breaking often on large transfers

## Resources

- Admin: added anti nick change spam option

- Freeroam: added chat spam and repeat message option

- Freeroam: added location bookmarking

## Editor

- Added LOD information to aid removing LOD's
