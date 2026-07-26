---
doc_id: "mta-wiki:5584"
title: "Modules/Functions/gd info"
source_title: "Modules/Functions/gd info"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/Functions/gd_info"
revision_id: 25270
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.751609+00:00"
---

# Modules/Functions/gd info

|  | This function is provided by the external module Texturizer . You must install this module to use this function. |
| --- | --- |
|  |  |

Gets a table of the info about the GD libary which the module is compiled against.

## Syntax

```
table gd_info ( )
```

### Required arguments

### Returns

The following table of gd info:

```
string GD Version: The version string of the GD libary the module is compiled against.
```

## Example

**Example 1:** This example displays the gd version to joining players

```
gdInfo = gd_info();

function gdVersion ( )
   outputDebugString(gdInfo["GD Version"], source);
end

addEventHandler("onPlayerJoin", getRootElement(), gdVersion)
```

## See also

### Texture Functions

- [createTxdContainer](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/createTxdContainer&action=edit&redlink=1)

- [txdContainerAddImage](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/txdContainerAddImage&action=edit&redlink=1)

- [saveTxdContainer](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/saveTxdContainer&action=edit&redlink=1)

### GD Functions

- gd_info

#### Create

- [imageCreate](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageCreate&action=edit&redlink=1)

- [imageCreateTrueColor](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageCreateTrueColor&action=edit&redlink=1)

- [imageCreateFromPng](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageCreateFromPng&action=edit&redlink=1)

- [imageCreateFromGif](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageCreateFromPng&action=edit&redlink=1)

- [imageCreateFromJpeg](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageCreateFromPng&action=edit&redlink=1)

#### Info

- [imageSX](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSX&action=edit&redlink=1)

- [imageSY](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSY&action=edit&redlink=1)

- [imageIsTrueColor](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageIsTrueColor&action=edit&redlink=1)

#### Save

- [imagePng](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imagePng&action=edit&redlink=1)

- [imageGif](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imagePng&action=edit&redlink=1)

- [imageJpeg](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imagePng&action=edit&redlink=1)

#### Cleanup

- [imageDestroy](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageDestroy&action=edit&redlink=1)

- [imageCleanup](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageCleanup&action=edit&redlink=1)

#### Alter

- [imageGetAlphaBlending](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetAlphaBlending&action=edit&redlink=1)

- [imageSetAlphaBlending](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetAlphaBlending&action=edit&redlink=1)

- [imageGetAntiAlias](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetAntiAlias&action=edit&redlink=1)

- [imageSetAntiAlias](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetAntiAlias&action=edit&redlink=1)

- [imageGetInterlace](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetInterlace&action=edit&redlink=1)

- [imageSetInterlace](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetInterlace&action=edit&redlink=1)

- [imageGetSaveAlpha](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetSaveAlpha&action=edit&redlink=1)

- [imageSetSaveAlpha](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetSaveAlpha&action=edit&redlink=1)

#### Color

- [imageColorAllocate](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorAllocate&action=edit&redlink=1)

- [imageColorAllocateAlpha](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorAllocateAlpha&action=edit&redlink=1)

- [imageColorClosest](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorClosest&action=edit&redlink=1)

- [imageColorClosestAlpha](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorClosestAlpha&action=edit&redlink=1)

- [imageColorExact](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorExact&action=edit&redlink=1)

- [imageColorExactAlpha](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorExactAlpha&action=edit&redlink=1)

- [imageColorResolve](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorResolve&action=edit&redlink=1)

- [imageColorResolveAlpha](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorResolveAlpha&action=edit&redlink=1)

- [imageGetColorAt](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetColorAt&action=edit&redlink=1)

- [imageSetColorAt](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetColorAt&action=edit&redlink=1)

- [imageColorDeallocate](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorDeallocate&action=edit&redlink=1)

- [imageColorsTotal](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorsTotal&action=edit&redlink=1)

- [imageColorSpecial](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageColorSpecial&action=edit&redlink=1)

#### Text

- [imageFontHeight](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageFontHeight&action=edit&redlink=1)

- [imageFontWidth](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageFontWidth&action=edit&redlink=1)

- [imageChar](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageChar&action=edit&redlink=1)

- [imageCharUp](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageCharUp&action=edit&redlink=1)

- [imageString](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageString&action=edit&redlink=1)

- [imageStringUp](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageStringUp&action=edit&redlink=1)

- [imageTtfText](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageTtfText&action=edit&redlink=1)

- [imageTtfBBox](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageTtfBBox&action=edit&redlink=1)

#### Draw

- [imageLine](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageLine&action=edit&redlink=1)

- [imageArc](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageArc&action=edit&redlink=1)

- [imageRectangle](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageRectangle&action=edit&redlink=1)

- [imageEllipse](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageEllipse&action=edit&redlink=1)

- [imageFill](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageFill&action=edit&redlink=1)

- [imageFillToBorder](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageFillToBorder&action=edit&redlink=1)

- [imageFilledArc](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageFilledArc&action=edit&redlink=1)

- [imageFilledRectangle](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageFilledRectangle&action=edit&redlink=1)

- [imageFilledEllipse](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageFilledEllipse&action=edit&redlink=1)

#### Draw Style

- [imageGetStyle](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetStyle&action=edit&redlink=1)

- [imageSetStyle](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetStyle&action=edit&redlink=1)

- [imageGetThickness](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetThickness&action=edit&redlink=1)

- [imageSetThickness](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetThickness&action=edit&redlink=1)

- [imageGetBrush](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetBrush&action=edit&redlink=1)

- [imageSetBrush](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetBrush&action=edit&redlink=1)

- [imageGetTile](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageGetTile&action=edit&redlink=1)

- [imageSetTile](https://wiki.multitheftauto.com/index.php?title=Modules/Functions/imageSetTile&action=edit&redlink=1)
