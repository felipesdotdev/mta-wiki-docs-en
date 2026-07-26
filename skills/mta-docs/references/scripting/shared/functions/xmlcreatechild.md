---
doc_id: "mta-wiki:3996"
title: "XmlCreateChild"
source_title: "XmlCreateChild"
source_url: "https://wiki.multitheftauto.com/wiki/XmlCreateChild"
revision_id: 74130
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# XmlCreateChild

This function creates a new child node under an XML node.

## Syntax

```
xmlnode xmlCreateChild ( xmlnode parentNode, string tagName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):createChild(...)*

### Required Arguments

- **parentNode:** the [xmlnode](mta://reference/misc/xmlnode.md) you want to create a new child node under.

- **tagName:** the type of the child node that will be created.

### Returns

Returns the created [xmlnode](mta://reference/misc/xmlnode.md) if successful, *false* otherwise.

## Example

This example allows a player to use the command 'createfile' to create an .xml file.

```
-- Creates a file named "new.xml" with root node "newroot" and childnode "newchild".
function createFileHandler()
local RootNode = xmlCreateFile("new.xml"," newroot")
local NewNode = xmlCreateChild(RootNode, "newchild")
xmlSaveFile(RootNode)
xmlUnloadFile(RootNode)
end

addCommandHandler("createfile", createFileHandler)
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- xmlCreateChild

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

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
