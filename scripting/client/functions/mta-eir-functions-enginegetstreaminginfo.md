---
doc_id: "mta-wiki:7381"
title: "MTA:Eir/functions/engineGetStreamingInfo"
source_title: "MTA:Eir/functions/engineGetStreamingInfo"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetStreamingInfo"
revision_id: 77718
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.420577+00:00"
---

# MTA:Eir/functions/engineGetStreamingInfo

This function returns a dictionary which is a snapshot of the current [GTA:SA Streaming System status](mta://reference/misc/gta-sa-resource-streaming.md). Since the streaming status changes rapidly every frame, it is recommended to draw it on the screen.

```
{
    usedMemory = 40985576,
    maxMemory = 533725184,
    numberOfRequests = 0,
    numberOfPriorityRequests = 0,
    numberOfSlicers = 2,
    numberOfRequestsPerSlicer = 16,
    activeStreamingThread = 0,
    isBusy = false,
    isLoadingBigModel = false
}
```

## Syntax

```
table engineGetStreamingInfo ()
```

### Returns

Returns a **dictionary** holding the Streaming system status.

## Example

Click to collapse [-]
Client

This snippet draws the engine streaming information on the screen.

```
local streamingEntryNames =
{
    "usedMemory", "maxMemory", "numberOfRequests",
    "numberOfPriorityRequests", "numberOfSlicers",
    "numberOfRequestsPerSlicer", "activeStreamingThread",
    "isBusy", "isLoadingBigModel"
};

local screenWidth, screenHeight = guiGetScreenSize();

addEventHandler( "onClientRender", root,
    function()
        local streamingInfo = engineGetStreamingInfo();
        
        local x, y = screenWidth - 200, 300;
        
        for m,n in ipairs(streamingEntryNames) do
            local entry = streamingInfo[n];
            
            if not ( entry == nil ) then
                dxDrawText( n .. ": " .. tostring( entry ), x, y );
            end
            
            y = y + 20;
        end
    end
);
```
