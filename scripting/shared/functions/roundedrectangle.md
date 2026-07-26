---
doc_id: "mta-wiki:11210"
title: "RoundedRectangle"
source_title: "RoundedRectangle"
source_url: "https://wiki.multitheftauto.com/wiki/RoundedRectangle"
revision_id: 81852
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:16:35.421889+00:00"
---

# RoundedRectangle

This function draws a rounded corner rectangle.

## Syntax

```
nil dxDrawRoundedRectangle(x, y, width, height, radius, color, align, postGUI, subPixelPositioning)
```

## Example

Click to collapse [-]
Client side

```
local sx, sy = guiGetScreenSize()
local x, y, w, h = sx/2-200, sy/2-200, 400, 400
local rounded = 10
local color = tocolor(0, 0, 0, 200)

addEventHandler('onClientRender', root, function ()
    dxDrawRoundedRectangle(x, y, w, h, rounded, color)
end)
```

Example by @IQ65

## Code 1

Click to collapse [-]
Client side

```
function dxDrawRoundedRectangle(x, y, width, height, radius, color, postGUI, subPixelPositioning)
    dxDrawRectangle(x+radius, y+radius, width-(radius*2), height-(radius*2), color, postGUI, subPixelPositioning)
    dxDrawCircle(x+radius, y+radius, radius, 180, 270, color, color, 16, 1, postGUI)
    dxDrawCircle(x+radius, (y+height)-radius, radius, 90, 180, color, color, 16, 1, postGUI)
    dxDrawCircle((x+width)-radius, (y+height)-radius, radius, 0, 90, color, color, 16, 1, postGUI)
    dxDrawCircle((x+width)-radius, y+radius, radius, 270, 360, color, color, 16, 1, postGUI)
    dxDrawRectangle(x, y+radius, radius, height-(radius*2), color, postGUI, subPixelPositioning)
    dxDrawRectangle(x+radius, y+height-radius, width-(radius*2), radius, color, postGUI, subPixelPositioning)
    dxDrawRectangle(x+width-radius, y+radius, radius, height-(radius*2), color, postGUI, subPixelPositioning)
    dxDrawRectangle(x+radius, y, width-(radius*2), radius, color, postGUI, subPixelPositioning)
end
```

## Code 2

## Syntax

```
nil dxDrawRoundedRectangle(x, y, w, h, radius = 10, color = tocolor(255, 255, 255, 255), align = 'full', postGUI = false, subPixelPositioning = false)
```

## Example

Click to collapse [-]
Client side

```
local data = {}
data.resolution = {}
data.resolution.x, data.resolution.y = guiGetScreenSize()
data.mainRect = {}
data.mainRect.width = 300
data.mainRect.height = 500

addEventHandler('onClientRender', root, function()
    dxDrawRoundedRectangle(
        data.resolution.x-data.mainRect.width,
        data.resolution.y-data.mainRect.height,
        data.mainRect.width,
        data.mainRect.height,
        10,
        0xffffffff,
        'top',
        false,
        false
    )
end)
```

## Code

Click to collapse [-]
Client side

```
function dxDrawRoundedRectangle(x, y, w, h, radius, color, align, postGUI)
	if not x or not y or not w or not h then return end

	local radius = radius or 10
	local color = color or tocolor(255, 255, 255, 255)
	local align = align or 'full'

	if w < radius then
		w = 0
		radius = 0
		
	elseif h < radius then
		h = 0
		radius = 0
	end
	
	if align == 'full' or align == 'top' or align == 'right' or align == 'left' then
		if align == 'right' then
			dxDrawRectangle(x, y, w - radius, radius, color, postGUI)
			dxDrawCircle((x+w)-radius, y+radius, radius, 270, 360, color, color, 16, 1, postGUI)

		elseif align == 'left' then
			dxDrawRectangle(x + radius, y, w - radius, radius, color, postGUI)
			dxDrawCircle(x+radius, y+radius, radius, 180, 270, color, color, 16, 1, postGUI)
		else
			dxDrawRectangle(x + radius, y, w - (radius * 2), radius, color, postGUI)
			dxDrawCircle(x+radius, y+radius, radius, 180, 270, color, color, 16, 1, postGUI)
			dxDrawCircle((x+w)-radius, y+radius, radius, 270, 360, color, color, 16, 1, postGUI)
		end

		if align == 'top' or align == 'right' or align == 'left' then
			dxDrawRectangle(x, y + radius, w, h - (radius * 2), color, postGUI)
		end
	end

	if align == 'full' or align == 'bottom' or align == 'right' or align == 'left' then
		if align == 'right' then
			dxDrawRectangle(x, y + h - radius, w - radius, radius, color, postGUI)
			dxDrawCircle((x+w)-radius, (y+h)-radius, radius, 0, 90, color, color, 16, 1, postGUI)
			
		elseif align == 'left' then
			dxDrawRectangle(x + radius, y + h - radius, w - radius, radius, color, postGUI)
			dxDrawCircle(x+radius, (y+h)-radius, radius, 90, 180, color, color, 16, 1, postGUI)
		else
			dxDrawRectangle(x + radius, y + h - radius, w - (radius * 2), radius, color, postGUI)
			dxDrawCircle(x+radius, (y+h)-radius, radius, 90, 180, color, color, 16, 1, postGUI)
			dxDrawCircle((x+w)-radius, (y+h)-radius, radius, 0, 90, color, color, 16, 1, postGUI)
		end

		if align == 'bottom' or align == 'right' or align == 'left' then
			dxDrawRectangle(x, y + radius, w, h - (radius * 2), color, postGUI)
		end
	end
		
	if align == 'full' then
		dxDrawRectangle(x, y + radius, w, h - (radius * 2), color, postGUI)
	end
end
```

Original by [User:Extasy](https://wiki.multitheftauto.com/wiki/User:Extasy)

Rewritten by [User:Woovie](https://wiki.multitheftauto.com/wiki/User:Woovie)

Code 2 by [User:.WhiteBlue](https://wiki.multitheftauto.com/index.php?title=User:.WhiteBlue&action=edit&redlink=1)
