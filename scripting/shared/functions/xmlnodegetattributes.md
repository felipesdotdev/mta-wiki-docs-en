---
doc_id: "mta-wiki:4025"
title: "XmlNodeGetAttributes"
source_title: "XmlNodeGetAttributes"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeGetAttributes"
revision_id: 46227
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:07.943960+00:00"
---

# XmlNodeGetAttributes

Returns all the attributes of a specific XML node.

## Syntax

```
table xmlNodeGetAttributes ( xmlnode node )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):getAttributes(...)*

**Variable**: *.attributes*

### Required Arguments

- **node:** the XML node to get the attributes of.

### Returns

If successful, returns a table with as keys the names of the attributes and as values the corresponding attribute values. If the node has no attributes, returns an empty table. In case of failure, returns *false*.

## Example

Click to collapse [-]
Server

This example code opens the meta.xml of the resource it belongs to, and prints all attributes of the <info> node to the console.

```
local meta = xmlLoadFile ( "meta.xml" )
local info = xmlFindChild ( meta, "info", 0 )
if info then
    local attrs = xmlNodeGetAttributes ( info )
    for name,value in pairs ( attrs ) do
        outputConsole ( name .. " = " .. value )
    end
end
xmlUnloadFile ( meta )
```

If the meta.xml looked like this:

```
<meta>
    <info type="gamemode" name="My gamemode" author="me"/>
    ...
</meta>
```

Then the above code would output (not necessarily in this order):

```
type = gamemode
name = My gamemode
author = me
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

- xmlNodeGetAttributes

- [xmlNodeGetChildren](mta://scripting/shared/functions/xmlnodegetchildren.md)

- [xmlNodeGetName](mta://scripting/shared/functions/xmlnodegetname.md)

- [xmlNodeGetParent](mta://scripting/shared/functions/xmlnodegetparent.md)

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
