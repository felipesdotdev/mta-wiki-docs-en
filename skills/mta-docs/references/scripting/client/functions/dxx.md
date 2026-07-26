---
doc_id: "mta-wiki:10177"
title: "DXX"
source_title: "DXX"
source_url: "https://wiki.multitheftauto.com/wiki/DXX"
revision_id: 55177
language: "en"
categories: ["Client_functions"]
---

# DXX

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *Use a dot instead of a colon to access class methods*

**Method**: *[Dxx](https://wiki.multitheftauto.com/index.php?title=Dxx&action=edit&redlink=1).on(...)*

## Syntax

```
bool Dxx.on(string eventName, function callbackFunction)
```

### Required Arguments

- **eventName:** The name of the event you want to listen for. Possible values are:

- **click**

- **close**

- **change**

- **destroy**

- **callbackFunction:** The function that is called when this event occurs.

- ***responseData*** - A string containing the remote response or "ERROR" if there was a problem

- ***errno*** - A number containing the error number or zero if there was no error.

- **arguments...** - The arguments that were passed into fetchRemote

### Returns

This function does not return anything

## Example

```
local win = Window(700, 400, 1000, 600, "cool window")
local btn = Button(55, 55, 125, 30, "click me")

btn.setParent(win)
btn.on("click", function() btn.value = "clicked" end)
```
