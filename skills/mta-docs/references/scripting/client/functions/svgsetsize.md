---
doc_id: "mta-wiki:13378"
title: "SvgSetSize"
source_title: "SvgSetSize"
source_url: "https://wiki.multitheftauto.com/wiki/SvgSetSize"
revision_id: 81324
language: "en"
categories: ["Client_functions", "Utility_templates"]
---

# SvgSetSize

Sets the underlying XML document from an SVG element.

| [[{{{image}}}\|link=\|]] | Important Note: Before r21155 ( 3157905 ) the provided callback wasn't stored on the SVG and was only fired once after the function had performed its task. This is no longer the case - each SVG can now store a single callback function (optional) which is fired every time the SVG texture has been changed/updated. |
| --- | --- |
|  |  |

## Syntax

```
bool svgSetSize( svg svgElement, int width, int height [, function callback ( element svg ) ] )
```

### Required Arguments

- **svgElement:** The svg element you want to set the size of.

- **width:** Desired width, preferably power of two (16, 32, 64 etc.), maximum is 4096

- **height :** Desired height, preferably power of two (16, 32, 64 etc.), maximum is 4096

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **callback:** A callback function which is stored on the SVG and fired every time the SVG texture is updated (for example, via [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md)). **Note**: if present, this will overwrite the current callback stored on the svg

### Returns

- Returns **true** if successful, **false** otherwise

## Example

This example creates an [svg](mta://reference/misc/svg.md) element including a keybind (F2) to resize the SVG randomly, with the use of callbacks to notify in debugscript when the SVG was updated.

```
-- This could also be a file, with the path provided to svgCreate instead
local rawSvgData = [[
    <svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
        <circle cx="250" cy="250" r="250" fill="#0fc0fc" />
    </svg>
]]

local svgs = {}

local function render(svg)
    if (not isElement(svg)) or (getElementType(svg) ~= "svg") then
        removeEventHandler("onClientRender", root, svgs[svg].handler)
        svgs[svg] = nil
    end

    local width, height = svgGetSize(svg)
    dxDrawImage(0, 0, width, height, svg, 0, 0, 0, tocolor(255, 255, 255), false)
end

local function onUpdate(svg)
    -- If this is the first update, add svg to our table and start drawing it
    if (not svgs[svg]) then
        svgs[svg] = {
            state = true,
            handler = function()
                render(svg)
            end
        }

        addEventHandler("onClientRender", root, svgs[svg].handler)
    end

    iprint("SVG texture updated", svg, getTickCount())
end

local function init()
    -- Create an SVG containing a circle, using the raw XML data above
    local mySvg = svgCreate(500, 500, rawSvgData, onUpdate)

    -- Bind a key to set SVG to a random size, which will trigger the onUpdate callback
    bindKey("F2", "down", function()
        setRandomSVGSize(mySvg)
    end)
end
addEventHandler("onClientResourceStart", resourceRoot, init)

function setRandomSVGSize(svg)
    local width, height = svgGetSize(svg)
    local diff = math.min(width, height) /  math.max(width, height)
    local size = math.random(100, 500)

    svgSetSize(svg, size, size * diff)
end
```

## See Also

- [svgCreate](mta://scripting/client/functions/svgcreate.md)

- [svgGetDocumentXML](mta://scripting/client/functions/svggetdocumentxml.md)

- [svgGetSize](mta://scripting/client/functions/svggetsize.md)

- [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md)

- svgSetSize

- [svgSetUpdateCallback](mta://scripting/client/functions/svgsetupdatecallback.md)
