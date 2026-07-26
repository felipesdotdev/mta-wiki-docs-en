---
doc_id: "mta-wiki:3997"
title: "XmlFindChild"
source_title: "XmlFindChild"
source_url: "https://wiki.multitheftauto.com/wiki/XmlFindChild"
revision_id: 62646
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:07.809312+00:00"
---

# XmlFindChild

This function returns a named child node of an XML node.

## Syntax

```
xmlnode xmlFindChild ( xmlnode parent, string tagName, int index )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):findChild(...)*

### Required Arguments

- **parent**: This is an [xmlnode](mta://reference/misc/xmlnode.md) that you want to find the child node under.

- **tagName**: This is the name of the child node you wish to find (case-sensitive).

- **index**: This is the 0-based index of the node you wish to find. For example, to find the 5th subnode with a particular name, you would use 4 as the index value. To find the first occurence, use 0.

### Returns

Returns an [xmlnode](mta://reference/misc/xmlnode.md) if the node was found, *false* otherwise.

## Example

Click to collapse [-]
Server

If you wanted to find an *instructions* node in an xml file like this:

```
<root version="2.0">
      <options>
            <instructions>Start at the beginning and keep going until the end!</instructions>
      </options>
</root>
```

You could use the following code to print the text in the *instructions* node to the chatbox:

```
local rootNode = xmlLoadFile ( "test.xml" )
local optionsNode = xmlFindChild ( rootNode, "options", 0 )
local instructionsNode = xmlFindChild ( optionsNode, "instructions", 0 )
local instructions = xmlNodeGetValue ( instructionsNode )
xmlUnloadFile(rootNode)

outputChatBox ( instructions )
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md)

- xmlFindChild

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
