---
doc_id: "mta-wiki:1805"
title: "CreateColSphere"
source_title: "CreateColSphere"
source_url: "https://wiki.multitheftauto.com/wiki/CreateColSphere"
revision_id: 78555
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# CreateColSphere

This function creates a collision sphere. This is a shape that has a position and a radius. See [Wikipedia](http://en.wikipedia.org/wiki/Sphere) for a definition of a sphere.

| [[{{{image}}}\|link=\|]] | Tip: To visualize a colshape when writing scripts, use the client console command showcol |
| --- | --- |
|  |  |

## Syntax

```
colshape createColSphere ( float fX, float fY, float fZ, float fRadius )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *ColShape.Sphere(...)*

### Required Arguments

- **fX:** The collision sphere's center point's X axis position.

- **fY:** The collision sphere's center point's Y axis position.

- **fZ:** The collision sphere's center point's Z axis position.

- **fRadius:** The collision sphere's radius.

### Returns

Returns a [colshape](https://wiki.multitheftauto.com/index.php?search=colshape) element if successful, *false* if invalid arguments were passed to the function.

## Example

Click to collapse [-]
Server

**Example 1:** This example displays a chat message when a player enters the colshape and allows the colshape to be created using a console function *set_zone*.

```
local theZone

function shapeHit(thePlayer)
    outputChatBox(getPlayerName(thePlayer).. " is in the zone!")
end

function setZone(playerSource, commandName, fX, fY, fZ, fRadius)
    local fX, fY, fZ, fRadius = tonumber(fX), tonumber(fY), tonumber(fZ), tonumber(fRadius)
    if (not fX) or (not fY) or (not fZ) or (not fRadius) then
        outputChatBox("Syntax: /"..commandName.." [X] [Y] [Z] [Radius]", playerSource)
    else
        if (theZone ~= nil) then
            destroyElement(theZone)
        end
        local tempCol = createColSphere(fX, fY, fZ, fRadius)
        addEventHandler("onColShapeHit", tempCol, shapeHit)
        outputChatBox("Zone has "..(theZone ~= nil and "moved" or "created").."!", playerSource)
        theZone = tempCol
    end
end
addCommandHandler("set_zone", setZone, false, false)
```

**Example 2:** This example allows creation of claymores, which trigger and explode.

```
function createClaymore ( x,y,z, creator )
	local x,y,z = getElementPosition ( creator )
	local claymoreObject = createObject ( 1945, x, y, z - 1, 0, 0, 90 ) --create an object which looks like a claymore
	local claymoreCol = createColSphere ( x, y, z, 1 ) --create a col sphere with radius 1
	setElementData ( claymoreCol , "type", "claymore" ) --store the type of colshape so it can be retrieved
	setElementData ( claymoreCol, "object", claymoreObject ) --store the object of the claymore
	setElementData ( claymoreCol, "creatorPlayer", creator ) --store the person who created it
end

function claymoreHit ( player, matchingDimension )
	if getElementData ( source, "type" ) == "claymore" then --ensure its a claymore
		--retrieve the object associated to the claymore, and who created it
		local claymoreObject = getElementData ( source, "object" )
		local claymoreCreator = getElementData ( source, "creatorPlayer" )
		--get the position of the claymore
		local x,y,z = getElementPosition ( source )
		createExplosion ( x,y,z, 12, claymoreCreator ) --create an explosion, associated to the creator, of a small size at the col's position
		--destroy the claymore object, and the col shape so it doesnt trigger again.
		destroyElement ( claymoreObject )
		destroyElement ( source )
	end
end
addEventHandler ( "onColShapeHit", getRootElement(), claymoreHit )
```

## See Also

- [addColPolygonPoint](mta://scripting/shared/functions/addcolpolygonpoint.md)

- [createColCircle](mta://scripting/shared/functions/createcolcircle.md)

- [createColCuboid](mta://scripting/shared/functions/createcolcuboid.md)

- [createColPolygon](mta://scripting/shared/functions/createcolpolygon.md)

- [createColRectangle](mta://scripting/shared/functions/createcolrectangle.md)

- createColSphere

- [createColTube](mta://scripting/shared/functions/createcoltube.md)

- [getColPolygonHeight](mta://scripting/shared/functions/getcolpolygonheight.md)

- [getColPolygonPoints](mta://scripting/shared/functions/getcolpolygonpoints.md)

- [getColPolygonPointPosition](mta://scripting/shared/functions/getcolpolygonpointposition.md)

- [getColShapeType](mta://scripting/shared/functions/getcolshapetype.md)

- [getColShapeRadius](mta://scripting/shared/functions/getcolshaperadius.md)

- [getColShapeSize](mta://scripting/shared/functions/getcolshapesize.md)

- [isInsideColShape](mta://scripting/shared/functions/isinsidecolshape.md)

- [removeColPolygonPoint](mta://scripting/shared/functions/removecolpolygonpoint.md)

- [setColPolygonHeight](mta://scripting/shared/functions/setcolpolygonheight.md)

- [setColPolygonPointPosition](mta://scripting/shared/functions/setcolpolygonpointposition.md)

- [setColShapeRadius](mta://scripting/shared/functions/setcolshaperadius.md)

- [setColShapeSize](mta://scripting/shared/functions/setcolshapesize.md)
