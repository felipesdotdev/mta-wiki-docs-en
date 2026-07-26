---
doc_id: "mta-wiki:13266"
title: "Resource : Custom edit"
source_title: "Resource:Custom edit"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3ACustom_edit"
revision_id: 79895
language: "en"
categories: ["Utility_templates", "Client_events", "Resource"]
---

# Resource : Custom edit

This resource allow you to create custom editbox.
Download [GitHub](https://github.com/sirphantasm/custom_edit).  

Resource developed by: Shuffle

## Exported functions/events

Click to collapse [-]
Functions/Events

By this function you can create new editbox with variable.

```
bool createCustomEdit(string default-text, float x, float y, float width, float height, bool postgui, string placeholder, bool masked, filepath font, table activecolor, table fontcolor table backgroundcolor, table caretcolor, bool visible, number length, number fontsize)
```

#### Required Arguments

- **text:** Default text to draw in the editbox. Recommended "".

- **x:** A float of the 2D screen x position.

- **y:** A float of the 2D screen y position.

- **width:** A float of the 2D screen y position.

- **heigth:** A float of the 2D screen y position.

#### Optional arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](https://wiki.multitheftauto.com/index.php?search=optional%20arguments).

- **postGUI:** A bool representing whether the text should be drawn on top of or behind any ingame GUI (default false).

- **placeHolder:** A string of the placeholder text of editbox (default false).

- **masked:** covering up the text being typed for password text fields (default false).

- **font:** Name of font from folder "fonts" (default false, arial).

- **activeColor:** Color of line on the bottom when edit is active (default red).

- **fontColor:** Color of font (default white).

- **backgroundColor:** Color of editbox (default black).

- **caretColor:** Color of caret in text field (default white).

- **visible:** Visibility of editbox (default true).

- **length:** Max length for text field (default 40).

- **font size:** Available for DXFont (default scaled to edit size).

- **block space:** If it is true, user cant enter space (for example - login edit).

#### Returns

Returns ID if element was successfully created, false otherwise.

This function change visibility of editbox.

```
bool editSetVisible(element theElement, bool state)
```

#### Required Arguments

- **theElement:** Element which you want to change.

- **state:** true or false.

#### Returns

Returns true if successfully , false otherwise.

This function set mask to password fields

```
bool editSetMasked(element theElement, bool mask)
```

#### Required Arguments

- **theElement:** Element which you want to set mask.

- **state:** true of false.

#### Returns

Returns true if editbox will be masked, false otherwise.

This function gets text from text field.

```
bool editGetText(element theElement)
```

#### Required Arguments

- **theElement:** Element from where you want to get text.

#### Returns

Returns string text if successfully , false otherwise.

This function changes text into text field.

```
bool editSetText(element theElement, string text)
```

#### Required Arguments

- **theElement:** Element which you want to change text.

- **text:** New value.

#### Returns

Returns true if text set successfully, false otherwise.

This function changes max length od text field

```
bool editMaxLength(element theElement, float length)
```

#### Required Arguments

- **theElement:** Element which you want to change length.

- **length:** New value.

#### Returns

Returns true if length set successfully, false otherwise.

This function change 2D position on the screen.

```
bool editChangePos(element theElement, float x, float y)
```

#### Required Arguments

- **theElement:** Element which you want to change position.

- **x:** 2D x position.

- **y:** 2D y position.

#### Returns

Returns true if succesfully, false otherwise.

This function changes all properties of editbox

```
bool editSetProperty(element theElement, string properties, string value)
```

#### Required Arguments

- **theElement:** Element which you want to change property.

- **property:** id,x,y,w,h,postgui,placeholder,masked,font,size,active,activecolor,bgcolor,caret,visible,cursor,maxLength,click,alpha,readOnly.

#### Returns

Returns true if properties set successfully, false otherwise.

This function destroy editbox

```
bool destroyCustomEdit(element theElement)
```

#### Required Arguments

- **theElement:** Element which you want to destroy.

#### Returns

Returns true if destroy successfully, false otherwise.

This function return count of character in edit

```
bool editGetLength(element theElement)
```

#### Required Arguments

- **theElement:** Element which want to check.

#### Returns

Returns count if successfully, false otherwise.

This event trigger when you blur edit

## Parameters

No parameters.

## Source

The source of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) who blur edit.

## Example

This example shows how to use "onCustomEditLeave"

```
addEventHandler("onCustomEditLeave",root,function(edit)
    print("You leave edit "..edit)
end)
```

This event trigger when you blur edit

## Parameters

No parameters.

## Source

The source of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) who focus edit.

## Example

This example shows how to use "onCustomEditFocus"

```
addEventHandler("onCustomEditFocus",root,function(edit)
    print("You focus edit "..edit)
end)
```

This event trigger when you typing in edit

## Parameters

No parameters.

## Source

The source of this event is the [player](https://wiki.multitheftauto.com/index.php?search=player) who typing.

## Example

This example shows how to use "onCustomEditType"

```
addEventHandler("onCustomEditType",root,function(edit)
    if edit==variable_of_edit then
       print("You typed in "..edit)
    end
end)
```

## Example

Click to collapse [-]
Example

This example creates editbox with some accessories.

```
local ce=exports.custom_edit

local edit=ce:createCustomEdit("",500,500,300,70,false,"Password",false,"font2",{255,0,0,255},{255,255,255,255},{0,0,0,150},{255,255,255,255},true,false,false)
ce:editSetMasked(edit,true)
ce:editSetProperty(edit,"bgcolor",{255,255,255,255})
ce:editChangePos(edit,700,700)
ce:editMaxLength(edit,50)
```
