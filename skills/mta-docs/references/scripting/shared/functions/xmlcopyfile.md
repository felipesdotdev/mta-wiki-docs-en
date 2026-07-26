---
doc_id: "mta-wiki:3331"
title: "XmlCopyFile"
source_title: "XmlCopyFile"
source_url: "https://wiki.multitheftauto.com/wiki/XmlCopyFile"
revision_id: 44632
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# XmlCopyFile

This function copies all contents of a certain node in a XML document to a new document file, so the copied node becomes the new file's root node.
The new file will not be saved to file system until [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)() is called

| [[{{{image}}}\|link=\|]] | Note: To prevent memory leaks, ensure each call to xmlCopyFile has a matching call to xmlUnloadFile |
| --- | --- |
|  |  |

## Syntax

```
xmlnode xmlCopyFile ( xmlnode nodeToCopy, string newFilePath )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):copy(...)*

### Required Arguments

- **nodeToCopy:** the [xmlnode](mta://reference/misc/xmlnode.md) that is to be copied to a new document.

- **newFilePath:** the path of the file that is to be created, in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, to create a file named 'newfile.xml' with myNode as the root node in the resource 'ctf', it can be done from another resource this way: *xmlCopyFile(myNode, ":ctf/newfile.xml")*.

If the file is to be in the current resource, only the file path is necessary, e.g. *xmlCopyFile(myNode, "newfile.xml")*.

### Returns

Returns the [xmlnode](mta://reference/misc/xmlnode.md) of the copy if the node was successfully copied, *false* if invalid arguments were passed.

## Example

In this example we will load an xml file (in the example config.xml) and create a copy in a new folder with the name of copy-config.xml:

```
local config = xmlLoadFile("config.xml")
-- create a copy of xml structure in memory
local newFile = xmlCopyFile(config, "copy/copy-config.xml")
if newFile then
  -- write this new copy to a filesystem
  xmlSaveFile(newFile)
end
-- unload config xml node from memory if it will not be used anytime soon
xmlUnloadFile(config)
```

## See Also

- xmlCopyFile

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

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
