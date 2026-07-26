---
doc_id: "mta-wiki:3827"
title: "OnClientProjectileCreation"
source_title: "OnClientProjectileCreation"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientProjectileCreation"
revision_id: 77608
language: "en"
categories: ["Client_events"]
---

# OnClientProjectileCreation

This event is triggered when a [projectile](https://wiki.multitheftauto.com/index.php?search=projectile) is created.

## Parameters

```
element creator
```

- **creator:** the [element](mta://reference/misc/element.md) that created the projectile.

## Source

The [source](mta://reference/misc/event-system.md) of this event is the [projectile](https://wiki.multitheftauto.com/index.php?search=projectile) that was created.

## Cancel effect

This event cannot be cancelled. To remove the projectile you can use setElementPosition (somewhere far away) and then destroyElement (which makes it explode).

## Example

This will output a chatbox message when someone creates a projectile.

```
function projectileCreation()
	outputChatBox("A projectile was created!")
end
addEventHandler("onClientProjectileCreation", root, projectileCreation)
```

This will punish a player for throwing a teargas grenade. When he throws it he keeps getting warped to the location where the teargas got created, and also the teargas keeps getting warped to it. This will result in  +/-60hp loss for the creator.

```
function projectileCreation( creator )
	local projectileType = getProjectileType( source ) -- We get the projectile type
	if projectileType == 17 then -- If is tear gas then...
		local creatorName = getPlayerName( creator ) -- We get the player name who creates the projectile
		local x, y, z = getElementPosition ( source ) --Getting the position from the projectile creator
		outputChatBox ( creatorName.." is a noob teargas user! But he got punished for it don't worry." )
		setTimer ( setElementPosition, 50, 250, source, x, y, z-0.5 )
		setTimer ( setElementPosition, 50, 250, creator, x, y, z-0.5 )
	end
end
addEventHandler( "onClientProjectileCreation", root, projectileCreation )
```

This will disable people from creating flares. ( Dropped by Hydras )

```
function disableFlares ( )
local projType = getProjectileType( source ) --  get the projectile type

    if projType == 58 then -- if the projectile is a flare
	
	destroyElement(source) -- notice cancelEvent() does not work, so this destroys the projectile element after it was created.
		
    end

end	

addEventHandler( "onClientProjectileCreation", root, disableFlares ) -- when a projectile gets created call disableFlares.
```

## See Also

### Client projectile events

- onClientProjectileCreation
