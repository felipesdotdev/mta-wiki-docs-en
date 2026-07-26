---
doc_id: "mta-wiki:10763"
title: "DxDrawPrimitive"
source_title: "DxDrawPrimitive"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawPrimitive"
revision_id: 77050
language: "en"
categories: ["Client_functions", "Changes_in_1.5.6", "Changes_in_1.6.0"]
---

# DxDrawPrimitive

This function draws a 2D primitive shape across the screen - rendered for one frame. This should be used in conjunction with [onClientRender](mta://scripting/client/events/onclientrender.md) in order to display continuously.

## Syntax

```
bool dxDrawPrimitive ( string pType, bool postGUI, table vertex1 [, table vertex2, ...] )
```

### Required Arguments

- **pType:** Type of primitive to be drawn.

- **postGUI:** A bool representing whether the line should be drawn on top of or behind any ingame GUI (rendered by CEGUI).

- **vertices:** Tables representing each primitive vertex, required amount of them is determined by primitive type.

## Allowed types

 

Available primitive types.

More info on primitives may be found on [this MSDN site](https://msdn.microsoft.com/en-us/library/windows/desktop/bb147291(v=vs.85).aspx)

- **pointlist:** Renders the vertices as a collection of isolated points.

- **linelist:** Renders the vertices as a list of isolated straight line segments.

- **linestrip:** Renders the vertices as a single polyline.

- **trianglelist:** Renders the specified vertices as a sequence of isolated triangles. Each group of three vertices defines a separate triangle.

- **trianglestrip:** Renders the vertices as a triangle strip.

- **trianglefan:** Renders the vertices as a triangle fan.

## Vertices format

- **posX:** An float representing the absolute X position of the vertex, represented by pixels on the screen.

- **posY:** An float representing the absolute Y position of the vertex, represented by pixels on the screen.

- **color (optional):** An integer of the hex color, produced using [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue). If it's not specified, white color is used.

### Returns

Returns a *true* if the operation was successful, *false* otherwise.

## Example

Click to collapse [-]
Example 1

This is a small example that creates trianglefan primitive with vertices in places that user clicks. It assigns every vertex random color.

```
local vertices = {}
function onClick(btn, state, x, y)
	if btn ~= "left" then return end
	if state ~= "up" then return end
	local vertex = {x, y, tocolor(math.random(255), math.random(255), math.random(255))}
	table.insert(vertices, vertex)
end
addEventHandler("onClientClick", root, onClick)

function draw()
	dxDrawPrimitive("trianglefan", true, unpack(vertices))
end
addEventHandler("onClientPreRender", root, draw)
```

Click to collapse [-]
Example 2

This example draws one complete oscillation of a sine wave starting in the center of the players screen using a linestrip type primitive.

```
local screenSizeX,screenSizeY = guiGetScreenSize() -- save the current screen dimensions
local sinCoords = {}

function resStart() -- do all this once during "onClientResourceStart", rather than every frame
	local range = math.pi * 2 -- to get 1 complete oscillation of the sine wave we need the range from 0 to 2pi
	local resolution = 100 -- resolution in this example means in how many steps we draw the linestrip, higher resolution means smoother curve at the expense of longer computation time and higher memory usage
	local scale = 50
	for i=0,range,range/resolution do -- "loop through this [resolution] times, starting at 0 and ending at [range]"
		local x = screenSizeX * 0.5 + i * scale -- start at the center of the screen and go from there
		local y = screenSizeY * 0.5 - math.sin(i) * scale -- subtract rather than add because greater y value means lower on the screen, which is the opposite of what we're used to seeing in graphs
		table.insert(sinCoords,{x,y})
	end
end
addEventHandler("onClientResourceStart",getResourceRootElement(getThisResource()), resStart)

function exampleRender()
	dxDrawPrimitive("linestrip",true,unpack(sinCoords)) -- render a linestrip type primitive with the coordinates we calculated earlier to draw our sine wave
end
addEventHandler("onClientRender",getRootElement(),exampleRender)
```

Click to expand [+]
Example 3

Modifying the previous example, we can also use it to draw a "loading circle"-symbol similar to what some modern games like using to indicate loading or cloud saving in progress.

```
local screenSizeX,screenSizeY = guiGetScreenSize() -- save the current screen dimensions
local circleCoords = {}
local resolution = 100 -- resolution in this example means in how many steps we draw the linestrip, higher resolution means smoother curve at the expense of longer computation time and higher memory usage
local scale = 20
local maxSegmentPercentage = 0.75 -- this means the largest our line will get is 3/4 of the full circle
local startPointRevolution = 2000 -- one full revolution around the circle for our starting point after this amount of milliseconds passed
local endPointOscillation = 3000 -- one full oscillation of our endpoint after this amount of milliseconds passed

function resStart() -- do all this once during "onClientResourceStart", rather than every frame
	local range = math.pi * 2 -- to complete a circle we need the range from 0 to 2pi
	for i=0,range,range/resolution do -- "loop through this [resolution] times, starting at 0 and ending at [range]"
		local x = screenSizeX * 0.5 + math.sin(i) * scale -- for a circle we get our x coordiante from sine and the y coordinate from cosine or vice versa
		local y = screenSizeY * 0.5 - math.cos(i) * scale -- subtract will later result in a clockwise spin, add in a counter clockwise one
		table.insert(circleCoords,{x,y})
	end
end
addEventHandler("onClientResourceStart",getResourceRootElement(getThisResource()), resStart)

function exampleRender()
	local tick = getTickCount() -- get the current time in milliseconds, then use it in a few clever ways to animate our circle
	local firstPoint = math.ceil( ((tick/startPointRevolution) % 1)*resolution ) -- firstly dividing it and using %1 (modulo 1) to repeatedly get a slowly, linearly increasing value from 0 to 1. This is our starting point
	local secondPoint = math.ceil( firstPoint + (math.sin(tick/endPointOscillation)) * resolution*maxSegmentPercentage ) -- secondly figuring out where we want our end point to be, using sine to get a pleasant looking pulse for the line growth
	
	if firstPoint > secondPoint then -- because of how we calculate our end point, half the time it will be smaller than the start point. for unpack() to give us the range we want we need to provide the smaller value first
		firstPoint, secondPoint = secondPoint, firstPoint
	end
	
	if secondPoint > resolution then -- sometimes we'll wrap around the origin point of our circle, those cases need to be taken care of, so we'll draw the linestrip in two parts for those.
		dxDrawPrimitive("linestrip",true,unpack(circleCoords,firstPoint,resolution)) -- [secondPoint] is overshooting, so first let's complete the circle from [firstPoint]
		dxDrawPrimitive("linestrip",true,circleCoords[resolution],unpack(circleCoords,1,secondPoint%resolution)) -- and then draw the remaining extra segments from the start of the circle to however many segments [secondPoint] went past [resolution]
	elseif firstPoint < 1 then -- lua tables start at an index of 1, so 0 and anything into the negatives needs to be handled
		dxDrawPrimitive("linestrip",true,unpack(circleCoords,resolution+firstPoint,resolution)) -- "how many segments before [resolution] do we have to start? Either way we complete it at [resolution]!"
		dxDrawPrimitive("linestrip",true,circleCoords[resolution],unpack(circleCoords,1,secondPoint)) -- draw the remaining segments from 1 all the way to [secondPoint]
	else
		dxDrawPrimitive("linestrip",true,unpack(circleCoords,firstPoint,secondPoint)) -- the line isn't currently crossing the origin point of the circle at the top, so drawing this one is straight forwards
	end

end
addEventHandler("onClientRender",getRootElement(),exampleRender)
```

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md)

- [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md)

- [dxCreateScreenSource](mta://scripting/client/functions/dxcreatescreensource.md)

- [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md)

- [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md)

- [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md)

- [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md)

- [dxDrawImageSection](mta://scripting/client/functions/dxdrawimagesection.md)

- [dxDrawLine](mta://scripting/client/functions/dxdrawline.md)

- [dxDrawLine3D](mta://scripting/client/functions/dxdrawline3d.md)

- [dxDrawMaterialLine3D](mta://scripting/client/functions/dxdrawmaterialline3d.md)

- [dxDrawMaterialPrimitive](mta://scripting/client/functions/dxdrawmaterialprimitive.md)

- [dxDrawMaterialPrimitive3D](mta://scripting/client/functions/dxdrawmaterialprimitive3d.md)

- [dxDrawMaterialSectionLine3D](mta://scripting/client/functions/dxdrawmaterialsectionline3d.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22271](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22271):

- [dxDrawModel3D](mta://scripting/client/functions/dxdrawmodel3d.md)

- dxDrawPrimitive

- [dxDrawPrimitive3D](mta://scripting/client/functions/dxdrawprimitive3d.md)

- [dxDrawRectangle](mta://scripting/client/functions/dxdrawrectangle.md)

- [dxDrawText](mta://scripting/client/functions/dxdrawtext.md)

- [dxDrawWiredSphere](mta://scripting/client/functions/dxdrawwiredsphere.md)

- [dxGetBlendMode](mta://scripting/client/functions/dxgetblendmode.md)

- [dxGetFontHeight](mta://scripting/client/functions/dxgetfontheight.md)

- [dxGetMaterialSize](mta://scripting/client/functions/dxgetmaterialsize.md)

- [dxGetPixelColor](mta://scripting/client/functions/dxgetpixelcolor.md)

- [dxGetPixelsSize](mta://scripting/client/functions/dxgetpixelssize.md)

- [dxGetPixelsFormat](mta://scripting/client/functions/dxgetpixelsformat.md)

- [dxGetStatus](mta://scripting/client/functions/dxgetstatus.md)

- [dxGetTextSize](mta://scripting/client/functions/dxgettextsize.md)

- [dxGetTextWidth](mta://scripting/client/functions/dxgettextwidth.md)

- [dxGetTexturePixels](mta://scripting/client/functions/dxgettexturepixels.md)

- [dxIsAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxisaspectratioadjustmentenabled.md)

- [dxSetAspectRatioAdjustmentEnabled](mta://scripting/client/functions/dxsetaspectratioadjustmentenabled.md)

- [dxSetBlendMode](mta://scripting/client/functions/dxsetblendmode.md)

- [dxSetPixelColor](mta://scripting/client/functions/dxsetpixelcolor.md)

- [dxSetRenderTarget](mta://scripting/client/functions/dxsetrendertarget.md)

- [dxSetShaderValue](mta://scripting/client/functions/dxsetshadervalue.md)

- [dxSetShaderTessellation](mta://scripting/client/functions/dxsetshadertessellation.md)

- [dxSetShaderTransform](mta://scripting/client/functions/dxsetshadertransform.md)

- [dxSetTestMode](mta://scripting/client/functions/dxsettestmode.md)

- [dxSetTextureEdge](mta://scripting/client/functions/dxsettextureedge.md)

- [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md)

- [dxUpdateScreenSource](mta://scripting/client/functions/dxupdatescreensource.md)
