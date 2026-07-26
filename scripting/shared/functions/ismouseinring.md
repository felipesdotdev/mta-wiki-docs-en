---
doc_id: "mta-wiki:9862"
title: "IsMouseInRing"
source_title: "IsMouseInRing"
source_url: "https://wiki.multitheftauto.com/wiki/IsMouseInRing"
revision_id: 53402
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:15:57.073731+00:00"
---

# IsMouseInRing

This function checks if is the cursor is inside of a ring-/part. Best way to use it is with [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md) or circle / ring images.

## Syntax

```
bool isMouseInRing ( float posX, float posY, float radius, float width, float startAngle, float stopAngle )
```

### Required Arguments

- **posX:** The center of the ring on the X-Axis.

- **posY:** The center of the ring on the Y-Axis.

- **radius:** The radius or the ring.

### Optional Arguments

- **width:** The width (thickness) of the ring you want to check. The radius means the center of the ring, so the width goes in and outside the ring.

- **startAngle:** The degrees where you want to start the check.

- **stopAngle:** The degrees where you want to stop the check.

### Returns

Returns *true* if the mouse is inside the ring-/part, *false* otherwise.

### Code

Click to collapse [-]
Client

```
function isMouseInRing(posX, posY, radius, width, startAngle, stopAngle)
    if isCursorShowing() then
	local SX, SY = guiGetScreenSize(); -- You can remove this line if you already got SX and SY for the screenSize
		
	if (not posX or not posY or not radius) then
	    outputDebugString("isMouseInRing: Required arguments are missing", 1);
	    return false
	end
		
	if not (width) then
	    width = SX / 50;
	end
		
	if not (startAngle) then
	    startAngle = 0;
	end
		
	if not (stopAngle) then
	    stopAngle = 359.99;
	end
		
        local cx, cy = getCursorPosition();
        local cx, cy = cx * SX, cy * SY;		
	local iMouseRot = findRotation(posX, posY, cx, cy) + 90;
		
	if (iMouseRot > 360) then
	    iMouseRot = iMouseRot - 360;
	end
		
	local diffX = math.max(cx, posX) - math.min(cx, posX); -- Calculate the X-Axis difference between mouse and ring center
	local diffY = math.max(cy, posY) - math.min(cy, posY); -- Calculate the Y-Axis difference between mouse and ring center	
	local iMouseDistance = math.sqrt(diffX * diffX + diffY * diffY); -- Get the distance in pixels between mouse and ring center

	if (startAngle > stopAngle) then -- Exchange start- and stop angle if startAngle is bigger then the stopAngle
	    local temp = startAngle;
	    startAngle = stopAngle;
	    stopAngle = temp;
	end

	if (iMouseRot >= startAngle and iMouseRot <= stopAngle and iMouseDistance <= radius + width and iMouseDistance >= radius - width) then
	    return true -- The mouse is inside the ring-/part
	else
	    return false -- It's somewhere else
	end
    end
    outputDebugString("isMouseInRing: Cursor is not showing!", 1); -- Remove this line if you know your cursor shouldn't always be showing.
    return false -- Cursor is not showing
end
```

By: Ceeser

## Example

