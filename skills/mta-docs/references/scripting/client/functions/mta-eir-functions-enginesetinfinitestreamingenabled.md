---
doc_id: "mta-wiki:7373"
title: "MTA:Eir/functions/engineSetInfiniteStreamingEnabled"
source_title: "MTA:Eir/functions/engineSetInfiniteStreamingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineSetInfiniteStreamingEnabled"
revision_id: 77712
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineSetInfiniteStreamingEnabled

This function enables or disables heap allocation of [streaming garbage collector](mta://reference/misc/gta-sa-streaming-garbage-collection.md) nodes. The allocation behavior order is changed using [engineSetStrictStreamingNodeDistributionEnabled](mta://scripting/client/functions/mta-eir-functions-enginesetstrictstreamingnodedistributionenabled.md). If enabled, GTA:SA can keep an theoretically infinite amount of entities inside of the streaming garbage collector. This also means that an theoretically infinite amount of entities can render on-screen at a time.

By default, infinite streaming is disabled.

## Syntax

```
bool engineSetInfiniteStreamingEnabled ( bool enabled )
```

### Arguments

- **enabled:** a boolean deciding whether heap allocating of Streaming GC nodes is a viable option.

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
