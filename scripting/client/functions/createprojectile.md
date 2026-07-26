---
doc_id: "mta-wiki:2692"
title: "CreateProjectile"
source_title: "CreateProjectile"
source_url: "https://wiki.multitheftauto.com/wiki/CreateProjectile"
revision_id: 79958
language: "en"
categories: ["Client_functions", "Utility_templates", "Functions_and_events_with_issues"]
generated_at: "2026-07-26T16:10:38.188570+00:00"
---

# CreateProjectile

This function creates a projectile of the specified type on the specified coordinates.

| [[{{{image}}}\|link=\|]] | Note: Model argument is not synchronized between clients. Clients differs from local player see always standard projectile model. Target argument valid elements are: player , ped , vehicle and object . |
| --- | --- |
|  |  |

## Syntax

```
projectile createProjectile ( element creator, int weaponType [, float posX, float posY, float posZ, float force = 1.0, element target = nil, float rotX, float rotY, float rotZ, float velX, float velY, float velZ, int model ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Projectile](mta://reference/misc/projectile.md)(...)*

### Required Arguments

- **creator:** The [element](mta://reference/misc/element.md) representing creator of the projectile. In case you want the projectile to be synced for everybody creator must be the local player or his vehicle.

- **weaponType:** [int](mta://reference/misc/int.md) representing the projectile weaponType (characteristics). Valid IDs are:

| ID | Name/Description |
| --- | --- |
| 16 | Grenade |
| 17 | Tear Gas Grenade |
| 18 | Molotov |
| 19 | Rocket (simple) |
| 20 | Rocket (heat seeking) |
| 21 | Air Bomb |
| 39 | Satchel Charge |
| 58 | Hydra flare |

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **posX**, **posY**, **posZ**: [float](mta://reference/misc/float.md) starting coordinates for the projectile. They are coordinates of creator by default.

- **force**: [float](mta://reference/misc/float.md) representing the starting force for throwable projectiles.

- **target**: [element](mta://reference/misc/element.md) target used for heat seeking rockets.

- **rotX**, **rotY**, **rotZ**: [float](mta://reference/misc/float.md) starting rotation for the projectile.

- **velX**, **velY**, **velZ**: [float](mta://reference/misc/float.md) starting velocity for the projectile.

- **model**: Integer representing the projectile's model, uses default model for weaponType if not specified.

## Returns

Returns a *[projectile](mta://reference/misc/projectile.md)* element if [projectile](mta://reference/misc/projectile.md) creation was successful. Returns *false* if unable to create a [projectile](mta://reference/misc/projectile.md) (wrong weapon ID or projectiles limit was reached).

## Example

This example makes a rocket minigun (minigun shooting with rockets).

```
function onClientPlayerWeaponFire(weaponID, weaponAmmo, weaponAmmoInClip, hitX, hitY, hitZ, hitElement)
	local minigunWeapon = (weaponID == 38) -- check if player is using minigun

	if (not minigunWeapon) then
		return false -- he doesn't, so don't continue
	end

	local playerX, playerY, playerZ = getElementPosition(source) -- get position of player
	local projectileType = 19 -- type of projectile
	local projectileForce = 200 -- force used for projectile
	local rocketProjectile = createProjectile(source, projectileType, playerX, playerY, playerZ, projectileForce) -- create rocket projectile

	if (not rocketProjectile) then -- if projectile limit is reached
		outputChatBox("Rocket minigun overheated! Give it a rest pal!", source) -- output a message
	end
end
addEventHandler("onClientPlayerWeaponFire", localPlayer, onClientPlayerWeaponFire)
```

This example code shoots a projectile from your occupied vehicle that travels in the direction your vehicle is facing when you press vehicle_fire (left mouse button with default controls)

```
function shootProjectile()
	local playerVehicle = getPedOccupiedVehicle(localPlayer)

	if (not playerVehicle) then -- only create projectile if we are inside a vehicle
		return false
	end

	local projectileType = 19 -- rocket
	local vehicleX, vehicleY, vehicleZ = getElementPosition(playerVehicle)

	createProjectile(playerVehicle, projectileType, vehicleX, vehicleY, vehicleZ)
end
bindKey("vehicle_fire", "down", shootProjectile)
```

## Issues

| Issue ID | Description |
| --- | --- |
| #584 | createProjectile creates one projectile for every person in the vehicle |
| #616 | Projectile rotation is set exactly opposite for creator |

## See also

- createProjectile

- [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- [getProjectileCreator](mta://scripting/client/functions/getprojectilecreator.md)

- [getProjectileForce](mta://scripting/client/functions/getprojectileforce.md)

- [getProjectileTarget](mta://scripting/client/functions/getprojectiletarget.md)

- [getProjectileType](mta://scripting/client/functions/getprojectiletype.md)

- [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)
  

- **Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)
