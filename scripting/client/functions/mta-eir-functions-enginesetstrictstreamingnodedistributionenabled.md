---
doc_id: "mta-wiki:7371"
title: "MTA:Eir/functions/engineSetStrictStreamingNodeDistributionEnabled"
source_title: "MTA:Eir/functions/engineSetStrictStreamingNodeDistributionEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineSetStrictStreamingNodeDistributionEnabled"
revision_id: 77710
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.465021+00:00"
---

# MTA:Eir/functions/engineSetStrictStreamingNodeDistributionEnabled

This function changes the streaming node allocation behavior of GTA:SA entities. It is only valid in conjunction with [engineSetInfiniteStreamingEnabled](mta://scripting/client/functions/mta-eir-functions-enginesetinfinitestreamingenabled.md). If strict streaming node distribution is enabled, entities first allocate from existing nodes. If disabled, entities are allowed to allocate new streaming nodes from the heap without touching existing nodes.

By default, strict node distribution is enabled.

## Syntax

```
bool engineSetStrictStreamingNodeDistributionEnabled ( bool enabled )
```

### Arguments

- **enabled:** switch to set strict node distribution on or off

### Returns

Returns *true* if enabled is passed as valid bool, *false* otherwise.

## Example

Click to collapse [-]
Client

This snippet ultimatively fixes the world flickering.

```
engineSetStrictStreamingNodeDistributionEnabled( false );
engineSetInfiniteStreamingEnabled( true );
```
