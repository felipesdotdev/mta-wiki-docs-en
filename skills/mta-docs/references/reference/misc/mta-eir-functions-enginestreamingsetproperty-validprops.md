---
doc_id: "mta-wiki:7614"
title: "MTA:Eir/functions/engineStreamingSetProperty/validProps"
source_title: "MTA:Eir/functions/engineStreamingSetProperty/validProps"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingSetProperty/validProps"
revision_id: 39629
language: "en"
categories: []
---

# MTA:Eir/functions/engineStreamingSetProperty/validProps

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| strictNodeDistrib | boolean | It is only valid in conjunction with infiniteStreaming . If enabled, entities first allocate from existing nodes. If disabled, entities are allowed to allocate new streaming nodes from the heap without touching existing nodes. | Enabled |
| infiniteStreaming | boolean | Enables or disables heap allocation of streaming garbage collector nodes. The allocation behavior order is changed using strictNodeDistrib . If enabled, GTA:SA can keep an theoretically infinite amount of entities inside of the streaming garbage collector. This also means that an theoretically infinite amount of entities can render on-screen at a time. | Disabled |
| gcOnDemand | boolean | Used to add a Streaming garbage collector run to the event that the engine runs out of freely available Streaming GC nodes. The whole world is checked for off-screen or far-away entities. Every entity it finds loses its RenderWare data. When the model info of the specific entity model is not used anymore, it is freed. This way multiple Streaming GC nodes are made available for allocation. It is a safer way to free nodes from in-game entities than the Streaming node stealing implemented by Rockstar Games. | Disabled |
| nodeStealing | boolean | Allows or disallows the Streaming GC node stealing performed by native GTA:SA. This is the functionality that directly causes world flickering if the engine encounters Streaming GC node shortage. Disabling this functionality will greatly reduce the amount of entities that can be freed of their Streaming GC nodes. | Enabled |
| isFibered | boolean | Switches between original and fibered loading of the GTA:SA Streaming system . In original mode, most resources are loaded in one go, but big ones (exceeding slicer buffer size) are loaded exclusively and in two pulses. In fibered mode, the Streaming system can only take a user-defined percentage of the game frame time, meaning that resources can take an arbitrary amount of pulses depending on the complexity of said resources. | Enabled |
| fiberedPerfMult | number | This function changes the fibered loading frame time execution percentage of the MTA:Eir Streaming system . 100% means that the Streaming system can take as much as the last frame time the engine took. If set to 0%, the Streaming system will not halt but take a step at a time, disregarding any time settings. Lower percentages decrease the CPU load that the Streaming loader issues every frame. While it does not affect high-end CPUs, low end CPUs can greatly benefit from lower percentages when traveling across the world or entering dense areas. In general, lower percentages reduce lag spikes that occur when loading dense areas. | 0.6 |
