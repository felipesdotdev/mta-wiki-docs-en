---
doc_id: "mta-wiki:14654"
title: "GetPostFXMode"
source_title: "GetPostFXMode"
source_url: "https://wiki.multitheftauto.com/wiki/GetPostFXMode"
revision_id: 82629
language: "en"
categories: ["Client_functions", "Changes_in_1.6"]
---

# GetPostFXMode

ADDED/UPDATED IN VERSION 1.6 [r23644](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23644):

Gets the current mode of PostFX.

## Syntax

```
int getPostFXMode ( )
```

### Returns

An integer for the current PostFX mode:

- 0: Disabled

- 1: Enabled in fullscreen mode

- 2: Enabled in windowed/borderless mode

## Example

This example gets the current PostFX mode and displays it in the chat.

```
local modes = {
    [0] = "Disabled",
    [1] = "Enabled in fullscreen mode",
    [2] = "Enabled in windowed/borderless mode"
}

addCommandHandler("getMyMode", 
    function()
        local currentMode = getPostFXMode()
        outputChatBox("Your PostFX mode is: "..modes[currentMode])
    end, false, false
)
```

## See Also

ADDED/UPDATED IN VERSION 1.6 [r23644](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23644):

- [getPostFXValue](mta://scripting/client/functions/getpostfxvalue.md)

- getPostFXMode

- [isPostFXEnabled](mta://scripting/client/functions/ispostfxenabled.md)
