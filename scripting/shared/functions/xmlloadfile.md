---
doc_id: "mta-wiki:1612"
title: "XmlLoadFile"
source_title: "XmlLoadFile"
source_url: "https://wiki.multitheftauto.com/wiki/XmlLoadFile"
revision_id: 60831
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:07.884740+00:00"
---

# XmlLoadFile

This function provides an alternative way to load XML files to [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md).
This function loads an XML file and returns the node by specifying a specific file path, while [getResourceConfig](mta://scripting/shared/functions/getresourceconfig.md) allows for loading an XML file from a resource.

| [[{{{image}}}\|link=\|]] | Note: To prevent memory leaks, ensure each call to xmlLoadFile has a matching call to xmlUnloadFile |
| --- | --- |
|  |  |

## Syntax

```
xmlnode xmlLoadFile ( string filePath [, bool readOnly = false ])
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the XML class.*

**Method**: *[XML](mta://reference/misc/xml.md).load(...)*

### Required Arguments

- **filePath:** The [filepath](mta://reference/misc/filepath.md) of the file in the following format: **":resourceName/path"**. 'resourceName' is the name of the resource the file is in, and 'path' is the path from the root directory of the resource to the file.

For example, if there is a file named 'settings.xml' in the resource 'ctf', it can be accessed from another resource this way: *xmlLoadFile(":ctf/settings.xml")*.

If the file is in the current resource, only the file path is necessary, e.g. *xmlLoadFile("settings.xml")*.

### Optional Arguments

- **readOnly:** By default, the XML file is opened with reading and writing access. You can specify *true* for this parameter if you only need reading access.

### Returns

Returns the root [xmlnode](mta://reference/misc/xmlnode.md) object of an xml file if successful, or *false* otherwise.
Print error if something wrong with xml.

## Example

This example loads an XML file called *settings.xml* that is in a resource called *ctv*.

```
node = xmlLoadFile ( ":ctv/settings.xml" )
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md)

- [xmlFindChild](mta://scripting/shared/functions/xmlfindchild.md)

- xmlLoadFile

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
