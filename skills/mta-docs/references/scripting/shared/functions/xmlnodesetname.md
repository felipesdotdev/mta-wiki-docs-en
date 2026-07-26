---
doc_id: "mta-wiki:4024"
title: "XmlNodeSetName"
source_title: "XmlNodeSetName"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeSetName"
revision_id: 62649
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# XmlNodeSetName

Sets the tag name of the specified XML node.

## Syntax

```
bool xmlNodeSetName ( xmlnode node, string name )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):setName(...)*

**Variable**: *.name*

**Counterpart**: *[xmlNodeGetName](mta://scripting/shared/functions/xmlnodegetname.md)*

### Required Arguments

- **node:** the node to change the tag name of.

- **name:** the new tag name to set.

### Returns

Returns *true* if successful, *false* otherwise.

## Example

```
local xml = xmlCreateFile("fileName.xml","Test")
local xmlNode = xmlCreateChild(xml,"Test1")
local xmlNodeName = xmlNodeGetName(xmlNode)
xmlUnloadFile(xml)
if xmlNodeName == "Test1" then
   xmlNodeSetName(xmlNode, "Test2")
end
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

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- xmlNodeSetName

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
