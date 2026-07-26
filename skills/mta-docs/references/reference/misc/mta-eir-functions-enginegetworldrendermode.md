---
doc_id: "mta-wiki:7439"
title: "MTA:Eir/functions/engineGetWorldRenderMode"
source_title: "MTA:Eir/functions/engineGetWorldRenderMode"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetWorldRenderMode"
revision_id: 38227
language: "en"
categories: []
---

# MTA:Eir/functions/engineGetWorldRenderMode

This function returns the rendering mode that the GTA:SA is assigned to use by scripts. Each render mode has unique properties as to how the world entities are rendered. Use different render modes in different parts of the world to archive best quality rendering.

## Syntax

```
string engineGetWorldRenderMode()
```

### Returns

Returns a string containing the **rendering mode** of the GTA:SA engine. Can be either **original**, **meshlocal_alphafix** or **scene_alphafix**.

## Example

Click to collapse [-]
Client

This snippet allows you to switch between rendering modes using the F3 key.

```
local renderModeSwitch =
{
    original = "meshlocal_alphafix",
    meshlocal_alphafix = "scene_alphafix",
    scene_alphafix = "original"
};

addEventHandler( "onClientRender", root,
    function()
        local screenWidth, screenHeight = guiGetScreenSize();
        
        local currentMode = engineGetWorldRenderMode();
    
        dxDrawText( "Current RenderMode: " .. currentMode, screenWidth - 300, 5 );
    end
);

addEventHandler( "onClientKey", root,
    function( key, state )
        if ( key == "F3" ) and ( state == true ) then
            engineSetWorldRenderMode( renderModeSwitch[ engineGetWorldRenderMode() ] );
        end
    end
);
```
