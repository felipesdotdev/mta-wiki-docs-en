---
doc_id: "mta-wiki:7436"
title: "MTA:Eir/functions/engineCreateLight"
source_title: "MTA:Eir/functions/engineCreateLight"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineCreateLight"
revision_id: 39061
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.380904+00:00"
---

# MTA:Eir/functions/engineCreateLight

This function creates a RenderWare RpLight object. A light is an object that affects its surrouding RpAtomic instances in a certain radius and casts effects on them. The most notable effect is the **pointlight**, that colors its surroundings based on attenuation settings.

## Syntax

```
rplight engineCreateLight ( string type )
```

### Arguments

- **type:** decides which type that light should have, can be **point**, **spot**, **spot_soft**, **directional** or **ambient**

### Returns

Returns the **rplight object** if creation was successful, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet creates a RenderWare light object and sets it up properly.

```
local light = engineCreateLight( "point" ); -- creates the new point light
light.setColor(1, 1, 1, 1); -- gives the point light a bright color
light.setAttenuation(0.8, 1.4, 4); -- makes the light fade somewhat
light.setRadius(100); -- makes the light affect atomics in a 100 unit radius

local lightFrame = engineCreateFrame(); -- create a 3D transformation for the light
light.setParent( lightFrame ); -- attaches the light to its frame, the light can now be active in the world.
light.addToScene(); -- activates the light object, so it illuminates its surroundings

lightFrame.setPosition( 0, 0, 10 ); -- repositions the light
```

Click to collapse [-]
Client

This snippet creates a spotlight that points in the direction of the player.

```
local light = engineCreateLight( "spot_soft" ); -- create a soft spot light
light.setColor( 1, 1, 1, 1 ); -- set its color to white
light.setAttenuation( 0, 10, 8 ); -- give it a random attenuation value
light.setRadius( 300 ); -- set its radius to 300 game units
light.setFalloff( 99 ); -- set the softness of the spot light
light.setConeAngle( 15 ); -- set the spot light's cone angle

-- Spot lights face in the direction of the "up" vector.
-- If we want to rotate it according to the player's "front" vector,
-- we must tilt the light so that the "up" vector becomes the "front" vector.
local lightFrame = engineCreateFrame();
light.setParent( lightFrame );
light.addToScene();

-- We tilt the light "up vector" onto the ped "x" axis using 90-degree y angle.
-- Then the "up" vector is rotated onto the "y" axis using 90-degree x angle.
local transMatrix = matrixNew();
transMatrix.setEulerAngles( 90, 90, 0 );
lightFrame.setModelling( transMatrix );

-- We use another transformation frame to actually face the direction of the player.
-- This frame is updated with the player's world matrix.
local lightPointTransform = engineCreateFrame();
lightFrame.setParent( lightPointTransform );

-- We need to update it every frame.
local function updateLight()
    local playerMatrix = localPlayer.getMatrix();
    
    -- I decided to offset the world matrix by 1 unit up.
    playerMatrix.setPosition(
        playerMatrix.offset( 0, 0, 1 )
    );
    
    -- Apply it to the light's root transformation.
    lightPointTransform.setModelling( playerMatrix );

    -- Remember to clean up resources to simplify the task of
    -- the garbage collector.
    playerMatrix.destroy();
end

addEventHandler( "onClientRender", root, updateLight );
```
