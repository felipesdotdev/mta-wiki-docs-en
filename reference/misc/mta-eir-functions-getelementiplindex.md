---
doc_id: "mta-wiki:7397"
title: "MTA:Eir/functions/getElementIPLIndex"
source_title: "MTA:Eir/functions/getElementIPLIndex"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/functions/getElementIPLIndex"
revision_id: 50698
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.571794+00:00"
---

# MTA:Eir/functions/getElementIPLIndex

This function returns the IPL index of the given entity. If the IPL index is != 0, then the entity is managed by native GTA:SA, otherwise MTA. The IPL index can be used with [getIPLSectorInfo](https://wiki.multitheftauto.com/index.php?title=MTA:Eir/functions/getIPLSectorInfo&action=edit&redlink=1) to retrieve additional information.

An IPL sector is a zone on the native GTA:SA world. It stores dummies, buildings and objects. Its buildings and objects are created when streamed in and destroyed when streamed out.

This function is part of the discussion: **shall buildings be made MTA entities?**

## Syntax

```
int getElementIPLIndex ( element entity )
```

### Arguments

- **entity:** a streamed in MTA entity

### Returns

Returns the IPL index associated with the given entity if it is streamed in, **false** otherwise.

## Example

Click to collapse [-]
Client

This snippet destroys all buildings that are managed by native GTA:SA (WIP; POD)

```
local function entityClearHandler( entity )
    if ( isElementStreamedIn( entity ) ) and not ( getElementIPLIndex( entity ) == 0 ) then
        destroyElement( entity );
    end
end

local function clearWorld()
    for m,n in ipairs( getElementsByType( "building" ) ) do entityClearHandler( n ); end
    for m,n in ipairs( getElementsByType( "dummy" ) ) do entityClearHandler( n ); end
    for m,n in ipairs( getElementsByType( "object" ) ) do entityClearHandler( n ); end
end
```
