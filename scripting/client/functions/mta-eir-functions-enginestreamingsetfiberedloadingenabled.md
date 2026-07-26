---
doc_id: "mta-wiki:7387"
title: "MTA:Eir/functions/engineStreamingSetFiberedLoadingEnabled"
source_title: "MTA:Eir/functions/engineStreamingSetFiberedLoadingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingSetFiberedLoadingEnabled"
revision_id: 77726
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.527390+00:00"
---

# MTA:Eir/functions/engineStreamingSetFiberedLoadingEnabled

This function switches between original and fibered loading of the [GTA:SA Streaming system](mta://reference/misc/gta-sa-resource-streaming.md). In original mode, most resources are loaded in one go, but big ones (exceeding slicer buffer size) are loaded exclusively and in two pulses. In fibered mode, the Streaming system can only take a user-defined percentage of the game frame time, meaning that resources can take an arbitrary amount of pulses depending on the complexity of said resources.

By default, fibered loading is enabled.

## Syntax

```
bool engineStreamingSetFiberedLoadingEnabled ( bool enabled )
```

### Returns

Returns **true** if enabled is passed as valid boolean, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet turns on fibered loading when the Streaming system is busy and leaves it that way for five seconds.

```
engineStreamingSetFiberedLoadingEnabled( false );

local lastBusyTime = false;
local fiberedDuration = 5000;

addEventHandler( "onClientRender", root,
    function()
        local isBusy = engineGetStreamingInfo().isBusy;

        if ( isBusy ) then
            local now = getTickCount();

            if not ( lastBusyTime ) then
                lastBusyTime = now;

                engineSetFiberedLoadingEnabled( true );
            end
        elseif ( lastBusyTime ) then
            if ( now - lastBusyTime > fiberedDuration ) then
                engineSetFiberedLoadingEnabled( false );
            end
        end
    end
);
```
