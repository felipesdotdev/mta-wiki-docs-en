---
doc_id: "mta-wiki:7385"
title: "MTA:Eir/functions/engineAllowStreamingNodeStealing"
source_title: "MTA:Eir/functions/engineAllowStreamingNodeStealing"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineAllowStreamingNodeStealing"
revision_id: 77724
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.372025+00:00"
---

# MTA:Eir/functions/engineAllowStreamingNodeStealing

This function allows or disallows the [Streaming GC](mta://reference/misc/gta-sa-streaming-garbage-collection.md) node stealing performed by native GTA:SA. This is the functionality that directly causes world flickering if the engine encounters Streaming GC node shortage. Disabling this functionality will greatly reduce the amount of entities that can be freed of their Streaming GC nodes.

By default, Streaming GC node stealing is allowed.

## Syntax

```
bool engineAllowStreamingNodeStealing ( bool allowed )
```

### Arguments

- **allowed:** a boolean deciding whether the GTA:SA engine can take away Streaming GC nodes from on screen/visible entities.

### Returns

Returns **true** if allowed is passed as valid boolean, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet is an alternative to the world flickering fix applied by infinite streaming. It once again sets the Streaming system into a sparse mode. Garbage Collection is considered better than node stealing.

```
engineAllowStreamingNodeStealing( false );
engineStreamingSetGCOnDemandEnabled( true );
```
