---
doc_id: "mta-wiki:2588"
title: "XmlSaveFile"
source_title: "XmlSaveFile"
source_url: "https://wiki.multitheftauto.com/wiki/XmlSaveFile"
revision_id: 62645
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:08.186455+00:00"
---

# XmlSaveFile

This function saves a loaded XML file.

## Syntax

```
bool xmlSaveFile ( xmlnode rootNode )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):saveFile(...)*

### Required Arguments

- **rootNode:** the root [xmlnode](mta://reference/misc/xmlnode.md) of the loaded XML file.

### Returns

Returns *true* if save was successful, *false* if the XML file does not exist.

## Example

Click to collapse [-]
Client

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

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- xmlSaveFile

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
