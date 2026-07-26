---
doc_id: "mta-wiki:5676"
title: "DxCreateTexture"
source_title: "CreateTexture"
source_url: "https://wiki.multitheftauto.com/wiki/CreateTexture"
revision_id: 73985
language: "en"
categories: ["Client_functions", "Utility_templates", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:11:27.729836+00:00"
---

# DxCreateTexture

This function creates a [texture](mta://reference/misc/texture.md) element that can be used in the dxDraw functions.

| [[{{{image}}}\|link=\|]] | Important Note: This function uses significant process RAM, make sure you don't load a lot of textures, because you'll run out of memory and crash MTA on your gaming PC beyond the technical limit of 3.5 GB (weak PC users much earlier). Besides that, don't make the common mistake of causing a memory leak by not destroying textures (causing dxTextures to pile up) when they should no longer display per your script, which causes FPS lag and crashes all over MTA due to so many scripters missing it |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: The times shown at the right of the page are only the time needed to add the thing to the draw queue, its not the actual time it takes to draw them. |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: It is recommended to pre-convert textures to whatever format you want to load them as. ARGB should be PNG, all other formats are self explanatory. By doing this you can load textures on the fly without any hickups (Note: There might still be some if the user has a slow HHD). See DirectXTex texconv tool . |
| --- | --- |
|  |  |

 
A speedtest showing the performance of a texture created with various settings of textureFormat.[Mipmaps = true][textureEdge = "wrap"]

 
A speedtest showing the performance of a texture created with various settings of textureFormat.[Mipmaps = false][textureEdge = "wrap"]

It is possible to use dxCreateTexture to load cubemaps and volume textures, but these will only be useable as inputs for a shader. The Microsoft utility [DxTex](http://nightly.mtasa.com/files/shaders/DxTex.zip) can view and change cubemaps and volume textures. DxTex can also convert standard textures into DXT1/3/5 compressed .dds which should reduce file sizes.

## Syntax

```
element dxCreateTexture ( string pixels / string filepath [, string textureFormat = "argb", bool mipmaps = true, string textureEdge = "wrap" ] )
```

```
element dxCreateTexture ( int width, int height [, string textureFormat = "argb", string textureEdge = "wrap", string textureType = "2d", int depth = 1 ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DxTexture](mta://reference/misc/texture.md)(...)*

### Required Arguments

- **filepath:** The filepath of the image. (.bmp, .dds, .jpg, .png, and .tga images are supported). Image files should ideally have dimensions that are a power of two, to prevent possible blurring.

or

- **pixels:** [Pixels](mta://reference/misc/texture-pixels.md) containing image data. ('plain', 'jpeg' or 'png' pixels can be used here)

or

- **width:** Desired width, preferably power of two (16, 32, 64 etc.), maximum is 16384

- **height :** Desired height, preferably power of two (16, 32, 64 etc.), maximum is 16384

### Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **textureFormat :** A string representing the desired texture format, which can be one of:

- **"argb"** : ARGB uncompressed 32 bit color (default).

- **"dxt1"** : DXT1 compressed - Can take a fraction of a second longer to load (unless the file is already a DXT1 .dds). Uses 8 times less video memory than ARGB and **can speed up drawing**. Quality not as good as ARGB. **It supports alpha blending, but it can only be on or off, that is: either 0 or 255.**

- **"dxt3"** : DXT3 compressed - Can take a fraction of a second longer to load (unless the file is already a DXT3 .dds). Uses 4 times less video memory than ARGB and **can speed up drawing**. Quality slightly better than DXT1 and supports crisp alpha blending.

- **"dxt5"** : DXT5 compressed - Can take a fraction of a second longer to load (unless the file is already a DXT5 .dds). Uses 4 times less video memory than ARGB and **can speed up drawing**. Quality slightly better than DXT1 and supports smooth alpha blending.

- **mipmaps :** True to create a mip-map chain so the texture looks good when drawn at various sizes.

- **textureEdge :** A string representing the desired texture edge handling, which can be one of:

- **"wrap"** : Wrap the texture at the edges (default)

- **"clamp"** : Clamp the texture at the edges. This may help avoid edge artifacts.

- **"mirror"** : Mirror the texture at the edges.

- **textureType :** A string representing the desired texture type, which can be one of:

- **"2d"** : Standard texture (default)

- **"3d"** : Volume texture

- **"cube"** : Cube map

- **depth:** Desired number of slices when creating a volume texture

## Returns

Returns a [texture](mta://reference/misc/texture.md) if successful, *false* if invalid arguments were passed to the function.

## Example

```
addEventHandler( "onClientRender", root,
    function()
        if myImage then
            dxDrawImage( 100, 350, 300, 350, myImage  )
        end
    end
)

-- Use 'toggle' command to switch image on and off
addCommandHandler( "toggle",
    function()
        if not myImage then
            myImage = dxCreateTexture( "moonpig.png" )  -- Create texture
        else        
            destroyElement( myImage )                 -- Destroy texture
            myImage = nil
        end
    end
)
```

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04021 | Added textureType and depth argument |
| --- | --- |

| 1.3.0-9.04035 | Added textureEdge argument |
| --- | --- |

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md)

- [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md)

- [dxCreateScreenSource](mta://scripting/client/functions/dxcreatescreensource.md)

- [dxCreateShader](mta://scripting/client/functions/dxcreateshader.md)

- dxCreateTexture

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

- [dxDrawPrimitive](mta://scripting/client/functions/dxdrawprimitive.md)

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
