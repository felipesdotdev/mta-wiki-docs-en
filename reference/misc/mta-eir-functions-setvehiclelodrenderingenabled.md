---
doc_id: "mta-wiki:7392"
title: "MTA:Eir/functions/setVehicleLODRenderingEnabled"
source_title: "MTA:Eir/functions/setVehicleLODRenderingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/setVehicleLODRenderingEnabled"
revision_id: 37870
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.646216+00:00"
---

# MTA:Eir/functions/setVehicleLODRenderingEnabled

This function switches the vehicle LOD rendering on or off. If vehicle LOD rendering is disabled, only the high quality version of the vehicle is allowed to render. Otherwise the low quality version of the vehicle will render after a specific distance (depending on vehicle type). This setting can be overridden by the users settings.

## Syntax

```
bool setVehicleLODRenderingEnabled ( bool enabled )
```

### Arguments

- **enabled:** a boolean deciding whether vehicle LOD rendering should be favorized or not

### Returns

Returns **true** if enabled is passed as valid boolean, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet usually forces high quality rendering of the in-game vehicles.

```
setVehicleLODRenderingEnabled( false );
```