This Example code will check if the mouse in the part of the [dxDrawCircle](mta://scripting/client/functions/dxdrawcircle.md) ring and the ring will change its color if so.

Click to expand [+]
Client

```
-- Example variables
local SX, SY 	= guiGetScreenSize();
local iCenterX 	= SX / 2;
local iCenterY	= SY / 2;
local iRadius	= SX / 10; 
local iWidth	= SX / 100;

function renderCircle()
    if (isMouseInRing(iCenterX, iCenterY, iRadius, iWidth, 0, 120)) then -- Check if the mouse is inside the circle
	dxDrawCircle(iCenterX, iCenterY, iRadius, iWidth, 1, 0, 120, tocolor(0, 255, 0, 255), false); -- If yes (returned true) its green.
    else
	dxDrawCircle(iCenterX, iCenterY, iRadius, iWidth, 1, 0, 120, tocolor(255, 0, 0, 255), false); -- If no (returned false) its red.
    end
end
addEventHandler("onClientRender", root, renderCircle);

function dxDrawCircle( posX, posY, radius, width, angleAmount, startAngle, stopAngle, color, postGUI )
    if ( type( posX ) ~= "number" ) or ( type( posY ) ~= "number" ) then
	return false
    end
	
    local function clamp( val, lower, upper )
	if ( lower > upper ) then lower, upper = upper, lower end
	return math.max( lower, math.min( upper, val ) )
    end
	
    radius = type( radius ) == "number" and radius or 50
    width = type( width ) == "number" and width or 5
    angleAmount = type( angleAmount ) == "number" and angleAmount or 1
    startAngle = clamp( type( startAngle ) == "number" and startAngle or 0, 0, 360 )
    stopAngle = clamp( type( stopAngle ) == "number" and stopAngle or 360, 0, 360 )
    color = color or tocolor( 255, 255, 255, 200 )
    postGUI = type( postGUI ) == "boolean" and postGUI or false
	
    if ( stopAngle < startAngle ) then
	local tempAngle = stopAngle
	stopAngle = startAngle
	startAngle = tempAngle
    end
	
    for i = startAngle, stopAngle, angleAmount do
	local startX = math.cos( math.rad( i ) ) * ( radius - width )
	local startY = math.sin( math.rad( i ) ) * ( radius - width )
	local endX = math.cos( math.rad( i ) ) * ( radius + width )
	local endY = math.sin( math.rad( i ) ) * ( radius + width )
	
	dxDrawLine( startX + posX, startY + posY, endX + posX, endY + posY, color, width, postGUI )
    end
	
    return true
end

function isMouseInRing(posX, posY, radius, width, startAngle, stopAngle)
    if isCursorShowing() then
	local SX, SY = guiGetScreenSize(); -- You can remove this line if you already got SX and SY for the screenSize
		
	if (not posX or not posY or not radius) then
	    outputDebugString("isMouseInRing: Required arguments are missing", 1);
	    return false
	end
		
	if not (width) then
	    width = SX / 50;
	end
		
	if not (startAngle) then
	    startAngle = 0;
	end
		
	if not (stopAngle) then
	    stopAngle = 359.99;
	end
		
        local cx, cy = getCursorPosition();
        local cx, cy = cx * SX, cy * SY;		
	local iMouseRot = findRotation(posX, posY, cx, cy) + 90;
		
	if (iMouseRot > 360) then
	    iMouseRot = iMouseRot - 360;
	end
		
	local diffX = math.max(cx, posX) - math.min(cx, posX); -- Calculate the X-Axis difference between mouse and ring center
	local diffY = math.max(cy, posY) - math.min(cy, posY); -- Calculate the Y-Axis difference between mouse and ring center	
	local iMouseDistance = math.sqrt(diffX * diffX + diffY * diffY); -- Get the distance in pixels between mouse and ring center

	if (startAngle > stopAngle) then -- Exchange start- and stop angle if startAngle is bigger then the stopAngle
	    local temp = startAngle;
	    startAngle = stopAngle;
	    stopAngle = temp;
	end

	if (iMouseRot >= startAngle and iMouseRot <= stopAngle and iMouseDistance <= radius + width and iMouseDistance >= radius - width) then
	    return true -- The mouse is inside the ring-/part
	else
	    return false -- It's somewhere else
	end
    end
    outputDebugString("isMouseInRing: Cursor is not showing!", 1); -- Remove this line if you know your cursor shouldn't always be showing.
    return false -- Cursor is not showing
end

function findRotation( x1, y1, x2, y2 ) 
    local t = -math.deg( math.atan2( x2 - x1, y2 - y1 ) )
    return t < 0 and t + 360 or t
end
```

By: Ceeser

## Notes

**The shown example** needs way more resources then a simple [dxDrawRectangle](mta://scripting/client/functions/dxdrawrectangle.md) function. Using it too often may cause performance issues.

The cursor must be visible to use this function. See [showCursor](mta://scripting/shared/functions/showcursor.md).

[findRotation](mta://scripting/shared/functions/findrotation.md) is required to get the rotation of the cursor towards to the center of the ring.
