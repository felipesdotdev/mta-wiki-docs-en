---
doc_id: "mta-wiki:14110"
title: "DxGetLibrary"
source_title: "DxGetLibrary"
source_url: "https://wiki.multitheftauto.com/wiki/DxGetLibrary"
revision_id: 77458
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:14:49.218620+00:00"
---

# DxGetLibrary

Esta funcion extrae los diferentes exports de la libreria en forma de variables para hacer el uso de la libreria mas facil para ello debe de complementarse con **loadstring**.

***Aviso: Esta es una función exportada por [Modern-Library](mta://reference/misc/modern-library.md)!***

## Sintaxis

```
string dxGetLibrary()
```

## Ejemplo

```
loadstring( exports.dxLibrary:dxGetLibrary( ) )( )
```

## Ver también

### General Functions

- dxGetLibrary

- [dxGetScreen](https://wiki.multitheftauto.com/index.php?title=DxGetScreen&action=edit&redlink=1)

- [dxSet](https://wiki.multitheftauto.com/index.php?title=DxSet&action=edit&redlink=1)

- [dxGet](https://wiki.multitheftauto.com/index.php?title=DxGet&action=edit&redlink=1)

- [dxSetText](https://wiki.multitheftauto.com/index.php?title=DxSetText&action=edit&redlink=1)

- [dxSetTitle](https://wiki.multitheftauto.com/index.php?title=DxSetTitle&action=edit&redlink=1)

- [dxSetVisible](https://wiki.multitheftauto.com/index.php?title=DxSetVisible&action=edit&redlink=1)

- [dxSetEnabled](https://wiki.multitheftauto.com/index.php?title=DxSetEnabled&action=edit&redlink=1)

- [dxSetPosition](https://wiki.multitheftauto.com/index.php?title=DxSetPosition&action=edit&redlink=1)

- [dxGetPosition](https://wiki.multitheftauto.com/index.php?title=DxGetPosition&action=edit&redlink=1)

- [dxSetSize](https://wiki.multitheftauto.com/index.php?title=DxSetSize&action=edit&redlink=1)

- [dxGetSize](https://wiki.multitheftauto.com/index.php?title=DxGetSize&action=edit&redlink=1)

- [dxGetRootParent](https://wiki.multitheftauto.com/index.php?title=DxGetRootParent&action=edit&redlink=1)

- [dxSetColorBackground](https://wiki.multitheftauto.com/index.php?title=DxSetColorBackground&action=edit&redlink=1)

- [dxSetColorText](https://wiki.multitheftauto.com/index.php?title=DxSetColorText&action=edit&redlink=1)

- [dxSetColorSelected](https://wiki.multitheftauto.com/index.php?title=DxSetColorSelected&action=edit&redlink=1)

- [dxSetColorBorder](https://wiki.multitheftauto.com/index.php?title=DxSetColorBorder&action=edit&redlink=1)

- [dxFont](https://wiki.multitheftauto.com/wiki/DxFont)

- [dxSetFont](mta://scripting/client/functions/dxsetfont.md)

- [dxGetText](https://wiki.multitheftauto.com/index.php?title=DxGetText&action=edit&redlink=1)

- [dxSetTitle](https://wiki.multitheftauto.com/index.php?title=DxSetTitle&action=edit&redlink=1)

- [dxGetTitle](https://wiki.multitheftauto.com/index.php?title=DxGetTitle&action=edit&redlink=1)

### Window

- [dxWindow](mta://scripting/client/functions/dxwindow.md)

- [dxWindowSetCloseState](mta://scripting/client/functions/dxwindowsetclosestate.md)

- [dxWindowGetCloseState](mta://scripting/client/functions/dxwindowgetclosestate.md)

### Button

- [dxButton](mta://scripting/client/functions/dxbutton.md)

### CheckBox

- [dxCheckBox](mta://scripting/client/functions/dxcheckbox.md)

- [dxCheckBoxSetState](mta://scripting/client/functions/dxcheckboxsetstate.md)

- [dxCheckBoxGetState](mta://scripting/client/functions/dxcheckboxgetstate.md)

### Edit

- [dxEdit](mta://scripting/client/functions/dxedit.md)

- [dxEditSetMasked](mta://scripting/client/functions/dxeditsetmasked.md)

- [dxEditSetMaxCharacters](mta://scripting/client/functions/dxeditsetmaxcharacters.md)

### GridList

- [dxGridList](mta://scripting/client/functions/dxgridlist.md)

- [dxGridListAddItem](mta://scripting/client/functions/dxgridlistadditem.md)

- [dxGridListRemoveItem](mta://scripting/client/functions/dxgridlistremoveitem.md)

- [dxGridListAddColumn](mta://scripting/client/functions/dxgridlistaddcolumn.md)

- [dxGridListRemoveColumn](mta://scripting/client/functions/dxgridlistremovecolumn.md)

- [dxGridListGetItemSelected](mta://scripting/client/functions/dxgridlistgetitemselected.md)

- [dxGridListSetItemSelected](mta://scripting/client/functions/dxgridlistsetitemselected.md)

- [dxGridListGetScrollHV](mta://scripting/client/functions/dxgridlistgetscrollhv.md)

### Image

- [dxImage](mta://scripting/client/functions/dximage.md)

- [dxImageApplyMask](https://wiki.multitheftauto.com/index.php?title=DxImageApplyMask&action=edit&redlink=1)

- [dxImageRemoveMask](https://wiki.multitheftauto.com/index.php?title=DxImageRemoveMask&action=edit&redlink=1)

### Label

- [dxLabel](mta://scripting/client/functions/dxlabel.md)

### List

- [dxList](mta://scripting/client/functions/dxlist.md)

- [dxListAddItem](mta://scripting/client/functions/dxlistadditem.md)

- [dxListRemoveItem](mta://scripting/client/functions/dxlistremoveitem.md)

- [dxListGetItemSelected](mta://scripting/client/functions/dxlistgetitemselected.md)

- [dxListSetItemSelected](https://wiki.multitheftauto.com/wiki/DxListSetItemSelected)

- [dxListSetColorFilaItem](https://wiki.multitheftauto.com/index.php?title=DxListSetColorFilaItem&action=edit&redlink=1)

### ProgressBar

- [dxProgressBar](mta://scripting/client/functions/dxprogressbar.md)

- [dxProgressBarSetProgress](mta://scripting/client/functions/dxprogressbarsetprogress.md)

- [dxProgressBarGetProgress](mta://scripting/client/functions/dxprogressbargetprogress.md)

- [dxProgressBarSetColor](mta://scripting/client/functions/dxprogressbarsetcolor.md)

### ScrollBar

- [dxScroll](mta://scripting/client/functions/dxscroll.md)

- [dxScrollGetCurrentPosition](mta://scripting/client/functions/dxscrollgetcurrentposition.md)

- [dxScrollSetCurrentPosition](mta://scripting/client/functions/dxscrollsetcurrentposition.md)

- [dxScrollSetColorButton](mta://scripting/client/functions/dxscrollsetcolorbutton.md)

- [dxScrollSetVertical](mta://scripting/client/functions/dxscrollsetvertical.md)
