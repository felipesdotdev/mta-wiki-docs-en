---
doc_id: "mta-wiki:1535"
title: "GetElementsByType"
source_title: "GetElementsByType"
source_url: "https://wiki.multitheftauto.com/wiki/GetElementsByType"
revision_id: 82681
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates"]
---

# GetElementsByType

This function is used to retrieve a list of all elements of the specified type. This can be useful, as it disregards *where* in the element tree it is. It can be used with either the built in types (listed below) or with any custom type used in a .map file. For example, if there is an element of type "flag" (e.g. <flag />) in the .map file, the using "flag" as the type argument would find it.

## Syntax

Click to collapse [-]
Server

```
table getElementsByType ( string theType, [ element startat=getRootElement() ] )
```

Click to collapse [-]
Client

```
table getElementsByType ( string theType, [ element startat=getRootElement(), bool streamedIn=false ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Element class.*

**Method**: *[Element](mta://reference/misc/element.md).getAllByType(...)*

### Required Arguments

- **theType:** The type of element you want a list of. This is the same as the tag name in the .map file, so this can be used with a custom element type if desired. Built in types can be found here: [Element](mta://reference/misc/element.md)

- **"player":** A player connected to the server

- **"ped":** A ped

- **"water":** A water polygon

- **"sound":** A playing sound

- **"vehicle":** A vehicle

- **"object":** An object

- **"pickup":** A pickup

- **"marker":** A marker

- **"colshape":** A collision shape

- **"blip":** A blip

- **"radararea":** A radar area

- **"team":** A team

- **"spawnpoint":** A spawnpoint

- **"console":** The server Console

- **"projectile":** A clientside projectile

- **"effect":** A clientside effect

- **"light":** A clientside light

- **"searchlight":** A clientside searchlight

- **"shader":** A shader

- **"texture":** A texture

- **"gui-window":** A GUI window (there's others like this for other GUI types)

- **"building":** A building (client side only)

- **"resource":** All the loaded resources

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **startat:** The [element](mta://reference/misc/element.md) the search should start at. Children of this element are searched, siblings or parents will not be found. By default, this is the root element which should suit most uses.

Click to collapse [-]
Client

- **streamedIn:** If true, function will only return elements that are streamed in.

### Returns

Returns a *table* containing all the elements of the specified type. Returns an empty *table* if there are no elements of the specified type. Returns *false* if the string specified is invalid (or not a string).

## Example

**Example 1:** This example retrieves a table of the players in the server, and checks whether or not each one is in a vehicle:

```
local players = getElementsByType ( "player" ) -- get a table of all the players in the server
for theKey,thePlayer in ipairs(players) do -- use a generic for loop to step through each player
   if ( isPlayerInVehicle ( thePlayer ) ) then -- if the player is in a vehicle, announce it
      outputChatBox ( getPlayerName ( thePlayer ) .. " is in a vehicle" )
   else -- if the player isn't in a vehicle, announce that he/she is on foot
      outputChatBox ( getPlayerName ( thePlayer ) .. " is on foot" )
   end
end
```

**Example 2:** This example retrieves a table of the teams in the server, and display them in chat:

```
local teams = getElementsByType("team")
for i,team in ipairs(teams) do
   local teamName = getTeamName(team) -- get the team name
   outputChatBox(teamName) -- display the team name in chat
end
```

**Example 3:** This shows how you could create a new element to describe a gas station:

```
function createGasStations(below)
    local gasstations = getElementsByType ( "gasstation", below ) -- get a table of all the gas station elements in the element tree
    for theKey,theGasStation in ipairs(gasstations) do 
        local x = getElementData(theGasStation, "posX") -- get the position of the element
        local y = getElementData(theGasStation, "posY")
        local z = getElementData(theGasStation, "posZ")
        setElementParent(createColSphere(x, y, z, 10), theGasStation) -- create a colshape for the gas station at the gas station's position
        addEventHandler("onColShapeHit", theGasStation, giveGas) -- when the player hits
    end
end

function mapLoad()
    createGasStations(source) -- create gas stations for the map that's just loaded
end
addEventHandler("onResourceStart", resourceRoot, mapLoad)

function giveGas(hittingElement)
    local theGasStation = source
    if getElementType(hittingElement) == "vehicle" then
        local gas_left = getElementData(theGasStation, "amount")
        local gas_speed = getElementData(theGasStation, "speed")
        if gas_left > 0 then

            local gas_to_remove = gas_speed 
            if gas_left < gas_speed then
                gas_to_remove = gas_left

            local current_vehicle_gas = getElementData(hittingElement, "gas")
            current_vehicle_gas = current_vehicle_gas + gas_to_remove
            gas_left = gas_left - gas_to_remove

            setElementData(hittingElement, "gas", current_vehicle_gas)
            setElementData(theGasStation, "amount", gas_left)
        else
            outputChatBox("Pump is out of gas!")
        end
    end
end
```

**Example 4:** This example loops trough all connected players and redirects them to another server host:

```
local serverIP = "99.88.77.66" -- Change to your server IP to redirect everyone
local serverPort = 22005 -- The destination server's port

function redirectAllPlayers()
    for _, p in ipairs(getElementsByType("player")) do
        if isElement(p) then
            redirectPlayer(p, serverIP, serverPort)
        end
    end
