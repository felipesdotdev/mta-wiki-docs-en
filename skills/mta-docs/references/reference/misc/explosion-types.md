---
doc_id: "mta-wiki:14230"
title: "Explosion types"
source_title: "Explosion types"
source_url: "https://wiki.multitheftauto.com/wiki/Explosion_types"
revision_id: 78768
language: "en"
categories: ["ID_Lists"]
---

# Explosion types

The following explosion types are used by events like [onExplosion](mta://scripting/server/events/onexplosion.md) or [onClientExplosion](mta://scripting/client/events/onclientexplosion.md), and function [createExplosion](mta://scripting/shared/functions/createexplosion.md).

| Explosion type | MTA description | Reference | Occurrence |
| --- | --- | --- | --- |
| 0 | Grenade | CProjectileInfo::RemoveNotAdd CProjectileInfo::RemoveDetonatorProjectiles CProjectileInfo::RemoveProjectile | When a grenade or satchel is thrown but is blocked by a surface and doesn't collide with a ped (TestSphereAgainstWorld 0,3m radius from origin) it doesn't create a projectile but an explosion directly. Needs testing. Satchel detonation. When a grenade or satchel projectile explodes normally. |
| 1 | Molotov | CProjectileInfo::RemoveNotAdd CProjectileInfo::RemoveProjectile CAutomobile::BlowUpCarCutSceneNoExtras | When a molotov is thrown but is blocked by a surface it doesn't create a projectile but an explosion directly. When a molotov projectile explodes normally. Probably not relevant in MTA. |
| 2 | Rocket | CProjectileInfo::RemoveNotAdd CProjectileInfo::RemoveProjectile CExplosion::Update CAutomobile::ProcessCarOnFireAndExplode | When a rocket launcher is fired but blocked by a surface (camera LOS), it doesn't create a projectile but an explosion directly. When a rocket projectile explodes normally. When a type 7 explosion occurs (with a victim i.e. vehicle source) and a 5% chance. If plane or heli (not RC vehicle) and below 250 hp and a 1.2% chance. |
| 3 | Rocket Weak | CProjectileInfo::RemoveProjectile | If a HS rocket projectile and the launcher is not local player (FindPlayerPed(-1) must be local player?) |
| 4 | Car | CAutomobile::BlowUpCar CBike::BlowUpCar | When a car blows up. When a bike blows up. |
| 5 | Car Quick | CAutomobile::BlowUpCar | When ID 564 or 441 blows up. (RC Tiger & Bandit) |
| 6 | Boat | CBoat::BlowUpCar | When a boat blows up. |
| 7 | Aircraft | CHeli::BlowUpCar CPlane::BlowUpCar | When a heli blows up. When a plane blows up. |
| 8 | Mine | CPickup::Update CPickup::ProcessGunShot | Related to PICKUP_NAUTICAL_MINE_ARMED, not spawnable in MTA? Most likely shooting a sea mine? |
| 9 | Object | CObject::Explode | Exploding object e.g. explosive barrel, tank stations. |
| 10 | Tank Grenade | CAutomobile::TankControl | Rhino shooting. |
| 11 | Small |  | Most likely only used by script. |
| 12 | Tiny | CHeli::BlowUpCar CPlane::BlowUpCar | When ID 465 or 501 blows up. (RC Raider & Goblin) When ID 464 blows up. (RC Baron) |

Explosion types in Lua table:

```
local explosionTypes = {
	[0] = "Grenade",
	[1] = "Molotov",
	[2] = "Rocket",
	[3] = "Rocket Weak",
	[4] = "Car",
	[5] = "Car Quick",
	[6] = "Boat",
	[7] = "Aircraft",
	[8] = "Mine",
	[9] = "Object",
	[10] = "Tank Grenade",
	[11] = "Small",
	[12] = "Tiny",
}
```
