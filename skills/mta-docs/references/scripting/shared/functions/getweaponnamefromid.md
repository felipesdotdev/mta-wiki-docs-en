---
doc_id: "mta-wiki:1606"
title: "GetWeaponNameFromID"
source_title: "GetWeaponNameFromID"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponNameFromID"
revision_id: 73885
language: "en"
categories: ["Server_functions", "Client_functions", "Functions_and_events_with_issues"]
---

# GetWeaponNameFromID

This function allows you to retrieve the name of a weapon from an ID.

| [[{{{image}}}\|link=\|]] | Note: You can also retrieve the name of other methods of death, such as Fall and Rammed. |
| --- | --- |
|  |  |

## Syntax

```
string getWeaponNameFromID ( int id )
```

### Required Arguments

- **id:** The ID you wish to retrieve the name of

### Returns

Returns a string of the name of the weapon or death type, *false* otherwise. Names will be like these: (Ignoring case)

- brassknuckle

- golfclub

- nightstick

- knife

- bat

- shovel

- poolstick

- katana

- chainsaw

- dildo

- vibrator

- flower

- cane

- grenade

- teargas

- molotov

- colt 45

- silenced

- deagle

- shotgun

- sawed-off

- combat shotgun

- uzi

- mp5

- ak-47

- m4

- tec-9

- rifle

- sniper

- rocket launcher

- rocket launcher hs

- flamethrower

- minigun

- satchel

- bomb

- spraycan

- fire extinguisher

- camera

- nightvision

- infrared

- parachute

## Example

Click to collapse [-]
Server

This example displays a death message in the format of "* *Killer* killed *dead* (*Weapon*)"

```
function scriptOnPlayerWasted ( totalammo, killer, killerweapon, bodypart ) --when a player dies
	local causeOfDeath = getWeaponNameFromID ( killerweapon ) --get the name of 'killerweapon' and define it as 'causeOfDeath'
	local killedPerson = getPlayerName ( source ) --get the name of the player who died and define it as 'killedPerson'
	if ( killer ) then --if there was a killer
	local killerPerson = getPlayerName ( killer ) --get the name of the killer and define it as 'killerPerson'
		if ( killer == source ) then --if the killer is the same as the person who died i.e. he killed himself
			outputChatBox ( "* "..killerPerson.." died ("..causeOfDeath..")", root, 255, 100, 100 ) --output in the chatbox that  he died and the method he died in the brackets
		else --if the killer is not the same as the person who died
			outputChatBox ( "* "..killerPerson.." killed "..killedPerson.." ("..causeOfDeath..")", root, 255, 100, 100 ) --output in the chatbox that he was killed by the killer and the method in brackets
		end
	else --if there was no killer
		outputChatBox ( "* "..killedPerson .. " died (" ..causeOfDeath..")", root, 255, 100, 100 ) --output in the chatbox that the person died and how he died
	end
end
addEventHandler ( "onPlayerWasted", root, scriptOnPlayerWasted ) --add an event handler for onPlayerWasted
```

## Issues

| Issue ID | Description |
| --- | --- |
| #514 | getWeaponNameFromID() returns duplicate ID's for 10/11 and 12/13 |

## See Also

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- getWeaponNameFromID

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)
