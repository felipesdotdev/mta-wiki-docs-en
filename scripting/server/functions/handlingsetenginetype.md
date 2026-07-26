---
doc_id: "mta-wiki:3936"
title: "HandlingSetEngineType"
source_title: "HandlingSetEngineType"
source_url: "https://wiki.multitheftauto.com/wiki/HandlingSetEngineType"
revision_id: 80950
language: "en"
categories: ["Server_functions", "Disabled_Functions_and_Events", "MTA_Wiki:Delete", "Deprecated", "Archived"]
generated_at: "2026-07-26T16:15:42.723726+00:00"
---

# HandlingSetEngineType

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Function has been removed Actions: Delete (Administrators) - Discuss - What links here - Category |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setVehicleHandling instead. |  |

Sets the engine type of a handling element (or more specifically, what kind of fuel it uses).

## Syntax

```
bool handlingSetEngineType ( handling theHandling, string engineType )
```

### Required Arguments

- **theHandling:** the handling of which you want to change the engine type.

- **engineType:** one of the following strings:

- **diesel**

- **electric**

- **petrol**

### Returns

Returns *true* on success, *false* in case of failure.

## Example

```
--TODO
```

## See Also
