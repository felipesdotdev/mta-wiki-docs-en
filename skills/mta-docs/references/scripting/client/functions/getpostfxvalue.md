---
doc_id: "mta-wiki:14655"
title: "GetPostFXValue"
source_title: "GetPostFXValue"
source_url: "https://wiki.multitheftauto.com/wiki/GetPostFXValue"
revision_id: 82630
language: "en"
categories: ["Client_functions", "Changes_in_1.6"]
---

# GetPostFXValue

ADDED/UPDATED IN VERSION 1.6 [r23644](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23644):

Gets the current float value of the selected PostFX type.

## Syntax

```
float getPostFXValue ( string fxType )
```

### Required arguments

- **fxType**: An string of the PostFX. Possible values are:

- **Gamma**

- **Brightness**

- **Contrast**

- **Saturation**

### Returns

Returns the current value of the specified PostFX parameter.

## Example

This example gets the current gamma PostFX value and display it in the chat.

```
addCommandHandler("getGammaValue", 
    function()
        local gammaValue = getPostFXValue("Gamma")
        outputChatBox("Your gamma value is: "..tostring(gammaValue))
    end, false, false
)
```

## See Also

ADDED/UPDATED IN VERSION 1.6 [r23644](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23644):

- getPostFXValue

- [getPostFXMode](mta://scripting/client/functions/getpostfxmode.md)

- [isPostFXEnabled](mta://scripting/client/functions/ispostfxenabled.md)
