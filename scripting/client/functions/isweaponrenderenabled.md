---
doc_id: "mta-wiki:14518"
title: "IsWeaponRenderEnabled"
source_title: "IsWeaponRenderEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsWeaponRenderEnabled"
revision_id: 81651
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:16:03.489695+00:00"
---

# IsWeaponRenderEnabled

ADDED/UPDATED IN VERSION 1.6.0 [r22880](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22880):

This function checks whether GTA weapon rendering is enabled for [ped](mta://reference/misc/ped.md) and [player](mta://reference/misc/player.md). 

## Syntax

```
bool isWeaponRenderEnabled ( )
```

### Returns

Returns **true** if weapon rendering is enabled, otherwise returns **false**.

## Example

This example allows you to disable/enable weapon rendering by using **/weaponrender** command.

```
function toggleWeaponRender()
	local weaponRenderEnabled = isWeaponRenderEnabled()
	local weaponRenderNewState = (not weaponRenderEnabled)

	setWeaponRenderEnabled(weaponRenderNewState)
end
addCommandHandler("weaponrender", toggleWeaponRender)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22880](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22880):

- [setWeaponRenderEnabled](mta://scripting/client/functions/setweaponrenderenabled.md)

- isWeaponRenderEnabled

- **Shared**

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)
