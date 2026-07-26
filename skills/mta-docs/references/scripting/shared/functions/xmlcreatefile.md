---
doc_id: "mta-wiki:3258"
title: "XmlCreateFile"
source_title: "XmlCreateFile"
source_url: "https://wiki.multitheftauto.com/wiki/XmlCreateFile"
revision_id: 54205
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# XmlCreateFile

This function creates a new XML document, which can later be saved to a file by using [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md). This function will overwrite the file specified if it already exists.

| [[{{{image}}}\|link=\|]] | Note: To prevent memory leaks, ensure each call to xmlCreateFile has a matching call to xmlUnloadFile |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Tip: If you do not want to share the content of the created file with other servers, prepend the file path with @ (See filepath for more information) |
| --- | --- |
|  |  |

## Syntax

```
xmlnode xmlCreateFile ( string filePath, string rootNodeName )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[XML](https://wiki.multitheftauto.com/index.php?search=XML)(...)*

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file will be in, and 'path' is the path from the root directory of the resource to the file.

For example, if you want to create a file named 'new.xml' in the resource 'ctf', it can be created from another resource this way: *xmlCreateFile(":ctf/new.xml", "newroot")*.

If the file is in the current resource, only the file path is necessary, e.g. *xmlCreateFile("new.xml", "newroot")*.

Note that if a different resource than default is being accessed, the caller resource needs access to general.ModifyOtherObjects in the [ACL](https://wiki.multitheftauto.com/index.php?search=ACL).

- **rootNodeName:** the name of the root node in the XML document.

### Returns

Returns the root [xmlnode](mta://reference/misc/xmlnode.md) object of the new XML file if successful, or *false* otherwise.

## Example

This example allows a player to use the command 'createfile' to create an .xml file.

```
-- Creates a file named "new.xml" with root node "newroot" and childnode "newchild".
function createFileHandler()
   local rootNode = xmlCreateFile("new.xml","newroot")
   local childNode = xmlCreateChild(rootNode, "newchild")
   xmlSaveFile(rootNode)
   xmlUnloadFile(rootNode)
end

addCommandHandler("createfile", createFileHandler)
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- xmlCreateFile

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
