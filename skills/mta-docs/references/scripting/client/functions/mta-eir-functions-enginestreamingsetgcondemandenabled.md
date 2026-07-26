---
doc_id: "mta-wiki:7383"
title: "MTA:Eir/functions/engineStreamingSetGCOnDemandEnabled"
source_title: "MTA:Eir/functions/engineStreamingSetGCOnDemandEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingSetGCOnDemandEnabled"
revision_id: 77722
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineStreamingSetGCOnDemandEnabled

This function is used to add a [Streaming garbage collector](mta://reference/misc/gta-sa-streaming-garbage-collection.md) run to the event that the engine runs out of freely available Streaming GC nodes. The whole world is checked for off-screen or far-away entities. Every entity it finds loses its RenderWare data. When the model info of the specific entity model is not used anymore, it is freed. This way multiple Streaming GC nodes are made available for allocation. It is a safer way to free nodes from in-game entities than the Streaming node stealing implemented by Rockstar Games.

By default, Streaming GC on demand is disabled.

## Syntax

```
bool engineStreamingSetGCOnDemandEnabled ( bool enabled )
```

### Arguments

- **enabled:** a boolean to decide whether to garbage collect on lacking free Streaming GC nodes

### Returns

Returns **true** if enabled is passed as valid boolean, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet sets the Streaming GC system to sparse mode. In this mode only the preallocated amount of Streaming GC nodes is allowed. Keeping a low amount of Streaming nodes is interesting for performance optimizations.

```
engineStreamingSetGCOnDemandEnabled( true );
engineSetInfiniteStreamingEnabled( false );
engineSetStrictNodeDistributionEnabled( true );
```
