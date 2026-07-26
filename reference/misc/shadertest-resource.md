---
doc_id: "mta-wiki:5674"
title: "Shadertest resource"
source_title: "Shadertest resource"
source_url: "https://wiki.multitheftauto.com/wiki/Shadertest_resource"
revision_id: 49267
language: "en"
categories: []
generated_at: "2026-07-26T16:16:50.384113+00:00"
---

# Shadertest resource

Example resource for testing [shaders](mta://reference/misc/shader.md)

File layout:

```
shadertest
       meta.xml
       clientscript.lua
       clientshader.fx
       hurry.png
```

meta.xml contains this:

```
<meta>
    <script src="clientscript.lua" type="client" />
    <file src="clientshader.fx" type="client" />
    <file src="hurry.png" type="client" />
</meta>
```

clientscript.lua contains this:

```
addEventHandler("onClientResourceStart", resourceRoot,
    function()
        myShader,tecName = dxCreateShader( "clientshader.fx" )
        myImage = dxCreateTexture( "hurry.png" )
        if myShader and myImage then
            dxSetShaderValue( myShader, "tex0", myImage )
            outputChatBox( "Shader using techinque " .. tecName )
        else
            outputChatBox( "Problem - use: debugscript 3" )
        end
    end
)

addEventHandler( "onClientRender", root,
    function()
        if myShader then
             dxDrawImage( 200, 300, 400, 200, myShader, 0, 0, 0, tocolor(255,255,0) )
        end
   end
)
```

clientshader.fx contains this:

```
// Insert your fabulous crap here
```

hurry.png is copied from the race resource. i.e. **race/img/hurry.png**
