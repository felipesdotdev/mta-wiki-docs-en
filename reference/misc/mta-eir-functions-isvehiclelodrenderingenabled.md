---
doc_id: "mta-wiki:7393"
title: "MTA:Eir/functions/isVehicleLODRenderingEnabled"
source_title: "MTA:Eir/functions/isVehicleLODRenderingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/isVehicleLODRenderingEnabled"
revision_id: 37872
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.595128+00:00"
---

# MTA:Eir/functions/isVehicleLODRenderingEnabled

This function returns whether LOD rendering of vehicles is enabled. If vehicle LOD rendering is disabled, only the high quality version of the vehicle is allowed to render. Otherwise the low quality version of the vehicle will render after a specific distance (depending on vehicle type).

## Syntax

```
bool isVehicleLODRenderingEnabled ()
```

### Returns

Returns **true** if the vehicle LOD rendering is enabled by scripts, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet removes all VLO atomics of a custom vehicle model if LOD rendering is disabled. This is done to increase engine performance as the LOD atomics are considered useless.

```
local myVehicleCollision = engineLoadCOL( "vehicle.col" );
local myVehicleModel = engineLoadDFF( "vehicle.dff", 0 );

if not ( isVehicleLODRenderingEnabled() ) then
    -- Scan the vehicle model for all frames containing "_vlo" and remove them
    local rootFrame = myVehicleModel.getFrame();

    local function removeVLOFrames( frame )
        local childFrames = frame.getLinkedFrames();

        for m,n in ipairs( childFrames ) do
            if ( string.find( n.getName(), "_vlo", 1, true ) ) then
                n.destroy();
            else
                removeVLOFrames( n );
            end
        end
    end

    removeVLOFrames( rootFrame );
end

addCommandHandler( "use_my_vehicle",
    function()
        local replaceWith = 411;

        engineReplaceModel( myVehicleModel, replaceWith );
        engineReplaceCOL( myVehicleCollision, replaceWith );
    end
);
```
