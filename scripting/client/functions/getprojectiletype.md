---
doc_id: "mta-wiki:4564"
title: "GetProjectileType"
source_title: "GetProjectileType"
source_url: "https://wiki.multitheftauto.com/wiki/GetProjectileType"
revision_id: 43082
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:22.321843+00:00"
---

# GetProjectileType

This function returns the type of the specified projectile.

## Syntax

```
int getProjectileType ( projectile theProjectile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[projectile](mta://reference/misc/projectile.md):getType(...)*

**Variable**: *.type*

### Required Arguments

- **theProjectile:** The [projectile](mta://reference/misc/element-projectile.md) element which type you want to retrieve.

## Returns

Returns an [integer](mta://reference/misc/int.md) over the type of the projectile or *false* if invalid arguments were passed.

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

## Example

```
function projectileCreation()
	local theType = getProjectileType(source)
	outputChatBox("A projectile was created! It's type: "..theType)
end
addEventHandler("onClientProjectileCreation", getRootElement(), projectileCreation)
```

## See also

- [createProjectile](mta://scripting/client/functions/createprojectile.md)

- [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- [getProjectileCreator](mta://scripting/client/functions/getprojectilecreator.md)

- [getProjectileForce](mta://scripting/client/functions/getprojectileforce.md)

- [getProjectileTarget](mta://scripting/client/functions/getprojectiletarget.md)

- getProjectileType

- [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)
  

- **Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)
