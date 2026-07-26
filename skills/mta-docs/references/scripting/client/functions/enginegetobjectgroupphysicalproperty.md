---
doc_id: "mta-wiki:11890"
title: "EngineGetObjectGroupPhysicalProperty"
source_title: "EngineGetObjectGroupPhysicalProperty"
source_url: "https://wiki.multitheftauto.com/wiki/EngineGetObjectGroupPhysicalProperty"
revision_id: 64803
language: "en"
categories: ["Client_functions", "Changes_in_1.5.7"]
---

# EngineGetObjectGroupPhysicalProperty

This function gets physical property of given properties group.

## Syntax

```
var engineGetObjectGroupPhysicalProperty ( int groupID, objectgroup-modifiable property )
```

### Required Arguments

- **groupID**: the id of physical properties group which you wish to get a property from.

- **objectgroup-modifiable**: the property which you wish to get, as per table below.

### Returns

Returns the value contained in given property if everything went well, error is raised otherwise.

### Properties

### Physical properties

| Property | Type | Description |
| --- | --- | --- |
| mass | float | Mass of an object |
| turn_mass | float | Turn mass (kg m^3) of an object |
| air_resistance | float | Air resistance of an object |
| elasticity | float | Elasticity of an object |
| buoyancy | float | Buoyancy of an object |
| uproot_limit | float | How much force is needed to uproot the object |
| col_damage_multiplier | float | Force multiplier used when colliding with object |
| col_damage_effect | DamageEffect | Dictates which damage effect is applied to object on collision |
| special_col_response | CollisionResponse | Dictates how object responds to being collided with |
| avoid_camera | bool | Dictates whether camera passes throught the object |
| cause_explosion | bool | Dictates whether objects exploded upon collision |
| fx_type | FxType | Dictates when particles will be created when colliding with object |
| fx_offset | Vector3D | Offset from center of mass where particles will be created upon collision |
| fx_system | FxEffect(string) | Effect that will be used upon collision |
| smash_multiplier | float | Force multiplier when destroying object |
| break_velocity | Vector3D | Velocity and direction in which the object is destroyed |
| break_velocity_randomness | float | Randomness of velocity and direction in which the object is destroyed, 0 means that object uses break_velocity without any randomness |
| break_mode | BreakMode | Dictates how object can be damaged |
| sparks_on_impact | bool | Dictates whether object creates sparks upon impact |

### Damage effect

| Effect | Description |
| --- | --- |
| none | Object doesn't change at all once it's damaged |
| change_model | Some of the objects change model on collision, those use this |
| smash | Object is smashed |
| change_smash | First CHANGE_MODEL, afterwards smash on collision |
| breakable | Object is breakable normally |
| breakable_remove | object.dat says: '(ie. never regenerated after destroyed)' |

### Collision Response

| Response | Description |
| --- | --- |
| none | Object doesn't respond in any special way |
| lamppost | Objects acts like an lamp post |
| small_box | - |
| big_box | - |
| fence_part | - |
| grenade | - |
| swingdoor | - |
| lockdoor | - |
| hanging | - |
| poolball | - |

### Fx Type

| Type | Description |
| --- | --- |
| none | No particles effect played on collision |
| play_on_hit | Particles effect is played on collision, even if object isn't destroyed |
| play_on_destroyed | Particles effect is played only once object is destroyed |
| play_on_hitdestroyed | Particles effect is played both when hit and destroyed |

### Break Mode

| Mode | Description |
| --- | --- |
| not_by_gun | not breakable by gun |
| by_gun | - |
| smashable | - |

### Fx Effect

| effect | Description |
| --- | --- |
| wallbust | - |
| shootlight | - |
| puke | Puke effect |
| explosion_door | - |
| explosion_crate | Crate break |
| explosion_barrel | Barrel explosion |
| blood_heli | Heli cutting peds |
| tree_hit_palm | - |
| tree_hit_fir | - |
| water_swim | Water ripples |
| water_splsh_sml | - |
| water_splash_big | - |
| water_splash | - |
| water_hydrant | - |
| tank_fire | - |
| riot_smoke | - |
| gunsmoke | Gun smoke when firing |
| gunflash | Gun flash when firing |
| explosion_tiny | - |
| explosion_small | - |
| explosion_molotov | Molotov explosion |
| explosion_medium | - |
| explosion_large | - |
| explosion_fuel_car | - |
| exhale | - |
| camflash | Camera photo flash |
| prt_wake | Wake on water behind boats |

## Example

Click to collapse [-]
Client

```
function getProperty(_, group, property)
    var prop = {engineGetObjectGroupPhysicalProperty(tonumber(group), property)}
    outputConsole(inspect(prop))
end
addCommandHandler ( "getProperty", getProperty )
--getProperty(120, "special_col_response")
```

## See Also

- [createObject](mta://scripting/shared/functions/createobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22489](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22489):

- [breakObject](mta://scripting/shared/functions/breakobject.md)

- [getObjectScale](mta://scripting/shared/functions/getobjectscale.md)

- [moveObject](mta://scripting/shared/functions/moveobject.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22708](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22708):

- [respawnObject](mta://scripting/shared/functions/respawnobject.md)

- [toggleObjectRespawn](mta://scripting/shared/functions/toggleobjectrespawn.md)

- [isObjectRespawnable](mta://scripting/shared/functions/isobjectrespawnable.md)

- [setObjectScale](mta://scripting/shared/functions/setobjectscale.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22430](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22430):

- [isObjectMoving](mta://scripting/shared/functions/isobjectmoving.md)

ADDED/UPDATED IN VERSION 1.6.0 [r21765](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=21765):

- [isObjectBreakable](mta://scripting/shared/functions/isobjectbreakable.md)

- [setObjectBreakable](mta://scripting/shared/functions/setobjectbreakable.md)

- [stopObject](mta://scripting/shared/functions/stopobject.md)

- [getObjectMass](mta://scripting/client/functions/getobjectmass.md)

- [getObjectProperty](mta://scripting/client/functions/getobjectproperty.md)

- [setObjectMass](mta://scripting/client/functions/setobjectmass.md)

- [setObjectProperty](mta://scripting/client/functions/setobjectproperty.md)
