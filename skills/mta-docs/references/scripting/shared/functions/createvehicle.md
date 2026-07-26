---
doc_id: "mta-wiki:1290"
title: "CreateVehicle"
source_title: "CreateVehicle"
source_url: "https://wiki.multitheftauto.com/wiki/CreateVehicle"
revision_id: 82223
language: "en"
categories: ["Server_functions", "Client_functions", "Utility_templates", "Changes_in_1.2", "Changes_in_1.6.0"]
---

# CreateVehicle

| [[{{{image}}}\|link=\|]] | Note: Vehicles (and other elements) created client-side are only seen by the client that created them, aren't synced and players cannot enter them. They are essentially for display only. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Due to how GTA works, creating a lot of vehicles in the same place will cause lag. The more geometries and unique textures has model the bigger the lag is. Even a lot of default vehicles will cause lag if in the same place. |
| --- | --- |
|  |  |

This function creates a vehicle at the specified location.

It's worth noting that the position of the vehicle is the center point of the vehicle, not its base. As such, you need to ensure that the z value (vertical axis) is some height above the ground. You can find the exact height using the client side function [getElementDistanceFromCentreOfMassToBaseOfModel](mta://scripting/client/functions/getelementdistancefromcentreofmasstobaseofmodel.md), or you can estimate it yourself and just spawn the vehicle so it drops to the ground.

## Syntax

```
vehicle createVehicle ( int model, float x, float y, float z [, float rx, float ry, float rz, string numberplate, bool bDirection, int variant1, int variant2, bool synced = true ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[Vehicle](https://wiki.multitheftauto.com/index.php?search=Vehicle)(...)*

### Required Arguments

- **model**: The [vehicle ID](mta://reference/misc/vehicle-ids.md) of the vehicle being created.

- **x**: A floating point number representing the X coordinate on the map.

- **y**: A floating point number representing the Y coordinate on the map.

- **z**: A floating point number representing the Z coordinate on the map.

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **rx**: A floating point number representing the rotation about the X axis in degrees.

- **ry**: A floating point number representing the rotation about the Y axis in degrees.

- **rz**: A floating point number representing the rotation about the Z axis in degrees.

- **numberplate**: A string that will go on the number plate of the vehicle (max 8 characters).

- **bDirection** *(serverside only)*: Placeholder [boolean](mta://reference/misc/boolean.md) which provides backward compatibility with some scripts. It never had any effect, but it is read by the code. It is recommended to ignore this argument, passing *false* or the *variant1* argument in its place.

- **variant1**: An integer for the first vehicle variant. See [vehicle variants](mta://reference/misc/vehicle-variants.md).

- **variant2**: An integer for the second vehicle variant. See [vehicle variants](mta://reference/misc/vehicle-variants.md).

ADDED/UPDATED IN VERSION 1.6.0 [r22477](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22477):

- **synced** *(serverside only)*: A boolean value representing whether or not the vehicle will be synced. Disabling the sync might be useful for frozen or static vehicles to increase the server performance.

### Returns

Returns the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) element that was created. Returns *false* if the arguments are incorrect, or if the vehicle limit of 65535 is exceeded.

## Using trains

Trains are created using the createVehicle function. They are placed at the nearest point of the GTASA train pathing (they usually are railroad tracks) from their spawning point.

## Example

Click to collapse [-]
Example 1: Server

This example creates a 'vehicle spawner' marker that gives the player a vehicle as soon they step into it.

```
local vehMark = createMarker(-2426.34106, -639.12714, 132.93631,"cylinder")

function vehicleSpawner(hitElement,matchingDimension)
	if getElementType(hitElement) == "player" then
		if getPedOccupiedVehicle(hitElement) == false then
		local x,y,z = getElementPosition(hitElement)
			local veh = createVehicle(551, x,y,z)
			warpPedIntoVehicle(hitElement,veh)
		end
	end 
end 
addEventHandler("onMarkerHit",vehMark,vehicleSpawner)
```

Click to collapse [-]
Example 2: Server

This example creates a vehicle five units to the right of a player when they type *createvehicle* and its name in the console:

```
local distance = 5 --units

