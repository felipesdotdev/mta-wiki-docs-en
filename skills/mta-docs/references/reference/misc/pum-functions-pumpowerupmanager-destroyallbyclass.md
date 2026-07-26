---
doc_id: "mta-wiki:3266"
title: "Pum/Functions/pumPowerupManager DestroyAllByClass"
source_title: "Pum/Functions/pumPowerupManager DestroyAllByClass"
source_url: "https://wiki.multitheftauto.com/wiki/Pum/Functions/pumPowerupManager_DestroyAllByClass"
revision_id: 29130
language: "en"
categories: ["Outdated_Pages"]
---

# Pum/Functions/pumPowerupManager DestroyAllByClass

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
|  |  |

This function destroys all created powerups of a certain type (class).

## Syntax

Click to collapse [-]
Server

```
void pumPowerupManager_DestroyAllByClass( string powerup_class )
```

### Required Arguments

- **powerup_class**: The name of the powerup class to destroy

## Example

Click to collapse [-]
Server

This example destroys all created powerups named "healthbonus"

```
pumPowerupManager_DestroyAllByClass(healthbonus)
```

## See Also

### PowerupManager functions

- [pumPowerupManager_DestroyAll](mta://reference/misc/pum-functions-pumpowerupmanager-destroyall.md)

- pumPowerupManager_DestroyAllByClass

### Powerup functions

- [pumPowerup_Create](mta://reference/misc/pum-functions-pumpowerup-create.md)

- [pumPowerup_Destroy](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_Destroy&action=edit&redlink=1)

- [pumPowerup_SetCollision](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_SetCollision&action=edit&redlink=1)

- [pumPowerup_GetCollision](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_GetCollision&action=edit&redlink=1)

- [pumPowerup_SetAnimation](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_SetAnimation&action=edit&redlink=1)

- [pumPowerup_GetAnimation](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_GetAnimation&action=edit&redlink=1)

- [pumPowerup_SetPosition](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_SetPosition&action=edit&redlink=1)

- [pumPowerup_GetPosition](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_GetPosition&action=edit&redlink=1)

- [pumPowerup_SetObjectID](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_SetObjectID&action=edit&redlink=1)

- [pumPowerup_GetObject](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_GetObject&action=edit&redlink=1)

- [pumPowerup_GetObjectID](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerup_GetObjectID&action=edit&redlink=1)

### PowerupHelper functions

- [pumPowerupHelper_GetObjectBoundingBox](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerupHelper_GetObjectBoundingBox&action=edit&redlink=1)

- [pumPowerupHelper_GetObjectID](https://wiki.multitheftauto.com/index.php?title=Pum/Functions/pumPowerupHelper_GetObjectID&action=edit&redlink=1)
