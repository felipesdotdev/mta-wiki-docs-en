---
doc_id: "mta-wiki:11197"
title: "DgsScrollPaneSetScrollBarState"
source_title: "DgsScrollPaneSetScrollBarState"
source_url: "https://wiki.multitheftauto.com/wiki/DgsScrollPaneSetScrollBarState"
revision_id: 62482
language: "en"
categories: ["Client_functions"]
---

# DgsScrollPaneSetScrollBarState

This function force the scroll bar of the scroll pane to be enabled/disabled.

- **true:** Force to be visible

- **false:** Force to be invisible

- **nil:** Auto adjusting

## Syntax

```
bool dgsScrollPaneSetScrollBarState( element scrollPane [, bool/nil verticalState = nil, bool/nil horizontalState = nil ] )
```

### Required Arguments

- **scrollPane:** The dgs scroll pane to set.

### Optional Arguments

- **verticalState :** A boolean value of the state of vertical scroll bar.

- **horizontalState :** A boolean value of the state of horizontal scroll bar.

### Returns

Returns *true* if succeed, *false* otherwise.

## Example

```
DGS = exports.dgs

local scrollPane = DGS:dgsCreateScrollPane ( 0.45, 0.45, 0.15, 0.15, true ) 
local label = DGS;dgsCreateLabel(0.2,5,0.2,0.2,"test",true,scrollPane)
DGS:dgsScrollPaneSetScrollBarState(scrollPane,false,false)    --Disable them
```

## See Also

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

