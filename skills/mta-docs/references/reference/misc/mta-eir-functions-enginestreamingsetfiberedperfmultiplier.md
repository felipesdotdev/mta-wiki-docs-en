---
doc_id: "mta-wiki:7389"
title: "MTA:Eir/functions/engineStreamingSetFiberedPerfMultiplier"
source_title: "MTA:Eir/functions/engineStreamingSetFiberedPerfMultiplier"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingSetFiberedPerfMultiplier"
revision_id: 37866
language: "en"
categories: []
---

# MTA:Eir/functions/engineStreamingSetFiberedPerfMultiplier

This function changes the fibered loading frame time execution percentage of the [MTA:Eir Streaming system](mta://reference/misc/gta-sa-resource-streaming.md). 100% means that the Streaming system can take as much as the last frame time the engine took. If set to 0%, the Streaming system will not halt but take a step at a time, disregarding any time settings.

Lower percentages decrease the CPU load that the Streaming loader issues every frame. While it does not affect high-end CPUs, low end CPUs can greatly benefit from lower percentages when traveling across the world or entering dense areas. In general, lower percentages reduce lag spikes that occur when loading dense areas.

By default, the frame time execution percentage is set to **0.6**.

## Syntax

```
bool engineStreamingSetFiberedPerfMultiplier ( double execPerc )
```

### Arguments

- **execPerc:** the new frame time execution percentage to assign to fibered loading

### Returns

Returns **true** if execPerc is passed as valid double number, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet makes the world load very slow. Lag spikes cannot occur due to Streaming loading anymore.

```
engineStreamingSetFiberedLoadingEnabled( true );
engineStreamingSetFiberedPerfMultiplier( 0 );
```
