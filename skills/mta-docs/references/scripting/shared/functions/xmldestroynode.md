---
doc_id: "mta-wiki:3317"
title: "XmlDestroyNode"
source_title: "XmlDestroyNode"
source_url: "https://wiki.multitheftauto.com/wiki/XmlDestroyNode"
revision_id: 43798
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# XmlDestroyNode

This function destroys a XML node from the XML node tree.

## Syntax

```
bool xmlDestroyNode ( xmlnode theXMLNode )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):destroy(...)*

### Required Arguments

- **theXMLNode:** The [xml node](https://wiki.multitheftauto.com/index.php?search=xml%20node) you want to destroy.

### Returns

Returns *true* if the [xml node](https://wiki.multitheftauto.com/index.php?search=xml%20node) was successfully destroyed, *false* otherwise.

### Example

Click to collapse [-]
Server

This example will add a command called '/delnode' and it will create an xml file called 'test.xml'.

```
addEventHandler("onResourceStart", resourceRoot, function()
    xml = xmlLoadFile("test.xml")
    if not xml then
        xml = xmlCreateFile("test.xml", "root")
        xmlCreateChild(xml, "node")
        xmlSaveFile(xml)
    end
end)

addCommandHandler("delnode", function(player)
    local node = xmlFindChild(xml, "node", 0)
    if not node then xmlUnloadFile(xml) return end
    xmlDestroyNode(node)
    xmlSaveFile(xml)
    xmlUnloadFile(xml)
    outputChatBox("You destroyed the node!", player, 0, 255, 0, false)
end)
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- xmlDestroyNode

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