- [dgsSetSystemFont](mta://scripting/client/functions/dgssetsystemfont.md)

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

## Custom Cursor Functions

- [dgsSetCustomCursorEnabled](mta://scripting/client/functions/dgssetcustomcursorenabled.md)

- [dgsGetCustomCursorEnabled](mta://scripting/client/functions/dgsgetcustomcursorenabled.md)

- [dgsSetCustomCursorImage](mta://scripting/client/functions/dgssetcustomcursorimage.md)

- [dgsGetCustomCursorImage](mta://scripting/client/functions/dgsgetcustomcursorimage.md)

- [dgsSetCustomCursorSize](mta://scripting/client/functions/dgssetcustomcursorsize.md)

- [dgsGetCustomCursorSize](mta://scripting/client/functions/dgsgetcustomcursorsize.md)

- [dgsGetCustomCursorType](mta://scripting/client/functions/dgsgetcustomcursortype.md)

- [dgsSetCustomCursorColor](mta://scripting/client/functions/dgssetcustomcursorcolor.md)

- [dgsGetCustomCursorColor](mta://scripting/client/functions/dgsgetcustomcursorcolor.md)

## [Multi Language Supports](mta://reference/misc/dgs-multilingual.md)

- [dgsTranslationTableExists](mta://scripting/client/functions/dgstranslationtableexists.md)

- [dgsSetTranslationTable](https://wiki.multitheftauto.com/index.php?search=dgsSetTranslationTable)

- [dgsAttachToTranslation](mta://scripting/client/functions/dgsattachtotranslation.md)

- [dgsDetachFromTranslation](mta://scripting/client/functions/dgsdetachfromtranslation.md)

- [dgsSetAttachTranslation](mta://scripting/client/functions/dgssetattachtranslation.md)

- [dgsGetTranslationName](mta://scripting/client/functions/dgsgettranslationname.md)

- [dgsTranslationAddPropertyListener](https://wiki.multitheftauto.com/index.php?title=DgsTranslationAddPropertyListener&action=edit&redlink=1)

- [dgsTranslationRemovePropertyListener](https://wiki.multitheftauto.com/index.php?title=DgsTranslationRemovePropertyListener&action=edit&redlink=1)

## Animation

- [dgsAnimTo](mta://scripting/client/functions/dgsanimto.md)

- [dgsIsAniming](mta://scripting/client/functions/dgsisaniming.md)

- [dgsStopAniming](mta://scripting/client/functions/dgsstopaniming.md)

- [dgsMoveTo](mta://scripting/client/functions/dgsmoveto.md)

- [dgsIsMoving](mta://scripting/client/functions/dgsismoving.md)

- [dgsStopMoving](mta://scripting/client/functions/dgsstopmoving.md)

- [dgsSizeTo](mta://scripting/client/functions/dgssizeto.md)

- [dgsIsSizing](mta://scripting/client/functions/dgsissizing.md)

- [dgsStopSizing](mta://scripting/client/functions/dgsstopsizing.md)

- [dgsAlphaTo](mta://scripting/client/functions/dgsalphato.md)

- [dgsIsAlphaing](mta://scripting/client/functions/dgsisalphaing.md)

- [dgsStopAlphaing](mta://scripting/client/functions/dgsstopalphaing.md)

- [dgsAddEasingFunction](mta://scripting/client/functions/dgsaddeasingfunction.md)

- [dgsRemoveEasingFunction](mta://scripting/client/functions/dgsremoveeasingfunction.md)

- [dgsEasingFunctionExists](mta://scripting/client/functions/dgseasingfunctionexists.md)

## 3D Element

- [dgs3DGetPosition](mta://scripting/client/functions/dgs3dgetposition.md)

- [dgs3DSetPosition](mta://scripting/client/functions/dgs3dsetposition.md)

- [dgs3DGetInterior](mta://scripting/client/functions/dgs3dgetinterior.md)

- [dgs3DSetInterior](mta://scripting/client/functions/dgs3dsetinterior.md)

- [dgs3DSetDimension](mta://scripting/client/functions/dgs3dsetdimension.md)

- [dgs3DGetDimension](mta://scripting/client/functions/dgs3dgetdimension.md)

## 3D Interface

- [dgsCreate3DInterface](mta://scripting/client/functions/dgscreate3dinterface.md)

- [dgs3DInterfaceProcessLineOfSight](mta://scripting/client/functions/dgs3dinterfaceprocesslineofsight.md)

- [dgs3DInterfaceGetBlendMode](mta://scripting/client/functions/dgs3dinterfacegetblendmode.md)

- [dgs3DInterfaceSetBlendMode](mta://scripting/client/functions/dgs3dinterfacesetblendmode.md)

- [dgs3DInterfaceGetDoublesided](https://wiki.multitheftauto.com/index.php?title=Dgs3DInterfaceGetDoublesided&action=edit&redlink=1)

- [dgs3DInterfaceSetDoublesided](https://wiki.multitheftauto.com/index.php?title=Dgs3DInterfaceSetDoublesided&action=edit&redlink=1)

- [dgs3DInterfaceGetFaceTo](mta://scripting/client/functions/dgs3dinterfacegetfaceto.md)

- [dgs3DInterfaceSetFaceTo](mta://scripting/client/functions/dgs3dinterfacesetfaceto.md)

- [dgs3DInterfaceGetResolution](mta://scripting/client/functions/dgs3dinterfacegetresolution.md)

- [dgs3DInterfaceSetResolution](mta://scripting/client/functions/dgs3dinterfacesetresolution.md)

- [dgs3DInterfaceSetRoll](mta://scripting/client/functions/dgs3dinterfacesetroll.md)

- [dgs3DInterfaceGetRoll](mta://scripting/client/functions/dgs3dinterfacegetroll.md)

- [dgs3DInterfaceGetSize](mta://scripting/client/functions/dgs3dinterfacegetsize.md)

- [dgs3DInterfaceSetSize](mta://scripting/client/functions/dgs3dinterfacesetsize.md)

- [dgs3DInterfaceIsAttached](mta://scripting/client/functions/dgs3dinterfaceisattached.md)

- [dgs3DInterfaceAttachToElement](mta://scripting/client/functions/dgs3dinterfaceattachtoelement.md)

- [dgs3DInterfaceDetachFromElement](mta://scripting/client/functions/dgs3dinterfacedetachfromelement.md)

- [dgs3DInterfaceSetAttachedOffsets](mta://scripting/client/functions/dgs3dinterfacesetattachedoffsets.md)

- [dgs3DInterfaceGetAttachedOffsets](mta://scripting/client/functions/dgs3dinterfacegetattachedoffsets.md)

## 3D Line

- [dgsCreate3DLine](mta://scripting/client/functions/dgscreate3dline.md)

- [dgs3DLineSetLineType](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineSetLineType&action=edit&redlink=1)

- [dgs3DLineGetLineType](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineGetLineType&action=edit&redlink=1)

- [dgs3DLineAddItem](mta://scripting/client/functions/dgs3dlineadditem.md)

- [dgs3DLineRemoveItem](mta://scripting/client/functions/dgs3dlineremoveitem.md)

- [dgs3DLineSetItemPosition](mta://scripting/client/functions/dgs3dlinesetitemposition.md)

- [dgs3DLineGetItemPosition](mta://scripting/client/functions/dgs3dlinegetitemposition.md)

- [dgs3DLineSetItemWidth](mta://scripting/client/functions/dgs3dlinesetitemwidth.md)

- [dgs3DLineGetItemWidth](mta://scripting/client/functions/dgs3dlinegetitemwidth.md)

- [dgs3DLineSetItemColor](mta://scripting/client/functions/dgs3dlinesetitemcolor.md)

- [dgs3DLineGetItemColor](mta://scripting/client/functions/dgs3dlinegetitemcolor.md)

- [dgs3DLineAttachToElement](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineAttachToElement&action=edit&redlink=1)

- [dgs3DLineIsAttached](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineIsAttached&action=edit&redlink=1)

- [dgs3DLineDetachFromElement](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineDetachFromElement&action=edit&redlink=1)

- [dgs3DLineSetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineSetAttachedOffsets&action=edit&redlink=1)

- [dgs3DLineGetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineGetAttachedOffsets&action=edit&redlink=1)

- [dgs3DLineSetRotation](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineSetRotation&action=edit&redlink=1)

- [dgs3DLineGetRotation](https://wiki.multitheftauto.com/index.php?title=Dgs3DLineGetRotation&action=edit&redlink=1)

## 3D Image

- [dgsCreate3DImage](mta://scripting/client/functions/dgscreate3dimage.md)

- [dgs3DImageSetSize](mta://scripting/client/functions/dgs3dimagesetsize.md)

- [dgs3DImageGetSize](mta://scripting/client/functions/dgs3dimagegetsize.md)

- [dgs3DImageSetImage](mta://scripting/client/functions/dgs3dimagesetimage.md)

- [dgs3DImageGetImage](mta://scripting/client/functions/dgs3dimagegetimage.md)

- [dgs3DImageAttachToElement](mta://scripting/client/functions/dgs3dimageattachtoelement.md)

- [dgs3DImageIsAttached](mta://scripting/client/functions/dgs3dimageisattached.md)

- [dgs3DImageDetachFromElement](mta://scripting/shared/functions/dgs3dimagedetachfromelement.md)

- [dgs3DImageSetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageSetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetAttachedOffsets](https://wiki.multitheftauto.com/index.php?title=Dgs3DImageGetAttachedOffsets&action=edit&redlink=1)

- [dgs3DImageGetNativeSize](mta://scripting/client/functions/dgs3dimagegetnativesize.md)

- [dgs3DImageSetUVPosition](mta://scripting/client/functions/dgs3dimagesetuvposition.md)

- [dgs3DImageGetUVPosition](mta://scripting/client/functions/dgs3dimagegetuvposition.md)

- [dgs3DImageSetUVSize](mta://scripting/client/functions/dgs3dimagesetuvsize.md)

- [dgs3DImageGetUVSize](mta://scripting/client/functions/dgs3dimagegetuvsize.md)

## 3D Text

- [dgsCreate3DText](mta://scripting/client/functions/dgscreate3dtext.md)

- [dgs3DTextIsAttached](mta://scripting/client/functions/dgs3dtextisattached.md)

- [dgs3DTextAttachToElement](mta://scripting/client/functions/dgs3dtextattachtoelement.md)

- [dgs3DTextDetachFromElement](mta://scripting/client/functions/dgs3dtextdetachfromelement.md)

- [dgs3DTextSetAttachedOffsets](mta://scripting/client/functions/dgs3dtextsetattachedoffsets.md)

- [dgs3DTextGetAttachedOffsets](mta://scripting/client/functions/dgs3dtextgetattachedoffsets.md)

## Browser

- [dgsCreateBrowser](mta://scripting/client/functions/dgscreatebrowser.md)

## Button

- [dgsCreateButton](mta://scripting/client/functions/dgscreatebutton.md)

- [dgsButtonGetTextExtent](mta://scripting/client/functions/dgsbuttongettextextent.md)

- [dgsButtonGetFontHeight](mta://scripting/client/functions/dgsbuttongetfontheight.md)

- [dgsButtonGetTextSize](mta://scripting/client/functions/dgsbuttongettextsize.md)

- [dgsButtonMakeForm](https://wiki.multitheftauto.com/index.php?title=DgsButtonMakeForm&action=edit&redlink=1)

- [dgsButtonRemoveForm](https://wiki.multitheftauto.com/index.php?title=DgsButtonRemoveForm&action=edit&redlink=1)

## Check Box

- [dgsCreateCheckBox](mta://scripting/client/functions/dgscreatecheckbox.md)

- [dgsCheckBoxGetSelected](mta://scripting/client/functions/dgscheckboxgetselected.md)

- [dgsCheckBoxSetSelected](mta://scripting/client/functions/dgscheckboxsetselected.md)

- [dgsCheckBoxSetHorizontalAlign](mta://scripting/client/functions/dgscheckboxsethorizontalalign.md)

- [dgsCheckBoxGetHorizontalAlign](mta://scripting/client/functions/dgscheckboxgethorizontalalign.md)

- [dgsCheckBoxSetVerticalAlign](mta://scripting/client/functions/dgscheckboxsetverticalalign.md)

- [dgsCheckBoxGetVerticalAlign](mta://scripting/client/functions/dgscheckboxgetverticalalign.md)

- [dgsCheckBoxGetButtonSide](mta://scripting/client/functions/dgscheckboxgetbuttonside.md)

- [dgsCheckBoxSetButtonSide](mta://scripting/client/functions/dgscheckboxsetbuttonside.md)

- [dgsCheckBoxGetButtonAlign](mta://scripting/client/functions/dgscheckboxgetbuttonalign.md)

- [dgsCheckBoxSetButtonAlign](mta://scripting/client/functions/dgscheckboxsetbuttonalign.md)

## Combo Box

- [dgsCreateComboBox](mta://scripting/client/functions/dgscreatecombobox.md)

- [dgsComboBoxAddItem](mta://scripting/client/functions/dgscomboboxadditem.md)

- [dgsComboBoxRemoveItem](mta://scripting/client/functions/dgscomboboxremoveitem.md)

- [dgsComboBoxSetItemText](mta://scripting/client/functions/dgscomboboxsetitemtext.md)

- [dgsComboBoxGetItemText](mta://scripting/client/functions/dgscomboboxgetitemtext.md)

- [dgsComboBoxSetItemData](mta://scripting/client/functions/dgscomboboxsetitemdata.md)

- [dgsComboBoxGetItemData](mta://scripting/client/functions/dgscomboboxgetitemdata.md)

- [dgsComboBoxGetItemCount](mta://scripting/client/functions/dgscomboboxgetitemcount.md)

- [dgsComboBoxClear](mta://scripting/client/functions/dgscomboboxclear.md)

- [dgsComboBoxSetSelectedItem](mta://scripting/client/functions/dgscomboboxsetselecteditem.md)

- [dgsComboBoxGetSelectedItem](mta://scripting/client/functions/dgscomboboxgetselecteditem.md)

- [dgsComboBoxSetItemColor](mta://scripting/client/functions/dgscomboboxsetitemcolor.md)

- [dgsComboBoxGetItemColor](mta://scripting/client/functions/dgscomboboxgetitemcolor.md)

- [dgsComboBoxSetItemImage](mta://scripting/client/functions/dgscomboboxsetitemimage.md)

- [dgsComboBoxGetItemImage](mta://scripting/client/functions/dgscomboboxgetitemimage.md)

- [dgsComboBoxRemoveItemImage](mta://scripting/client/functions/dgscomboboxremoveitemimage.md)

- [dgsComboBoxSetItemBackGroundImage](mta://scripting/client/functions/dgscomboboxsetitembackgroundimage.md)

- [dgsComboBoxGetItemBackGroundImage](mta://scripting/client/functions/dgscomboboxgetitembackgroundimage.md)

- [dgsComboBoxSetItemBackGroundColor](mta://scripting/client/functions/dgscomboboxsetitembackgroundcolor.md)

- [dgsComboBoxGetItemBackGroundColor](mta://scripting/client/functions/dgscomboboxgetitembackgroundcolor.md)

- [dgsComboBoxSetItemFont](mta://scripting/client/functions/dgscomboboxsetitemfont.md)

- [dgsComboBoxGetItemFont](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxGetItemFont&action=edit&redlink=1)

- [dgsComboBoxGetState](mta://scripting/client/functions/dgscomboboxgetstate.md)

- [dgsComboBoxSetState](mta://scripting/client/functions/dgscomboboxsetstate.md)

- [dgsComboBoxGetBoxHeight](mta://scripting/client/functions/dgscomboboxgetboxheight.md)

- [dgsComboBoxSetBoxHeight](mta://scripting/client/functions/dgscomboboxsetboxheight.md)

- [dgsComboBoxSetViewCount](mta://scripting/client/functions/dgscomboboxsetviewcount.md)

- [dgsComboBoxGetViewCount](mta://scripting/client/functions/dgscomboboxgetviewcount.md)

- [dgsComboBoxGetScrollBar](mta://scripting/client/functions/dgscomboboxgetscrollbar.md)

- [dgsComboBoxSetScrollBarState](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxSetScrollBarState&action=edit&redlink=1)

- [dgsComboBoxGetScrollBarState](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxGetScrollBarState&action=edit&redlink=1)

- [dgsComboBoxSetScrollPosition](mta://scripting/client/functions/dgscomboboxsetscrollposition.md)

- [dgsComboBoxGetScrollPosition](mta://scripting/client/functions/dgscomboboxgetscrollposition.md)

- [dgsComboBoxSetCaptionText](mta://scripting/client/functions/dgscomboboxsetcaptiontext.md)

- [dgsComboBoxGetCaptionText](mta://scripting/client/functions/dgscomboboxgetcaptiontext.md)

- [dgsComboBoxSetEditEnabled](mta://scripting/client/functions/dgscomboboxseteditenabled.md)

- [dgsComboBoxGetEditEnabled](mta://scripting/client/functions/dgscomboboxgeteditenabled.md)

- [dgsComboBoxGetText](mta://scripting/client/functions/dgscomboboxgettext.md)

- [dgsComboBoxSetSortFunction](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxSetSortFunction&action=edit&redlink=1)

- [dgsComboBoxGetSortFunction](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxGetSortFunction&action=edit&redlink=1)

- [dgsComboBoxSort](https://wiki.multitheftauto.com/index.php?title=DgsComboBoxSort&action=edit&redlink=1)

## Custom Renderer

- [dgsCreateCustomRenderer](mta://scripting/client/functions/dgscreatecustomrenderer.md)

- [dgsCustomRendererSetFunction](mta://scripting/client/functions/dgscustomrenderersetfunction.md)

## Edit

- [dgsCreateEdit](mta://scripting/client/functions/dgscreateedit.md)

- [dgsEditMoveCaret](mta://scripting/client/functions/dgseditmovecaret.md)

- [dgsEditGetCaretPosition](mta://scripting/client/functions/dgseditgetcaretposition.md)

- [dgsEditSetCaretPosition](mta://scripting/client/functions/dgseditsetcaretposition.md)

- [dgsEditSetCaretStyle](mta://scripting/client/functions/dgseditsetcaretstyle.md)

- [dgsEditGetCaretStyle](mta://scripting/client/functions/dgseditgetcaretstyle.md)

- [dgsEditSetTextFilter](mta://scripting/client/functions/dgseditsettextfilter.md)

- [dgsEditGetMaxLength](mta://scripting/client/functions/dgseditgetmaxlength.md)

- [dgsEditSetMaxLength](mta://scripting/client/functions/dgseditsetmaxlength.md)

- [dgsEditSetReadOnly](mta://scripting/client/functions/dgseditsetreadonly.md)

- [dgsEditGetReadOnly](mta://scripting/client/functions/dgseditgetreadonly.md)

- [dgsEditSetMasked](mta://scripting/client/functions/dgseditsetmasked.md)

- [dgsEditGetMasked](mta://scripting/client/functions/dgseditgetmasked.md)

- [dgsEditSetUnderlined](mta://scripting/client/functions/dgseditsetunderlined.md)

- [dgsEditGetUnderlined](mta://scripting/client/functions/dgseditgetunderlined.md)

- [dgsEditSetHorizontalAlign](mta://scripting/client/functions/dgseditsethorizontalalign.md)

- [dgsEditSetVerticalAlign](mta://scripting/client/functions/dgseditsetverticalalign.md)

- [dgsEditGetHorizontalAlign](mta://scripting/client/functions/dgseditgethorizontalalign.md)

- [dgsEditGetVerticalAlign](mta://scripting/client/functions/dgseditgetverticalalign.md)

- [dgsEditSetAlignment](mta://scripting/client/functions/dgseditsetalignment.md)

- [dgsEditGetAlignment](mta://scripting/client/functions/dgseditgetalignment.md)

- [dgsEditInsertText](mta://scripting/client/functions/dgseditinserttext.md)

- [dgsEditDeleteText](mta://scripting/client/functions/dgseditdeletetext.md)

- [dgsEditGetPartOfText](mta://scripting/client/functions/dgseditgetpartoftext.md)

- [dgsEditClearText](mta://scripting/client/functions/dgseditcleartext.md)

- [dgsEditReplaceText](mta://scripting/client/functions/dgseditreplacetext.md)

- [dgsEditSetTypingSound](mta://scripting/client/functions/dgseditsettypingsound.md)

- [dgsEditGetTypingSound](mta://scripting/client/functions/dgseditgettypingsound.md)

- [dgsEditSetTypingSoundVolume](mta://scripting/client/functions/dgseditsettypingsoundvolume.md)

- [dgsEditGetTypingSoundVolume](mta://scripting/client/functions/dgseditgettypingsoundvolume.md)

- [dgsEditSetPlaceHolder](mta://scripting/client/functions/dgseditsetplaceholder.md)

- [dgsEditGetPlaceHolder](mta://scripting/client/functions/dgseditgetplaceholder.md)

- [dgsEditAddAutoComplete](mta://scripting/client/functions/dgseditaddautocomplete.md)

- [dgsEditRemoveAutoComplete](mta://scripting/client/functions/dgseditremoveautocomplete.md)

- [dgsEditSetAutoComplete](mta://scripting/client/functions/dgseditsetautocomplete.md)

- [dgsEditGetAutoComplete](mta://scripting/client/functions/dgseditgetautocomplete.md)

- [dgsEditAutoCompleteAddParameterFunction](mta://scripting/client/functions/dgseditautocompleteaddparameterfunction.md)

- [dgsEditAutoCompleteRemoveParameterFunction](https://wiki.multitheftauto.com/index.php?title=DgsEditAutoCompleteRemoveParameterFunction&action=edit&redlink=1)

## Detect Area

- [dgsCreateDetectArea](mta://scripting/client/functions/dgscreatedetectarea.md)

- [dgsGetDetectArea](mta://scripting/client/functions/dgsgetdetectarea.md)

- [dgsApplyDetectArea](mta://scripting/client/functions/dgsapplydetectarea.md)

- [dgsRemoveDetectArea](mta://scripting/client/functions/dgsremovedetectarea.md)

- [dgsDetectAreaSetFunction](mta://scripting/client/functions/dgsdetectareasetfunction.md)

- [dgsDetectAreaSetDebugModeEnabled](mta://scripting/client/functions/dgsdetectareasetdebugmodeenabled.md)

- [dgsDetectAreaGetDebugModeEnabled](mta://scripting/client/functions/dgsdetectareagetdebugmodeenabled.md)

## Drag'N Drop

- [dgsSendDragNDropData](mta://scripting/client/functions/dgssenddragndropdata.md)

- [dgsRetrieveDragNDropData](mta://scripting/client/functions/dgsretrievedragndropdata.md)

- [dgsIsDragNDropData](mta://scripting/client/functions/dgsisdragndropdata.md)

- [dgsAddDragHandler](https://wiki.multitheftauto.com/index.php?title=DgsAddDragHandler&action=edit&redlink=1)

- [dgsRemoveDragHandler](https://wiki.multitheftauto.com/index.php?title=DgsRemoveDragHandler&action=edit&redlink=1)

## Grid List

- [dgsCreateGridList](mta://scripting/client/functions/dgscreategridlist.md)

- [dgsGridListClear](mta://scripting/client/functions/dgsgridlistclear.md)

- [dgsGridListGetScrollBar](mta://scripting/client/functions/dgsgridlistgetscrollbar.md)

- [dgsGridListSetScrollPosition](mta://scripting/client/functions/dgsgridlistsetscrollposition.md)

- [dgsGridListGetScrollPosition](mta://scripting/client/functions/dgsgridlistgetscrollposition.md)

- [dgsGridListScrollTo](mta://scripting/client/functions/dgsgridlistscrollto.md)

- [dgsGridListSetHorizontalScrollPosition](mta://scripting/client/functions/dgsgridlistsethorizontalscrollposition.md)

- [dgsGridListGetHorizontalScrollPosition](mta://scripting/client/functions/dgsgridlistgethorizontalscrollposition.md)

- [dgsGridListSetVerticalScrollPosition](mta://scripting/client/functions/dgsgridlistsetverticalscrollposition.md)

- [dgsGridListGetVerticalScrollPosition](mta://scripting/client/functions/dgsgridlistgetverticalscrollposition.md)

- [dgsGridListResetScrollBarPosition](mta://scripting/client/functions/dgsgridlistresetscrollbarposition.md)

- [dgsGridListSetColumnRelative](mta://scripting/client/functions/dgsgridlistsetcolumnrelative.md)

- [dgsGridListGetColumnRelative](mta://scripting/client/functions/dgsgridlistgetcolumnrelative.md)

- [dgsGridListAddColumn](mta://scripting/client/functions/dgsgridlistaddcolumn.md)

- [dgsGridListRemoveColumn](mta://scripting/client/functions/dgsgridlistremovecolumn.md)

- [dgsGridListClearColumn](mta://scripting/client/functions/dgsgridlistclearcolumn.md)

- [dgsGridListGetColumnCount](mta://scripting/client/functions/dgsgridlistgetcolumncount.md)

- [dgsGridListGetColumnAllWidth](mta://scripting/client/functions/dgsgridlistgetcolumnallwidth.md)

- [dgsGridListGetColumnHeight](mta://scripting/client/functions/dgsgridlistgetcolumnheight.md)

- [dgsGridListSetColumnHeight](mta://scripting/client/functions/dgsgridlistsetcolumnheight.md)

- [dgsGridListGetColumnWidth](mta://scripting/client/functions/dgsgridlistgetcolumnwidth.md)

- [dgsGridListSetColumnWidth](mta://scripting/client/functions/dgsgridlistsetcolumnwidth.md)

- [dgsGridListAutoSizeColumn](mta://scripting/client/functions/dgsgridlistautosizecolumn.md)

- [dgsGridListGetColumnTextSize](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetColumnTextSize&action=edit&redlink=1)

- [dgsGridListSetColumnTextSize](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetColumnTextSize&action=edit&redlink=1)

- [dgsGridListGetColumnTitle](mta://scripting/client/functions/dgsgridlistgetcolumntitle.md)

- [dgsGridListSetColumnTitle](mta://scripting/client/functions/dgsgridlistsetcolumntitle.md)

- [dgsGridListGetColumnFont](mta://scripting/client/functions/dgsgridlistgetcolumnfont.md)

- [dgsGridListSetColumnFont](mta://scripting/client/functions/dgsgridlistsetcolumnfont.md)

- [dgsGridListGetColumnAlignment](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetColumnAlignment&action=edit&redlink=1)

- [dgsGridListSetColumnAlignment](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetColumnAlignment&action=edit&redlink=1)

- [dgsGridListSetColumnTextColor](mta://scripting/client/functions/dgsgridlistsetcolumntextcolor.md)

- [dgsGridListGetColumnTextColor](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetColumnTextColor&action=edit&redlink=1)

- [dgsGridListSetSortColumn](mta://scripting/client/functions/dgsgridlistsetsortcolumn.md)

- [dgsGridListGetSortColumn](mta://scripting/client/functions/dgsgridlistgetsortcolumn.md)

- [dgsGridListGetEnterColumn](mta://scripting/client/functions/dgsgridlistgetentercolumn.md)

- [dgsGridListAddRow](mta://scripting/client/functions/dgsgridlistaddrow.md)

- [dgsGridListAddRows](https://wiki.multitheftauto.com/index.php?title=DgsGridListAddRows&action=edit&redlink=1)

- [dgsGridListRemoveRow](mta://scripting/client/functions/dgsgridlistremoverow.md)

- [dgsGridListClearRow](mta://scripting/client/functions/dgsgridlistclearrow.md)

- [dgsGridListGetRowCount](mta://scripting/client/functions/dgsgridlistgetrowcount.md)

- [dgsGridListGetRowBackGroundImage](mta://scripting/client/functions/dgsgridlistgetrowbackgroundimage.md)

- [dgsGridListSetRowBackGroundImage](mta://scripting/client/functions/dgsgridlistsetrowbackgroundimage.md)

- [dgsGridListSetRowBackGroundColor](mta://scripting/client/functions/dgsgridlistsetrowbackgroundcolor.md)

- [dgsGridListGetRowBackGroundColor](mta://scripting/client/functions/dgsgridlistgetrowbackgroundcolor.md)

- [dgsGridListSetRowAsSection](mta://scripting/client/functions/dgsgridlistsetrowassection.md)

- [dgsGridListGetRowSelectable](mta://scripting/client/functions/dgsgridlistgetrowselectable.md)

- [dgsGridListSetRowSelectable](mta://scripting/client/functions/dgsgridlistsetrowselectable.md)

- [dgsGridListGetRowHoverable](mta://scripting/client/functions/dgsgridlistgetrowhoverable.md)

- [dgsGridListSetRowHoverable](mta://scripting/client/functions/dgsgridlistsetrowhoverable.md)

- [dgsGridListGetItemAlignment](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetItemAlignment&action=edit&redlink=1)

- [dgsGridListSetItemAlignment](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetItemAlignment&action=edit&redlink=1)

- [dgsGridListSetItemTextSize](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetItemTextSize&action=edit&redlink=1)

- [dgsGridListGetItemTextSize](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetItemTextSize&action=edit&redlink=1)

- [dgsGridListSetItemColor](mta://scripting/client/functions/dgsgridlistsetitemcolor.md)

- [dgsGridListGetItemColor](mta://scripting/client/functions/dgsgridlistgetitemcolor.md)

- [dgsGridListSetItemTextOffset](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetItemTextOffset&action=edit&redlink=1)

- [dgsGridListGetItemTextOffset](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetItemTextOffset&action=edit&redlink=1)

- [dgsGridListSetItemText](mta://scripting/client/functions/dgsgridlistsetitemtext.md)

- [dgsGridListGetItemText](mta://scripting/client/functions/dgsgridlistgetitemtext.md)

- [dgsGridListSetItemFont](mta://scripting/client/functions/dgsgridlistsetitemfont.md)

- [dgsGridListGetItemFont](mta://scripting/client/functions/dgsgridlistgetitemfont.md)

- [dgsGridListSetItemData](mta://scripting/client/functions/dgsgridlistsetitemdata.md)

- [dgsGridListGetItemData](mta://scripting/client/functions/dgsgridlistgetitemdata.md)

- [dgsGridListSetItemImage](mta://scripting/client/functions/dgsgridlistsetitemimage.md)

- [dgsGridListGetItemImage](mta://scripting/client/functions/dgsgridlistgetitemimage.md)

- [dgsGridListRemoveItemImage](mta://scripting/client/functions/dgsgridlistremoveitemimage.md)

- [dgsGridListSetItemBackGroundColorTemplate](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetItemBackGroundColorTemplate&action=edit&redlink=1)

- [dgsGridListSetItemBackGroundImage](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetItemBackGroundImage&action=edit&redlink=1)

- [dgsGridListGetItemBackGroundImage](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetItemBackGroundImage&action=edit&redlink=1)

- [dgsGridListSetItemBackGroundColor](https://wiki.multitheftauto.com/index.php?title=DgsGridListSetItemBackGroundColor&action=edit&redlink=1)

- [dgsGridListGetItemBackGroundColor](https://wiki.multitheftauto.com/index.php?title=DgsGridListGetItemBackGroundColor&action=edit&redlink=1)

- [dgsGridListSelectItem](mta://scripting/client/functions/dgsgridlistselectitem.md)

- [dgsGridListItemIsSelected](mta://scripting/client/functions/dgsgridlistitemisselected.md)

- [dgsGridListGetSelectedCount](mta://scripting/client/functions/dgsgridlistgetselectedcount.md)

- [dgsGridListGetPreselectedItem](mta://scripting/client/functions/dgsgridlistgetpreselecteditem.md)

- [dgsGridListGetSelectedItem](mta://scripting/client/functions/dgsgridlistgetselecteditem.md)

- [dgsGridListSetSelectedItem](mta://scripting/client/functions/dgsgridlistsetselecteditem.md)

- [dgsGridListGetSelectedItems](mta://scripting/client/functions/dgsgridlistgetselecteditems.md)

- [dgsGridListSetSelectedItems](mta://scripting/client/functions/dgsgridlistsetselecteditems.md)

- [dgsGridListGetItemSelectable](mta://scripting/client/functions/dgsgridlistgetitemselectable.md)

- [dgsGridListSetItemSelectable](mta://scripting/client/functions/dgsgridlistsetitemselectable.md)

- [dgsGridListGetItemHoverable](mta://scripting/client/functions/dgsgridlistgetitemhoverable.md)

- [dgsGridListSetItemHoverable](mta://scripting/client/functions/dgsgridlistsetitemhoverable.md)

- [dgsGridListSetSelectionMode](mta://scripting/client/functions/dgsgridlistsetselectionmode.md)

- [dgsGridListGetSelectionMode](mta://scripting/client/functions/dgsgridlistgetselectionmode.md)

- [dgsGridListSetNavigationEnabled](mta://scripting/client/functions/dgsgridlistsetnavigationenabled.md)

- [dgsGridListGetNavigationEnabled](mta://scripting/client/functions/dgsgridlistgetnavigationenabled.md)

- [dgsGridListSetMultiSelectionEnabled](mta://scripting/client/functions/dgsgridlistsetmultiselectionenabled.md)

- [dgsGridListGetMultiSelectionEnabled](mta://scripting/client/functions/dgsgridlistgetmultiselectionenabled.md)

- [dgsGridListSetAutoSortEnabled](mta://scripting/client/functions/dgsgridlistsetautosortenabled.md)

- [dgsGridListGetAutoSortEnabled](mta://scripting/client/functions/dgsgridlistgetautosortenabled.md)

- [dgsGridListSetSortFunction](mta://scripting/client/functions/dgsgridlistsetsortfunction.md)

- [dgsGridListSetSortEnabled](mta://scripting/client/functions/dgsgridlistsetsortenabled.md)

- [dgsGridListGetSortEnabled](mta://scripting/client/functions/dgsgridlistgetsortenabled.md)

- [dgsGridListSort](mta://scripting/client/functions/dgsgridlistsort.md)

- [dgsAttachToGridList](mta://scripting/client/functions/dgsattachtogridlist.md)

- [dgsDetachFromGridList](mta://scripting/client/functions/dgsdetachfromgridlist.md)

## Image

- [dgsCreateImage](mta://scripting/client/functions/dgscreateimage.md)

- [dgsImageSetImage](mta://scripting/client/functions/dgsimagesetimage.md)

- [dgsImageGetImage](mta://scripting/client/functions/dgsimagegetimage.md)

- [dgsImageSetUVSize](mta://scripting/client/functions/dgsimagesetuvsize.md)

- [dgsImageGetUVSize](mta://scripting/client/functions/dgsimagegetuvsize.md)

- [dgsImageSetUVPosition](mta://scripting/client/functions/dgsimagesetuvposition.md)

- [dgsImageGetUVPosition](mta://scripting/client/functions/dgsimagegetuvposition.md)

- [dgsImageGetNativeSize](mta://scripting/client/functions/dgsimagegetnativesize.md)

## Memo

- [dgsCreateMemo](mta://scripting/client/functions/dgscreatememo.md)

- [dgsMemoMoveCaret](mta://scripting/client/functions/dgsmemomovecaret.md)

- [dgsMemoSeekPosition](mta://scripting/client/functions/dgsmemoseekposition.md)

- [dgsMemoGetScrollBar](mta://scripting/client/functions/dgsmemogetscrollbar.md)

- [dgsMemoSetScrollPosition](mta://scripting/client/functions/dgsmemosetscrollposition.md)

- [dgsMemoGetScrollPosition](mta://scripting/client/functions/dgsmemogetscrollposition.md)

- [dgsMemoSetHorizontalScrollPosition](mta://scripting/client/functions/dgsmemosethorizontalscrollposition.md)

- [dgsMemoGetHorizontalScrollPosition](mta://scripting/client/functions/dgsmemogethorizontalscrollposition.md)

- [dgsMemoSetVerticalScrollPosition](mta://scripting/client/functions/dgsmemosetverticalscrollposition.md)

- [dgsMemoGetVerticalScrollPosition](mta://scripting/client/functions/dgsmemogetverticalscrollposition.md)

- [dgsMemoSetCaretPosition](mta://scripting/client/functions/dgsmemosetcaretposition.md)

- [dgsMemoGetCaretPosition](mta://scripting/client/functions/dgsmemogetcaretposition.md)

- [dgsMemoSetCaretStyle](mta://scripting/client/functions/dgsmemosetcaretstyle.md)

- [dgsMemoGetCaretStyle](mta://scripting/client/functions/dgsmemogetcaretstyle.md)

- [dgsMemoSetReadOnly](mta://scripting/client/functions/dgsmemosetreadonly.md)

- [dgsMemoGetReadOnly](mta://scripting/client/functions/dgsmemogetreadonly.md)

- [dgsMemoGetPartOfText](mta://scripting/client/functions/dgsmemogetpartoftext.md)

- [dgsMemoAppendText](mta://scripting/client/functions/dgsmemoappendtext.md)

- [dgsMemoDeleteText](mta://scripting/client/functions/dgsmemodeletetext.md)

- [dgsMemoInsertText](mta://scripting/client/functions/dgsmemoinserttext.md)

- [dgsMemoClearText](mta://scripting/client/functions/dgsmemocleartext.md)

- [dgsMemoGetTextBoundingBox](mta://scripting/client/functions/dgsmemogettextboundingbox.md)

- [dgsMemoSetTypingSound](mta://scripting/client/functions/dgsmemosettypingsound.md)

- [dgsMemoGetTypingSound](mta://scripting/client/functions/dgsmemogettypingsound.md)

- [dgsMemoSetTypingSoundVolume](mta://scripting/client/functions/dgsmemosettypingsoundvolume.md)

- [dgsMemoGetTypingSoundVolume](mta://scripting/client/functions/dgsmemogettypingsoundvolume.md)

- [dgsMemoGetLineCount](mta://scripting/client/functions/dgsmemogetlinecount.md)

- [dgsMemoSetWordWrapState](mta://scripting/client/functions/dgsmemosetwordwrapstate.md)

- [dgsMemoGetWordWrapState](mta://scripting/client/functions/dgsmemogetwordwrapstate.md)

- [dgsMemoSetScrollBarState](mta://scripting/client/functions/dgsmemosetscrollbarstate.md)

- [dgsMemoGetScrollBarState](mta://scripting/client/functions/dgsmemogetscrollbarstate.md)

- [dgsMemoSetMaxLength](mta://scripting/client/functions/dgsmemosetmaxlength.md)

- [dgsMemoGetMaxLength](mta://scripting/client/functions/dgsmemogetmaxlength.md)

## Menu

- [dgsCreateMenu](mta://scripting/client/functions/dgscreatemenu.md)

- [dgsMenuShow](mta://scripting/client/functions/dgsmenushow.md)

- [dgsMenuHide](mta://scripting/client/functions/dgsmenuhide.md)

- [dgsMenuAddItem](mta://scripting/client/functions/dgsmenuadditem.md)

- [dgsMenuSetItemCommand](mta://scripting/client/functions/dgsmenusetitemcommand.md)

- [dgsMenuGetItemCommand](mta://scripting/client/functions/dgsmenugetitemcommand.md)

- [dgsMenuSetItemText](mta://scripting/client/functions/dgsmenusetitemtext.md)

- [dgsMenuGetItemText](mta://scripting/client/functions/dgsmenugetitemtext.md)

- [dgsMenuSetItemTextSize](mta://scripting/client/functions/dgsmenusetitemtextsize.md)

- [dgsMenuGetItemTextSize](mta://scripting/client/functions/dgsmenugetitemtextsize.md)

- [dgsMenuSetItemColor](mta://scripting/client/functions/dgsmenusetitemcolor.md)

- [dgsMenuGetItemColor](mta://scripting/client/functions/dgsmenugetitemcolor.md)

- [dgsMenuAddSeparator](mta://scripting/client/functions/dgsmenuaddseparator.md)

- [dgsMenuRemoveItem](mta://scripting/client/functions/dgsmenuremoveitem.md)

## Label

- [dgsCreateLabel](mta://scripting/client/functions/dgscreatelabel.md)

- [dgsLabelSetColor](mta://scripting/client/functions/dgslabelsetcolor.md)

- [dgsLabelGetColor](mta://scripting/client/functions/dgslabelgetcolor.md)

- [dgsLabelSetHorizontalAlign](mta://scripting/client/functions/dgslabelsethorizontalalign.md)

- [dgsLabelGetHorizontalAlign](mta://scripting/client/functions/dgslabelgethorizontalalign.md)

- [dgsLabelSetVerticalAlign](mta://scripting/client/functions/dgslabelsetverticalalign.md)

- [dgsLabelGetVerticalAlign](mta://scripting/client/functions/dgslabelgetverticalalign.md)

- [dgsLabelGetTextExtent](mta://scripting/client/functions/dgslabelgettextextent.md)

- [dgsLabelGetFontHeight](mta://scripting/client/functions/dgslabelgetfontheight.md)

- [dgsLabelGetTextSize](mta://scripting/client/functions/dgslabelgettextsize.md)

## Layout

- [dgsCreateLayout](https://wiki.multitheftauto.com/index.php?title=DgsCreateLayout&action=edit&redlink=1)

- [dgsLayoutAddItem](https://wiki.multitheftauto.com/index.php?title=DgsLayoutAddItem&action=edit&redlink=1)

- [dgsLayoutRemoveItem](https://wiki.multitheftauto.com/index.php?title=DgsLayoutRemoveItem&action=edit&redlink=1)

- [dgsLayoutGetItemIndex](https://wiki.multitheftauto.com/index.php?title=DgsLayoutGetItemIndex&action=edit&redlink=1)

## Line

- [dgsCreateLine](mta://scripting/client/functions/dgscreateline.md)

- [dgsLineAddItem](mta://scripting/client/functions/dgslineadditem.md)

- [dgsLineRemoveItem](mta://scripting/client/functions/dgslineremoveitem.md)

- [dgsLineSetItemPosition](mta://scripting/client/functions/dgslinesetitemposition.md)

- [dgsLineGetItemPosition](mta://scripting/client/functions/dgslinegetitemposition.md)

- [dgsLineSetItemWidth](mta://scripting/client/functions/dgslinesetitemwidth.md)

- [dgsLineGetItemWidth](mta://scripting/client/functions/dgslinegetitemwidth.md)

- [dgsLineSetItemColor](mta://scripting/client/functions/dgslinesetitemcolor.md)

- [dgsLineGetItemColor](mta://scripting/client/functions/dgslinegetitemcolor.md)

## Progress Bar

- [dgsCreateProgressBar](mta://scripting/client/functions/dgscreateprogressbar.md)

- [dgsProgressBarGetProgress](mta://scripting/client/functions/dgsprogressbargetprogress.md)

- [dgsProgressBarSetProgress](mta://scripting/client/functions/dgsprogressbarsetprogress.md)

- [dgsProgressBarGetMode](mta://scripting/client/functions/dgsprogressbargetmode.md)

- [dgsProgressBarSetMode](mta://scripting/client/functions/dgsprogressbarsetmode.md)

- [dgsProgressBarGetStyle](mta://scripting/client/functions/dgsprogressbargetstyle.md)

- [dgsProgressBarSetStyle](mta://scripting/client/functions/dgsprogressbarsetstyle.md)

## Radio Button

- [dgsCreateRadioButton](mta://scripting/client/functions/dgscreateradiobutton.md)

- [dgsRadioButtonGetSelected](mta://scripting/client/functions/dgsradiobuttongetselected.md)

- [dgsRadioButtonSetSelected](mta://scripting/client/functions/dgsradiobuttonsetselected.md)

- [dgsRadioButtonSetHorizontalAlign](mta://scripting/client/functions/dgsradiobuttonsethorizontalalign.md)

- [dgsRadioButtonGetHorizontalAlign](mta://scripting/client/functions/dgsradiobuttongethorizontalalign.md)

- [dgsRadioButtonSetVerticalAlign](mta://scripting/client/functions/dgsradiobuttonsetverticalalign.md)

- [dgsRadioButtonGetVerticalAlign](mta://scripting/client/functions/dgsradiobuttongetverticalalign.md)

- [dgsRadioButtonGetButtonSide](mta://scripting/client/functions/dgsradiobuttongetbuttonside.md)

- [dgsRadioButtonSetButtonSide](mta://scripting/client/functions/dgsradiobuttonsetbuttonside.md)

- [dgsRadioButtonGetButtonAlign](mta://scripting/client/functions/dgsradiobuttongetbuttonalign.md)

- [dgsRadioButtonSetButtonAlign](mta://scripting/client/functions/dgsradiobuttonsetbuttonalign.md)

## Scale Pane

- [dgsCreateScalePane](https://wiki.multitheftauto.com/index.php?title=DgsCreateScalePane&action=edit&redlink=1)

- [dgsScalePaneGetScrollBar](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneGetScrollBar&action=edit&redlink=1)

- [dgsScalePaneSetScrollBarState](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneSetScrollBarState&action=edit&redlink=1)

- [dgsScalePaneGetScrollBarState](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneGetScrollBarState&action=edit&redlink=1)

- [dgsScalePaneSetScrollPosition](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneSetScrollPosition&action=edit&redlink=1)

- [dgsScalePaneGetScrollPosition](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneGetScrollPosition&action=edit&redlink=1)

- [dgsScalePaneSetHorizontalScrollPosition](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneSetHorizontalScrollPosition&action=edit&redlink=1)

- [dgsScalePaneGetHorizontalScrollPosition](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneGetHorizontalScrollPosition&action=edit&redlink=1)

- [dgsScalePaneSetVerticalScrollPosition](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneSetVerticalScrollPosition&action=edit&redlink=1)

- [dgsScalePaneGetVerticalScrollPosition](https://wiki.multitheftauto.com/index.php?title=DgsScalePaneGetVerticalScrollPosition&action=edit&redlink=1)

## Scroll Bar

- [dgsCreateScrollBar](mta://scripting/client/functions/dgscreatescrollbar.md)

- [dgsScrollBarSetScrollPosition](mta://scripting/client/functions/dgsscrollbarsetscrollposition.md)

- [dgsScrollBarGetScrollPosition](mta://scripting/client/functions/dgsscrollbargetscrollposition.md)

- [dgsScrollBarSetGrades](mta://scripting/client/functions/dgsscrollbarsetgrades.md)

- [dgsScrollBarGetGrades](mta://scripting/client/functions/dgsscrollbargetgrades.md)

- [dgsScrollBarSetLocked](mta://scripting/client/functions/dgsscrollbarsetlocked.md)

- [dgsScrollBarGetLocked](mta://scripting/client/functions/dgsscrollbargetlocked.md)

- [dgsScrollBarSetCursorLength](mta://scripting/client/functions/dgsscrollbarsetcursorlength.md)

- [dgsScrollBarGetCursorLength](mta://scripting/client/functions/dgsscrollbargetcursorlength.md)

- [dgsScrollBarSetCursorWidth](mta://scripting/client/functions/dgsscrollbarsetcursorwidth.md)

- [dgsScrollBarGetCursorWidth](mta://scripting/client/functions/dgsscrollbargetcursorwidth.md)

- [dgsScrollBarSetTroughWidth](mta://scripting/client/functions/dgsscrollbarsettroughwidth.md)

- [dgsScrollBarGetTroughWidth](mta://scripting/client/functions/dgsscrollbargettroughwidth.md)

- [dgsScrollBarSetArrowSize](mta://scripting/client/functions/dgsscrollbarsetarrowsize.md)

- [dgsScrollBarGetArrowSize](mta://scripting/client/functions/dgsscrollbargetarrowsize.md)

- [dgsScrollBarSetTroughClickAction](https://wiki.multitheftauto.com/index.php?title=DgsScrollBarSetTroughClickAction&action=edit&redlink=1)

- [dgsScrollBarGetTroughClickAction](https://wiki.multitheftauto.com/index.php?title=DgsScrollBarGetTroughClickAction&action=edit&redlink=1)

## Scroll Pane

- [dgsCreateScrollPane](mta://scripting/client/functions/dgscreatescrollpane.md)

- [dgsScrollPaneGetScrollBar](mta://scripting/client/functions/dgsscrollpanegetscrollbar.md)

- [dgsScrollPaneSetScrollPosition](mta://scripting/client/functions/dgsscrollpanesetscrollposition.md)

- [dgsScrollPaneGetScrollPosition](mta://scripting/client/functions/dgsscrollpanegetscrollposition.md)

- [dgsScrollPaneSetHorizontalScrollPosition](mta://scripting/client/functions/dgsscrollpanesethorizontalscrollposition.md)

- [dgsScrollPaneGetHorizontalScrollPosition](mta://scripting/client/functions/dgsscrollpanegethorizontalscrollposition.md)

- [dgsScrollPaneSetVerticalScrollPosition](mta://scripting/client/functions/dgsscrollpanesetverticalscrollposition.md)

- [dgsScrollPaneGetVerticalScrollPosition](mta://scripting/client/functions/dgsscrollpanegetverticalscrollposition.md)

- dgsScrollPaneSetScrollBarState

- [dgsScrollPaneGetScrollBarState](mta://scripting/client/functions/dgsscrollpanegetscrollbarstate.md)

## Selector

- [dgsCreateSelector](mta://scripting/client/functions/dgscreateselector.md)

- [dgsSelectorAddItem](mta://scripting/client/functions/dgsselectoradditem.md)

- [dgsSelectorRemoveItem](mta://scripting/client/functions/dgsselectorremoveitem.md)

- [dgsSelectorClear](mta://scripting/client/functions/dgsselectorclear.md)

- [dgsSelectorSetSelectedItem](mta://scripting/client/functions/dgsselectorsetselecteditem.md)

- [dgsSelectorGetSelectedItem](mta://scripting/client/functions/dgsselectorgetselecteditem.md)

- [dgsSelectorGetItemText](mta://scripting/client/functions/dgsselectorgetitemtext.md)

- [dgsSelectorSetItemText](mta://scripting/client/functions/dgsselectorsetitemtext.md)

- [dgsSelectorSetItemData](https://wiki.multitheftauto.com/index.php?title=DgsSelectorSetItemData&action=edit&redlink=1)

- [dgsSelectorGetItemData](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetItemData&action=edit&redlink=1)

- [dgsSelectorSetItemColor](https://wiki.multitheftauto.com/index.php?title=DgsSelectorSetItemColor&action=edit&redlink=1)

- [dgsSelectorGetItemColor](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetItemColor&action=edit&redlink=1)

- [dgsSelectorSetItemFont](mta://scripting/client/functions/dgsselectorsetitemfont.md)

- [dgsSelectorGetItemFont](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetItemFont&action=edit&redlink=1)

- [dgsSelectorSetItemTextSize](https://wiki.multitheftauto.com/index.php?title=DgsSelectorSetItemTextSize&action=edit&redlink=1)

- [dgsSelectorGetItemTextSize](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetItemTextSize&action=edit&redlink=1)

- [dgsSelectorSetItemAlignment](https://wiki.multitheftauto.com/index.php?title=DgsSelectorSetItemAlignment&action=edit&redlink=1)

- [dgsSelectorGetItemAlignment](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetItemAlignment&action=edit&redlink=1)

- [dgsSelectorSetItemImage](https://wiki.multitheftauto.com/index.php?title=DgsSelectorSetItemImage&action=edit&redlink=1)

- [dgsSelectorGetItemImage](https://wiki.multitheftauto.com/index.php?title=DgsSelectorGetItemImage&action=edit&redlink=1)

- [dgsSelectorRemoveItemImage](https://wiki.multitheftauto.com/index.php?title=DgsSelectorRemoveItemImage&action=edit&redlink=1)

## Style

- [dgsAddStyle](mta://scripting/client/functions/dgsaddstyle.md)

- [dgsLoadStyle](mta://scripting/client/functions/dgsloadstyle.md)

- [dgsUnloadStyle](mta://scripting/client/functions/dgsunloadstyle.md)

- [dgsSetStyle](mta://scripting/client/functions/dgssetstyle.md)

- [dgsGetStyle](mta://scripting/client/functions/dgsgetstyle.md)

- [dgsGetLoadedStyleList](mta://scripting/client/functions/dgsgetloadedstylelist.md)

- [dgsGetAddedStyleList](mta://scripting/client/functions/dgsgetaddedstylelist.md)

- [dgsGetValueFromStyle](mta://scripting/client/functions/dgsgetvaluefromstyle.md)

## Switch Button

- [dgsCreateSwitchButton](mta://scripting/client/functions/dgscreateswitchbutton.md)

- [dgsSwitchButtonGetState](mta://scripting/client/functions/dgsswitchbuttongetstate.md)

- [dgsSwitchButtonSetState](mta://scripting/client/functions/dgsswitchbuttonsetstate.md)

- [dgsSwitchButtonSetText](mta://scripting/client/functions/dgsswitchbuttonsettext.md)

- [dgsSwitchButtonGetText](mta://scripting/client/functions/dgsswitchbuttongettext.md)

## Tab Panel

- [dgsCreateTabPanel](mta://scripting/client/functions/dgscreatetabpanel.md)

- [dgsCreateTab](mta://scripting/client/functions/dgscreatetab.md)

- [dgsGetSelectedTab](mta://scripting/client/functions/dgsgetselectedtab.md)

- [dgsSetSelectedTab](mta://scripting/client/functions/dgssetselectedtab.md)

- [dgsTabPanelGetTabFromID](mta://scripting/client/functions/dgstabpanelgettabfromid.md)

- [dgsTabPanelMoveTab](mta://scripting/client/functions/dgstabpanelmovetab.md)

- [dgsTabPanelGetTabID](mta://scripting/client/functions/dgstabpanelgettabid.md)

- [dgsDeleteTab](mta://scripting/client/functions/dgsdeletetab.md)

## Window

- [dgsCreateWindow](mta://scripting/client/functions/dgscreatewindow.md)

- [dgsWindowSetSizable](mta://scripting/client/functions/dgswindowsetsizable.md)

- [dgsWindowSetMovable](mta://scripting/client/functions/dgswindowsetmovable.md)

- [dgsWindowGetSizable](mta://scripting/client/functions/dgswindowgetsizable.md)

- [dgsWindowGetMovable](mta://scripting/client/functions/dgswindowgetmovable.md)

- [dgsCloseWindow](mta://scripting/client/functions/dgsclosewindow.md)

- [dgsWindowSetCloseButtonEnabled](mta://scripting/client/functions/dgswindowsetclosebuttonenabled.md)

- [dgsWindowGetCloseButtonEnabled](mta://scripting/client/functions/dgswindowgetclosebuttonenabled.md)

- [dgsWindowSetCloseButtonSize](mta://scripting/client/functions/dgswindowsetclosebuttonsize.md)

- [dgsWindowGetCloseButtonSize](mta://scripting/client/functions/dgswindowgetclosebuttonsize.md)

- [dgsWindowGetCloseButton](mta://scripting/client/functions/dgswindowgetclosebutton.md)

- [dgsWindowSetHorizontalAlign](mta://scripting/client/functions/dgswindowsethorizontalalign.md)

- [dgsWindowSetVerticalAlign](mta://scripting/client/functions/dgswindowsetverticalalign.md)

- [dgsWindowGetHorizontalAlign](mta://scripting/client/functions/dgswindowgethorizontalalign.md)

- [dgsWindowGetVerticalAlign](mta://scripting/client/functions/dgswindowgetverticalalign.md)

- [dgsWindowGetTextExtent](mta://scripting/client/functions/dgswindowgettextextent.md)

- [dgsWindowGetFontHeight](mta://scripting/client/functions/dgswindowgetfontheight.md)

- [dgsWindowGetTextSize](mta://scripting/client/functions/dgswindowgettextsize.md)

## Basic Shape Plugins

### Circle

- [dgsCreateCircle](mta://scripting/client/functions/dgscreatecircle.md)

- [dgsCircleSetRadius](mta://scripting/client/functions/dgscirclesetradius.md)

- [dgsCircleGetRadius](mta://scripting/client/functions/dgscirclegetradius.md)

- [dgsCircleSetTexture](mta://scripting/client/functions/dgscirclesettexture.md)

- [dgsCircleGetTexture](mta://scripting/client/functions/dgscirclegettexture.md)

- [dgsCircleSetColor](mta://scripting/client/functions/dgscirclesetcolor.md)

- [dgsCircleGetColor](mta://scripting/client/functions/dgscirclegetcolor.md)

- [dgsCircleSetColorOverwritten](https://wiki.multitheftauto.com/index.php?title=DgsCircleSetColorOverwritten&action=edit&redlink=1)

- [dgsCircleGetColorOverwritten](https://wiki.multitheftauto.com/index.php?title=DgsCircleGetColorOverwritten&action=edit&redlink=1)

- [dgsCircleSetDirection](mta://scripting/client/functions/dgscirclesetdirection.md)

- [dgsCircleGetDirection](mta://scripting/client/functions/dgscirclegetdirection.md)

- [dgsCircleSetAngle](mta://scripting/client/functions/dgscirclesetangle.md)

- [dgsCircleGetAngle](mta://scripting/client/functions/dgscirclegetangle.md)

- [dgsCircleSetRotation](mta://scripting/client/functions/dgscirclesetrotation.md)

- [dgsCircleGetRotation](mta://scripting/client/functions/dgscirclegetrotation.md)

- [dgsCircleSetTextureRotation](mta://scripting/client/functions/dgscirclesettexturerotation.md)

- [dgsCircleGetTextureRotation](mta://scripting/client/functions/dgscirclegettexturerotation.md)

### Quadrilateral

- [dgsCreateQuad](mta://scripting/client/functions/dgscreatequad.md)

- [dgsQuadSetVertices](https://wiki.multitheftauto.com/index.php?title=DgsQuadSetVertices&action=edit&redlink=1)

- [dgsQuadGetVertices](https://wiki.multitheftauto.com/index.php?title=DgsQuadGetVertices&action=edit&redlink=1)

- [dgsQuadSetTexture](https://wiki.multitheftauto.com/index.php?title=DgsQuadSetTexture&action=edit&redlink=1)

- [dgsQuadGetTexture](https://wiki.multitheftauto.com/index.php?title=DgsQuadGetTexture&action=edit&redlink=1)

- [dgsQuadSetColor](https://wiki.multitheftauto.com/index.php?title=DgsQuadSetColor&action=edit&redlink=1)

- [dgsQuadGetColor](https://wiki.multitheftauto.com/index.php?title=DgsQuadGetColor&action=edit&redlink=1)

- [dgsQuadSetColorOverwritten](https://wiki.multitheftauto.com/index.php?title=DgsQuadSetColorOverwritten&action=edit&redlink=1)

- [dgsQuadGetColorOverwritten](https://wiki.multitheftauto.com/index.php?title=DgsQuadGetColorOverwritten&action=edit&redlink=1)

- [dgsQuadSetRotation](https://wiki.multitheftauto.com/index.php?title=DgsQuadSetRotation&action=edit&redlink=1)

- [dgsQuadSetRotation](https://wiki.multitheftauto.com/index.php?title=DgsQuadSetRotation&action=edit&redlink=1)

- [dgsQuadSetTextureRotation](https://wiki.multitheftauto.com/index.php?title=DgsQuadSetTextureRotation&action=edit&redlink=1)

- [dgsQuadGetTextureRotation](https://wiki.multitheftauto.com/index.php?title=DgsQuadGetTextureRotation&action=edit&redlink=1)

### Rounded Rectangle

- [dgsCreateRoundRect](mta://scripting/client/functions/dgscreateroundrect.md)

- [dgsRoundRectSetTexture](mta://scripting/client/functions/dgsroundrectsettexture.md)

- [dgsRoundRectGetTexture](mta://scripting/client/functions/dgsroundrectgettexture.md)

- [dgsRoundRectSetRadius](mta://scripting/client/functions/dgsroundrectsetradius.md)

- [dgsRoundRectGetRadius](mta://scripting/client/functions/dgsroundrectgetradius.md)

- [dgsRoundRectSetColor](mta://scripting/client/functions/dgsroundrectsetcolor.md)

- [dgsRoundRectGetColor](mta://scripting/client/functions/dgsroundrectgetcolor.md)

- [dgsRoundRectSetColorOverwritten](mta://scripting/client/functions/dgsroundrectsetcoloroverwritten.md)

- [dgsRoundRectGetColorOverwritten](mta://scripting/client/functions/dgsroundrectgetcoloroverwritten.md)

- [dgsRoundRectSetBorderThickness](mta://scripting/client/functions/dgsroundrectsetborderthickness.md)

- [dgsRoundRectGetBorderThickness](mta://scripting/client/functions/dgsroundrectgetborderthickness.md)

- [dgsRoundRectGetBorderOnly](mta://scripting/client/functions/dgsroundrectgetborderonly.md)

## Other Plugins

### Blur Box

- [dgsCreateBlurBox](mta://scripting/client/functions/dgscreateblurbox.md)

- [dgsBlurBoxSetTexture](mta://scripting/client/functions/dgsblurboxsettexture.md)

- [dgsBlurBoxGetTexture](mta://scripting/client/functions/dgsblurboxgettexture.md)

- [dgsBlurBoxSetResolution](mta://scripting/client/functions/dgsblurboxsetresolution.md)

- [dgsBlurBoxSetIntensity](mta://scripting/client/functions/dgsblurboxsetintensity.md)

- [dgsBlurBoxSetLevel](mta://scripting/client/functions/dgsblurboxsetlevel.md)

- [dgsBlurBoxGetResolution](mta://scripting/client/functions/dgsblurboxgetresolution.md)

- [dgsBlurBoxGetLevel](mta://scripting/client/functions/dgsblurboxgetlevel.md)

- [dgsBlurBoxGetIntensity](mta://scripting/client/functions/dgsblurboxgetintensity.md)

- [dgsBlurBoxSetFilter](mta://scripting/client/functions/dgsblurboxsetfilter.md)

### Canvas

- [dgsCreateCanvas](mta://scripting/client/functions/dgscreatecanvas.md)

### Chart

- [dgsCreateChart](mta://scripting/client/functions/dgscreatechart.md)

- [dgsChartAddDataset](https://wiki.multitheftauto.com/index.php?title=DgsChartAddDataset&action=edit&redlink=1)

- [dgsChartRemoveDataset](https://wiki.multitheftauto.com/index.php?title=DgsChartRemoveDataset&action=edit&redlink=1)

- [dgsChartSetLabels](https://wiki.multitheftauto.com/index.php?title=DgsChartSetLabels&action=edit&redlink=1)

- [dgsChartDatasetSetStyle](https://wiki.multitheftauto.com/index.php?title=DgsChartDatasetSetStyle&action=edit&redlink=1)

- [dgsChartDatasetSetLabel](https://wiki.multitheftauto.com/index.php?title=DgsChartDatasetSetLabel&action=edit&redlink=1)

- [dgsChartDatasetSetData](https://wiki.multitheftauto.com/index.php?title=DgsChartDatasetSetData&action=edit&redlink=1)

- [dgsChartDatasetAddData](https://wiki.multitheftauto.com/index.php?title=DgsChartDatasetAddData&action=edit&redlink=1)

- [dgsChartDatasetRemoveData](https://wiki.multitheftauto.com/index.php?title=DgsChartDatasetRemoveData&action=edit&redlink=1)

- [dgsChartDatasetClearData](https://wiki.multitheftauto.com/index.php?title=DgsChartDatasetClearData&action=edit&redlink=1)

### Color Picker

- [dgsCreateColorPicker](mta://scripting/client/functions/dgscreatecolorpicker.md)

- [dgsColorPickerSetColor](mta://scripting/client/functions/dgscolorpickersetcolor.md)

- [dgsColorPickerGetColor](mta://scripting/client/functions/dgscolorpickergetcolor.md)

- [dgsBindToColorPicker](mta://scripting/client/functions/dgsbindtocolorpicker.md)

- [dgsUnbindFromColorPicker](mta://scripting/client/functions/dgsunbindfromcolorpicker.md)

- [dgsColorPickerCreateComponentSelector](mta://scripting/client/functions/dgscolorpickercreatecomponentselector.md)

- [dgsColorPickerGetComponentSelectorValue](mta://scripting/client/functions/dgscolorpickergetcomponentselectorvalue.md)

- [dgsColorPickerSetComponentSelectorValue](mta://scripting/client/functions/dgscolorpickersetcomponentselectorvalue.md)

- [dgsColorPickerGetComponentSelectorMask](https://wiki.multitheftauto.com/index.php?title=DgsColorPickerGetComponentSelectorMask&action=edit&redlink=1)

- [dgsColorPickerSetComponentSelectorMask](https://wiki.multitheftauto.com/index.php?title=DgsColorPickerSetComponentSelectorMask&action=edit&redlink=1)

### Effect 3D

- [dgsCreateEffect3D](mta://scripting/client/functions/dgscreateeffect3d.md)

- [dgsEffect3DApplyToScrollPane](mta://scripting/client/functions/dgseffect3dapplytoscrollpane.md)

- [dgsEffect3DRemoveFromScrollPane](mta://scripting/client/functions/dgseffect3dremovefromscrollpane.md)

- [dgsEffect3DSetRotationFactor](https://wiki.multitheftauto.com/index.php?title=DgsEffect3DSetRotationFactor&action=edit&redlink=1)

- [dgsEffect3DGetRotationFactor](https://wiki.multitheftauto.com/index.php?title=DgsEffect3DGetRotationFactor&action=edit&redlink=1)

- [dgsEffect3DSetAlwaysEnabled](https://wiki.multitheftauto.com/index.php?title=DgsEffect3DSetAlwaysEnabled&action=edit&redlink=1)

- [dgsEffect3DGetAlwaysEnabled](https://wiki.multitheftauto.com/index.php?title=DgsEffect3DGetAlwaysEnabled&action=edit&redlink=1)

### GIF

- [dgsCreateGIF](mta://scripting/client/functions/dgscreategif.md)

- [dgsGIFGetSize](mta://scripting/client/functions/dgsgifgetsize.md)

- [dgsGIFGetImageCount](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetImageCount&action=edit&redlink=1)

- [dgsGIFGetImages](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetImages&action=edit&redlink=1)

- [dgsGIFPlay](https://wiki.multitheftauto.com/index.php?title=DgsGIFPlay&action=edit&redlink=1)

- [dgsGIFStop](https://wiki.multitheftauto.com/index.php?title=DgsGIFStop&action=edit&redlink=1)

- [dgsGIFSetSpeed](https://wiki.multitheftauto.com/index.php?title=DgsGIFSetSpeed&action=edit&redlink=1)

- [dgsGIFGetSpeed](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetSpeed&action=edit&redlink=1)

- [dgsGIFGetPlaying](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetPlaying&action=edit&redlink=1)

- [dgsGIFSetLooped](https://wiki.multitheftauto.com/index.php?title=DgsGIFSetLooped&action=edit&redlink=1)

- [dgsGIFGetLooped](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetLooped&action=edit&redlink=1)

- [dgsGIFSetFrameID](https://wiki.multitheftauto.com/index.php?title=DgsGIFSetFrameID&action=edit&redlink=1)

- [dgsGIFGetFrameID](https://wiki.multitheftauto.com/index.php?title=DgsGIFGetFrameID&action=edit&redlink=1)

### Gradient

- [dgsCreateGradient](mta://scripting/client/functions/dgscreategradient.md)

- [dgsGradientSetColor](mta://scripting/client/functions/dgsgradientsetcolor.md)

- [dgsGradientGetColor](https://wiki.multitheftauto.com/index.php?title=DgsGradientGetColor&action=edit&redlink=1)

- [dgsGradientSetRotation](https://wiki.multitheftauto.com/index.php?title=DgsGradientSetRotation&action=edit&redlink=1)

- [dgsGradientGetRotation](https://wiki.multitheftauto.com/index.php?title=DgsGradientGetRotation&action=edit&redlink=1)

- [dgsGradientSetTexture](https://wiki.multitheftauto.com/index.php?title=DgsGradientSetTexture&action=edit&redlink=1)

- [dgsGradientGetTexture](https://wiki.multitheftauto.com/index.php?title=DgsGradientGetTexture&action=edit&redlink=1)

- [dgsGradientSetColorOverwritten](mta://scripting/client/functions/dgsgradientsetcoloroverwritten.md)

- [dgsGradientGetColorOverwritten](mta://scripting/client/functions/dgsgradientgetcoloroverwritten.md)

### Mask

- [dgsCreateMask](mta://scripting/client/functions/dgscreatemask.md)

- [dgsMaskGetSetting](https://wiki.multitheftauto.com/index.php?title=DgsMaskGetSetting&action=edit&redlink=1)

- [dgsMaskSetSetting](https://wiki.multitheftauto.com/index.php?title=DgsMaskSetSetting&action=edit&redlink=1)

- [dgsMaskGetTexture](mta://scripting/client/functions/dgsmaskgettexture.md)

- [dgsMaskSetTexture](mta://scripting/client/functions/dgsmasksettexture.md)

- [dgsMaskCenterTexturePosition](mta://scripting/client/functions/dgsmaskcentertextureposition.md)

- [dgsMaskAdaptTextureSize](mta://scripting/client/functions/dgsmaskadapttexturesize.md)

### Media Browser

- [dgsCreateMediaBrowser](mta://scripting/client/functions/dgscreatemediabrowser.md)

- [dgsMediaLoadMedia](mta://scripting/client/functions/dgsmedialoadmedia.md)

- [dgsMediaGetMediaPath](mta://scripting/client/functions/dgsmediagetmediapath.md)

- [dgsMediaClearMedia](mta://scripting/client/functions/dgsmediaclearmedia.md)

- [dgsMediaIsStreamMedia](mta://scripting/client/functions/dgsmediaisstreammedia.md)

- [dgsMediaPlay](mta://scripting/client/functions/dgsmediaplay.md)

- [dgsMediaPause](mta://scripting/client/functions/dgsmediapause.md)

- [dgsMediaStop](mta://scripting/client/functions/dgsmediastop.md)

- [dgsMediaGetDuration](mta://scripting/client/functions/dgsmediagetduration.md)

- [dgsMediaGetCurrentPosition](mta://scripting/client/functions/dgsmediagetcurrentposition.md)

- [dgsMediaSetCurrentPosition](https://wiki.multitheftauto.com/index.php?title=DgsMediaSetCurrentPosition&action=edit&redlink=1)

- [dgsMediaGetLooped](mta://scripting/client/functions/dgsmediagetlooped.md)

- [dgsMediaSetLooped](mta://scripting/client/functions/dgsmediasetlooped.md)

- [dgsMediaGetSpeed](https://wiki.multitheftauto.com/index.php?title=DgsMediaGetSpeed&action=edit&redlink=1)

- [dgsMediaSetSpeed](https://wiki.multitheftauto.com/index.php?title=DgsMediaSetSpeed&action=edit&redlink=1)

### Nine Slice

- [dgsCreateNineSlice](mta://scripting/client/functions/dgscreatenineslice.md)

- [dgsNineSliceSetGrid](mta://scripting/client/functions/dgsnineslicesetgrid.md)

- [dgsNineSliceGetGrid](mta://scripting/client/functions/dgsnineslicegetgrid.md)

### Object Preview Supports

- [dgsCreateObjectPreviewHandle](mta://scripting/client/functions/dgscreateobjectpreviewhandle.md)

- [dgsLocateObjectPreviewResource](mta://scripting/client/functions/dgslocateobjectpreviewresource.md)

- [dgsAttachObjectPreviewToImage](mta://scripting/client/functions/dgsattachobjectpreviewtoimage.md)

- [dgsRemoveObjectPreviewFromImage](mta://scripting/client/functions/dgsremoveobjectpreviewfromimage.md)

- [dgsObjectPreviewGetHandleByID](mta://scripting/client/functions/dgsobjectpreviewgethandlebyid.md)

- [dgsConfigureObjectPreview](mta://scripting/client/functions/dgsconfigureobjectpreview.md)

### Paste Handler

- [dgsPasteHandlerSetEnabled](mta://scripting/client/functions/dgspastehandlersetenabled.md)

- [dgsPasteHandlerIsEnabled](mta://scripting/client/functions/dgspastehandlerisenabled.md)

- [dgsPasteHandlerSetFocused](mta://scripting/client/functions/dgspastehandlersetfocused.md)

- [dgsPasteHandlerIsFocused](mta://scripting/client/functions/dgspastehandlerisfocused.md)

### QRCode

- [dgsRequestQRCode](mta://scripting/client/functions/dgsrequestqrcode.md)

- [dgsGetQRCodeLoaded](mta://scripting/client/functions/dgsgetqrcodeloaded.md)

### Remote Image

- [dgsCreateRemoteImage](mta://scripting/client/functions/dgscreateremoteimage.md)

- [dgsRemoteImageRequest](mta://scripting/client/functions/dgsremoteimagerequest.md)

- [dgsRemoteImageAbort](mta://scripting/client/functions/dgsremoteimageabort.md)

- [dgsRemoteImageGetTexture](mta://scripting/client/functions/dgsremoteimagegettexture.md)

- [dgsGetRemoteImageLoadState](mta://scripting/client/functions/dgsgetremoteimageloadstate.md)

### Render Target

### Screen Source

- [dgsCreateScreenSource](https://wiki.multitheftauto.com/index.php?title=DgsCreateScreenSource&action=edit&redlink=1)

- [dgsScreenSourceSetUVPosition](https://wiki.multitheftauto.com/index.php?title=DgsScreenSourceSetUVPosition&action=edit&redlink=1)

- [dgsScreenSourceGetUVPosition](https://wiki.multitheftauto.com/index.php?title=DgsScreenSourceGetUVPosition&action=edit&redlink=1)

- [dgsScreenSourceSetUVSize](https://wiki.multitheftauto.com/index.php?title=DgsScreenSourceSetUVSize&action=edit&redlink=1)

- [dgsScreenSourceGetUVSize](https://wiki.multitheftauto.com/index.php?title=DgsScreenSourceGetUVSize&action=edit&redlink=1)

### SVG

- [dgsCreateSVG](mta://scripting/client/functions/dgscreatesvg.md)

- [dgsSVGGetRawDocument](mta://scripting/client/functions/dgssvggetrawdocument.md)

- [dgsSVGGetDocument](mta://scripting/client/functions/dgssvggetdocument.md)

- [dgsSVGCreateNode](mta://scripting/client/functions/dgssvgcreatenode.md)

- [dgsSVGDestroyNode](mta://scripting/client/functions/dgssvgdestroynode.md)

- [dgsSVGNodeSetAttribute](mta://scripting/client/functions/dgssvgnodesetattribute.md)

- [dgsSVGNodeGetAttribute](mta://scripting/client/functions/dgssvgnodegetattribute.md)

- [dgsSVGNodeSetAttributes](mta://scripting/client/functions/dgssvgnodesetattributes.md)

- [dgsSVGNodeGetAttributes](mta://scripting/client/functions/dgssvgnodegetattributes.md)

### Tooltips

- [dgsCreateToolTip](mta://scripting/client/functions/dgscreatetooltip.md)

- [dgsTooltipApplyTo](mta://scripting/client/functions/dgstooltipapplyto.md)

- [dgsTooltipRemoveFrom](mta://scripting/client/functions/dgstooltipremovefrom.md)
