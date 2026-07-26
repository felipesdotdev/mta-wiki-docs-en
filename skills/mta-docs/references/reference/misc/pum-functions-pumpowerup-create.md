---
doc_id: "mta-wiki:3267"
title: "Pum/Functions/pumPowerup Create"
source_title: "Pum/Functions/pumPowerup Create"
source_url: "https://wiki.multitheftauto.com/wiki/Pum/Functions/pumPowerup_Create"
revision_id: 29128
language: "en"
categories: ["Outdated_Pages"]
---

# Pum/Functions/pumPowerup Create

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
|  |  |

This function creates and spawns a new powerup.

If the powerup is created, it triggers the public event, pumEvent_PowerupCreated on both the client and server.

## Syntax

Click to collapse [-]
Server

```
mixed pumPowerup Create( int object_id, string powerup_class, float x, float y, float z, int respawnTime, int animation_mode, [mixed extra_data] )
```

### Required Arguments

- **object_id,**: The name of the powerup class to destroy

- **powerup_class**: The internal name for the newly created powerup

- **x**: The X position of the powerup

- **y**: The Y position of the powerup

- **z**: The Z position of the powerup

- **respawnTime**: Time in ms to respawn (when making use of this feature)

- **animation_mode**: 0 = Static, 1 = Spinning

### Optional Arguments

- **extra_data**: Optional data to link to this this powerup

## Example

Click to collapse [-]
Server

-todo description-

```
- todo example -
```

## See Also

### PowerupManager functions

- [pumPowerupManager_DestroyAll](mta://reference/misc/pum-functions-pumpowerupmanager-destroyall.md)

- [pumPowerupManager_DestroyAllByClass](mta://reference/misc/pum-functions-pumpowerupmanager-destroyallbyclass.md)

### Powerup functions

- pumPowerup_Create

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
