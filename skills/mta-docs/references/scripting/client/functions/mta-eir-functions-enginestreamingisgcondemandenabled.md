---
doc_id: "mta-wiki:7384"
title: "MTA:Eir/functions/engineStreamingIsGCOnDemandEnabled"
source_title: "MTA:Eir/functions/engineStreamingIsGCOnDemandEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingIsGCOnDemandEnabled"
revision_id: 77721
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineStreamingIsGCOnDemandEnabled

This function returns whether a [Streaming garbage collector](mta://reference/misc/gta-sa-streaming-garbage-collection.md) run is performed to free required Streaming GC nodes for allocation by certain types of entities. Objects, buildings and dummies require Streaming GC nodes so the overall **Streaming memory** does not grow too high. They are the ones using most of the game memory.

By default, Streaming GC on demand is disabled.

## Syntax

```
bool engineStreamingIsGCOnDemandEnabled ()
```

### Returns

Returns **true** if a Streaming garbage collector run is performed on node shortage, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet enables infinite Streaming node allocation after two seconds of node shortage.

```
local firstNodeShortageTime = false;
local nodeShortageDuration = 2000;

local function isNodeShortage()
    return engineGetActiveStreamingFreeSlotCount() == 0;
end

local function enableStrictlessNodeAllocation( enabled )
    engineSetInfiniteStreamingEnabled( enabled );
    engineSetStrictNodeDistributionEnabled( not enabled );
    return true;
end

addEventHandler( "onClientPreRender", root,
    function()
        local isShortage = isNodeShortage();

        if ( isShortage ) then
            local now = getTickCount();

            if not ( firstNodeShortageTime ) then
                firstNodeShortageTime = now;
            elseif ( now - firstNodeShortageTime > nodeShortageDuration ) then
                engineStrictlessNodeAllocation( true );
            end
        else
            firstNodeShortageTime = false;
        end
    end
);
```
