---
doc_id: "mta-wiki:7390"
title: "MTA:Eir/functions/engineStreamingGetFiberedPerfMultiplier"
source_title: "MTA:Eir/functions/engineStreamingGetFiberedPerfMultiplier"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingGetFiberedPerfMultiplier"
revision_id: 37902
language: "en"
categories: []
---

# MTA:Eir/functions/engineStreamingGetFiberedPerfMultiplier

This function returns the fibered loading execution time percentage of the [MTA:Eir Streaming system](mta://reference/misc/gta-sa-resource-streaming.md). It is responsible for the CPU load caused by the Streaming system. Lower values decrease the probability of lag-spikes that happen when loading big resources (such as TXDs or COLL sectors).

Since every Streaming slicer is assigned its own fiber, the execution time may be a multiplied by the amount of slicers (internally only).

By default, the frame time execution percentage is set to **0.6**.

## Syntax

```
double engineStreamingGetFiberedPerfMultiplier ()
```

### Returns

Returns a **double** that designates the percentage of frame time the Streaming loading is allowed to take in fibered mode.

## Example

Click to collapse [-]
Client

This snippet doubles the amount of frame time the fibered loader is allowed to take when the Streaming system is busy.

```
local normalFiberedPerc = false;

addEventHandler( "onClientPreRender", root,
    function()
        local isBusy = engineGetStreamingInfo().isBusy;

        if ( isBusy ) then
            if not ( normalFiberedPerc ) then
                normalFiberedPerc = engineStreamingGetFiberedPerfMultiplier();
                engineStreamingSetFiberedPerfMultiplier( normalFiberedPerc * 2 );
            end
        elseif ( normalFiberedPerc ) then
            engineStreamingSetFiberedPerfMultiplier( normalFiberedPerc );

            normalFiberedPerc = false;
        end
    end
);
```
