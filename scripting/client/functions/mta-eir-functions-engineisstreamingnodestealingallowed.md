---
doc_id: "mta-wiki:7386"
title: "MTA:Eir/functions/engineIsStreamingNodeStealingAllowed"
source_title: "MTA:Eir/functions/engineIsStreamingNodeStealingAllowed"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineIsStreamingNodeStealingAllowed"
revision_id: 77725
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.440331+00:00"
---

# MTA:Eir/functions/engineIsStreamingNodeStealingAllowed

This function returns whether [Streaming GC](mta://reference/misc/gta-sa-streaming-garbage-collection.md) node stealing is performed by GTA:SA. This is the functionality that directly causes world flickering if the engine encounters Streaming GC node shortage. It is recommended to disable this functionality and use [garbage collection](mta://scripting/client/functions/mta-eir-functions-enginestreamingsetgcondemandenabled.md) instead.

By default, Streaming GC node stealing is allowed.

## Syntax

```
bool engineIsStreamingNodeStealingAllowed ()
```

### Returns

Returns **true** if the GTA:SA engine is allowed to take away Streaming GC nodes from on-screen/visible entities, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet turns on garbage collection if Streaming node stealing is found enabled.

```
if ( engineIsStreamingNodeStealingAllowed() ) then
    engineAllowStreamingNodeStealing( false );
    engineStreamingSetGCOnDemandEnabled( true );
end
```
