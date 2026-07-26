---
doc_id: "mta-wiki:3315"
title: "XmlCreateSubNode"
source_title: "XmlCreateSubNode"
source_url: "https://wiki.multitheftauto.com/wiki/XmlCreateSubNode"
revision_id: 44603
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
---

# XmlCreateSubNode

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use xmlCreateChild instead. |  |

This function creates a subnode for a specified XML node.

## Syntax

```
xmlnode xmlCreateSubNode ( xmlnode parentNode, string tagname )
```

### Required Arguments

- **parentNode:** the [xmlnode](mta://reference/misc/xmlnode.md) you want to create a subnode of.

- **tagname:** the type of the subnode that will be created.

### Returns

Returns the created [xmlnode](mta://reference/misc/xmlnode.md) if successful, *false* otherwise.

## Example

Click to collapse [-]
Server

We need to create a new node between the tags <config> and </ config>.
config.xml:

```
<config>
    <newnode>somevalue</newnode>
</config>
```

Lua code:

```
function()
    config = xmlLoadFile("config.xml")
    local newNode = xmlCreateSubNode ( config, "newnode" )
    xmlNodeSetValue ( newNode, "somevalue" )
    xmlSaveFile( config )
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

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
