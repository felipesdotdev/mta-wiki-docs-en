---
doc_id: "mta-wiki:7231"
title: "Resource : DxDraw3DText"
source_title: "Resource:DxDraw3DText"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ADxDraw3DText"
revision_id: 53300
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:17:00.340936+00:00"
---

# Resource : DxDraw3DText

This resource allow you to draw 3D-DX texts any where in the game. You need to add a Text to display only once.

## How it works

You need to use the exported function called **dxDraw3DText** to draw a text in the 3D world. (Use the exported function like this: exports.3d_dx_texts:dxDraw3DText)

## The dxDraw3DText function

### Syntax

```
element dxDraw3DText( string text, int x, int y, int z [, int scale = 2, string font = "default", int r = 255, int g = 255, int b = 255, int maxDistance = 12 ] )
```

### Required Arguments

- **text :** A [string](mta://reference/misc/string.md) representing the text you wish to draw .

- **x, y, z :** Three integers representing the world coordinates of where you want the text to be .

### Optional Arguments

- **scale :** An [int](mta://reference/misc/int.md) representing the size of the font .

- **font :** A [string](mta://reference/misc/string.md) representing the font type, This CAN'T be a [DX font](mta://reference/misc/dx-font.md) element, It can ONLY be :

- **"default":**  Tahoma

- **"default-bold":** Tahoma Bold

- **"clear":** Verdana

- **"arial":** Arial

- **"sans":** Microsoft Sans Serif

- **"pricedown":** Pricedown (GTA's theme text)

- **"bankgothic":** Bank Gothic Medium

- **"diploma":** Diploma Regular

- **"beckett":** Beckett Regular

- **"unifont":** Unifont

- **r, g, b :** Three integers representing the RGB Color codes for the text .

- **maxDistance :** An [int](mta://reference/misc/int.md) representing the max distance the text will show in .

### Returns

The function returns a *text element* if successfule, *false* otherwise .

### Example

This example will draw a 3D text near a player when the resource starts, And destroys it after 5 seconds .

```
local dxDraw3DText = exports.3D_DX_Texts:dxDraw3DText -- define the function

addEventHandler( "onClientResourceStart", getResourceRootElement( getThisResource( ) ),
	function( )
		local x, y, z = getElementPosition( getLocalPlayer( ) ) -- getting the player coordinates
		local playerName = getPlayerName( getLocalPlayer( ) ) -- getting the player name
		local theText = dxDraw3DText( "Welcome " .. playerName, x, y, z ) -- dtawing the text
		if theText then -- if it was drawn
			setTimer( destroyElement, 5000, 1, theText ) -- set a time to destroy it after 5 seconds
		end
	end
)
```

## Notes

- The *dxDraw3DText* function is client side only .

- The *dxDraw3DText* function doesn't need the [onClientRender](mta://scripting/client/events/onclientrender.md) event to work .

- The *dxDraw3DText* function only creates a *text element*, The drawing and stuff is done in the resource, So it MUST be running so the texts show .

## Download

You can download the resource, comment about it, rate it and report any bugs at the community page : [[1]](https://community.multitheftauto.com/index.php?p=resources&s=details&id=7613)

## Alternative Function

This alternative function is meant to be used directly with the eventHandler [onClientRender](mta://scripting/client/events/onclientrender.md).

### Syntax

```
bool dxDraw3DText( string text, int x, int y, int z [, int scale = 2, string font = "default", int color = white, int maxDistance = 12, bool colorCoded = false ] )
```

### Returns

The function return *true* and displays a *text* if successful, *false* otherwise.

### Required Arguments

- **text :** A [string](mta://reference/misc/string.md) representing the text you wish to draw .

- **x, y, z :** Three integers representing the world coordinates of where you want the text to be .

### Optional Arguments

- **scale :** An [int](mta://reference/misc/int.md) representing the size of the font .

- **font :** A [string](mta://reference/misc/string.md) representing the font type, This CAN'T be a [DX font](mta://reference/misc/dx-font.md) element, It can ONLY be :

- **"default":**  Tahoma

- **"default-bold":** Tahoma Bold

- **"clear":** Verdana

- **"arial":** Arial

- **"sans":** Microsoft Sans Serif

- **"pricedown":** Pricedown (GTA's theme text)

- **"bankgothic":** Bank Gothic Medium

- **"diploma":** Diploma Regular

- **"beckett":** Beckett Regular

- **"unifont":** Unifont

- **color:** the color of the text, a value produced by [tocolor](mta://scripting/shared/functions/tocolor.md) or 0xAARRGGBB (AA = alpha, RR = red, GG = green, BB = blue).

- **maxDistance :** An [int](mta://reference/misc/int.md) representing the max distance the text will show in .

- **colorCoded :** Set to true to enable embedded #FFFFFF color codes. **Note: clip and wordBreak are forced false if this is set.**

### Code

Click to collapse [-]
Client

```
function dxDraw3DText(text, x, y, z, scale, font, color, maxDistance, colorCoded)
	if not (x and y and z) then
		outputDebugString("dxDraw3DText: One of the world coordinates is missing", 1);
		return false;
	end

	if not (scale) then
		scale = 2;
	end
	
	if not (font) then
		font = "default";
	end
	
	if not (color) then
		color = tocolor(255, 255, 255, 255);
	end
	
	if not (maxDistance) then
		maxDistance = 12;
	end
	
	if not (colorCoded) then
		colorCoded = false;
	end
	
	local pX, pY, pZ = getElementPosition( localPlayer );	
	local distance = getDistanceBetweenPoints3D(pX, pY, pZ, x, y, z);
	
	if (distance <= maxDistance) then
		local x, y = getScreenFromWorldPosition(x, y, z);
		
		if (x and y) then
			dxDrawText( text, x, y, _, _, color, scale, font, "center", "center", false, false, false, colorCoded);
			return true;
		end
	end
end
```

By: Ceeser
