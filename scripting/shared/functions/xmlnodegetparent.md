---
doc_id: "mta-wiki:3995"
title: "XmlNodeGetParent"
source_title: "XmlNodeGetParent"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeGetParent"
revision_id: 46234
language: "en"
categories: ["Server_functions", "Client_functions", "Needs_Example"]
generated_at: "2026-07-26T16:17:08.000592+00:00"
---

# XmlNodeGetParent

|  | Script Example Missing Function XmlNodeGetParent needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

Returns the parent node of an xml node.

## Syntax

```
xmlnode xmlNodeGetParent ( xmlnode node )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):getParent(...)*

**Variable**: *.parent*

### Required Arguments

- **node:** the node of which you want to know the parent.

### Returns

Returns the parent node of the specified node if successful. Returns *false* if the specified node is the root node or an invalid node was passed.

## Example

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

- xmlNodeGetParent

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
