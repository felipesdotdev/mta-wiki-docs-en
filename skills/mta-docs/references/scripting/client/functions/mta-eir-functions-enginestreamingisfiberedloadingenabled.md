---
doc_id: "mta-wiki:7388"
title: "MTA:Eir/functions/engineStreamingIsFiberedLoadingEnabled"
source_title: "MTA:Eir/functions/engineStreamingIsFiberedLoadingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineStreamingIsFiberedLoadingEnabled"
revision_id: 77727
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineStreamingIsFiberedLoadingEnabled

This function returns whether the [GTA:SA Streaming system](mta://reference/misc/gta-sa-resource-streaming.md) is in original or fibered mode. In original mode, most resources are loaded in one go, but big ones (exceeding slicer buffer size) are loaded exclusively and in two pulses. In fibered mode, the Streaming system can only take a user-defined percentage of the game frame time, meaning that resources can take an arbitrary amount of pulses depending on the complexity of said resources.

By default, fibered loading is enabled.

## Syntax

```
bool engineStreamingIsFiberedLoadingEnabled ()
```

### Returns

Returns **true** if fibered loading is enabled, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet draws on the screen whether fibered loading is enabled or not.

```
addEventHandler( "onClientRender", root,
    function()
        local isEnabled = engineStreamingIsFiberedLoadingEnabled();

        dxDrawText( "Streaming Mode: " .. ( isEnabled and "fibered loading" or "single execution" ), 100, 400 );
    end
);
```
