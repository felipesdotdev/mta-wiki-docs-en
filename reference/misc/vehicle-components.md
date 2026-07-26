---
doc_id: "mta-wiki:7672"
title: "Vehicle Components"
source_title: "Vehicle Components"
source_url: "https://wiki.multitheftauto.com/wiki/Vehicle_Components"
revision_id: 80683
language: "en"
categories: []
generated_at: "2026-07-26T16:16:52.558773+00:00"
---

# Vehicle Components

This page aims to provide an overview of vehicle components. The list is currently incomplete.

| [[{{{image}}}\|link=\|]] | Note: Changing wheel position on Z axis doesn't work. |
| --- | --- |
|  |  |

| Component Name | Description |
| --- | --- |
| boot_dummy | Trunk door |
| ug_nitro | Nitro (tuning part) |
| wheel_rf_dummy | Right Front Wheel |
| wheel_lf_dummy | Left Front Wheel |
| wheel_rb_dummy | Right Back Wheel |
| wheel_lb_dummy | Left Back Wheel |
| chassis | Chassis |
| chassis_vlo | Chassis (lod)[Can't be hid] |
| ug_roof | Roof [Can't be hid] |
| door_rf_dummy | Right Front Door |
| door_lf_dummy | Left Front Door |
| door_rr_dummy | Right Back Door |
| door_lr_dummy | Left Back Door |
| bonnet_dummy | Hood |
| ug_wing_right | Right wing (tuning part) [Can't be hid] |
| bump_front_dummy | Front bumper |
| bump_rear_dummy | Back bumper |
| windscreen_dummy | Windscreen |
| misc_a | Tow bar position on models: 514, 515, 403, 591, 552, 485, 583, 606, 607, 608. |
| ug_wing_left | Leftwing (tuning part) [Can't be hid] |
| exhaust_ok | Exhausts |

## Bike Components

| [[{{{image}}}\|link=\|]] | Note: Vehicles in the 'bike' category have 8 different components from the others, so a separate table was created.. |
| --- | --- |
|  |  |

 

An illustrative image showing the components of the bike.

Many different:

| Component Name | Description |
| --- | --- |
| chassis_dummy | Vehicle chassis |
| plate_rear | Back plate |
| handlebars | Handlebars |
| mudguard | Mudguard |
| wheel_rear | Rear tire |
| wheel_front | Front Tire |
| froks_rear | Froks rear |
| froks_front | Froks front |
|  |  |

Equals:

| Component Name |
| --- |
| chassis |
| chassis_vlo |

## Component nodes

Component nodes for [spawnVehicleFlyingComponent](mta://scripting/shared/functions/spawnvehicleflyingcomponent.md) function.

### Car (Automobile) & Trailer

| Node index | Component name |  |
| --- | --- | --- |
| 1 | chassis |  |
| 2 | wheel_rf_dummy |  |
| 3 | wheel_rm_dummy |  |
| 4 | wheel_rb_dummy |  |
| 5 | wheel_lf_dummy |  |
| 6 | wheel_lm_dummy |  |
| 7 | wheel_lb_dummy |  |
| 8 | door_rf_dummy |  |
| 9 | door_rr_dummy |  |
| 10 | door_lf_dummy |  |
| 11 | door_lr_dummy |  |
| 12 | bump_front_dummy |  |
| 13 | bump_rear_dummy |  |
| 14 | wing_rf_dummy |  |
| 15 | wing_lf_dummy |  |
| 16 | bonnet_dummy |  |
| 17 | boot_dummy |  |
| 18 | windscreen_dummy |  |
| 19 | exhaust_ok |  |
| 20 | misc_a |  |
| 21 | misc_b |  |
| 22 | misc_c |  |
| 23 | misc_d |  |
| 24 | misc_e |  |

### Bike

| Node index | Component name |
| --- | --- |
| 1 | chassis |
| 2 | forks_front |
| 3 | forks_rear |
| 4 | wheel_front |
| 5 | wheel_rear |
| 6 | mudguard |
| 7 | handlebars |
| 8 | misc_a |
| 9 | misc_b |
|  |  |

### Bicycle (BMX)

| Node index | Component name |
| --- | --- |
| 1 | chassis |
| 2 | forks_front |
| 3 | forks_rear |
| 4 | wheel_front |
| 5 | wheel_rear |
| 6 | handlebars |
| 7 | chainset |
| 8 | pedal_r |
| 9 | pedal_b |
|  |  |

### Quadbike

| Node index | Component name |
| --- | --- |
| 1 | chassis |
| 2 | wheel_rf |
| 3 | wheel_rm |
| 4 | wheel_rb |
| 5 | wheel_lf |
| 6 | wheel_lm |
| 7 | wheel_lb |
| 8 | door_rf |
| 9 | door_rr |
| 10 | door_lf |
| 11 | door_lr |
| 12 | body_front |
| 13 | body_rear |
| 14 | suspension_rf |
| 15 | suspension_lf |
| 16 | rear_axle |
| 17 | handlebars |
| 18 | misc_a |
| 19 | misc_b |
|  |  |

### Monster Truck

| Node index | Component name |
| --- | --- |
| 1 | chassis |
| 2 | wheel_rf |
| 3 | wheel_rm |
| 4 | wheel_rb |
| 5 | wheel_lf |
| 6 | wheel_lm |
| 7 | wheel_lb |
| 8 | door_rf |
| 9 | door_rr |
| 10 | door_lf |
| 11 | door_lr |
| 12 | bump_front |
| 13 | bump_rear |
| 14 | wing_rf |
| 15 | wing_lf |
| 16 | bonnet |
| 17 | boot |
| 18 | windscreen |
| 19 | transmission_f |
| 20 | transmission_r |
| 21 | loadbay |
| 22 | misc_a |
|  |  |

### Boat

| [[{{{image}}}\|link=\|]] | Note: Jetmax and Tropic cannot spawn any components. |
| --- | --- |
|  |  |

| Node index | Component name |
| --- | --- |
| 1 | moving |
| 2 | windscreen |
| 3 | rudder |
| 4 | flap_left |
| 5 | flap_right |
| 6 | rearflap_left |
| 7 | rearflap_right |
| 8 | static_prop |
| 9 | moving_prop |
| 10 | static_prop2 |
| 11 | moving_prop2 |
|  |  |

### Train & Tram

| Node index | Component name |
| --- | --- |
| 1 | door_lf |
| 2 | door_rf |
| 3 | wheel_rf1 |
| 4 | wheel_rf2 |
| 5 | wheel_rf3 |
| 6 | wheel_rb1 |
| 7 | wheel_rb2 |
| 8 | wheel_rb3 |
| 9 | wheel_lf1 |
| 10 | wheel_lf2 |
| 11 | wheel_lf2 |
| 12 | wheel_lf3 |
| 13 | wheel_lb1 |
| 14 | wheel_lb2 |
| 15 | wheel_lb3 |
| 16 | bogie_front |
| 17 | bogie_rear |
|  |  |

### Plane

| Node index | Component name |
| --- | --- |
| 1 | chassis |
| 2 | wheel_rf |
| 3 | wheel_rm |
| 4 | wheel_rb |
| 5 | wheel_lf |
| 6 | wheel_lm |
| 7 | wheel_lb |
| 8 | door_rf |
| 9 | door_rr |
| 10 | door_lf |
| 11 | door_lr |
| 12 | static_prop |
| 13 | moving_prop |
| 14 | static_prop2 |
| 15 | moving_prop2 |
| 16 | rudder |
| 17 | elevator_l |
| 18 | elevator_r |
| 19 | aileron_l |
| 20 | aileron_r |
| 21 | gear_l |
| 22 | gear_r |
| 23 | misc_a |
| 23 | misc_b |
|  |  |

### Helicopter

| Node index | Component name |
| --- | --- |
| 1 | chassis |
| 2 | wheel_rf |
| 3 | wheel_rm |
| 4 | wheel_rb |
| 5 | wheel_lf |
| 6 | wheel_lm |
| 7 | wheel_lb |
| 8 | door_rf |
| 9 | door_rr |
| 10 | door_lf |
| 11 | door_lr |
| 12 | static_rotor |
| 13 | moving_rotor |
| 14 | static_rotor2 |
| 15 | moving_rotor2 |
| 16 | rudder |
| 17 | elevators |
| 18 | misc_a |
| 19 | misc_b |
| 20 | misc_c |
| 21 | misc_d |
|  |  |

## Code that shows all the components of the vehicle you are inside.

There are more components that are not yet in these tables above, and if you want to know all of them use this code below. This code works as follows: you enter / climb the vehicle and it will show you all the components as in the image above.

Click to collapse [-]
Client

```
addEventHandler ( "onClientRender", root,
function()
	countTest = 0
	if isPedInVehicle ( localPlayer ) and getPedOccupiedVehicle ( localPlayer ) then
		local veh = getPedOccupiedVehicle ( localPlayer )
		for v in pairs ( getVehicleComponents(veh) ) do
			countTest = countTest + 1
			local x,y,z = getVehicleComponentPosition ( veh, v, "world" )
			local sx,sy = getScreenFromWorldPosition ( x, y, z )
			if sx and sy then
				dxDrawRectangle(sx,sy, 10, 10)
				dxDrawLine(sx, sy, sx - (100 + (countTest * 5)), sy-(200+ (countTest * 10)))
				dxDrawText ( v, (sx-(120 + (countTest * 5))) -1, (sy-(220 + (countTest * 10))) -1, 0 -1, 0 -1, tocolor(0,0,0), 1, "default-bold" )
				dxDrawText ( v, (sx-(120 + (countTest * 5))) +1, (sy-(220 + (countTest * 10))) -1, 0 +1, 0 -1, tocolor(0,0,0), 1, "default-bold" )
				dxDrawText ( v, (sx-(120 + (countTest * 5))) -1, (sy-(220 + (countTest * 10))) +1, 0 -1, 0 +1, tocolor(0,0,0), 1, "default-bold" )
				dxDrawText ( v, (sx-(120 + (countTest * 5))) +1, (sy-(220 + (countTest * 10))) +1, 0 +1, 0 +1, tocolor(0,0,0), 1, "default-bold" )
				dxDrawText ( v, (sx-(120 + (countTest * 5))), (sy-(220 + (countTest * 10))), 0, 0, tocolor(0,255,255), 1, "default-bold" )
			end
		end
	end
end)
```

## Related scripting functions

- [setVehicleComponentVisible](mta://scripting/client/functions/setvehiclecomponentvisible.md)

- [setVehicleComponentPosition](mta://scripting/client/functions/setvehiclecomponentposition.md)

- [setVehicleComponentRotation](mta://scripting/client/functions/setvehiclecomponentrotation.md)

- [setVehicleComponentScale](mta://scripting/client/functions/setvehiclecomponentscale.md)

- [resetVehicleComponentPosition](mta://scripting/client/functions/resetvehiclecomponentposition.md)

- [resetVehicleComponentRotation](mta://scripting/client/functions/resetvehiclecomponentrotation.md)

- [resetVehicleComponentScale](mta://scripting/client/functions/resetvehiclecomponentscale.md)

- [getVehicleComponents](mta://scripting/client/functions/getvehiclecomponents.md)

- [getVehicleComponentVisible](mta://scripting/client/functions/getvehiclecomponentvisible.md)

- [getVehicleComponentScale](mta://scripting/client/functions/getvehiclecomponentscale.md)

- [getVehicleComponentRotation](mta://scripting/client/functions/getvehiclecomponentrotation.md)

- [getVehicleComponentPosition](mta://scripting/client/functions/getvehiclecomponentposition.md)

- [spawnVehicleFlyingComponent](mta://scripting/shared/functions/spawnvehicleflyingcomponent.md)

## See Also

- [Vehicle](mta://reference/misc/vehicle.md)

- [Vehicle IDs](mta://reference/misc/vehicle-ids.md)

- [Vehicle functions](https://wiki.multitheftauto.com/wiki/Template:Vehicle_functions)

- [ID Lists](mta://reference/misc/id--474ae526.md)
