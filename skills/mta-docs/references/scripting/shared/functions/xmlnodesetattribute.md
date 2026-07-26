---
doc_id: "mta-wiki:1611"
title: "XmlNodeSetAttribute"
source_title: "XmlNodeSetAttribute"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeSetAttribute"
revision_id: 48704
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# XmlNodeSetAttribute

This function is used to edit an attribute of a node in a configuration file.

## Syntax

```
bool xmlNodeSetAttribute ( xmlnode node, string name, string/float value )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):setAttribute(...)*

**Counterpart**: *[xmlNodeGetAttribute](mta://scripting/shared/functions/xmlnodegetattribute.md)*

### Required Arguments

- **node:** The node of which you wish to edit an attribute.

- **name:** The name of the attribute.

- **value:** The value which you wish to change the attribute to. (**Note:** *nil* will delete the attribute)

### Returns

Returns *true* if the attribute was set successfully, *false* if the node and/or attribute do not exist, or if they're faulty.

## Example

Click to collapse [-]
Server

In a gamemode, we want a command to change the marker color in the configuration file and remove a deprecated attribute.

config.xml:

```
<config>
    <markers color="255,100,0" foo="deprecated" />
</config>
```

Lua code:

```
function changeConfigMarkerColor(thePlayer, command, r, g, b)
    local config = xmlLoadFile("config.xml")
    local markernode = xmlFindChild(config, "markers", 0)
    xmlNodeSetAttribute(markernode, "color", r .. "," .. g .. "," .. b)
    xmlNodeSetAttribute(markernode, "foo", nil) -- remove 'foo' attribute
    xmlSaveFile(config)
    xmlUnloadFile(config)
end
addCommandHandler("markercolor", changeConfigMarkerColor)
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md)

- [xmlFindChild](mta://scripting/shared/functions/xmlfindchild.md)

- [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md)

- [xmlLoadString](mta://scripting/shared/functions/xmlloadstring.md)

- [xmlNodeGetAttribute](mta://scripting/shared/functions/xmlnodegetattribute.md)

- [xmlNodeGetAttributes](mta://scripting/shared/functions/xmlnodegetattributes.md)

- [xmlNodeGetChildren](mta://scripting/shared/functions/xmlnodegetchildren.md)

- [xmlNodeGetName](mta://scripting/shared/functions/xmlnodegetname.md)

- [xmlNodeGetParent](mta://scripting/shared/functions/xmlnodegetparent.md)

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- xmlNodeSetAttribute

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
