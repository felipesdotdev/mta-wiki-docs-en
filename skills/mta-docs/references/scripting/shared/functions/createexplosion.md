---
doc_id: "mta-wiki:1633"
title: "CreateExplosion"
source_title: "CreateExplosion"
source_url: "https://wiki.multitheftauto.com/wiki/CreateExplosion"
revision_id: 78765
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# CreateExplosion

Creates an explosion of a certain type at a specified point in the world. If creator is specified, the explosion will occur only in its dimension.

## Syntax

Click to collapse [-]
Server

```
bool createExplosion ( float x, float y, float z, int theType [, player creator = nil ] )
```

### Required Arguments

- **x:** a float value that specifies the X world coordinate where the explosion is created at.

- **y:** a float value that specifies the Y world coordinate where the explosion is created at.

- **z:** a float value that specifies the Z world coordinate where the explosion is created at.

- **theType:** an integer specifying the explosion type, see: [Explosion types](mta://reference/misc/explosion-types.md)

### Optional Arguments

- **creator:** the explosion's simulated creator, the [player](https://wiki.multitheftauto.com/index.php?search=player) responsible for it.

Click to collapse [-]
Client

```
bool createExplosion ( float x, float y, float z, int theType [, bool makeSound = true, float camShake = -1.0, bool damaging = true ] )
```

### Required Arguments

- **x:** a float value that specifies the X world coordinate where the explosion is created at.

- **y:** a float value that specifies the Y world coordinate where the explosion is created at.

- **z:** a float value that specifies the Z world coordinate where the explosion is created at.

- **theType:** a integer specifying the explosion type, see: [Explosion types](mta://reference/misc/explosion-types.md)

### Optional Arguments

- **makeSound:** a boolean specifying whether the explosion should be heard or not.

- **camShake:** a float specifying the camera shake's intensity.

- **damaging:** a boolean specifying whether the explosion should cause damage or not.

### Returns

- *true* if the explosion was created.

- *false* if invalid parameters were passed.

## Example

Click to collapse [-]
Server

**Example 1:** This code will create an explosion at the player's position when they spawn.

```
function explosionOnSpawn ( )
  -- get the spawned player's position
  local pX, pY, pZ = getElementPosition ( source )
  -- and create an explosion there, making him the creator
  createExplosion ( pX, pY, pZ, 6, source )
end
-- add this function as a handler for any player that spawns
addEventHandler ( "onPlayerSpawn", root, explosionOnSpawn )
```

**Example 2:** This example allows creation of claymore mines, which trigger and explode.

```
function createClaymore ( creator )
	local x, y, z = getElementPosition ( creator )
	local claymoreObject = createObject ( 1945, x, y, z - 1, 0, 0, 90 ) --create an object which looks like a claymore
	local claymoreCol = createColSphere ( x, y, z, 1 ) --create a collision sphere with radius 1
	setElementData ( claymoreCol , "type", "claymore" ) --store the type of colshape so it can be retrieved
	setElementData ( claymoreCol, "object", claymoreObject ) --store the object of the claymore
	setElementData ( claymoreCol, "creatorPlayer", creator ) --store the person who created it
end

function claymoreHit ( player )
	if getElementData ( source, "type" ) == "claymore" then --ensure its a claymore
		--retrieve the object associated to the claymore, and who created it
		local claymoreObject = getElementData ( source, "object" )
		local claymoreCreator = getElementData ( source, "creatorPlayer" )
		--get the position of the claymore
		local x, y, z = getElementPosition ( source )
		createExplosion ( x, y, z, 12, claymoreCreator ) --create an explosion, associated to the creator, of a small size at the col's position
		--destroy the claymore object, and the col shape so it doesnt trigger again.
		destroyElement ( claymoreObject )
		destroyElement ( source )
	end
end
addEventHandler ( "onColShapeHit", root, claymoreHit )
```

**Example 3:** This will cause an explosion that will not harm the player.

```
function fakeBombAt(el)
	if isElement(el) then
		local x,y,z = getElementPosition(el)
		triggerClientEvent ( "fakeBomb", root, x, y, z, 0 )
	end
end

function onPlayerSpawnEvent(spawnpoint, team)
	fakeBombAt(source)
end

function onPlayerQuitEvent(reason)
	fakeBombAt(source)
end

function onPlayerDiedEvent(totalAmmo, killer, killerWeapon, bodypart)
	setTimer(fadeCamera, 2000, 1, source, false)
	fakeBombAt(source)
	setTimer(spawnPlayer, 4000, 1, source, 0, 0, 0)
	setTimer(fadeCamera, 4500, 1, source, true)
end

addEventHandler("onPlayerQuit",root,onPlayerQuitEvent)
addEventHandler("onPlayerWasted",root,onPlayerDiedEvent)
addEventHandler("onPlayerSpawn",root,onPlayerSpawnEvent)
```

Click to collapse [-]
Client

**Example 1:** This code will create an explosion for the local player when they spawn.

```
function explosionOnSpawn ( )
  -- get the spawned player's position
  local pX, pY, pZ = getElementPosition ( source )
  -- and create an explosion there
  createExplosion ( pX, pY, pZ, 6 )
end
-- add this function as a handler for any player that spawns
addEventHandler ( "onClientPlayerSpawn", localPlayer, explosionOnSpawn )
```

**Example 2:** This will cause an explosion that will not harm the player.

```
function fakeBomb(x,y,z,d)
	if d then --Check the players Dimension
		if getElementDimension(localPlayer) == d then
                        --If the players Dimension is the current dimension
                        --Then people on other dimensions cant see this explosion
			createExplosion(x, y, z, 0, true, -1.0, false)
		end
	else
		createExplosion(x,y,z,0,true,-1.0,false)
	end
end
addEvent("fakeBomb",true)
addEventHandler("fakeBomb",root,fakeBomb)
```

## See Also

- createExplosion
