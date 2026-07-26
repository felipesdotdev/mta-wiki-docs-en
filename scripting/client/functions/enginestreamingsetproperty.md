---
doc_id: "mta-wiki:14184"
title: "EngineStreamingSetProperty"
source_title: "EngineStreamingSetProperty"
source_url: "https://wiki.multitheftauto.com/wiki/EngineStreamingSetProperty"
revision_id: 82808
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:59.284716+00:00"
---

# EngineStreamingSetProperty

**THIS IS NOT AN MTA FUNCTION!** This should be deleted as it's part of an unfinished project.

This function changes the behavior of the GTA:SA streaming system. It is meant to optimize the performance of the game for your custom server. Changes in these properties affect the gameplay quality of the entire server.

## Syntax

```
bool engineStreamingSetProperty ( string propertyName, var propValue )
```

### Arguments

- **propertyName:** the name of the streaming property you want to change

- **propValue:** value to pass to the property

### Valid Properties

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| strictNodeDistrib | boolean | It is only valid in conjunction with infiniteStreaming . If enabled, entities first allocate from existing nodes. If disabled, entities are allowed to allocate new streaming nodes from the heap without touching existing nodes. | Enabled |
| infiniteStreaming | boolean | Enables or disables heap allocation of streaming garbage collector nodes. The allocation behavior order is changed using strictNodeDistrib . If enabled, GTA:SA can keep an theoretically infinite amount of entities inside of the streaming garbage collector. This also means that an theoretically infinite amount of entities can render on-screen at a time. | Disabled |
| gcOnDemand | boolean | Used to add a Streaming garbage collector run to the event that the engine runs out of freely available Streaming GC nodes. The whole world is checked for off-screen or far-away entities. Every entity it finds loses its RenderWare data. When the model info of the specific entity model is not used anymore, it is freed. This way multiple Streaming GC nodes are made available for allocation. It is a safer way to free nodes from in-game entities than the Streaming node stealing implemented by Rockstar Games. | Disabled |
| nodeStealing | boolean | Allows or disallows the Streaming GC node stealing performed by native GTA:SA. This is the functionality that directly causes world flickering if the engine encounters Streaming GC node shortage. Disabling this functionality will greatly reduce the amount of entities that can be freed of their Streaming GC nodes. | Enabled |
| isFibered | boolean | Switches between original and fibered loading of the GTA:SA Streaming system . In original mode, most resources are loaded in one go, but big ones (exceeding slicer buffer size) are loaded exclusively and in two pulses. In fibered mode, the Streaming system can only take a user-defined percentage of the game frame time, meaning that resources can take an arbitrary amount of pulses depending on the complexity of said resources. | Enabled |
| fiberedPerfMult | number | This function changes the fibered loading frame time execution percentage of the MTA:Eir Streaming system . 100% means that the Streaming system can take as much as the last frame time the engine took. If set to 0%, the Streaming system will not halt but take a step at a time, disregarding any time settings. Lower percentages decrease the CPU load that the Streaming loader issues every frame. While it does not affect high-end CPUs, low end CPUs can greatly benefit from lower percentages when traveling across the world or entering dense areas. In general, lower percentages reduce lag spikes that occur when loading dense areas. | 0.6 |

### Useful Media

- [https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_opt.zip](https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_opt.zip) - streaming debugging resource

- [https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_test.zip](https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_test.zip) - streaming mode example resource

- [https://www.youtube.com/watch?v=sk8WsHwPgsU](https://www.youtube.com/watch?v=sk8WsHwPgsU) - showcase video

### Returns

Returns *true* if valid arguments have been passed, *false* otherwise.

## Examples

Click to collapse [-]
Client

This snippet ultimatively fixes the world flickering.

```
engineStreamingSetProperty( "strictNodeDistrib", false );
engineStreamingSetProperty( "infiniteStreaming", true );
```

Click to collapse [-]
Client

This snippet sets the Streaming GC system to sparse mode. In this mode only the preallocated amount of Streaming GC nodes is allowed. Keeping a low amount of Streaming nodes is interesting for performance optimizations.

```
engineStreamingSetProperty( "gcOnDemand", true );
engineStreamingSetProperty( "infiniteStreaming", false );
engineStreamingSetProperty( "strictNodeDistrib", true );
```

Click to collapse [-]
Client

This snippet turns on fibered loading when the Streaming system is busy and leaves it that way for five seconds.

```
engineStreamingSetProperty( "isFibered", false );

local lastBusyTime = false;
local fiberedDuration = 5000;

addEventHandler( "onClientRender", root,
    function()
        local isBusy = engineGetStreamingInfo().isBusy;

        if ( isBusy ) then
            local now = getTickCount();

            if not ( lastBusyTime ) then
                lastBusyTime = now;

                engineStreamingSetProperty( "isFibered", true );
            end
        elseif ( lastBusyTime ) then
            if ( now - lastBusyTime > fiberedDuration ) then
                engineStreamingSetProperty( "isFibered", false );
            end
        end
    end
);
```

Click to collapse [-]
Client

This snippet makes the world load very slow. Lag spikes cannot occur due to Streaming loading anymore.

```
engineStreamingSetProperty( "isFibered", true );
engineStreamingSetProperty( "fiberedPerfMult", 0 );
```
