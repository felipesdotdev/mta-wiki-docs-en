---
doc_id: "mta-wiki:5677"
title: "DxCreateShader"
source_title: "CreateShader"
source_url: "https://wiki.multitheftauto.com/wiki/CreateShader"
revision_id: 76190
language: "en"
categories: ["Client_functions", "Changes_in_1.6.0"]
generated_at: "2026-07-26T16:11:27.767224+00:00"
---

# DxCreateShader

This function creates a [shader](mta://reference/misc/shader.md) element that can be used in the dxDraw functions. Successful shader creation is not guaranteed unless the [Effect File](mta://reference/misc/shader.md) contains a fallback technique which will work on every existing PC.

| [[{{{image}}}\|link=\|]] | Note: It is highly recommended that dxSetTestMode is used when writing and testing scripts using dxCreateShader. |
| --- | --- |
|  |  |

BEFORE VERSION 1.5.8 [r20688](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=20688):

## Syntax

```
element, string dxCreateShader ( string filepath / string raw_data [, float priority = 0, float maxDistance = 0, bool layered = false, string elementTypes = "world,ped,vehicle,object,other,all" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DxShader](mta://reference/misc/shader.md)(...)*

### Required Arguments

- **filepath / raw_data:** The filepath of the [shader Effect File](mta://reference/misc/shader.md) (.fx) file or whole data buffer of the shader file

### Optional Arguments

*All the following optional arguments are only relevant when the shader is used with [engineApplyShaderToWorldTexture](mta://scripting/client/functions/engineapplyshadertoworldtexture.md)*

- **priority:** If more than one shader is matched to a world texture, the shader with the highest priority will be used. If there is more than one shader with the same highest priority, the most recently created shader is used.

- **maxDistance:** If non-zero, the shader will be applied to textures nearer than maxDistance only. This can speed up rendering, but (to look good) may require the shader to fade out it's own effect as the texture reaches maxDistance.

- **layered:** When set to true, the shader will be drawn in a separate render pass. Several layered shaders can be drawn on the same world texture. (To avoid [Z fighting](http://en.wikipedia.org/wiki/Z-fighting) artifacts, you may have to add **DepthBias=-0.0002;** to the technique pass, but this might cause visual artifacts when applied on vehicles)

- **elementTypes:** A comma seperated list of element types to restrict this shader to. Valid element types are:

- world - Textures in the GTA world

- ped - Player and ped textures

- vehicle - Vehicles textures

- object - Objects textures

- other - Element textures which are not peds, vehicles or objects

- all - Everything

### Returns

- **element:** A [shader](mta://reference/misc/shader.md) element if successful, *false* if invalid arguments were passed to the function. **You should always check to see if this function has returned false.**

- **string:** The name of the technique that will be used.

## Syntax

```
element, string dxCreateShader ( string filepath / string raw_data [ [, table macros = {} ], float priority = 0, float maxDistance = 0, bool layered = false, string elementTypes = "world,ped,vehicle,object,other,all" ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[DxShader](mta://reference/misc/shader.md)(...)*

### Required Arguments

- **filepath / raw_data:** The filepath of the [shader Effect File](mta://reference/misc/shader.md) (.fx) file or whole data buffer of the shader file

### Optional Arguments

*All the following optional arguments are only relevant when the shader is used with [engineApplyShaderToWorldTexture](mta://scripting/client/functions/engineapplyshadertoworldtexture.md)*

- **macros:** A table contains macros in an ordered and/or unordered way. See example below.

- **priority:** If more than one shader is matched to a world texture, the shader with the highest priority will be used. If there is more than one shader with the same highest priority, the most recently created shader is used.

- **maxDistance:** If non-zero, the shader will be applied to textures nearer than maxDistance only. This can speed up rendering, but (to look good) may require the shader to fade out it's own effect as the texture reaches maxDistance.

- **layered:** When set to true, the shader will be drawn in a separate render pass. Several layered shaders can be drawn on the same world texture. (To avoid [Z fighting](http://en.wikipedia.org/wiki/Z-fighting) artifacts, you may have to add **DepthBias=-0.0002;** to the technique pass, but this might cause visual artifacts when applied on vehicles)

- **elementTypes:** A comma seperated list of element types to restrict this shader to. Valid element types are:

- world - Textures in the GTA world

- ped - Player and ped textures

- vehicle - Vehicles textures

- object - Objects textures

- other - Element textures which are not peds, vehicles or objects

- all - Everything

### Returns

- **element:** A [shader](mta://reference/misc/shader.md) element if successful, *false* if invalid arguments were passed to the function. **You should always check to see if this function has returned false.**

- **string:** The name of the technique that will be used.

## Example

```
addEventHandler( "onClientRender", root,
    function()
        if myShader then
            dxDrawImage( 100, 350, 300, 350, myShader )
        end
    end
)

-- Use 'toggle' command to switch shader on and off
addCommandHandler( "toggle",
    function()
        if not myShader then
            myShader = dxCreateShader( "fancything.fx" )  -- Create shader
        else        
            destroyElement( myShader )                    -- Destroy shader
            myShader = nil
        end
    end
)
```

This example creates basic shader from raw data (without i/o) on resource start:

```
local myShader_raw_data = [[
	texture tex;
	technique replace {
		pass P0 {
			Texture[0] = tex;
		}
	}
]]

addEventHandler("onClientResourceStart", resourceRoot, function()
	local myShader = dxCreateShader(myShader_raw_data) -- create shader from raw data
	if isElement(myShader) then
		local myTexture = dxCreateTexture("some_image.png") -- create texture from image file
		if isElement(myTexture) then
			-- apply image to world texture via shader
			dxSetShaderValue(myShader, "tex", myTexture)
			engineApplyShaderToWorldTexture(myShader, "shad_ped")
		else
			outputDebugString("Unable to load texture", 1)
		end
	else
		outputDebugString("Unable to create shader", 1)
	end
end)
```

You can pass raw data (shader code) directly into the function (example uses variable *myShader_raw_data*).

This example creates a basic shader using macros to change shader's behaviour:

```
local shaderRawStr = [[
    texture MACRO_TEX_NAME;

    technique simple
    {
        pass P0
        {
            //-- Set up texture stage 0
            Texture[0] = MACRO_TEX_NAME;
	    ColorOp[0] = SelectArg1;
	#ifdef MACRO_FIRST_ARG
	    ColorArg1[0] = Texture;
	#else
	    ColorArg1[0] = Diffuse;
	#endif
	    AlphaOp[0] = SelectArg1;
	    AlphaArg1[0] = Texture;
                
            //-- Disable texture stage 1
            ColorOp[1] = Disable;
            AlphaOp[1] = Disable;
        }
    }
]]

addEventHandler( "onClientResourceStart", resourceRoot,
    function ( )
        local shader, tech = dxCreateShader( shaderRawStr,  { MACRO_TEX_NAME = "Tex0",  MACRO_FIRST_ARG = true } )
        if not shader or tech ~= "simple" then
            outputDebugString( "An error was occured" )
	    return
        end	
        
        local texture = dxCreateTexture( "test.png" )
        if not texture then
	    outputDebugString( "An error was occured" )
	    return
	end

	dxSetShaderValue( shader, "Tex0", texture )
		
	addEventHandler( "onClientRender", root,
	    function()
	        dxDrawImage( 0, 0, 500, 500, shader )
	    end
	, false )
    end
, false )
```

You can also pass macros in key-value pairs when the order is important.

## Changelog

| Version | Description |
| --- | --- |

| 1.3.0-9.04435 | Added layered and elementTypes arguments |
| --- | --- |

| 1.5.6-9.14403 | Added option to use raw data instead of a file name |
| --- | --- |

| 1.5.8-9.20688 | Added option to use macros |
| --- | --- |

## See Also

- [dxConvertPixels](mta://scripting/client/functions/dxconvertpixels.md)

- [dxCreateFont](mta://scripting/client/functions/dxcreatefont.md)

- [dxCreateRenderTarget](mta://scripting/client/functions/dxcreaterendertarget.md)

- [dxCreateScreenSource](mta://scripting/client/functions/dxcreatescreensource.md)

- dxCreateShader

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
