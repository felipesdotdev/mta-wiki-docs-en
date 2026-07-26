---
doc_id: "mta-wiki:13660"
title: "Modern-Library"
source_title: "Modern-Library"
source_url: "https://wiki.multitheftauto.com/wiki/Modern-Library"
revision_id: 81692
language: "en"
categories: ["Resource"]
---

# Modern-Library

Modern DX Library

This resource is designed to allow you to create directX GUI's as an alternative to the original MTA:SA GUI functions.

| [[{{{image}}}\|link=\|]] | Note: This wiki is always for the latest Modern DX Library version! |
| --- | --- |
|  |  |

**Full Name**: Modern DX Library for User Interface

**Developer Team**: [ClawSuit](https://wiki.multitheftauto.com/index.php?title=User:ClawSuit&action=edit&redlink=1), [PandFort](https://wiki.multitheftauto.com/wiki/User:PandFort)

**Wiki contributor**: [BR4](https://wiki.multitheftauto.com/index.php?title=User:BR4&action=edit&redlink=1)

**GitHub Repo**: *[https://github.com/clawsuit/dxLibrary](https://github.com/clawsuit/dxLibrary)*

**Current Version**: 1.0 Estable

# Features

 

Demo Window

**How does it work?**

- Modern DX Library is based on [element](mta://reference/misc/element.md) system, which just likes the cegui system. To make Modern DX Library easier to use and understand, I choose to follow the usage of cegui's.

- Modern DX Library elements are rendered in the event "onClientRender". When "onClientRender" is called, every Modern DX Library elements will be looped and calculated.

**What's different from cegui?**

- This resource is based on dx* functions, so its style will be more flexible than cegui, which means you can define the style by yourself.

**You Should Know**

- Some of Modern DX Library elements use **Render Target**, which means if you don't have enough video memory, **Render Target won't be created**, and therefore those Modern DX Library elements won't be shown.

# Examples

**Demonstration**: [https://www.youtube.com/watch?v=qakLp6Znws0](https://www.youtube.com/watch?v=qakLp6Znws0)

**Notice**

- It is recommended to change the resource name to 'dxLibrary'.

- This is a resource, if you want to use the functions exported by this resource,  you should use an exported function prefix (**exports[ "dxLibrary" ]:**) call in your code, such as

```
button = exports[ "dxLibrary" ]:dxButton( 50, 50, 40, 20, "Button Test" )
```

- Here is a feasible way to shorten the name of an exported function:

```
dxLib = exports[ "dxLibrary" ] -- shorten the export function prefix

button = dxLib:dxButton( 50, 50, 40, 20, "Button Test" ) -- create a button
```

# **Client Functions**

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

# **Client Events**

### General Events

- [onClick](https://wiki.multitheftauto.com/index.php?search=onClick)

- [onClose](https://wiki.multitheftauto.com/index.php?title=OnClose&action=edit&redlink=1)

- [onScrollChange](https://wiki.multitheftauto.com/index.php?title=OnScrollChange&action=edit&redlink=1)

# Last

**Everyone is welcome to make suggestions, test the script, help make adjustments/finish the wiki, etc.**
