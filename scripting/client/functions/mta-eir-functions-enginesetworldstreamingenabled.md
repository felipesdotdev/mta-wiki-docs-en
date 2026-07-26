---
doc_id: "mta-wiki:7378"
title: "MTA:Eir/functions/engineSetWorldStreamingEnabled"
source_title: "MTA:Eir/functions/engineSetWorldStreamingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineSetWorldStreamingEnabled"
revision_id: 77716
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.479752+00:00"
---

# MTA:Eir/functions/engineSetWorldStreamingEnabled

This function enables or disables the rendering and streaming of world instances. World instances are IPL sectors, COL sectors, buildings, objects and dummies. This function does not affect world instances created by MTA.

## Syntax

```
bool engineSetWorldStreamingEnabled ( bool enabled )
```

### Returns

Returns **true** if enabled is passed as valid bool, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet clears the entire GTA:SA world of native entities and increases engine performance.

```
addEvent( "onClientGameEnterTCMode", true );
addEventHandler( "onClientGameEnterTCMode", root,
    function()
        engineSetWorldStreamingEnabled( false );
    end
);
```