-- define our handler (we'll take a variable number of parameters where the name goes, because there are vehicle names with more than one word)
function consoleCreateVehicle ( sourcePlayer, commandName, ... )
   -- if a player triggered it, not the admin,
   if ( sourcePlayer ) then
      -- calculate the position of the vehicle based on the player's position and rotation:
      local x, y, z = getElementPosition ( sourcePlayer ) -- get the player's position
      local rotZ = getElementRotation ( sourcePlayer ) -- get the player's rotation around the Z axis in degrees
      x = x + ( ( math.cos ( math.rad ( rotZ ) ) ) * distance ) -- calculate the X position of the vehicle
      y = y + ( ( math.sin ( math.rad ( rotZ ) ) ) * distance ) -- calculate the Y position of the vehicle

      -- get the complete vehicle name by joining all passed parameters using Lua function table.concat
      local vehicleName = table.concat({...}, " ")
      -- get the vehicle's model ID from the name
      local vehicleID = getVehicleModelFromName ( vehicleName )
      -- if vehicle ID is valid,
      if vehicleID then
            -- create the vehicle using the information gathered above:
            local newVehicle = createVehicle ( vehicleID, x, y, z, 0, 0, rotZ )
            -- if vehicle creation failed, give the player a message
            if not newVehicle then
               outputConsole ( "Failed to create vehicle.", sourcePlayer )
            end
      end
   end
end

-- Attach the 'consoleCreateVehicle' function to the "createvehicle" command
addCommandHandler ( "createvehicle", consoleCreateVehicle )
```

Click to expand [+]
Example 3: Server

This script spawns a Rhino on top of one lucky individual.

```
function scriptCreateTank ( player, command )
      local luckyBugger = getRandomPlayer() -- get a random player
      local x, y, z = getElementPosition ( luckyBugger ) -- retrive the player's position
      createVehicle ( 432, x, y, z + 10 ) -- create the tank 10 units above them
      outputChatBox ( "You got Tank'd!", luckyBugger )
end
--Attach the 'scriptCreateTank' function to the "tank" command
addCommandHandler ( "tank", scriptCreateTank )
```

Click to expand [+]
Example 4: Server

This example adds a */spveh* command to spawn a car model in the provided coordinates. If any car created by this command gets blown up, it will respawn where it was created.

```
-- Do not allow the following IDs to be spawned
local forbiddenCars = { [435] = true, [441] = true, [449] = true, [450] = true, [464] = true, [465] = true, [501] = true,
                        [537] = true, [538] = true, [564] = true, [569] = true, [570] = true, [584] = true, [590] = true,
                        [591] = true, [594] = true, [606] = true, [607] = true, [608] = true, [610] = true, [611] = true }

local cmdVehRoot = createElement("commandVehicles") -- Dummy element containing the cars that this command has created
addCommandHandler("spveh",
    function(player, cmd, modelID, x, y, z, platetext)
        -- Check whether arguments are correct
        local modelID, x, y, z = tonumber(modelID), tonumber(x), tonumber(y), tonumber(z)
        if modelID and x and y and z then
            -- Do not continue if we shouldn't
            if forbiddenCars[modelID] then
                outputChatBox("The car model you provided is not allowed.", player, 255, 0, 0)
                return
            end
            local platetext = type(platetext) == "string" and platetext or "PRIVATE"
            -- Create the actual vehicle and set it as a children of our dummy element
            setElementParent(createVehicle(modelID, x, y, z, 0, 0, 0, platetext), cmdVehRoot)
            -- Inform the player about what we did
            outputChatBox("You have created a " .. getVehicleNameFromModel(modelID) .. " (model ID: " .. modelID .. ") at " .. table.concat({ x, y, z }, ", ") .. " with numberplate " .. platetext .. " successfully.", player, 0, 255, 0)
        else
            outputChatBox("Syntax: /" .. cmd .. " (modelID) (x) (y) (z) [numberplate]", player, 255, 255, 255)
        end
    end
)

-- If a vehicle that has been created using the command blows up, respawn it where it was created
addEventHandler("onVehicleExplode", cmdVehRoot,
    function()
        respawnVehicle(source)
    end
)
```

Click to collapse [-]
Example 5: Client

This script spawns a Rhino on top of the local player.

```
function scriptCreateTank ( commandName )
      local x, y, z = getElementPosition ( localPlayer ) -- retrive the player's position
      createVehicle ( 432, x, y, z + 10 ) -- create the tank 10 units above them
      outputChatBox ( "You got Tank'd!", 255, 0, 0)
end
--Attach the 'scriptCreateTank' function to the "tank" command
addCommandHandler ( "tank", scriptCreateTank )
```

This is an example of how this function is executed in an OOP environment.

Click to collapse [-]
OOP server

This script will create an Infernus at the center (0, 0, 3) of San Andreas upon execution.

```
addEventHandler( "onResourceStart", resourceRoot,
    function()
        infernus = Vehicle(411, Vector3(0, 0, 3)); -- Create an Infernus and spawn it at the middle of SA.
        infernus:setColor(0, 0, 0); -- Set its color to black.
        infernus.damageProof = true; -- Make it damage proof
    end
)
	
addCommandHandler( "blowinfernus",
    function(p)
        if not infernus.blown then -- Check if the Infernus is blown up or not.
            infernus:blow();
        else -- Ouch, it's blown up, let's output an error to the player.
            outputChatBox( "The Infernus has already been blown up by you.", p, 255, 0, 0, false );
        end
    end)
```

## See Also

- [addVehicleUpgrade](mta://scripting/shared/functions/addvehicleupgrade.md)

- [addVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md)

- [attachTrailerToVehicle](mta://scripting/shared/functions/attachtrailertovehicle.md)

- [blowVehicle](mta://scripting/shared/functions/blowvehicle.md)

- createVehicle

- [detachTrailerFromVehicle](mta://scripting/shared/functions/detachtrailerfromvehicle.md)

- [fixVehicle](mta://scripting/shared/functions/fixvehicle.md)

- [getOriginalHandling](mta://scripting/shared/functions/getoriginalhandling.md)

- [getTrainDirection](mta://scripting/shared/functions/gettraindirection.md)

- [getTrainPosition](mta://scripting/shared/functions/gettrainposition.md)

- [getTrainSpeed](mta://scripting/shared/functions/gettrainspeed.md)

- [getVehicleColor](mta://scripting/shared/functions/getvehiclecolor.md)

- [getVehicleCompatibleUpgrades](mta://scripting/shared/functions/getvehiclecompatibleupgrades.md)

- [getVehicleController](mta://scripting/shared/functions/getvehiclecontroller.md)

- [getVehicleDoorOpenRatio](mta://scripting/shared/functions/getvehicledooropenratio.md)

- [getVehicleDoorState](mta://scripting/shared/functions/getvehicledoorstate.md)

- [getVehicleEngineState](mta://scripting/shared/functions/getvehicleenginestate.md)

- [getVehicleHandling](mta://scripting/shared/functions/getvehiclehandling.md)

- [getVehicleHeadLightColor](mta://scripting/shared/functions/getvehicleheadlightcolor.md)

- [getVehicleLandingGearDown](mta://scripting/shared/functions/getvehiclelandinggeardown.md)

- [getVehicleLightState](mta://scripting/shared/functions/getvehiclelightstate.md)

- [getVehicleMaxPassengers](mta://scripting/shared/functions/getvehiclemaxpassengers.md)

- [getVehicleModelFromName](mta://scripting/shared/functions/getvehiclemodelfromname.md)

- [getVehicleName](mta://scripting/shared/functions/getvehiclename.md)

- [getVehicleNameFromModel](mta://scripting/shared/functions/getvehiclenamefrommodel.md)

- [setVehicleNitroActivated](mta://scripting/shared/functions/setvehiclenitroactivated.md)

- [getVehicleOccupant](mta://scripting/shared/functions/getvehicleoccupant.md)

- [getVehicleOccupants](mta://scripting/shared/functions/getvehicleoccupants.md)

- [getVehicleOverrideLights](mta://scripting/shared/functions/getvehicleoverridelights.md)

- [getVehiclePaintjob](mta://scripting/shared/functions/getvehiclepaintjob.md)

- [getVehiclePanelState](mta://scripting/shared/functions/getvehiclepanelstate.md)

- [getVehiclePlateText](mta://scripting/shared/functions/getvehicleplatetext.md)

- [getVehicleSirenParams](mta://scripting/shared/functions/getvehiclesirenparams.md)

- [getVehicleSirens](mta://scripting/shared/functions/getvehiclesirens.md)

- [getVehicleSirensOn](mta://scripting/shared/functions/getvehiclesirenson.md)

- [getVehicleTowedByVehicle](mta://scripting/shared/functions/getvehicletowedbyvehicle.md)

- [getVehicleTowingVehicle](mta://scripting/shared/functions/getvehicletowingvehicle.md)

- [getVehicleTurretPosition](mta://scripting/shared/functions/getvehicleturretposition.md)

- [getVehicleType](mta://scripting/shared/functions/getvehicletype.md)

- [getVehicleUpgradeOnSlot](mta://scripting/shared/functions/getvehicleupgradeonslot.md)

- [getVehicleUpgradeSlotName](mta://scripting/shared/functions/getvehicleupgradeslotname.md)

- [getVehicleUpgrades](mta://scripting/shared/functions/getvehicleupgrades.md)

- [getVehicleVariant](mta://scripting/shared/functions/getvehiclevariant.md)

- [getVehicleWheelStates](mta://scripting/shared/functions/getvehiclewheelstates.md)

- [isTrainDerailable](mta://scripting/shared/functions/istrainderailable.md)

- [isTrainDerailed](mta://scripting/shared/functions/istrainderailed.md)

- [isVehicleBlown](mta://scripting/shared/functions/isvehicleblown.md)

- [isVehicleDamageProof](mta://scripting/shared/functions/isvehicledamageproof.md)

- [isVehicleFuelTankExplodable](mta://scripting/shared/functions/isvehiclefueltankexplodable.md)

- [isVehicleLocked](mta://scripting/shared/functions/isvehiclelocked.md)

- [isVehicleOnGround](mta://scripting/shared/functions/isvehicleonground.md)

- [isVehicleTaxiLightOn](mta://scripting/shared/functions/isvehicletaxilighton.md)

- [removeVehicleUpgrade](mta://scripting/shared/functions/removevehicleupgrade.md)

- [removeVehicleSirens](mta://scripting/shared/functions/removevehiclesirens.md)

- [setTrainDerailable](mta://scripting/shared/functions/settrainderailable.md)

- [setTrainDerailed](mta://scripting/shared/functions/settrainderailed.md)

- [setTrainDirection](mta://scripting/shared/functions/settraindirection.md)

- [setTrainPosition](mta://scripting/shared/functions/settrainposition.md)

- [setTrainSpeed](mta://scripting/shared/functions/settrainspeed.md)

- [setVehicleColor](mta://scripting/shared/functions/setvehiclecolor.md)

- [setVehicleDamageProof](mta://scripting/shared/functions/setvehicledamageproof.md)

- [setVehicleDoorOpenRatio](mta://scripting/shared/functions/setvehicledooropenratio.md)

- [setVehicleDoorState](mta://scripting/shared/functions/setvehicledoorstate.md)

- [setVehicleDoorsUndamageable](mta://scripting/shared/functions/setvehicledoorsundamageable.md)

- [setVehicleEngineState](mta://scripting/shared/functions/setvehicleenginestate.md)

- [setVehicleFuelTankExplodable](mta://scripting/shared/functions/setvehiclefueltankexplodable.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22771](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22771):

- [spawnVehicleFlyingComponent](mta://scripting/shared/functions/spawnvehicleflyingcomponent.md)

- [setVehicleHandling](mta://scripting/shared/functions/setvehiclehandling.md)

- [setVehicleHeadLightColor](mta://scripting/shared/functions/setvehicleheadlightcolor.md)

- [setVehicleLandingGearDown](mta://scripting/shared/functions/setvehiclelandinggeardown.md)

- [setVehicleLightState](mta://scripting/shared/functions/setvehiclelightstate.md)

- [setVehicleLocked](mta://scripting/shared/functions/setvehiclelocked.md)

- [setVehicleOverrideLights](mta://scripting/shared/functions/setvehicleoverridelights.md)

- [setVehiclePaintjob](mta://scripting/shared/functions/setvehiclepaintjob.md)

- [setVehiclePanelState](mta://scripting/shared/functions/setvehiclepanelstate.md)

- [setVehiclePlateText](mta://scripting/shared/functions/setvehicleplatetext.md)

- [setVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- [setVehicleSirensOn](mta://scripting/shared/functions/setvehiclesirenson.md)

- [setVehicleTaxiLightOn](mta://scripting/shared/functions/setvehicletaxilighton.md)

- [setVehicleTurretPosition](mta://scripting/shared/functions/setvehicleturretposition.md)

- [setVehicleVariant](mta://scripting/shared/functions/setvehiclevariant.md)

- [setVehicleWheelStates](mta://scripting/shared/functions/setvehiclewheelstates.md)
