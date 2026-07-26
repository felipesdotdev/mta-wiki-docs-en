---
doc_id: "mta-wiki:1610"
title: "XmlNodeGetAttribute"
source_title: "XmlNodeGetAttribute"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeGetAttribute"
revision_id: 48703
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:07.924785+00:00"
---

# XmlNodeGetAttribute

This function is used to return an attribute of a node in a configuration file.

## Syntax

```
string xmlNodeGetAttribute ( xmlnode node, string name )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):getAttribute(...)*

**Counterpart**: *[xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)*

### Required Arguments

- **node:** The node from which you wish to return the attribute

- **name:** The name of the attribute.

### Returns

Returns the attribute in string form or *false*, if the attribute is not defined.

## Example

Suppose we have a gametype where only one type of car is used, and this type should not depend on the map but rather be set in an external configuration file and be used in all maps. Here's an example where the configuration file is an XML document:

settings.xml

```
<car model="528" posX="123.4" posY="456.7" posZ="12.3" rot="90.0" />
```

Lua code

```
local xml = getResourceConfig("settings.xml")      -- load XML file and get its root element
local carmodel = xmlNodeGetAttribute(xml, "model")    -- get attribute of root element
local carX = xmlNodeGetAttribute(xml, "posX")
local carY = xmlNodeGetAttribute(xml, "posY")
local carZ = xmlNodeGetAttribute(xml, "posZ")
local carA = xmlNodeGetAttribute(xml, "rot")
createVehicle(carmodel, tonumber(carX), tonumber(carY), tonumber(carZ), 0.0, 0.0, tonumber(carA))
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md)

- [xmlFindChild](mta://scripting/shared/functions/xmlfindchild.md)

- [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md)

- [xmlLoadString](mta://scripting/shared/functions/xmlloadstring.md)

- xmlNodeGetAttribute

- [xmlNodeGetAttributes](mta://scripting/shared/functions/xmlnodegetattributes.md)

- [xmlNodeGetChildren](mta://scripting/shared/functions/xmlnodegetchildren.md)

- [xmlNodeGetName](mta://scripting/shared/functions/xmlnodegetname.md)

- [xmlNodeGetParent](mta://scripting/shared/functions/xmlnodegetparent.md)

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
