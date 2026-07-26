---
doc_id: "mta-wiki:5147"
title: "GetProjectileCreator"
source_title: "GetProjectileCreator"
source_url: "https://wiki.multitheftauto.com/wiki/GetProjectileCreator"
revision_id: 43079
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:22.285792+00:00"
---

# GetProjectileCreator

This function returns the creator of the specified projectile.

## Syntax

```
element getProjectileCreator ( projectile theProjectile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[projectile](mta://reference/misc/projectile.md):getCreator(...)*

**Variable**: *.creator*

### Required Arguments

- **theProjectile:** The [projectile](mta://reference/misc/projectiles.md) element which creator you want to retrieve.

## Returns

Returns the element which created the projectile if successful, *false* otherwise.

## Example

Click to collapse [-]
Client

This example will output a message in the chatbox saying who created
the projectile.

```
addEventHandler("onClientProjectileCreation", root, function(projectile)
    local creator = getProjectileCreator(projectile)
    if (getElementType(creator) == "player") then
        local pName = getPlayerName(creator)
	local projectileID = getProjectileType(projectile)
        outputChatBox(pName.." created a projectile! (ID: "..projectileID..")", 255, 200, 0, false)
    end
end)
```

## See also

- [createProjectile](mta://scripting/client/functions/createprojectile.md)

- [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- getProjectileCreator

- [getProjectileForce](mta://scripting/client/functions/getprojectileforce.md)

- [getProjectileTarget](mta://scripting/client/functions/getprojectiletarget.md)

- [getProjectileType](mta://scripting/client/functions/getprojectiletype.md)

- [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)
  

- **Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)
