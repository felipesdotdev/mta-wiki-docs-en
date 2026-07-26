---
doc_id: "mta-wiki:13373"
title: "SvgCreate"
source_title: "SvgCreate"
source_url: "https://wiki.multitheftauto.com/wiki/SvgCreate"
revision_id: 81320
language: "en"
categories: ["Client_functions", "Utility_templates"]
generated_at: "2026-07-26T16:16:54.265566+00:00"
---

# SvgCreate

Creates an [svg](mta://reference/misc/svg.md) from size (blank document), filepath or raw data.

| [[{{{image}}}\|link=\|]] | Important Note: Before r21155 ( 3157905 ) the provided callback was only fired once after the function had performed its task. This is no longer the case - each SVG can now store a single callback function (optional) which is fired every time the SVG texture has been changed/updated. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: SVG in MTA is handled by the lunasvg rendering engine - Some features in MTA may not work properly, compared to the browser. |
| --- | --- |
|  |  |

*Check the list of supported [features](https://github.com/sammycage/lunasvg?tab=readme-ov-file#features).'*

| [[{{{image}}}\|link=\|]] | Tip: If you are experiencing poor texture quality or artifacts in the form of black outlines, setting the blend mode to add might help |
| --- | --- |
|  |  |

## Syntax

```
svg svgCreate ( int width, int height [, string pathOrRawData, function callback ( element svg ) ] )
```

### Required Arguments

- **width:** Desired width, preferably power of two (16, 32, 64 etc.), maximum is 4096

- **height :** Desired height, preferably power of two (16, 32, 64 etc.), maximum is 4096

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **pathOrRawData:** A string representing the path to your SVG file, or the raw SVG data

- **callback:** A callback function which is stored on the SVG and fired every time the SVG texture is updated (for example, via [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md)).

**Note:** See [svgSetUpdateCallback](mta://scripting/client/functions/svgsetupdatecallback.md) for setting an svg's callback function after it has been created.

### Returns

- Returns an [svg](mta://reference/misc/svg.md) if created successfully, *false* otherwise.

## Example

This is a basic example of how you can create an SVG from raw data (or path) and draw it with [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md) via [onClientRender](mta://scripting/client/events/onclientrender.md).

```
-- This could also be a file, with the path provided to svgCreate instead
local rawSvgData = [[
    <svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
        <circle cx="250" cy="250" r="250" fill="#0fc0fc" />
    </svg>
]]

local myCircleSvg

local function drawCircleSvg()
    dxDrawImage(0, 0, 500, 500, myCircleSvg, 0, 0, 0, tocolor(255, 255, 255), false)
end

local function init()
    -- Create an SVG containing a circle, using the raw XML data above
    myCircleSvg = svgCreate(500, 500, rawSvgData)
    addEventHandler("onClientRender", root, drawCircleSvg)
end
addEventHandler("onClientResourceStart", resourceRoot, init)
```

Here's another, more in-depth example which utilizes the callback argument. You can use the F2 key to set the SVG to a random size and see the update callback output a message to debugscript.

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

- svgCreate

- [svgGetDocumentXML](mta://scripting/client/functions/svggetdocumentxml.md)

- [svgGetSize](mta://scripting/client/functions/svggetsize.md)

- [svgSetDocumentXML](mta://scripting/client/functions/svgsetdocumentxml.md)

- [svgSetSize](mta://scripting/client/functions/svgsetsize.md)

- [svgSetUpdateCallback](mta://scripting/client/functions/svgsetupdatecallback.md)
