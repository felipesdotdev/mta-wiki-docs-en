---
doc_id: "mta-wiki:7379"
title: "MTA:Eir/functions/engineIsWorldStreamingEnabled"
source_title: "MTA:Eir/functions/engineIsWorldStreamingEnabled"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineIsWorldStreamingEnabled"
revision_id: 77720
language: "en"
categories: ["Client_functions"]
---

# MTA:Eir/functions/engineIsWorldStreamingEnabled

This function returns whether the native GTA:SA world is allowed to stream and render. This property is meant to be used along with maps that are meant to exist stand-alone (such as total conversion maps).

## Syntax

```
bool engineIsWorldStreamingEnabled ()
```

### Returns

Returns **true** if native world streaming is enabled, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet plays a sound depending on whether world streaming is enabled or not. It expects two sound files: "win.wav" and "fail.wav"

```
addCommandHandler( "world_check",
    function()
        local isEnabled = engineIsWorldStreamingEnabled();

        if ( isEnabled ) then
            playSound( "win.wav" );
        else
            playSound( "fail.wav" );
        end
    end
);
```
