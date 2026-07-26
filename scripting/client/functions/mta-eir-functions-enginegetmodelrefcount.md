---
doc_id: "mta-wiki:7376"
title: "MTA:Eir/functions/engineGetModelRefCount"
source_title: "MTA:Eir/functions/engineGetModelRefCount"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/engineGetModelRefCount"
revision_id: 77714
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:16:06.410849+00:00"
---

# MTA:Eir/functions/engineGetModelRefCount

This function returns the reference count of a GTA:SA model info. The reference count describes how often a model info is used by the game (including MTA).

## Syntax

```
int engineGetModelRefCount ( int modelIndex )
```

### Arguments

- **modelIndex:** value ranging from [0..19999] that denotes an internal model info

### Returns

Returns the model reference count if **modelIndex** is a valid model info index and the model info that it points to is allocated, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet destroys every MTA object whose model is used more than twice.

```
addEvent( "onClientElementModelSweep", true );
addEventHandler( "onClientElementModelSweep", root,
    function()
        for m,n in ipairs( getElementsByType( "object" ) ) do
            local refCount = engineGetModelRefCount( getElementModel( n ) );

            if ( refCount > 2 ) then
                destroyElement( n );
            end
        end
    end
);
```
