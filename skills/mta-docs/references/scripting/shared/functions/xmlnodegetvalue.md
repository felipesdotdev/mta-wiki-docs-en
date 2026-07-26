---
doc_id: "mta-wiki:1608"
title: "XmlNodeGetValue"
source_title: "XmlNodeGetValue"
source_url: "https://wiki.multitheftauto.com/wiki/XmlNodeGetValue"
revision_id: 62648
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# XmlNodeGetValue

This function is made to be able to read tag values in XML files (eg. <something>anything</something>).

## Syntax

```
string xmlNodeGetValue ( xmlnode theXMLNode )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[xmlnode](mta://reference/misc/xmlnode.md):getValue(...)*

**Variable**: *.value*

**Counterpart**: *[xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)*

### Required Arguments

- **theXMLNode:** The [xml node](https://wiki.multitheftauto.com/index.php?search=xml%20node) of which you need to know the value.

### Returns

Returns the value of the node as a [string](mta://reference/misc/string.md) if it was received successfully, *false* otherwise.

## Example

Click to collapse [-]
Server Example: return a sample file from a XML file

In this example a sample value is returned from a XML file.

```
local xmlFile = xmlLoadFile ( "exampleFile.xml" ) -- Open a file that we have already created
if xmlFile then -- If it's indeed opened
    local node = xmlFindChild( xmlFile, "somesubnode", 0 ) -- Find our first sub node
    local success = xmlNodeGetValue ( node ) -- Get the value of it
    xmlUnloadFile(xmlFile)
    if success then -- Check if it was successful
        outputChatBox ( tostring ( success ) ) -- Output "somevalue" to the chatbox
    end
end
```

In order for the result to be valid, the xml file has to look like this:
<section name="exampleFile.xml" class="server" show="true">

```
<somenode>
        <somesubnode>somevalue</somesubnode>
</somenode>
```

Click to collapse [-]
Client Example: Save and load from a clientside XML

This shows an example of a clientside XML file. You can use this to store user preferences and load them the next time the script loads. Almost always, you should have an options GUI for clients to interact with to set these values.
  
  

Since the XML will change, it should NOT be included in the resource's meta.xml file. MTA will think that file is corrupted and will download it again from the server. Instead, you should create the XML within the script, and then load it within the script on future script runs if it exists.

**This xml will be created from the script following it below**

```
<root>
    <hud_display>
        <IconSizeX>60</IconSizeX>
        <IconSizeY>60</IconSizeY>
    </hud_display>
    <hud_binds>
        <weaponSlot0>tab</weaponSlot0>
        <weaponSlot1>1</weaponSlot1>
    </hud_binds>
</root>
```

**This script will create the xml or load it if it exists**

```
function ClientResourceStart ()
	if source ~= getResourceRootElement() then return end --This event will happen with any resource start, isolate it to this resource	
	xmlRootTree = xmlLoadFile ( "userSettings.xml" ) --Attempt to load the xml file	

	if xmlRootTree then -- If the xml loaded then...
		xmlHudBranch = xmlFindChild(xmlRootTree,"hud_display",0) -- Find the hud sub-node
		xmlBindsBranch = xmlFindChild(xmlRootTree,"hud_binds",0) -- Find the binds sub-node
		outputChatBox ( "XML Found and Loaded" )
	else -- If the xml does not exist then...
		xmlRootTree = xmlCreateFile ( "userSettings.xml", "root" ) -- Create the xml file	
		xmlHudBranch = xmlCreateChild ( xmlRootTree, "hud_display" ) -- Create the hud sub-node under the root node
		xmlBindsBranch = xmlCreateChild ( xmlRootTree, "hud_binds" )-- Create the binds sub-node under the root node
		xmlNodeSetValue (xmlCreateChild ( xmlHudBranch, "IconSizeX"), "60" ) --Create sub-node values under the hud sub-node
		xmlNodeSetValue (xmlCreateChild ( xmlHudBranch, "IconSizeY"), "60" ) --Create sub-node values under the hud sub-node
		xmlNodeSetValue (xmlCreateChild ( xmlBindsBranch, "weaponSlot0"), "tab" ) --Create sub-node values under the binds sub-node
		xmlNodeSetValue (xmlCreateChild ( xmlBindsBranch, "weaponSlot1"), "1" ) --Create sub-node values under the binds sub-node
		outputChatBox ( "XML Created" )
	end

	--Retrieve a single sub-node name or value
	outputChatBox( "Node name: "..xmlNodeGetName (xmlFindChild(xmlHudBranch,"IconSizeX",0)), 0, 0, 255 ) --blue outputs
	outputChatBox( "Node Value: "..xmlNodeGetValue (xmlFindChild(xmlHudBranch,"IconSizeX",0)), 0, 0, 255 ) --blue outputs
	
        --Retrieve multiple sub-node names or values	
	xmlHudChildrenTable = xmlNodeGetChildren ( xmlHudBranch ) --Create a table of this branch's children
	for i,node in pairs(xmlHudChildrenTable ) do --Loop through the branch's children for sub-nodes
            outputChatBox( "Node name: "..xmlNodeGetName (node), 0, 255, 0 ) --green outputs
	    outputChatBox( "Node Value: "..xmlNodeGetValue(node), 0, 255, 0 ) --green outputs
	end
end
addEventHandler ( "onClientResourceStart", root, ClientResourceStart )
 
function ClientResourceStop ()
	if source ~= getResourceRootElement() then return end --This event will happen with any resource stop, isolate it to this resource
	xmlSaveFile ( xmlRootTree ) --Save the xml from memory for use next time
	xmlUnloadFile ( xmlRootTree ) --Unload the xml from memory
	outputChatBox ( "Saved and unloaded the XML." )
end
addEventHandler ( "onClientResourceStop", root, ClientResourceStop )
```

</section>

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

- xmlNodeGetValue

- [xmlNodeSetAttribute](mta://scripting/shared/functions/xmlnodesetattribute.md)

- [xmlNodeSetName](mta://scripting/shared/functions/xmlnodesetname.md)

- [xmlNodeSetValue](mta://scripting/shared/functions/xmlnodesetvalue.md)

- [xmlSaveFile](mta://scripting/shared/functions/xmlsavefile.md)

- [xmlUnloadFile](mta://scripting/shared/functions/xmlunloadfile.md)
