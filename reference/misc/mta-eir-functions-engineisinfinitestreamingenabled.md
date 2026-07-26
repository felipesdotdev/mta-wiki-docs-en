---
doc_id: "mta-wiki:7374"
title: "MTA:Eir/functions/engineIsInfiniteStreamingEnabled"
source_title: "MTA:Eir/functions/engineIsInfiniteStreamingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineIsInfiniteStreamingEnabled"
revision_id: 37834
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.435127+00:00"
---

# MTA:Eir/functions/engineIsInfiniteStreamingEnabled

This function returns whether infinite streaming node allocation is enabled. With it being enabled, the only limitation to world entity streaming is the clientside hardware.

By default, infinite streaming is disabled.

## Syntax

```
bool engineIsInfiniteStreamingEnabled ()
```

### Returns

Returns *true* if infinite streaming is enabled, *false* otherwise.

## Example

Click to collapse [-]
Client

This snippet prints out to the user whether infinite streaming is enabled.

```
addCommandHandler( "inf_stream",
    function()
        local isEnabled = engineIsInfiniteStreamingEnabled();

        outputChatBox( "Infinite Streaming Node Allocation is " .. ( isEnabled and "" or "not " ) .. "enabled." );
    end
);
```
