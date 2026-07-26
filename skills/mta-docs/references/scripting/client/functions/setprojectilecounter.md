---
doc_id: "mta-wiki:6733"
title: "SetProjectileCounter"
source_title: "SetProjectileCounter"
source_url: "https://wiki.multitheftauto.com/wiki/SetProjectileCounter"
revision_id: 81140
language: "en"
categories: ["Client_functions"]
---

# SetProjectileCounter

Will change the projectile counter timer which depending on the projectile type will do different things:

- Rockets and Grenades will explode when it hits 0

- Teargas may be a duration timer

- Satchels restart (we currently assume it doesn't cause an effect)

- Molotov will explode with search ground level when it hits 0

## Syntax

```
bool setProjectileCounter ( projectile projectile, int timeToDetonate )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[projectile](https://wiki.multitheftauto.com/index.php?search=projectile):setCounter(...)*

**Variable**: *.counter*

**Counterpart**: *[getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)*

### Required Arguments

- **projectile:** The projectile to edit the timer of.

- **timeToDetonate:** The time in milliseconds to detonation.

### Returns

Returns *true* on success, *false* otherwise.

### Example

Click to collapse [-]
Client

With this example you can use /setbombtime to set a delay duration of a projectile explosion.

```
function changeProjectileDelay( cmd, bombIndex, duration )
	local bombIndex = tonumber( bombIndex ) or nil
	local duration = tonumber( duration ) or nil
	
	if ( bombIndex ) and ( duration ) then
		local found = false

		for index,projectile in ipairs( getElementsByType( "projectile" ) ) do
			if ( index == bombIndex ) then
				if ( setProjectileCounter( projectile, duration * 1000 ) ) then
					outputChatBox( "Projectile (" .. index .. ") detonates in " .. duration .. " seconds.", 0, 255, 0, false )
				else
					outputChatBox( "Something went wrong when setting the duration.", 255, 0, 0, false )
				end

				found = true
				break
			end
		end

		if ( not found ) then
			outputChatBox( "Projectile with index " .. bombIndex .. " was not found.", 255, 0, 0, false )
		end
	else
		outputChatBox( "SYNTAX: /" .. cmd .. " [bomb index] [duration in seconds]", 220, 180, 0, false )
	end
end
addCommandHandler( "setbombtime", changeProjectileDelay )
```

## See Also

- [createProjectile](mta://scripting/client/functions/createprojectile.md)

- [getProjectileCounter](mta://scripting/client/functions/getprojectilecounter.md)

- [getProjectileCreator](mta://scripting/client/functions/getprojectilecreator.md)

- [getProjectileForce](mta://scripting/client/functions/getprojectileforce.md)

- [getProjectileTarget](mta://scripting/client/functions/getprojectiletarget.md)

- [getProjectileType](mta://scripting/client/functions/getprojectiletype.md)

- setProjectileCounter
  

- **Shared**

- [detonateSatchels](mta://scripting/shared/functions/detonatesatchels.md)
