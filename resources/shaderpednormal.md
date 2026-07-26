---
doc_id: "mta-wiki:7280"
title: "Resource : ShaderPedNormal"
source_title: "Resource:ShaderPedNormal"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AShaderPedNormal"
revision_id: 40568
language: "en"
categories: ["Resource"]
generated_at: "2026-07-26T16:17:14.315933+00:00"
---

# Resource : ShaderPedNormal

This is a normal map resource for MTA. It enables normal mapping effect for peds. Also adds sun and moon light to make gtasa lighting a bit more interesting. It is compatible with the peds created to work with normalmap plugin for gtasa.

## Overview

You'll have to extract normals from the txd file and apply them with the applyNormalToPedTexture function.

This test resource should present a better explanation. [Download here](http://www.solidfiles.com/d/be237103ee/) Choose (!SKIN ID 7!) after starting.

The resource itself adds exported clientside functions:

## Exported functions

#### applyNormalToPedTexture

Click to collapse [-]
Client

This function applies the normal mapping effect to ped textures.

```
bool exports.shaderPedNormal:applyNormalToPedTexture( table filepath strings )
```

### Required Arguments

- **filepath strings:** The table of filepaths to apply. Those should be paths for the normals extracted from the txd archive.

### Returns

The function returns true if set successfully, false otherwise.

#### removeNormalFromPedTexture

Click to collapse [-]
Client

This function removes the normal mapping effect from ped textures.

```
bool exports.shaderPedNormal:removeNormalFromPedTexture( table filepath strings )
```

### Required Arguments

- **filepath strings:** The table of previously applied normals to be disabled.

### Returns

The function returns true if set successfully, false otherwise.

#### applySpecularToGTAPeds

Click to collapse [-]
Client

This function applies a custom specular lighting effect to ped by ID.

```
bool exports.shaderPedNormal:applySpecularToGTAPeds(table ped model id table,bool sobel)
```

### Optional Arguments

- **ped model id table:** The ped model id table If left blank the effect is applied to all standard ped textures.

- **sobel:** The second argument generates normals based on original textures if set true. Sobel filter works only when your graphics card supports shader model 3.

### Returns

The function returns true if set successfully, false otherwise.

#### removeSpecularFromGTAPeds

Click to collapse [-]
Client

This function removes custom specular lighting effect from ped by ID.

```
bool exports.shaderPedNormal:removeSpecularFromGTAPeds(table ped model ids)
```

### Optional Arguments

- **ped model ids:** the ped model id table If left blank the effect is removed from all ped textures.

### Returns

The function returns true if set successfully, false otherwise.

## Examples

```
local resourceName = ":"..getResourceName(getThisResource()).."/" 
exports.shaderPedNormal:applyNormalToPedTexture({resourceName.."normals/face_nrm1.0.png",resourceName.."normals/skin_nrm1.0.png"})
```

This applies normal map effect to textures "face" and "skin". Notice that the nrm textures should be placed in the resource the function is being called from.

```
exports.shaderPedNormal:applySpecularToGTAPeds({0,7,121},false)
```

This applies the specular effect to peds by id 0,7,121

```
exports.shaderPedNormal:removeSpecularFromGTAPeds()
```

removes the specular effect from all the peds.

Of course when you want to use theese functions in your resources you have to include
the ShaderPedNormal resource in meta.

## See Also

[Resource page on community.mtasa](https://community.multitheftauto.com/index.php?p=resources&s=details&id=7665)
