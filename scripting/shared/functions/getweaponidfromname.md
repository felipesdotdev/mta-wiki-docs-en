---
doc_id: "mta-wiki:1607"
title: "GetWeaponIDFromName"
source_title: "GetWeaponIDFromName"
source_url: "https://wiki.multitheftauto.com/wiki/GetWeaponIDFromName"
revision_id: 51075
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:30.085762+00:00"
---

# GetWeaponIDFromName

This function will obtain the ID of a particular weapon from its name.

## Syntax

```
int getWeaponIDFromName ( string name )
```

### Required Arguments

- **name:** A [string](mta://reference/misc/string.md) containing the name of the weapon. Names can be: (Case is ignored)

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

### Returns

Returns an [int](mta://reference/misc/int.md) if the name matches that of a weapon, *false* otherwise.

## Example

Click to collapse [-]
Server

This example will give the player the weapon they specify 20 ammo whenever they type "weapon *name*" into the console.

```
-- Define our function that will handle this command
function consoleGiveWeapon ( playerSource, commandName, weapName )
	-- If a player triggered it (rather than the admin) then
	if ( playerSource ) then
		-- Get the weapon ID from the name
		local weapID = getWeaponIDFromName ( weapName )
		-- If it's a valid weapon
		if ( weapID ) then
		 	-- Give the weapon to the player
			giveWeapon ( playerSource, weapID, 20 )
			-- Output it in the chat box
			outputChatBox ( "You got a " .. weapName, playerSource )
		else outputChatBox ( "Invalid weapon name." )
		end
	end
end
-- Register the command handler and attach it to the 'consoleGiveWeapon' function
addCommandHandler ( "weapon", consoleGiveWeapon )
```

## See Also

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- getWeaponIDFromName

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)
