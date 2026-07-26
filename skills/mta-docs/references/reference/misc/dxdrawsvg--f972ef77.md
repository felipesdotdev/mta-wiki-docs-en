---
doc_id: "mta-wiki:14612"
title: "DxDrawSVG"
source_title: "DxDrawSVG"
source_url: "https://wiki.multitheftauto.com/wiki/DxDrawSVG"
revision_id: 82403
language: "en"
categories: []
---

# DxDrawSVG

Description

Draws an SVG image on screen using dxDrawImage, with automatic caching.  
Supports both raw SVG strings and external .svg files from the resource folder.

- - This function runs on the client-side.**

## Syntax

```
dxDrawSVG(x, y, width, height, svgPathOrCode [, rotation = 0], [rotationCenterX = 0], [rotationCenterY = 0], [color = white], [postGUI = false])
```

## Required Arguments

- **x**: *float* – X position on screen.

- **y**: *float* – Y position on screen.

- **width**: *float* – Width of the image.

- **height**: *float* – Height of the image.

- **svgPathOrCode**: *string* – Raw SVG code or a file path to `.svg`.

## Optional Arguments

- **rotation**: *float* – Rotation in degrees.

- **rotationCenterX**: *float* – Rotation center X.

- **rotationCenterY**: *float* – Rotation center Y.

- **color**: *int* – Color (use tocolor()).

- **postGUI**: *bool* – Whether to draw after GUI.

## Code (Client-side)

```
local HsoData = {}

function dxDrawSVG(x, y, w, h, rawOrPath, ...)
    if not HsoData[rawOrPath] then
        if fileExists(rawOrPath) then
            local file = fileOpen(rawOrPath)
            if file then
                local content = fileRead(file, fileGetSize(file))
                fileClose(file)
                HsoData[rawOrPath] = svgCreate(w, h, content)
            end
        else
            HsoData[rawOrPath] = svgCreate(w, h, rawOrPath)
        end
    end

    if HsoData[rawOrPath] then
        dxSetBlendMode('add')
        dxDrawImage(x, y, w, h, HsoData[rawOrPath], ...)
        dxSetBlendMode('blend')
    end
end
```

## Example: Raw SVG string

```
dxDrawSVG(400, 200, 128, 128, [[
<svg width="128" height="128" xmlns="http://www.w3.org/2000/svg">
  <circle cx="64" cy="64" r="60" stroke="white" stroke-width="8" fill="blue" />
</svg>
]], 0, 0, 0, tocolor(255, 255, 255, 200))
```

## Example: SVG file

**meta.xml:**

```
<file src="files/icon.svg" />
```

**Lua:**

```
dxDrawSVG(400, 200, 64, 64, "files/icon.svg", 0, 0, 0, tocolor(255, 255, 255, 255))
```

## Notes

- Supports both raw SVG content and external SVG files.

- Automatically caches each unique SVG to improve performance.

- Some complex SVGs may not be fully supported by svgCreate.

- This function should be used on the **client-side** only.

## See also

- [dxDrawImage](mta://scripting/client/functions/dxdrawimage.md)

- [svgCreate](mta://scripting/client/functions/svgcreate.md)

- [Useful functions](https://wiki.multitheftauto.com/index.php?title=Useful_functions&action=edit&redlink=1)

## Credits

- Function by **Hussein Ali**

Instagram : pkw_3****
