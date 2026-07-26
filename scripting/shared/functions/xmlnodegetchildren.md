---
doc_id: "mta-wiki:3846"
title: "XmlNodeGetChildren"
source_title: "XmlNodeGetChildren"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeGetChildren"
revision_id: 49255
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:17:07.963984+00:00"
---

# XmlNodeGetChildren

This function returns all children of a particular XML node, or a particular child node.

## Syntax

```
table/xmlnode xmlNodeGetChildren ( xmlnode parent, [ int index ] )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):getChildren(...)*

**Variable**: *.children*

### Required Arguments

- **parent:** This is the [xmlnode](mta://reference/misc/xmlnode.md) you want to retrieve one or all child nodes of.

### Optional Arguments

- **index:** If you only want to retrieve one particular child node, specify its (0-based) index here. For example if you only want the first node, specify 0; the fifth node has index 4, etc.

### Returns

If **index** isn't specified, returns a table containing all child nodes. If **index** is specified, returns the corresponding child node if it exists. If no nodes are found, it returns an empty table. Returns *false* in case of failure.

## Example

Click to collapse [-]
Server

Suppose you have an .xml file with random welcome messages:

```
<messages>
    <message>Welcome to the deathmatch server, enjoy your stay.</message>
    <message>Welcome. Be sure to get your free pizza at Matt's!</message>
    <message>Party going on at the LS beach, be there</message>
</messages>
```

To show a random message from this list to joining players, you could use the following code:

```
addEventHandler("onResourceStart", getResourceRootElement(),
    function()
        local xml = xmlLoadFile("welcome.xml")             -- open the XML file
        local messageNodes = xmlNodeGetChildren(xml)       -- get all child nodes of the root node (<messages>)
        g_WelcomeMessages = {}                             -- create a new global variable to store the welcome messages
        for i,node in ipairs(messageNodes) do              -- loop over all the message nodes
            g_WelcomeMessages[i] = xmlNodeGetValue(node)   -- retrieve the text in each node
        end
        xmlUnloadFile(xml)                                 -- close the XML file
    end
)

addEventHandler("onPlayerJoin", getRootElement(),
    function()
        local numMessages = #g_WelcomeMessages                        -- get the number of messages
        local message = g_WelcomeMessages[math.random(numMessages)]   -- pick a random message
        outputChatBox(message, source, 0, 255, 0)                     -- display it to the joining player
    end
)
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

- xmlNodeGetChildren

- [xmlNodeGetName](mta://scripting/shared/functions/xmlnodegetname.md)

- [xmlNodeGetParent](mta://scripting/shared/functions/xmlnodegetparent.md)

- [xmlNodeGetValue](mta://scripting/shared/functions/xmlnodegetvalue.md)

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
