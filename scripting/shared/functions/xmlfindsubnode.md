---
doc_id: "mta-wiki:1297"
title: "XmlFindSubNode"
source_title: "XmlFindSubNode"
source_url: "https://wiki.multitheftauto.com/wiki/XmlFindSubNode"
revision_id: 44558
language: "en"
categories: ["Server_functions", "Client_functions", "Deprecated"]
generated_at: "2026-07-26T16:17:07.829985+00:00"
---

# XmlFindSubNode

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use xmlFindChild instead. |  |

This function returns a named sub node of a particular XML node.

## Syntax

```
xmlnode xmlFindSubNode ( xmlnode parent, string subnode, int index )
```

### Required Arguments

- **parent**: This is an [xmlnode](mta://reference/misc/xmlnode.md) that you want to find the subnode under. This could be a node returned from another call to xmlFindSubNode.

- **subnode**: This is the name of the subnode you wish to find.

- **index**: This is the index of the node you wish to find. For example, to find the 5th subnode with a particular name, you would use 4 as the index value. To find the first occurence, use 0.

### Returns

Returns an [xmlnode](mta://reference/misc/xmlnode.md) object if the node was found, *false* otherwise.

## Example

Click to collapse [-]
Server

If you wanted to find the 'instructions' node in a map file like this:

```
<map version="2.0">
      <options>
            <instructions>Start at the begining and keep going until the end!</instructions>
      </options>
</map>
```

You could use the following code:

```
maproot = getLoadedMapXMLRoot ()
optionsnode = xmlFindSubNode ( maproot, "options", 0 )
instructionsnode = xmlFindSubNode ( optionsnode, "instructions", 0 )
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
