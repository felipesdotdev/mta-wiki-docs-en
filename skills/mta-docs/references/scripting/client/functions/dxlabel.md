---
doc_id: "mta-wiki:14431"
title: "DxLabel"
source_title: "DxLabel"
source_url: "https://wiki.multitheftauto.com/wiki/DxLabel"
revision_id: 80638
language: "en"
categories: ["Client_functions"]
---

# DxLabel

Esta función crea una etiqueta de texto DX.

***Aviso: Esta es una función exportada por [Modern-Library](mta://reference/misc/modern-library.md)!***

## Syntax

```
element dxLabel( int x, int y, int w, int h, string texto, [ element parent = nil , string alignX = 'left', string alignY = 'top', int outline = nil, int colorText = tocolor(255, 255, 255, 255), int colorBorder = tocolor(255, 255, 255, 255), bool guiCoord = false] )
```

### Argumentos requeridos

- **x**: Un entero que representa la posición X de la pantalla.

- **y**: Un entero que representa la posición Y de la pantalla.

- **w**: Un entero que representa el ancho del dxLabel.

- **h**: Un entero que representa la altura del dxLabel.

- **texto**: Una cadena de texto que representa el **titulo** visible.

### Argumentos Opcionales

- **parent**: Este es el padre el cual la [dxLabel](https://wiki.multitheftauto.com/wiki/dxLabel) se adjunta.

- **alignX**: Realineación horizontal ('**izquierda'**, '**centro'** o '**derecha'**): 'left', 'center', 'right'..

- **alignY**: Realineación vertical ('arriba', 'centro' o 'abajo'): 'top', 'center', 'bottom'..

- **outline**: Un número entero que representa el peso del contorno del texto.

- **colortext**: El color del texto, un valor producido por [tocolor](https://wiki.multitheftauto.com/wiki/Tocolor) o 0xAARRGGBB (AA = alfa, RR = rojo, GG = verde, BB = azul).

- **colorborder**: El color del borde del texto, un valor producido por [tocolor](https://wiki.multitheftauto.com/wiki/Tocolor) o 0xAARRGGBB (AA = alfa, RR = rojo, GG = verde, BB = azul).

- **guiCoord**: Suma de valores para adaptar el tamaño a su respectivo **parent**. usa [true](https://wiki.multitheftauto.com/wiki/Boolean) para habilitarlo.

## Ejemplo

```
-- Activación de la libreria

loadstring(exports.dxlibrary:dxGetLibrary())()

-- Texto de Ejemplo

dxLabel(282, 212, 780, 226, 'Label Test', false)
```

## Ver también

### General Functions

- [dxGetLibrary](mta://scripting/client/functions/dxgetlibrary.md)

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

- dxLabel

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
