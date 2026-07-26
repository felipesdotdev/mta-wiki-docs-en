---
doc_id: "mta-wiki:5148"
title: "GetProjectileForce"
source_title: "GetProjectileForce"
source_url: "https://wiki.multitheftauto.com/wiki/GetProjectileForce"
revision_id: 43080
language: "en"
categories: ["Client_functions"]
---

# GetProjectileForce

This function returns the force of the specified projectile.

## Syntax

```
float getProjectileForce ( projectile theProjectile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[projectile](https://wiki.multitheftauto.com/index.php?search=projectile):getForce(...)*

**Variable**: *.force*

### Required Arguments

- **theProjectile:** The [projectile](mta://reference/misc/projectiles.md) element which force you want to retrieve.

## Returns

Returns a [float](mta://reference/misc/float.md) if successful, *false* otherwise.

## Example

**Example 1:** This example would outputs the force of the projectile on 1-100 scale. This function just works with projectiles which you throw so just grenades, satchel charge etc

```
addEventHandler("onClientProjectileCreation", getRootElement(),
--The source of this event is the projectile that was created.
function ()
    local getForce = getProjectileForce(source)
    outputChatBox(getForce*100) -- outputs the force of the projectile on 1-100 scale
end
)
```

## See also

- [createProjectile](mta://scripting/client/functions/createprojectile.md)

- [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- [getProjectileCreator](mta://scripting/client/functions/getprojectilecreator.md)

- getProjectileForce

- [getProjectileTarget](mta://scripting/client/functions/getprojectiletarget.md)

- [getProjectileType](mta://scripting/client/functions/getprojectiletype.md)

- [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)
  

- **Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)
