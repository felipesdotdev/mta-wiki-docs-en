---
doc_id: "mta-wiki:10194"
title: "DgsSetSystemFont"
source_title: "DgsSetSystemFont"
source_url: "https://wiki.multitheftauto.com/wiki/DgsSetSystemFont"
revision_id: 71013
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:33.395222+00:00"
---

# DgsSetSystemFont

This function creates a dx font element as default font stored in dgs.

Successful font creation is not guaranteed, and may fail due to hardware or memory limitations.

**This function will copy the font file into dgs folder and then load it**

## Syntax

```
element dgsSetSystemFont ( string filepath [, int size=9, bool bold=false, string quality="proof" ] )
```

**DGS OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**:  ***dgsRootInstance**:setSystemFont(...)*

**Counterpart**: *[dgsGetSystemFont](mta://scripting/client/functions/dgsgetsystemfont.md)*

### Required Arguments

- **filepath:** the name of the file containing the font. Or built-in fonts are available (see here [Standard_DGS_Font_Names](mta://reference/misc/standard-dgs-font-names.md)):

- default

- default-bold

- clear

- arial

- sans

- pricedown

- bankgothic

- diploma

- beckett

### Optional Arguments

- **size:** size of the font

- **bold:** flag to indicate if the font should be bold

- **quality:** the font quality

- "default": not the actual default

- "draft"

- "proof": the default

- "nonantialiased"

- "antialiased"

- "cleartype"

- "cleartype_natural"

### Returns

Returns a true if successful, *false* otherwise.

## Example

```
DGS = exports.dgs

DGS:dgsSetSystemFont("example.ttf")
```

```
DGS = exports.dgs

DGS:dgsSetSystemFont("default-bold")
```

# See Also

## General Functions

- [dgsGetPosition](mta://scripting/client/functions/dgsgetposition.md)

- [dgsSetPosition](mta://scripting/client/functions/dgssetposition.md)

- [dgsSetParent](mta://scripting/client/functions/dgssetparent.md)

- [dgsGetParent](mta://scripting/client/functions/dgsgetparent.md)

- [dgsGetChild](mta://scripting/client/functions/dgsgetchild.md)

- [dgsGetChildren](mta://scripting/client/functions/dgsgetchildren.md)

- [dgsGetSize](mta://scripting/client/functions/dgsgetsize.md)

- [dgsSetSize](mta://scripting/client/functions/dgssetsize.md)

- [dgsGetType](mta://scripting/client/functions/dgsgettype.md)

- [dgsSetLayer](mta://scripting/client/functions/dgssetlayer.md)

- [dgsGetLayer](mta://scripting/client/functions/dgsgetlayer.md)

- [dgsSetCurrentLayerIndex](mta://scripting/client/functions/dgssetcurrentlayerindex.md)

- [dgsGetCurrentLayerIndex](mta://scripting/client/functions/dgsgetcurrentlayerindex.md)

- [dgsGetLayerElements](mta://scripting/client/functions/dgsgetlayerelements.md)

- [dgsGetProperty](mta://scripting/client/functions/dgsgetproperty.md)

- [dgsSetProperty](mta://scripting/client/functions/dgssetproperty.md)

- [dgsSetPropertyInherit](mta://scripting/client/functions/dgssetpropertyinherit.md)

- [dgsGetProperties](mta://scripting/client/functions/dgsgetproperties.md)

- [dgsSetProperties](mta://scripting/client/functions/dgssetproperties.md)

- [dgsGetVisible](mta://scripting/client/functions/dgsgetvisible.md)

- [dgsSetVisible](mta://scripting/client/functions/dgssetvisible.md)

- [dgsGetEnabled](mta://scripting/client/functions/dgsgetenabled.md)

- [dgsSetEnabled](mta://scripting/client/functions/dgssetenabled.md)

- [dgsGetPositionAlignment](mta://scripting/client/functions/dgsgetpositionalignment.md)

- [dgsSetPositionAlignment](mta://scripting/client/functions/dgssetpositionalignment.md)

- [dgsGetAlpha](mta://scripting/client/functions/dgsgetalpha.md)

- [dgsSetAlpha](mta://scripting/client/functions/dgssetalpha.md)

- [dgsGetFont](mta://scripting/client/functions/dgsgetfont.md)

- [dgsSetFont](mta://scripting/client/functions/dgssetfont.md)

- [dgsGetText](mta://scripting/client/functions/dgsgettext.md)

- [dgsSetText](mta://scripting/client/functions/dgssettext.md)

- [dgsGetPostGUI](mta://scripting/client/functions/dgsgetpostgui.md)

- [dgsSetPostGUI](mta://scripting/client/functions/dgssetpostgui.md)

- [dgsGetInputEnabled](mta://scripting/client/functions/dgsgetinputenabled.md)

- [dgsSetInputEnabled](mta://scripting/client/functions/dgssetinputenabled.md)

- [dgsGetInputMode](mta://scripting/client/functions/dgsgetinputmode.md)

- [dgsSetInputMode](mta://scripting/client/functions/dgssetinputmode.md)

- [dgsAttachToAutoDestroy](mta://scripting/client/functions/dgsattachtoautodestroy.md)

- [dgsDetachFromAutoDestroy](mta://scripting/client/functions/dgsdetachfromautodestroy.md)

- [dgsFocus](mta://scripting/client/functions/dgsfocus.md)

- [dgsBlur](mta://scripting/client/functions/dgsblur.md)

- [dgsCreateFont](mta://scripting/client/functions/dgscreatefont.md)

- [dgsBringToFront](mta://scripting/client/functions/dgsbringtofront.md)

- [dgsMoveToBack](mta://scripting/client/functions/dgsmovetoback.md)

- [dgsGetScreenSize](mta://scripting/client/functions/dgsgetscreensize.md)

- [dgsGetCursorPosition](mta://scripting/client/functions/dgsgetcursorposition.md)

- [dgsGetMouseEnterGUI](mta://scripting/client/functions/dgsgetmouseentergui.md)

- [dgsGetMouseLeaveGUI](mta://scripting/client/functions/dgsgetmouseleavegui.md)

- [dgsIsMouseWithinGUI](mta://scripting/client/functions/dgsismousewithingui.md)

- dgsSetSystemFont

- [dgsGetSystemFont](mta://scripting/client/functions/dgsgetsystemfont.md)

- [dgsGetElementsInLayer](mta://scripting/client/functions/dgsgetelementsinlayer.md)

- [dgsGetElementsFromResource](mta://scripting/client/functions/dgsgetelementsfromresource.md)

- [dgsGetFocusedGUI](mta://scripting/client/functions/dgsgetfocusedgui.md)

- [dgsImportFunction](mta://scripting/client/functions/dgsimportfunction.md)

- [dgsImportOOPClass](mta://scripting/client/functions/dgsimportoopclass.md)

- [dgsG2DLoadHooker](mta://scripting/client/functions/dgsg2dloadhooker.md)

- [dgsSetRenderSetting](mta://scripting/client/functions/dgssetrendersetting.md)

- [dgsGetRenderSetting](mta://scripting/client/functions/dgsgetrendersetting.md)

- [dgsSimulateClick](mta://scripting/client/functions/dgssimulateclick.md)

- [dgsGetRootElement](mta://scripting/client/functions/dgsgetrootelement.md)

- [dgsAddMoveHandler](mta://scripting/client/functions/dgsaddmovehandler.md)

- [dgsRemoveMoveHandler](mta://scripting/client/functions/dgsremovemovehandler.md)

- [dgsIsMoveHandled](mta://scripting/client/functions/dgsismovehandled.md)

- [dgsAddSizeHandler](mta://scripting/client/functions/dgsaddsizehandler.md)

- [dgsRemoveSizeHandler](mta://scripting/client/functions/dgsremovesizehandler.md)

- [dgsIsSizeHandled](mta://scripting/client/functions/dgsissizehandled.md)

- [dgsAttachElements](mta://scripting/client/functions/dgsattachelements.md)

- [dgsDetachElements](mta://scripting/client/functions/dgsdetachelements.md)

- [dgsElementIsAttached](mta://scripting/client/functions/dgselementisattached.md)

- [dgsAddPropertyListener](mta://scripting/client/functions/dgsaddpropertylistener.md)

- [dgsRemovePropertyListener](https://wiki.multitheftauto.com/index.php?title=DgsRemovePropertyListener&action=edit&redlink=1)

- [dgsGetListenedProperties](https://wiki.multitheftauto.com/index.php?title=DgsGetListenedProperties&action=edit&redlink=1)

- [dgsSetMultiClickInterval](mta://scripting/client/functions/dgssetmulticlickinterval.md)

- [dgsGetMultiClickInterval](mta://scripting/client/functions/dgsgetmulticlickinterval.md)

- [dgsSetMouseStayDelay](mta://scripting/client/functions/dgssetmousestaydelay.md)

- [dgsGetMouseStayDelay](mta://scripting/client/functions/dgsgetmousestaydelay.md)

- [dgsCenterElement](mta://scripting/client/functions/dgscenterelement.md)

- [dgsSetElementKeeperEnabled](mta://scripting/client/functions/dgssetelementkeeperenabled.md)

- [dgsGetElementKeeperEnabled](mta://scripting/client/functions/dgsgetelementkeeperenabled.md)

- [dgsSetClickingSound](mta://scripting/client/functions/dgssetclickingsound.md)

- [dgsGetClickingSound](mta://scripting/client/functions/dgsgetclickingsound.md)

- [dgsSetClickingSoundVolume](mta://scripting/client/functions/dgssetclickingsoundvolume.md)

- [dgsGetClickingSoundVolume](mta://scripting/client/functions/dgsgetclickingsoundvolume.md)

## General Events

- [onDgsBlur](mta://scripting/client/events/ondgsblur.md)

- [onDgsCreate](mta://scripting/client/events/ondgscreate.md)

- [onDgsCursorTypeChange](mta://scripting/client/events/ondgscursortypechange.md)

- [onDgsCursorStateChange](https://wiki.multitheftauto.com/index.php?title=OnDgsCursorStateChange&action=edit&redlink=1)

- [onDgsDestroy](mta://scripting/client/events/ondgsdestroy.md)

- [onDgsElementRender](mta://scripting/client/events/ondgselementrender.md)

- [onDgsElementMove](mta://scripting/client/events/ondgselementmove.md)

- [onDgsElementSize](mta://scripting/client/events/ondgselementsize.md)

- [onDgsElementEnter](mta://scripting/client/events/ondgselemententer.md)

- [onDgsElementLeave](mta://scripting/client/events/ondgselementleave.md)

- [onDgsFocus](mta://scripting/client/events/ondgsfocus.md)

- [onDgsKey](mta://scripting/client/events/ondgskey.md)

- [onDgsPositionChange](mta://scripting/client/events/ondgspositionchange.md)

- [onDgsPreRender](mta://scripting/client/events/ondgsprerender.md)

- [onDgsRender](mta://scripting/client/events/ondgsrender.md)

- [onDgsElementScroll](mta://scripting/client/events/ondgselementscroll.md)

- [onDgsSizeChange](mta://scripting/client/events/ondgssizechange.md)

- [onDgsTextChange](mta://scripting/client/events/ondgstextchange.md)

- [onDgsWindowClose](mta://scripting/client/events/ondgswindowclose.md)

- [onDgsPropertyChange](mta://scripting/client/events/ondgspropertychange.md)
