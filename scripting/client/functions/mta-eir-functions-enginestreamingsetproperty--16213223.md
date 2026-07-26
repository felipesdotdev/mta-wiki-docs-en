---
doc_id: "mta-wiki:7676"
title: "MTA Eir/Functions/engineStreamingSetProperty"
source_title: "MTA Eir/Functions/engineStreamingSetProperty"
source_url: "https://wiki.multitheftauto.com/wiki/MTA_Eir/Functions/engineStreamingSetProperty"
revision_id: 77733
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:07.073137+00:00"
---

# MTA Eir/Functions/engineStreamingSetProperty

This function changes the behavior of the GTA:SA streaming system. It is meant to optimize the performance of the game for your custom server. Changes in these properties affect the gameplay quality of the entire server.

## Syntax

```
bool engineStreamingSetProperty ( string propertyName, var propValue )
```

### Arguments

- **propertyName:** the name of the streaming property you want to change

- **propValue:** value to pass to the property

### Valid Properties

[MTA:Eir/functions/engineStreamingSetProperty/validProps ru](https://wiki.multitheftauto.com/index.php?title=MTA:Eir/functions/engineStreamingSetProperty/validProps_ru&action=edit&redlink=1)

### Useful Media

- [https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_opt.zip](https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_opt.zip) - streaming debugging resource

- [https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_test.zip](https://dl.dropboxusercontent.com/u/55896914/eir_resources/streaming_test.zip) - streaming mode example resource

- [http://youtu.be/sk8WsHwPgsU](http://youtu.be/sk8WsHwPgsU) - showcase video

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