end
addEventHandler("onResourceStart", resourceRoot, redirectAllPlayers)
```

## See Also

- [attachElements](mta://scripting/shared/functions/attachelements.md)

- [createElement](mta://scripting/shared/functions/createelement.md)

- [destroyElement](mta://scripting/shared/functions/destroyelement.md)

- [detachElements](mta://scripting/shared/functions/detachelements.md)

- [getAttachedElements](mta://scripting/shared/functions/getattachedelements.md)

- [getElementAlpha](mta://scripting/shared/functions/getelementalpha.md)

- [getElementAttachedOffsets](mta://scripting/shared/functions/getelementattachedoffsets.md)

- [getElementAttachedTo](mta://scripting/shared/functions/getelementattachedto.md)

- [getElementByIndex](mta://scripting/shared/functions/getelementbyindex.md)

- [getElementByID](mta://scripting/shared/functions/getelementbyid.md)

- [getElementChild](mta://scripting/shared/functions/getelementchild.md)

- [getElementChildren](mta://scripting/shared/functions/getelementchildren.md)

- [getElementChildrenCount](mta://scripting/shared/functions/getelementchildrencount.md)

- [getElementCollisionsEnabled](mta://scripting/shared/functions/getelementcollisionsenabled.md)

- [getElementColShape](mta://scripting/shared/functions/getelementcolshape.md)

- [getElementData](mta://scripting/shared/functions/getelementdata.md)

- [getAllElementData](mta://scripting/shared/functions/getallelementdata.md)

- [hasElementData](mta://scripting/shared/functions/haselementdata.md)

- [getElementDimension](mta://scripting/shared/functions/getelementdimension.md)

- [getElementHealth](mta://scripting/shared/functions/getelementhealth.md)

- [getElementID](mta://scripting/shared/functions/getelementid.md)

- [getElementInterior](mta://scripting/shared/functions/getelementinterior.md)

- [getElementMatrix](mta://scripting/shared/functions/getelementmatrix.md)

- [getElementModel](mta://scripting/shared/functions/getelementmodel.md)

- [getElementParent](mta://scripting/shared/functions/getelementparent.md)

- [getElementPosition](mta://scripting/shared/functions/getelementposition.md)

- [getElementRotation](mta://scripting/shared/functions/getelementrotation.md)

- getElementsByType

- [getElementsWithinColShape](mta://scripting/shared/functions/getelementswithincolshape.md)

- [getElementsWithinRange](mta://scripting/shared/functions/getelementswithinrange.md)

- [getElementType](mta://scripting/shared/functions/getelementtype.md)

- [getElementVelocity](mta://scripting/shared/functions/getelementvelocity.md)

- [getLowLODElement](mta://scripting/shared/functions/getlowlodelement.md)

- [getRootElement](mta://scripting/shared/functions/getrootelement.md)

- [isElement](mta://scripting/shared/functions/iselement.md)

- [isElementAttached](mta://scripting/shared/functions/iselementattached.md)

- [isElementCallPropagationEnabled](mta://scripting/shared/functions/iselementcallpropagationenabled.md)

- [isElementDoubleSided](mta://scripting/shared/functions/iselementdoublesided.md)

- [isElementFrozen](mta://scripting/shared/functions/iselementfrozen.md)

- [isElementInWater](mta://scripting/shared/functions/iselementinwater.md)

- [isElementLowLOD](mta://scripting/shared/functions/iselementlowlod.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [isElementOnFire](mta://scripting/shared/functions/iselementonfire.md)

- [isElementWithinColShape](mta://scripting/shared/functions/iselementwithincolshape.md)

- [isElementWithinMarker](mta://scripting/shared/functions/iselementwithinmarker.md)

- [setElementAlpha](mta://scripting/shared/functions/setelementalpha.md)

- [setElementAngularVelocity](mta://scripting/shared/functions/setelementangularvelocity.md)

- [getElementAngularVelocity](mta://scripting/shared/functions/getelementangularvelocity.md)

- [setElementAttachedOffsets](mta://scripting/shared/functions/setelementattachedoffsets.md)

- [setElementCallPropagationEnabled](mta://scripting/shared/functions/setelementcallpropagationenabled.md)

- [setElementCollisionsEnabled](mta://scripting/shared/functions/setelementcollisionsenabled.md)

- [setElementData](mta://scripting/shared/functions/setelementdata.md)

- [setElementDimension](mta://scripting/shared/functions/setelementdimension.md)

- [setElementDoubleSided](mta://scripting/shared/functions/setelementdoublesided.md)

- [setElementFrozen](mta://scripting/shared/functions/setelementfrozen.md)

- [setElementHealth](mta://scripting/shared/functions/setelementhealth.md)

- [setElementID](mta://scripting/shared/functions/setelementid.md)

- [setElementInterior](mta://scripting/shared/functions/setelementinterior.md)

- [setElementModel](mta://scripting/shared/functions/setelementmodel.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22864](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22864):

- [setElementOnFire](mta://scripting/shared/functions/setelementonfire.md)

- [setElementParent](mta://scripting/shared/functions/setelementparent.md)

- [setElementPosition](mta://scripting/shared/functions/setelementposition.md)

- [setElementRotation](mta://scripting/shared/functions/setelementrotation.md)

- [setElementVelocity](mta://scripting/shared/functions/setelementvelocity.md)

- [setLowLODElement](mta://scripting/shared/functions/setlowlodelement.md)
