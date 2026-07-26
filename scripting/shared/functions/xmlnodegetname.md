---
doc_id: "mta-wiki:4023"
title: "XmlNodeGetName"
source_title: "XmlNodeGetName"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeGetName"
revision_id: 68882
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:07.980258+00:00"
---

# XmlNodeGetName

Gets the tag name of the specified XML node.

## Syntax

```
string xmlNodeGetName ( xmlnode node )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):getName(...)*

**Variable**: *.name*

**Counterpart**: *[xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)*

### Required Arguments

- **node:** the node to get the tag name of.

### Returns

Returns the tag name of the node if successful, *false* otherwise.

## Example

Click to collapse [-]
Example 1

```
local xml = xmlCreateFile("test.xml","test")
local xmlNode = xmlCreateChild(xml,"nextTest")
local xmlNodeName = xmlNodeGetName(xmlNode)
xmlUnloadFile(xml)
outputConsole(xmlNodeName) --This should output "nextTest".
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

- xmlNodeGetName

- [xmlNodeGetParent](mta://scripting/shared/functions/xmlnodegetparent.md)

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
