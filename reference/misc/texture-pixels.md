---
doc_id: "mta-wiki:6057"
title: "Texture pixels"
source_title: "Texture pixels"
source_url: "https://wiki.multitheftauto.com/wiki/Texture_pixels"
revision_id: 81896
language: "en"
categories: []
generated_at: "2026-07-26T16:16:58.137222+00:00"
---

# Texture pixels

Pixels

***** MTA refers to the raw information that a [texture](mta://reference/misc/texture.md) contains as 'pixels'.

***** Pixels can be retrieved from any [texture](mta://reference/misc/texture.md) type including [render targets](mta://scripting/client/functions/dxcreaterendertarget.md) and [screen sources](mta://scripting/client/functions/dxcreatescreensource.md) by using the function [dxGetTexturePixels](mta://scripting/client/functions/dxgettexturepixels.md).

***** Pixels are just a string to Lua, so they can be saved to a file or even sent over the 'internet'.

#### Pixels properties

Pixels have two properties:

- **dimensions** (width and height) which is retrieved by using the function [dxGetPixelsSize](mta://scripting/client/functions/dxgetpixelssize.md)

- **format** (plain,jpeg,png,dds) which is retrieved by using the function [dxGetPixelsFormat](mta://scripting/client/functions/dxgetpixelsformat.md)

- *plain* - Fastest and simplest - It's default format of the pixels returned by [dxGetTexturePixels](mta://scripting/client/functions/dxgettexturepixels.md) and the only one that can be used with [dxSetTexturePixels](mta://scripting/client/functions/dxsettexturepixels.md), [dxGetPixelColor](mta://scripting/client/functions/dxgetpixelcolor.md) and [dxSetPixelColor](mta://scripting/client/functions/dxsetpixelcolor.md). But it also uses a lot of bytes, so internet transfers will be longer. Also can't be read by Photoshop or browsers etc.

- *png* - A few less bytes, still quite big for net transfers. Can be saved to a file and read by Photoshop and browsers etc.

- *jpeg* - A lot less bytes, so best for net transfers. Can be saved to a file and read by Photoshop and browsers etc.

- *dds* - DirectDraw Surface. Game's native texture format with various compressed and uncompressed options. Used to store standard, cube or volume textures. Compressed pixels in this format can be loaded nearly instantly by [dxCreateTexture](mta://scripting/client/functions/dxcreatetexture.md).

To convert between the 3 different formats, use the function [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

#### Pixels more

Pixels can also be loaded from any png/jpeg file just like this:

```
local fileHandler = fileOpen("hello.jpg")

if (not fileHandler) then
	return false
end

local fileSize = fileGetSize(fileHandler)
local filePixels = fileRead(fileHandler, fileSize)

fileClose(fileHandler)
```

Pixels can be used to create textures just like this:

```
local newTexture = dxCreateTexture(pixelsData)
```

Pixels can be used to save textures just like this:

```
local texturePixels = dxGetTexturePixels(myRenderTarget)
local texturePixelsConverted = dxConvertPixels(texturePixels, "jpeg")
local fileHandler = fileCreate("piccy.jpg")

if (not fileHandler) then
	return false
end

fileWrite(fileHandler, texturePixelsConverted)
fileClose(fileHandler)
```

#### Pixels performance

Getting/setting pixels from textures is not quick and not something you want to be doing every frame (in onClientRender for example).
Setting pixels to a render target is especially slow. Pixels are ideal however for transferring composite images built on a render target into a normal texture for later use. For example, making a custom radar map.
