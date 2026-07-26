---
doc_id: "mta-wiki:13253"
title: "DxDrawBluredRectangle"
source_title: "DxDrawBluredRectangle"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawBluredRectangle"
revision_id: 81467
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:14:43.977959+00:00"
---

# DxDrawBluredRectangle

This function draws a 2D blured rectangle on the screen - rendered for one frame. This should be used in conjunction with onClientRender for continuous display.

## Syntax

```
bool dxDrawBluredRectangle ( float x, float y, float width, float height )
```

### Required Arguments

- **x:** An float representing the **absolute** origin X position of the rectangle, represented by pixels on the screen.

- **y:** An float representing the **absolute** origin Y position of the rectangle, represented by pixels on the screen.

- **width:** An float representing the width of the rectangle, drawn in a *right* direction from the origin.

- **height:** An float representing the height of the rectangle, drawn in a *downwards* direction from the origin.

### Required Files

[mta-helper.fx](https://cdn.discordapp.com/attachments/851000636484747274/861170045651910686/mta-helper.fx),
[blurV.fx](https://cdn.discordapp.com/attachments/851000636484747274/861170037255307294/blurV.fx),
[blurH.fx](https://cdn.discordapp.com/attachments/851000636484747274/861170034495455232/blurH.fx)

### Returns

Returns true if the operation was successful, false otherwise.

## Code

Click to collapse [-]
Client

```
local scx, scy = guiGetScreenSize()

Settings = {}
Settings.var = {}
Settings.var.blur = 1
Settings.var.optim = 4
Settings.screenRectangle = {}

local current

function createShader()
        myScreenSource = dxCreateScreenSource( scx/Settings.var.optim, scy/Settings.var.optim )
        blurHShader,tecName = dxCreateShader( "shaders/blurH.fx" )
        blurVShader,tecName = dxCreateShader( "shaders/blurV.fx" )
	bAllValid = myScreenSource and blurHShader and blurVShader
end
createShader()

function preRender ()
	if not Settings.var then
		return
	end
	RTPool.frameStart()
	dxUpdateScreenSource( myScreenSource )
	current = myScreenSource
	current = applyGBlurH( current, Settings.var.blur )
	current = applyGBlurV( current, Settings.var.blur )
	dxSetRenderTarget()
end
addEventHandler ("onClientRender", root, preRender)

function dxDrawBluredRectangle (pos_x, pos_y, size_x, size_y, color)
	 if bAllValid then
	 dxDrawImageSection  ( pos_x, pos_y, size_x, size_y, pos_x/Settings.var.optim, pos_y/Settings.var.optim, size_x/Settings.var.optim, size_y/Settings.var.optim, current, 0,0,0, color)
	 end
end

function applyGBlurH( Src, blur )
	if not Src then return nil end
	local mx,my = dxGetMaterialSize( Src )
	local newRT = RTPool.GetUnused(mx,my)
	if not newRT then return nil end
	dxSetRenderTarget( newRT, true )
	dxSetShaderValue( blurHShader, "TEX0", Src )
	dxSetShaderValue( blurHShader, "TEX0SIZE", mx,my )
	dxSetShaderValue( blurHShader, "BLUR", blur )
	dxDrawImage( 0, 0, mx, my, blurHShader )
	return newRT
end

function applyGBlurV( Src, blur )
	if not Src then return nil end
	local mx,my = dxGetMaterialSize( Src )
	local newRT = RTPool.GetUnused(mx,my)
	if not newRT then return nil end
	dxSetRenderTarget( newRT, true )
	dxSetShaderValue( blurVShader, "TEX0", Src )
	dxSetShaderValue( blurVShader, "TEX0SIZE", mx,my )
	dxSetShaderValue( blurVShader, "BLUR", blur )
	dxDrawImage( 0, 0, mx,my, blurVShader )
	return newRT
end

RTPool = {}
RTPool.list = {}

function RTPool.frameStart()
	for rt,info in pairs(RTPool.list) do
		info.bInUse = false
	end
end

function RTPool.GetUnused( mx, my )
	for rt,info in pairs(RTPool.list) do
		if not info.bInUse and info.mx == mx and info.my == my then
			info.bInUse = true
			return rt
		end
	end

	local rt = dxCreateRenderTarget( mx, my )
	if rt then
		RTPool.list[rt] = { bInUse = true, mx = mx, my = my }
	end
	return rt
end
```

## Example

Click to collapse [-]
Client

```
local scx, scy = guiGetScreenSize()

function drawBluredRectangle()
	dxDrawBluredRectangle( scx/3.8, scy/3.8, scx/2.02, scy/2 )
end

addEventHandler("onClientRender", root, drawBluredRectangle)
```

##### Author: fiXlly, WaRuS
