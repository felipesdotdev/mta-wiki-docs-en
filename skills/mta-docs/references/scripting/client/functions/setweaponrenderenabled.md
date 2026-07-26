---
doc_id: "mta-wiki:14517"
title: "SetWeaponRenderEnabled"
source_title: "SetWeaponRenderEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/SetWeaponRenderEnabled"
revision_id: 81691
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
---

# SetWeaponRenderEnabled

ADDED/UPDATED IN VERSION 1.6.0 [r22880](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22880):

This function allows you to completely disable/enable GTA weapon rendering for [ped](https://wiki.multitheftauto.com/index.php?search=ped) and [player](https://wiki.multitheftauto.com/index.php?search=player). It is particularly useful for creating custom weapon systems, where singular weapon ID could have many different models/variations, or to simply get rid of one frame delay when switching weapons. 

| [[{{{image}}}\|link=\|]] | Note: If you want to selectively hide weapons use engineSetModelLODDistance with weapon model ID and value of 0.001 . Do note that game will still process default rendering regardless, which isn't the case when using this function to hide weapon models. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: You can use it for example with optimized bone_attach resource called pAttach . |
| --- | --- |
|  |  |

## Syntax

```
bool setWeaponRenderEnabled ( bool enabled )
```

### Required Arguments

- **enabled:** Whether weapon render should be enabled.

### Returns

Always returns **true**.

## Example

This example disables weapon rendering once resource has started.

```
function onClientResourceStartDisableWeaponRender()
	setWeaponRenderEnabled(false)
end
addEventHandler("onClientResourceStart", resourceRoot, onClientResourceStartDisableWeaponRender)
```

## See Also

ADDED/UPDATED IN VERSION 1.6.0 [r22880](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22880):

- setWeaponRenderEnabled

- [isWeaponRenderEnabled](mta://scripting/client/functions/isweaponrenderenabled.md)

- **Shared**

- [getWeaponProperty](mta://scripting/shared/functions/getweaponproperty.md)

- [getOriginalWeaponProperty](mta://scripting/shared/functions/getoriginalweaponproperty.md)

- [getSlotFromWeapon](mta://scripting/shared/functions/getslotfromweapon.md)

- [getWeaponIDFromName](mta://scripting/shared/functions/getweaponidfromname.md)

- [getWeaponNameFromID](mta://scripting/shared/functions/getweaponnamefromid.md)

- [setWeaponAmmo](mta://scripting/shared/functions/setweaponammo.md)

- [setWeaponProperty](mta://scripting/shared/functions/setweaponproperty.md)
