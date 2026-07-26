---
doc_id: "mta-wiki:11723"
title: "XmlLoadString"
source_title: "XmlLoadString"
source_url: "https://wiki.multitheftauto.com/wiki/XmlLoadString"
revision_id: 81443
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.7"]
generated_at: "2026-07-26T16:17:07.904074+00:00"
---

# XmlLoadString

This function creates an [Xmlnode](mta://reference/misc/xmlnode.md) from a string input.

## Syntax

```
xmlnode xmlLoadString ( string xmlString )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Note**: *This function is a static function underneath the XML class.*

**Method**: *[XML](mta://reference/misc/xml.md).loadstring(...)*

### Required Arguments

- **xmlString:** A string containing XML data

### Returns

Returns the root [xmlnode](mta://reference/misc/xmlnode.md) object of an xml string if successful, or *false* otherwise (invalid XML string).

## Example

This example loads an XML string and loops the children while outputting to debugscript.

```
local rootNode = xmlLoadString("<animals test='x'><wolf name='timmy'></wolf> <fox name='luxy'></fox></animals>")

if rootNode then
	local rootAttributes = xmlNodeGetAttributes(rootNode)
	print("Root Node", "Name: "..xmlNodeGetName(rootNode),  "Attributes :"..toJSON(rootAttributes))
	
	local children = xmlNodeGetChildren(rootNode)
	
	for i, childNode in ipairs(children) do
		local attributes = xmlNodeGetAttributes(childNode)
		print("Child #"..i, "Name: "..xmlNodeGetName(childNode), "Attributes :"..toJSON(attributes))
	end
end
```

## See Also

- [xmlCopyFile](mta://scripting/shared/functions/xmlcopyfile.md)

- [xmlCreateChild](mta://scripting/shared/functions/xmlcreatechild.md)

- [xmlCreateFile](mta://scripting/shared/functions/xmlcreatefile.md)

- [xmlDestroyNode](mta://scripting/shared/functions/xmldestroynode.md)

- [xmlFindChild](mta://scripting/shared/functions/xmlfindchild.md)

- [xmlLoadFile](mta://scripting/shared/functions/xmlloadfile.md)

- xmlLoadString

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
