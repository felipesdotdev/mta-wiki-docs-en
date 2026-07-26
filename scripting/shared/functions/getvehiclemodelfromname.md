---
doc_id: "mta-wiki:4450"
title: "GetVehicleModelFromName"
source_title: "GetVehicleModelFromName"
source_url: "https://wiki.multitheftauto.com/wiki/GetVehicleModelFromName"
revision_id: 51078
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:28.113430+00:00"
---

# GetVehicleModelFromName

This function retrieves the model ID of a vehicle as an [integer](mta://reference/misc/int.md) value from its name.

## Syntax

```
int getVehicleModelFromName ( string name )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the Vehicle class.*

**Method**: *[Vehicle](mta://reference/misc/vehicle.md).getModelFromName(...)*

### Required Arguments

- **name:** A [string](mta://reference/misc/string.md) containing the name of the vehicle.

- at-400

- admiral

- alpha

- ambulance

- andromada

- bf injection

- bf-400

- bmx

- baggage

- baggage trailer (uncovered)

- baggage trailer (covered)

- bandito

- banshee

- barracks

- beagle

- benson

- berkley's rc van

- bike

- blade

- blista compact

- bloodring banger

- bobcat

- box freight

- boxville

- boxville mission

- bravura

- broadway

- buccaneer

- buffalo

- bullet

- burrito

- bus

- cabbie

- caddy

- cadrona

- camper

- cargobob

- cement truck

- cheetah

- clover

- club

- coach

- coastguard

- combine harvester

- comet

- cropduster

- dft-30

- dinghy

- dodo

- dozer

- dumper

- dune

- elegant

- elegy

- emperor

- enforcer

- esperanto

- euros

- fbi rancher

- fbi truck

- fcr-900

- faggio

- farm trailer

- feltzer

- fire truck

- fire truck ladder

- flash

- flatbed

- forklift

- fortune

- freeway

- freight

- freight train flatbed

- glendale

- glendale damaged

- greenwood

- hpv1000

- hermes

- hotdog

- hotknife

- hotring racer

- hotring racer 2

- hotring racer 3

- hunter

- huntley

- hustler

- hydra

- infernus

- intruder

- jester

- jetmax

- journey

- kart

- landstalker

- launch

- leviathan

- linerunner

- majestic

- manana

- marquis

- maverick

- merit

- mesa

- monster 1

- monster 2

- monster 3

- moonbeam

- mountain bike

- mower

- mr. whoopee

- mule

- nrg-500

- nebula

- nevada

- news chopper

- newsvan

- oceanic

- pcj-600

- packer

- patriot

- perennial

- phoenix

- picador

- pizzaboy

- police ls

- police lv

- police maverick

- police ranger

- police sf

- pony

- predator

- premier

- previon

- primo

- quadbike

- rc bandit

- rc baron

- rc cam

- rc goblin

- rc raider

- rc tiger

- raindance

- rancher

- rancher lure

- reefer

- regina

- remington

- rhino

- roadtrain

- romero

- rumpo

- rustler

- s.w.a.t.

- sabre

- sadler

- sadler damaged

- sanchez

- sandking

- savanna

- seasparrow

- securicar

- sentinel

- shamal

- skimmer

- slamvan

- solair

- sparrow

- speeder

- squalo

- stafford

- stallion

- stratum

- streak

- streak train trailer

- street clean trailer

- stretch

- stuntplane

- sultan

- sunrise

- super gt

- sweeper

- tahoma

- tampa

- tanker

- taxi

- tornado

- towtruck

- tractor

- trailer (stairs)

- trailer (tanker commando)

- trailer 1

- trailer 2

- trailer 3

- tram

- trashmaster

- tropic

- tug

- turismo

- uranus

- utility van

- vincent

- virgo

- voodoo

- vortex

- walton

- washington

- wayfarer

- willard

- windsor

- yankee

- yosemite

- zr-350

### Returns

Returns an [integer](mta://reference/misc/int.md) if the name exists, *false* otherwise.
If you use this function on vehicles with shared names, such as "police", it will return the earliest occurrence of that vehicle's ID.

## Example

Click to expand [+]
Server

This will allow the player to create a vehicle by name and it's model ID will be displayed in the chatbox when the vehicle is spawned.

```
function createVehicleCommand ( thePlayer, commandName, carName )
    -- This function is triggered by the text "spawnvehicle" in the console.
    -- The player must specify the added parameter 'carName' to specify
    -- what car they wish to spawn.
    local carModel = getVehicleModelFromName ( carName )
    -- Get the model ID of the car the player asked for and store it to the
    -- variable 'carModel'
    local x, y, z = getElementPosition ( thePlayer )
    -- Get the position of the player to spawn the car near this location
    if not carModel then
        outputChatBox ( "That is not a valid car name" )
    else
        createVehicle ( carModel, x + 5, y, z )
        -- Spawn the car using its model ID. Spawn it at x + 5 from the player so it doesn't crush him
	outputChatBox ( "A vehicle with model ID of " .. carModel .. " was created!" )
    end
    -- If the entered car name returns no car model ID, the string will be empty and false will be returned.
    -- If the string does have any value, we create the car and announce the car model ID in the chatbox,
    -- because a car did exist under the given car name.
end
addCommandHandler ( "spawnvehicle", createVehicleCommand )
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

- getVehicleModelFromName

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
