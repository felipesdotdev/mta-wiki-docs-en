---
doc_id: "mta-wiki:3268"
title: "PowerupManager"
source_title: "PowerupManager"
source_url: "https://wiki.multitheftauto.com/wiki/PowerupManager"
revision_id: 35982
language: "en"
categories: ["Outdated_Pages"]
generated_at: "2026-07-26T16:16:29.633539+00:00"
---

# PowerupManager

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
|  |  |

The powerupManager library was created to ease the use of advanced, more custom pickups (powerups).

It exists out of server and client scripts to create, handle and destroy custom powerup items.

Advanced features contain: custom clientside animations (spin, up-down), custom collision element for triggering, server side triggering (to prevent cheating), change powerup object on the fly (for example triggering such a powerup gives a random advantage based on current modelID), ...

Also since it allows you to set a custom colShape, you can use it to create tripmines, ...

# Used by

# Exported scripting functions

## Server

- [createPowerup](https://wiki.multitheftauto.com/index.php?title=PowerupManager/createPowerup&action=edit&redlink=1)

- [destroyPowerup](https://wiki.multitheftauto.com/index.php?title=PowerupManager/destroyPowerup&action=edit&redlink=1)

- [destroyAllPowerups](https://wiki.multitheftauto.com/index.php?title=PowerupManager/destroyAllPowerups&action=edit&redlink=1)

- [setPowerupDimension](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupDimension&action=edit&redlink=1)

- [getPowerupDimension](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupDimension&action=edit&redlink=1)

- [setPowerupAnimation](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupAnimation&action=edit&redlink=1)

- [getPowerupAnimation](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupAnimation&action=edit&redlink=1)

- [setPowerupCanRespawn](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupCanRespawn&action=edit&redlink=1)

- [getPowerupCanRespawn](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupCanRespawn&action=edit&redlink=1)

- [setPowerupRespawnTime](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupRespawnTime&action=edit&redlink=1)

- [getPowerupRespawnTime](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupRespawnTime&action=edit&redlink=1)

- [getPowerupObject](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupObject&action=edit&redlink=1)

- [setPowerupObject](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupObject&action=edit&redlink=1)

- [setPowerupModelID](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupModelID&action=edit&redlink=1)

- [getPowerupModelID](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupModelID&action=edit&redlink=1)

- [setPowerupColShape](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupColShape&action=edit&redlink=1)

- [getPowerupColShape](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupColShape&action=edit&redlink=1)

- [setPowerupTemporaryTime](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupTemporaryTime&action=edit&redlink=1)

- [getPowerupTemporaryTime](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupTemporaryTime&action=edit&redlink=1)

- [setPowerupIsTemporary](https://wiki.multitheftauto.com/index.php?title=PowerupManager/setPowerupIsTemporary&action=edit&redlink=1)

- [getPowerupIsTemporary](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupIsTemporary&action=edit&redlink=1)

## Client

- [getPowerupDimension](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupDimension&action=edit&redlink=1)

- [getPowerupAnimation](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupAnimation&action=edit&redlink=1)

- [getPowerupCanRespawn](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupCanRespawn&action=edit&redlink=1)

- [getPowerupRespawnTime](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupRespawnTime&action=edit&redlink=1)

- [getPowerupObject](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupObject&action=edit&redlink=1)

- [getPowerupModelID](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupModelID&action=edit&redlink=1)

- [getPowerupColShape](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupColShape&action=edit&redlink=1)

- [getPowerupTemporaryTime](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupTemporaryTime&action=edit&redlink=1)

- [getPowerupIsTemporary](https://wiki.multitheftauto.com/index.php?title=PowerupManager/getPowerupIsTemporary&action=edit&redlink=1)

# Events

Events prefixed with pum are ceated for internal usage only. You still can hook them, but we suggest you don't.

## Server

- [onPowerupPickup](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/onPowerupPickup&action=edit&redlink=1)

- [onPowerupSpawn](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/onPowerupSpawn&action=edit&redlink=1)

- [onPowerupDestroy](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/onPowerupDestroy&action=edit&redlink=1)

- [pumOnGotObjectBoundingBox](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/pumOnGotObjectBoundingBox&action=edit&redlink=1)

## Client

- [onPowerupPickup](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/onPowerupPickup&action=edit&redlink=1)

- [onPowerupSpawn](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/onPowerupSpawn&action=edit&redlink=1)

- [pumOnGetObjectBoundingBox](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/pumOnGetObjectBoundingBox&action=edit&redlink=1)

- [pumOnSetCollisionsEnabled](https://wiki.multitheftauto.com/index.php?title=PowerupManager/Events/pumOnSetCollisionsEnabled&action=edit&redlink=1)
