---
doc_id: "mta-wiki:5149"
title: "GetProjectileTarget"
source_title: "GetProjectileTarget"
source_url: "https://wiki.multitheftauto.com/wiki/GetProjectileTarget"
revision_id: 49070
language: "en"
categories: ["Client_functions", "Changes_in_1.4.0"]
---

# GetProjectileTarget

This function returns the target of the specified projectile.

## Syntax

```
element getProjectileTarget ( projectile theProjectile )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[projectile](https://wiki.multitheftauto.com/index.php?search=projectile):getTarget(...)*

**Variable**: *.target*

### Required Arguments

- **theProjectile:** The [projectile](mta://reference/misc/projectiles.md) element which target you want to retrieve.

## Returns

Returns the [element](mta://reference/misc/element.md) which is the projectile's target if the projectile is valid and can have a target (like a heat-seeking rocket), *false* otherwise.

If the projectile is a satchel charge, returns the [element](mta://reference/misc/element.md) at which it is glued to (or *nil* if it isn't glued to any).

## Example

This example allows a player to send projectiles at other players.

```
function projectileCreating(command,targetPlayer)
    local x,y,z = getElementPosition(getLocalPlayer()) -- Get the position of the player
    local target = getPlayerFromName(targetPlayer) or nil -- Get the target, or set it to nil if no target specified
    local theProjectile = createProjectile(getLocalPlayer(),20,x,y,z+50,1.0,target)
    if (target) then
        outputChatBox("Created projectile's target: "..getPlayerName(getProjectileTarget(theProjectile)))
    else
        outputChatBox("Created projectile with no target")
    end
end
addCommandHandler("rocket",projectileCreating) -- Bind the 'rocket' command to projectileCreating function
```

## See also

- [createProjectile](mta://scripting/client/functions/createprojectile.md)

- [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- [getProjectileCreator](mta://scripting/client/functions/getprojectilecreator.md)

- [getProjectileForce](mta://scripting/client/functions/getprojectileforce.md)

- getProjectileTarget

- [getProjectileType](mta://scripting/client/functions/getprojectiletype.md)

- [setProjectileCounter](mta://scripting/client/functions/setprojectilecounter.md)
  

- **Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)
