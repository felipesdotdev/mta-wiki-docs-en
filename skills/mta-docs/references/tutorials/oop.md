---
doc_id: "mta-wiki:7714"
title: "OOP"
source_title: "OOP"
source_url: "https://wiki.multitheftauto.com/wiki/OOP"
revision_id: 79544
language: "en"
categories: ["OOP", "Incomplete", "Tutorials"]
---

# OOP

Object Orientated Programming was introduced in MTA:SA 1.4 and comes with special utility classes like [Vector](mta://reference/misc/vector.md) and [Matrix](mta://reference/misc/matrix.md). This page contains general information about the OOP functions and provides useful links.

## Turning it on

By default, OOP is disabled (however, vectors and matrices are always available) - this is mainly because the vast majority of servers will prefer to stick to what they know - procedural programming. In fact, functions are still available even when OOP is enabled. Enabling OOP is as simple as adding the following line to the resource meta file:

```
<oop>true</oop>
```

## Vectors and Matrices

[Vectors](mta://reference/misc/vector.md) and [Matrices](mta://reference/misc/matrix.md) make it easier to drop the complex maths and go straight ahead with fun part of maths. As mentioned above, OOP does not have to be enabled in the server config for this to be enabled.

## ADVANCED: OOP Metatable Structure

You will understand this if you're proficient with Lua and have a decent understanding of metatables. Understanding this section is not necessary to use OOP.

```
-- Exposed to global environment
Element = {
    Element = createElement,
    setPosition = setElementPosition,
    ...
}

Vehicle = {
    Vehicle = createVehicle,
    setColor = setVehicleColor,
    ...
}

-- Hidden in lua registry, applied to userdata
ElementMT = {
    __index = CLuaClassDefs::Index,
    __newindex = CLuaClassDefs::NewIndex,
    __class = Element,
    __call = __class.create,
    __set = {
        type = CLuaClassDefs::ReadOnly,
        health = setElementHealth,
        ...
    },
    __get = {
        type = getElementType,
        health = getElementHealth,
        ...
    },
}

VehicleMT = {
    __index = CLuaClassDefs::Index,
    __newindex = CLuaClassDefs::NewIndex,
    __class = Vehicle,
    __parent = ElementMT,
    __call = __class.create,
    __set = {
        damageProof = setVehicleDamageProof
        ...
    },
    __get = {
        damageProof = isVehicleDamageProof
        ...
    },
}
```

## Useful Links

- **[OOP Introduction](mta://tutorials/oop-introduction.md)** - teaches you about the basics of OOP

- **[Function list (client)](mta://reference/misc/oop-client.md)** and **[Function list (server)](mta://reference/misc/oop-server.md)** - a list of functions implemented
