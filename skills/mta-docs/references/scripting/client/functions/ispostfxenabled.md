---
doc_id: "mta-wiki:14656"
title: "IsPostFXEnabled"
source_title: "IsPostFXEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/IsPostFXEnabled"
revision_id: 82641
language: "en"
categories: ["Client_functions", "Changes_in_1.6"]
---

# IsPostFXEnabled

ADDED/UPDATED IN VERSION 1.6 [r23644](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23644):

Checks whether a specific PostFX effect is currently enabled.

## Syntax

```
bool isPostFXEnabled ( string fxType )
```

### Required arguments

- **fxType**: An string of the PostFX. Possible values are:

- **Gamma**

- **Brightness**

- **Contrast**

- **Saturation**

### Returns

Returns **true** if the selected type is enabled, otherwise **false**

## Example

This example gets whether the gamma PostFX is enabled and displays it in the chat.

```
addCommandHandler("isGammaEnabled", 
    function()
        local isEnabled = isPostFXEnabled("Gamma")
        outputChatBox("Your gamma mode is: "..(isEnabled and "Enabled" or "Disabled"))
    end, false, false
)
```

## See Also

ADDED/UPDATED IN VERSION 1.6 [r23644](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23644):

- [getPostFXValue](mta://scripting/client/functions/getpostfxvalue.md)

- [getPostFXMode](mta://scripting/client/functions/getpostfxmode.md)

- isPostFXEnabled
