---
doc_id: "mta-wiki:2276"
title: "SetVehicleWheelStates"
source_title: "SetVehicleWheelStates"
source_url: "https://wiki.multitheftauto.com/wiki/SetVehicleWheelStates"
revision_id: 64226
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# SetVehicleWheelStates

This function sets the state of wheels on the vehicle.

Internally, no vehicles have more than 4 wheels. If they appear to, they will be duplicating other wheels.

## Syntax

```
bool setVehicleWheelStates ( vehicle theVehicle, int frontLeft, [ int rearLeft = -1, int frontRight = -1, int rearRight = -1 ])
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle):setWheelStates(...)*

**Counterpart**: *[getVehicleWheelStates](mta://scripting/shared/functions/getvehiclewheelstates.md)*

## Required Arguments

- **theVehicle:** A handle to the [vehicle](https://wiki.multitheftauto.com/index.php?search=vehicle) that you wish to change the wheel states of.

- **frontLeft:** A whole number representing the wheel state (-1 for no change)

## Optional Arguments

- **rearLeft:** A whole number representing the wheel state (-1 for no change)

- **frontRight:** A whole number representing the wheel state (-1 for no change)

- **rearRight:** A whole number representing the wheel state (-1 for no change)

## Wheel-State values

- **0:** Inflated

- **1:** Flat

- **2:** Fallen off

- **3:** Collisionless

## Returns

Returns a boolean value *true* or *false* that tells you if it was successful or not.

## Example

Click to collapse [-]
Server

This example displays the states of the vehicle's wheels and changes their states if any arguments were passed.

```
function scriptWheelStates ( thePlayer, command, newFLeft, newRLeft, newFRight, newRRight )
    local theVehicle = getPedOccupiedVehicle ( thePlayer )
    if ( theVehicle ) then      -- check if the player is in a car
        if ( newFLeft ) then    -- if there's at least one argument passed, we change the wheel states
            if not setVehicleWheelStates ( theVehicle, newFLeft, newRLeft, newFRight, newRRight ) then
                outputChatBox ( "Bad arguments." )
            end
        end
        local states = { [0]="inflated", [1]="flat", [2]="fallen off" }    -- we store the states in a table
        local frontLeft, rearLeft, frontRight, rearRight = getVehicleWheelStates ( theVehicle )
        outputChatBox ( "Your vehicle's wheel states:", thePlayer )        -- output them in the chatbox
        outputChatBox ( "Front-Left: " .. states [ frontLeft ] .. ", Front-Right: " .. states [ frontRight ] ..
           ", Rear-Left: " .. states [ rearLeft ] .. ", Rear-Right: " .. states [ rearRight ], thePlayer )
    else
        outputChatBox ( "You have to be in a vehicle to use this command.", thePlayer )
    end
end
addCommandHandler ( "wheelstates", scriptWheelStates )
```

Click to expand [+]
Client

This example displays the states of the vehicle's wheels and changes their states if any arguments were passed.

```
function scriptWheelStates (command, newFLeft, newRLeft, newFRight, newRRight )
    local theVehicle = getPedOccupiedVehicle ( localPlayer )
    if ( theVehicle ) then      -- check if the player is in a car
        if ( newFLeft ) then    -- if there's at least one argument passed, we change the wheel states
            if not setVehicleWheelStates ( theVehicle, newFLeft, newRLeft, newFRight, newRRight ) then
                outputChatBox ( "Bad arguments." )
            end
        end
        local states = { [0]="inflated", [1]="flat", [2]="fallen off" }    -- we store the states in a table
        local frontLeft, rearLeft, frontRight, rearRight = getVehicleWheelStates ( theVehicle )
        outputChatBox ( "Your vehicle's wheel states:")        -- output them in the chatbox
        outputChatBox ( "Front-Left: " .. states [ frontLeft ] .. ", Front-Right: " .. states [ frontRight ] ..
           ", Rear-Left: " .. states [ rearLeft ] .. ", Rear-Right: " .. states [ rearRight ])
    else
        outputChatBox ( "You have to be in a vehicle to use this command.")
    end
end
addCommandHandler ( "wheelstates", scriptWheelStates )
```

## See Also

- [addVehicleUpgrade](mta://scripting/shared/functions/addvehicleupgrade.md)

- [addVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md)

- [attachTrailerToVehicle](mta://scripting/shared/functions/attachtrailertovehicle.md)

- [blowVehicle](mta://scripting/shared/functions/blowvehicle.md)

- [createVehicle](mta://scripting/shared/functions/createvehicle.md)

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

- setVehicleWheelStates
