---
doc_id: "mta-wiki:8437"
title: "IsVehicleWindowOpen"
source_title: "IsVehicleWindowOpen"
source_url: "https://wiki.multitheftauto.com/wiki/IsVehicleWindowOpen"
revision_id: 49605
language: "en"
categories: ["Client_functions", "Changes_in_1.5.3", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:03.404656+00:00"
---

# IsVehicleWindowOpen

This function gets the vehicle window state.

## Syntax

```
bool isVehicleWindowOpen ( vehicle theVehicle, int window )
```

### Required arguments

- **theVehicle:** The vehicle that you wish to get the window state.

- **window:** An [integer](mta://reference/misc/int.md) representing a vehicle window. It can be:

- **0:** motorbike shield

- **1:** rear window

- **2:** right front window

- **3:** right back window

- **4:** left front (driver) window

- **5:** left back window

- **6:** windshield

## Returns

This function returns a boolean which represents window open state.

## Example

This example opens the vehicle windows when the local player use /openwindow <window number>.

```
function openVehicleWindow (cmd,number)
   if (isPedInVehicle (localPlayer)) then
      local vehicle = getPedOccupiedVehicle(localPlayer) 
      if number and tonumber(number) then
	 if tonumber(number) > 0 and tonumber(number) < 7 then
	    setVehicleWindowOpen(vehicle,tonumber(number), not isVehicleWindowOpen( vehicle, tonumber(number)))
	 end
      end
   end
end
addCommandHandler ("openwindow",openVehicleWindow)
```

## See also

- [areVehicleLightsOn](mta://scripting/client/functions/arevehiclelightson.md)

- [getHeliBladeCollisionsEnabled](mta://scripting/client/functions/gethelibladecollisionsenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22344](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22344):

- [getVehicleRotorSpeed](mta://scripting/client/functions/getvehiclerotorspeed.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22862](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22862):

- [getVehicleRotorState](mta://scripting/client/functions/getvehiclerotorstate.md)

- [getVehicleAdjustableProperty](mta://scripting/client/functions/getvehicleadjustableproperty.md)

- [getVehicleComponentPosition](mta://scripting/client/functions/getvehiclecomponentposition.md)

- [getVehicleComponentRotation](mta://scripting/client/functions/getvehiclecomponentrotation.md)

- [getVehicleComponents](mta://scripting/client/functions/getvehiclecomponents.md)

- [getVehicleComponentScale](mta://scripting/client/functions/getvehiclecomponentscale.md)

- [getVehicleComponentVisible](mta://scripting/client/functions/getvehiclecomponentvisible.md)

- [getVehicleCurrentGear](mta://scripting/client/functions/getvehiclecurrentgear.md)

- [getVehicleDummyPosition](mta://scripting/client/functions/getvehicledummyposition.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22649](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22649):

- [getVehicleEntryPoints](mta://scripting/client/functions/getvehicleentrypoints.md)

- [getVehicleGravity](mta://scripting/client/functions/getvehiclegravity.md)

- [getVehicleModelDummyDefaultPosition](mta://scripting/client/functions/getvehiclemodeldummydefaultposition.md)

- [getVehicleModelDummyPosition](mta://scripting/client/functions/getvehiclemodeldummyposition.md)

- [getVehicleModelExhaustFumesPosition](mta://scripting/client/functions/getvehiclemodelexhaustfumesposition.md)

- [getVehicleModelWheelSize](mta://scripting/client/functions/getvehiclemodelwheelsize.md)

- [getVehicleNitroCount](mta://scripting/client/functions/getvehiclenitrocount.md)

- [getVehicleNitroLevel](mta://scripting/client/functions/getvehiclenitrolevel.md)

- [getVehicleWheelFrictionState](mta://scripting/client/functions/getvehiclewheelfrictionstate.md)

- [getVehicleWheelScale](mta://scripting/client/functions/getvehiclewheelscale.md)

- [isTrainChainEngine](mta://scripting/client/functions/istrainchainengine.md)

- [isVehicleNitroActivated](mta://scripting/client/functions/isvehiclenitroactivated.md)

- [isVehicleNitroRecharging](mta://scripting/client/functions/isvehiclenitrorecharging.md)

- [isVehicleWheelOnGround](mta://scripting/client/functions/isvehiclewheelonground.md)

- isVehicleWindowOpen

- [resetVehicleComponentPosition](mta://scripting/client/functions/resetvehiclecomponentposition.md)

- [resetVehicleComponentRotation](mta://scripting/client/functions/resetvehiclecomponentrotation.md)

- [resetVehicleComponentScale](mta://scripting/client/functions/resetvehiclecomponentscale.md)

- [resetVehicleDummyPositions](mta://scripting/client/functions/resetvehicledummypositions.md)

- [setHeliBladeCollisionsEnabled](mta://scripting/client/functions/sethelibladecollisionsenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22344](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22344):

- [setVehicleRotorSpeed](mta://scripting/client/functions/setvehiclerotorspeed.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22862](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22862):

- [setVehicleRotorState](mta://scripting/client/functions/setvehiclerotorstate.md)

- [setVehicleAdjustableProperty](mta://scripting/client/functions/setvehicleadjustableproperty.md)

- [setVehicleComponentPosition](mta://scripting/client/functions/setvehiclecomponentposition.md)

- [setVehicleComponentRotation](mta://scripting/client/functions/setvehiclecomponentrotation.md)

- [setVehicleComponentScale](mta://scripting/client/functions/setvehiclecomponentscale.md)

- [setVehicleComponentVisible](mta://scripting/client/functions/setvehiclecomponentvisible.md)

- [setVehicleDummyPosition](mta://scripting/client/functions/setvehicledummyposition.md)

- [setVehicleGravity](mta://scripting/client/functions/setvehiclegravity.md)

- [setVehicleModelDummyPosition](mta://scripting/client/functions/setvehiclemodeldummyposition.md)

- [setVehicleModelExhaustFumesPosition](mta://scripting/client/functions/setvehiclemodelexhaustfumesposition.md)

- [setVehicleModelWheelSize](mta://scripting/client/functions/setvehiclemodelwheelsize.md)

- [setVehicleNitroCount](mta://scripting/client/functions/setvehiclenitrocount.md)

- [setVehicleNitroLevel](mta://scripting/client/functions/setvehiclenitrolevel.md)

- [setVehicleWheelScale](mta://scripting/client/functions/setvehiclewheelscale.md)

- [setVehicleWindowOpen](mta://scripting/client/functions/setvehiclewindowopen.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22592](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22592):

- [setVehicleWheelsRotation](mta://scripting/client/functions/setvehiclewheelsrotation.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22815](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22815):

- [setVehicleSmokeTrailEnabled](mta://scripting/client/functions/setvehiclesmoketrailenabled.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22815](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22815):

- [isVehicleSmokeTrailEnabled](mta://scripting/client/functions/isvehiclesmoketrailenabled.md)

- **Shared**

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

- [setVehicleWheelStates](mta://scripting/shared/functions/setvehiclewheelstates.md)
