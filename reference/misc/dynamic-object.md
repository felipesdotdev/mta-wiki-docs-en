---
doc_id: "mta-wiki:7610"
title: "Dynamic object"
source_title: "Dynamic object"
source_url: "https://wiki.multitheftauto.com/wiki/Dynamic_object"
revision_id: 43574
language: "en"
categories: []
generated_at: "2026-07-26T16:14:51.954296+00:00"
---

# Dynamic object

| [[{{{image}}}\|link=\|]] | Note: This page is under construction. |
| --- | --- |
|  |  |

There should be description.

## Behaviour

- If object has originally 99999.0 Mass or TurnMass you can't move them like other dynamic objects (ex. beachball). Changing this property using [setObjectMass](mta://scripting/client/functions/setobjectmass.md) doesn't change this effect.

- Some dynamic objects (propably only weapon models, ex. ID 355) doesn't have collision until GTA create [projectile](mta://reference/misc/element-projectile.md).

## List

| Property | Description |
| --- | --- |
| Mass | weight of the object (kilograms 1 to 50000) |
| TurnMass | kg m^3 or some such dimension |
| Air Resistance | scale 0 (total resistance) to 1 (zero resistance) |
| Elasticity | scale 0 (no bounce) to 1 (full bounce) or more) |
| Percent Submerged | percentage 10 to 120 |
| Uproot Limit | force magnitude required to uproot |
| CDMult | Collision Damage Multiplier (0.1 - 5.0 ish) |
| CDEff | Collision Damage Effect |
| SpCDR | Special Collision Response Cases |
| CamAv | Camera to avoid this object (0) for no (1) for yes |
| Expl | Causes Explosion or not |
| FX_TYPE | 0 - no FxSystem, 1 - play when hit, 2 - play when destroyed, 3 - play when hit or destroyed |
| FX_OFFSET | offset from the pivot of the object (set x value to -999.0 to play at the point of collision) |
| FX_NAME | needs to be "none" if FX_TYPE is 0, otherwise must be the name of a valid effect |
| B-SM | Smash Multiplier |
| B-VX | Break Velocity X - velocity of breakable parts |
| B-VY | Break Velocity Y |
| B-VZ | Break Velocity Z |
| B-VR | Break Velocity Rand - velocity randomness factor |
| B-GUN | Gun Break Mode (0 - not breakable by gun, 1 - breakable, 2 - smashable) |
| G_SPK | Produce Sparks on Impact (0 - no sparks, 1 - sparks produced) |

Special collision response cases

| ID | Description |
| --- | --- |
| 0 | none (default) |
| 1 | lamppost |
| 2 | smallbox |
| 3 | bigbox |
| 4 | fencepart (used for gates & garage doors) |
| 5 | grenade |
| 6 | door (used for moving interiors doors) |
| 7 | lock door (static door used for EnEx?) |
| 8 | hanging (object is attached to some point, like punching bag) |
| 9 | pool ball |

| ID | Name | Mass | TurnMass | AirResistance | Elasticity | PercSubmerged | Uproot | CDMult | CDEff | SpCDR | CamAv | Expl | FX_TYPE | FX_OFFSET | FX_NAME | B-SM | B-VX | B-VY | B-VZ | B-VR | B-GUN | B_SPK |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | cardboardbox2 | 20.0 | 20.0 | 0.99 | 0.03 | 50.0 | 0.0 | 2.5 | 20 | 2 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_crate |  |  |  |  |  |  |  |
|  | cardboardbox4 | 20.0 | 20.0 | 0.99 | 0.03 | 50.0 | 0.0 | 2.5 | 20 | 2 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_crate |  |  |  |  |  |  |  |
|  | cardboardbox | 10.0 | 10.0 | 0.99 | 0.03 | 50.0 | 0.0 | 2.5 | 20 | 2 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_crate |  |  |  |  |  |  |  |
|  | cm_box | 10.0 | 10.0 | 0.99 | 0.03 | 50.0 | 0.0 | 2.5 | 20 | 2 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_crate |  |  |  |  |  |  |  |
|  | temp_cardbox | 10.0 | 10.0 | 0.99 | 0.03 | 50.0 | 0.0 | 2.5 | 20 | 2 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_crate |  |  |  |  |  |  |  |
|  | pizzabox | 10.0 | 10.0 | 1.00 | 0.03 | 50.0 | 0.0 | 2.0 | 20 | 2 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_crate |  |  |  |  |  |  |  |
|  | tar_gun1 | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | tar_gun2 | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | kb_beer | 30.0 | 30.0 | 0.99 | 0.03 | 50.0 | 0.0 | 1.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | kb_beer01 | 30.0 | 30.0 | 0.99 | 0.03 | 50.0 | 0.0 | 1.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | record1 | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | record2 | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | record3 | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | e_test | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | w_test | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | cutscene_beer | 99999.0 | 99999.0 | 0.99 | 0.1 | 50.0 | 0.0 | 5.0 | 20 | 0 | 1 | 0 | 2 | 0.0 | 0.0 | 0.0 | explosion_door |  |  |  |  |  |  |  |
|  | dyn_wine_break | 50.0 | 150.0 | 0.99 | 0.0 | 50.0 | 350.0 | 5.0 | 200 | 0 | 1 | 0 | 0 | 0.0 | 0.0 | 0.0 | none | 1.0 | 0.0 | 0.0 | 0.1 | 0.07 | 2 | 0 |
|  | dyn_wine_BOUNCE | 50.0 | 150.0 | 0.99 | 0.0 | 50.0 | 350.0 | 5.0 | 200 | 0 | 1 | 0 | 0 | 0.0 | 0.0 | 0.0 | none | 1.0 | 0.0 | 0.0 | 0.1 | 0.07 | 2 | 0 |
|  | CJ_B_OPTIC1 | 50.0 | 150.0 | 0.99 | 0.0 | 50.0 | 350.0 | 5.0 | 200 | 0 | 1 | 0 | 0 | 0.0 | 0.0 | 0.0 | none | 1.0 | 0.0 | 0.0 | 0.1 | 0.07 | 2 | 0 |

## Related functions

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

- [onClientObjectBreak](mta://scripting/client/events/onclientobjectbreak.md)

- [onClientObjectDamage](mta://scripting/client/events/onclientobjectdamage.md)

- [onClientObjectMoveStart](mta://scripting/client/events/onclientobjectmovestart.md)

- [onClientObjectMoveStop](mta://scripting/client/events/onclientobjectmovestop.md)
