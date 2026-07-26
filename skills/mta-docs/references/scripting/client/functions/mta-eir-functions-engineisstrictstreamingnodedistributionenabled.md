---
doc_id: "mta-wiki:7372"
title: "MTA:Eir/functions/engineIsStrictStreamingNodeDistributionEnabled"
source_title: "MTA:Eir/functions/engineIsStrictStreamingNodeDistributionEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineIsStrictStreamingNodeDistributionEnabled"
revision_id: 77711
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineIsStrictStreamingNodeDistributionEnabled

This function returns whether strict streaming node distribution is enabled. Strict streaming node distribution is meant to rationalize the streaming node allocation, so the number of total streaming nodes does not grow too high.

By default, strict node distribution is enabled.

## Syntax

```
bool engineIsStrictStreamingNodeDistributionEnabled ()
```

### Returns

Returns *true* is strict streaming node distribution is enabled, *false* otherwise.

## Example

Click to collapse [-]
Client

This snippet prints out the current strict node distribution status to the user.

```
addCommandHandler( "node_alloc",
    function()
        local isEnabled = engineIsStrictStreamingNodeDistributionEnabled();

        outputChatBox( "Strict Streaming Node Distribution is " .. ( isEnabled and "" or "not " ) .. "enabled." );
    end
);
```
