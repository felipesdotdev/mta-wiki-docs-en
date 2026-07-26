---
doc_id: "mta-wiki:2623"
title: "GetSlotFromWeapon"
source_title: "GetSlotFromWeapon"
source_url: "https://wiki.multitheftauto.com/wiki/GetSlotFromWeapon"
revision_id: 22273
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:25.208607+00:00"
---

# GetSlotFromWeapon

This function allows you to identify the weapon slot that a weapon belongs to.

## Syntax

```
int getSlotFromWeapon ( int weaponid )
```

### Required Arguments

- **weaponid:** [Weapon](mta://reference/misc/weapon.md) to find the weapon slot of.

### Returns

Returns an integer representing the given weapon ID's associated weapon slot, *false* if the ID was invalid.

## Example

This will output to the chatbox what weapon slot a given weapon number belongs to when entered into the console (i.e. 'getWeaponSlot 10').

```
function outputWeaponSlot ( source, commandName, weaponID )
	local weaponSlot = getSlotFromWeapon ( weaponID )
	
	if (weaponSlot) then
	    outputChatBox ( "Weapon ID " .. weaponID ..  " is in weapon slot " .. weaponSlot)
	else
	    outputChatBox ( "Invalid weapon ID" )
	end
end
addCommandHandler ( "getWeaponSlot", outputWeaponSlot )
```

## See Also

[Weapon IDs](mta://reference/misc/weapons.md)

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- getSlotFromWeapon

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)
