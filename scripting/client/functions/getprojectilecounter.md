---
doc_id: "mta-wiki:6718"
title: "GetProjectileCounter"
source_title: "GetProjectileCounter"
source_url: "https://wiki.multitheftauto.com/wiki/GetProjectileCounter"
revision_id: 81126
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:22.273859+00:00"
---

# GetProjectileCounter

Get the time left before a projectile detonates.

## Syntax

```
int getProjectileCounter ( projectile projectile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[projectile](mta://reference/misc/projectile.md):getCounter(...)*

**Variable**: *.counter*

**Counterpart**: *[setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)*

### Required Arguments

- **projectile**: the projectile to get the timer of.

### Returns

Returns the the time in milliseconds to detonation which depending on the projectile type will do different things:

- Grenades will explode when it hits 0

- Teargas may be a duration timer

- Both types of rockets will explode when it hits 0

- Satchels restarts so I do not think it does anything

### Example

Click to collapse [-]
Client

With this example you can find out how long does it take for a projectile to explode/end

```
function getProjectileBoomTime()
outputChatBox("Time for "..getProjectileType(source).." to explode/end is "..getProjectileCounter(source).." miliseconds.",255,0,0)
end
addEventHandler("onClientProjectileCreation",root,getProjectileBoomTime)
```

## See Also

- [createProjectile](mta://scripting/client/functions/createprojectile.md)

- getProjectileCounter

- [getProjectileCreator](mta://scripting/client/functions/getprojectilecreator.md)

- [getProjectileForce](mta://scripting/client/functions/getprojectileforce.md)

- [getProjectileTarget](mta://scripting/client/functions/getprojectiletarget.md)

- [getProjectileType](mta://scripting/client/functions/getprojectiletype.md)

- [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)
  

- **Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)
