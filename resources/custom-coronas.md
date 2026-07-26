---
doc_id: "mta-wiki:7777"
title: "Resource : Custom coronas"
source_title: "Resource:Custom coronas"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ACustom_coronas"
revision_id: 50142
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:10.770435+00:00"
---

# Resource : Custom coronas

This resource lets You create some coronas. Not just your typical gtasa coronas 
that often times fail to appear. Since in this case corona Elements are created using
dxDrawMaterialLine3d MTA function. I have changed the behaviour of the material 
to act as cylindrical billboards do.

## Overview

It is easy to use, gives a few options to manage coronas.

The resource itself adds exported clientside functions:

## Exported functions

#### createCorona

Click to collapse [-]
Client

This function creates a shadered materialLine3d Corona.

```
coronaElement exports.custom_coronas:createCorona(float posX,posY,posZ,size,int colorR,colorG,colorB,colorA,[bool isSoftParticle = false])
```

### Required Arguments

- **float posX, posY, posZ:** Position in world space.

- **float size:** Size of the corona.

- **int colorR,colorG,colorB,colorA:** RGBA color (0 - 255).

### Optional Arguments

- **bool isSoftParticle:** The aim with soft particles is to remove the ugly artifact that appears when the particle quad intersects the scene. The option requires DepthBuffer access.

### Returns

The function returns coronaElement if set successfully, false otherwise.

#### createMaterialCorona

Click to collapse [-]
Client

This function creates a shadered materialLine3d Corona with a custom material.

```
coronaElement exports.custom_coronas:createMaterialCorona(element material,float posX,posY,posZ,size,int colorR,colorG,colorB,colorA,[bool isSoftParticle = false])
```

### Required Arguments

- **element material:** Material to replace the standard corona texture with.

- **float posX, posY, posZ:** Position in world space.

- **float size:** Size of the corona.

- **int colorR,colorG,colorB,colorA:** RGBA color (0 - 255).

### Optional Arguments

- **bool isSoftParticle:** The aim with soft particles is to remove the ugly artifact that appears when the particle quad intersects the scene. The option requires DepthBuffer access.

### Returns

The function returns coronaElement if set successfully, false otherwise.

#### destroyCorona

Click to collapse [-]
Client

This function destroys a shadered materialLine3d Corona element.

```
bool exports.custom_coronas:destroyCorona(element coronaElement)
```

### Required Arguments

- **element coronaElement:** A previously declared corona element.

### Returns

The function returns true if set successfully, false otherwise.

#### setCoronaMaterial

Click to collapse [-]
Client

This function sets custom material for the corona.

```
bool exports.custom_coronas:setCoronaMaterial(element coronaElement,element material)
```

### Required Arguments

- **element coronaElement:** A previously declared corona element.

- **element material:** Material to replace the standard corona texture with.

### Returns

The function returns true if set successfully, false otherwise.

#### setCoronaSize

Click to collapse [-]
Client

This function sets size of the corona.

```
bool exports.custom_coronas:setCoronaSize(element coronaElement,float size)
```

### Required Arguments

- **element coronaElement:** A previously declared corona element.

- **float size:** Size of the corona.

### Returns

The function returns true if set successfully, false otherwise.

#### setCoronaSizeXY

Click to collapse [-]
Client

This function sets size of the corona (width and height).

```
bool exports.custom_coronas:setCoronaSizeXY(element coronaElement,float width,height)
```

### Required Arguments

- **element coronaElement:** A previously declared corona element.

- **float width, height:** Size of the corona.

### Returns

The function returns true if set successfully, false otherwise.

#### setCoronaDepthBias

Click to collapse [-]
Client

On createCorona the depthBias is set properly (0-1). You can however set other value depending on your needs. To see the results you'll need to set enableDepthBiasScale to true.

```
bool exports.custom_coronas:setCoronaDepthBias(element coronaElement,float depthBiasValue)
```

### Required Arguments

- **element coronaElement:** A previously declared corona element.

- **float depthBiasValue:** depthBias value.

### Returns

The function returns true if set successfully, false otherwise.

#### setCoronaPosition

Click to collapse [-]
Client

This function sets corona position.

```
bool exports.custom_coronas:setCoronaPosition(element coronaElement,float posX,posY,posZ)
```

### Required Arguments

- **element coronaElement:** A previously declared corona element.

- **float posX, posY, posZ:** Position in world space.

### Returns

The function returns true if set successfully, false otherwise.

#### setCoronaColor

Click to collapse [-]
Client

This function sets light color values.

```
bool exports.custom_coronas:setCoronaColor(element coronaElement,float colorR,colorG,colorB,colorA)
```

### Required Arguments

- **element coronaElement:** A previously declared corona element.

- **float colorR,colorG,colorB,colorA:** RGBA color (0 - 255).

### Returns

The function returns true if set successfully, false otherwise.

#### setCoronasDistFade

Click to collapse [-]
Client

Set the Max distance of the corona to sync and the distance on which the it starts to fade out.

```
bool exports.custom_coronas:setCoronasDistFade(int MaxEffectFade,int MinEffectFade)
```

### Required Arguments

- **int MaxEffectFade:** Set the Max distance of the corona to sync.(Must be greater than MinEffectFade).

- **int MinEffectFade:** Set the distance on which the corona starts to fade out.

### Returns

The function returns true if set successfully, false otherwise.

#### enableDepthBiasScale

Click to collapse [-]
Client

Standard depthBias for GTASA coronas is about 1 unit, despite the corona scale. This function elables depthBias scaling.

```
bool exports.custom_coronas:enableDepthBiasScale(bool isDepthScaleEnabled)
```

### Required Arguments

- **bool isDepthScaleEnabled:** Enable/disable depthBias scaling.

### Returns

The function returns true if set successfully, false otherwise.

## Examples

```
function addStuff()
	for i=1,30 do
		for j=1,30 do
			exports.custom_coronas:createCorona(i * 7,j * 7,10,4,math.random()*255,math.random()*255,math.random()*255,1*255,false) 
		end	
	end
end

addEventHandler("onClientResourceStart", getResourceRootElement( getThisResource()), addStuff)
```

This creates a 400 coronas near position (0,0,0)

```
local vehicle1 = nil
addEventHandler("onClientVehicleEnter", getRootElement(),
    function(thePlayer, seat)
        if thePlayer == getLocalPlayer() then
            vehicle1 = source
        end
    end
)

local carLight = exports.custom_coronas:createCorona(0,0,0,4,math.random()*255,math.random()*255,math.random()*255,1*255)
addEventHandler("onClientPreRender", root, function()
	if vehicle1 then 
		xxx1,yyy1,zzz1 = getElementPosition(vehicle1)
		exports.custom_coronas:setCoronaPosition(carLight,xxx1,yyy1,zzz1)
	end
end
)
```

This creates a corona and attaches it to a vehicle that the player enters.

Of course when you want to use these functions in your resources you have to include
the custom_coronas resource in meta.

## See Also

[A youtube video](http://www.youtube.com/watch?v=5lruyY1fviQ)

[Custom Coronas resource on MTA Community](http://community.multitheftauto.com/index.php?p=resources&s=details&id=9558)

[WebGL Orthographic 3D](http://www.html5rocks.com/en/tutorials/webgl/webgl_orthographic_3d)
