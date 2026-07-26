---
doc_id: "mta-wiki:7438"
title: "MTA:Eir/functions/engineSetWorldRenderMode"
source_title: "MTA:Eir/functions/engineSetWorldRenderMode"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineSetWorldRenderMode"
revision_id: 39346
language: "en"
categories: []
---

# MTA:Eir/functions/engineSetWorldRenderMode

This function modifies the rendering order, the rendering complexity and the render-states assigned to world entity rendering. It allows you to switch between rendering modes. Each has unique properties as to how entities are ordered for rendering and how their alpha is treated. This function has been created to fight rendering artifacts on the GTA:SA world.

## Syntax

```
bool engineSetWorldRenderMode( string mode )
```

### Arguments

- **mode**: can be either **original**, **meshlocal_alphafix** or **scene_alphafix**

### Returns

Returns **true** if a valid mode has been passed, **false** otherwise.

### Useful Media

- [https://dl.dropboxusercontent.com/u/55896914/eir_resources/rendermode.zip](https://dl.dropboxusercontent.com/u/55896914/eir_resources/rendermode.zip) - resource to easily switch between render modes

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
